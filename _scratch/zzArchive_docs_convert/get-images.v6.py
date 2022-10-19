import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml

_imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')
# _imgURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')

# _imageRefsYamlFileName = './_data/_image-refs.CI.yml'

_mdRoot = './OUT_markdown/MODULE_NAME/'
_imgRoot = './OUT_markdown/MODULE_NAME/static/'
_imgMap = {}

# for each markdown file:
#     for each line in file:
#         for each image URL in line:
#             imageFileName = getFileFromURL(imgURL)
#             if imageFileName == "": 
#                 imageFileName = getImage(imgURL)
#             addToImageMap(imgURL, imageFileName)
#             imgTarget = getImageTarget(mdFileName, imgFileName)

    

def getStringFromFile(fileName):
    with open(fileName, 'r') as f:
        str = f.read()
    return str    


def getFileNameFromRoot(fileNameFull): 
    return fileNameFull.replace(_mdRoot,'' )
        
def fileIsInFolder(fileName, rootFolder):
    p, f = os.path.split(fileName)
    print("rootFolder = ", rootFolder)
    for root, dirs, files in os.walk(rootFolder):  
        if f in files:
            print("Found file: ", os.path.basename(f) + '/' + os.path.basename(f) )
            return True
    print("File not found: ", fileName)
    return False
    
# https://stackoverflow.com/questions/17506552/python-os-path-relpath-behavior
def getRealRelPath(origin, dest): 
    '''Get the relative path between two paths, accounting for filepaths'''

    # get the absolute paths so that strings can be compared
    origin = os.path.abspath(origin) 
    dest = os.path.abspath(dest) 

    # find out if the origin and destination are filepaths
    origin_isfile = os.path.isfile(origin)
    dest_isfile = os.path.isfile(dest)

    # if dealing with filepaths, 
    if origin_isfile or dest_isfile:
        # get the base filename
        filename = os.path.basename(origin) if origin_isfile else os.path.basename(dest)
        # in cases where we're dealing with a file, use only the directory name
        origin = os.path.dirname(origin) if origin_isfile else origin
        dest = os.path.dirname(dest) if dest_isfile else dest 
        # get the relative path between directories, then re-add the filename
        return os.path.join(os.path.relpath(dest, origin), filename)  
    else:
        # if not dealing with any filepaths, just run relpath as usual
        return os.path.relpath(dest, origin)   


def getImage(imgURL, imageFileNameFull):
    
    res = requests.get(imgURL, stream = True)

    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image downloaded:           ',imageFileNameFull)
        return os.path.abspath(imageFileNameFull)
    else:
        print('Image download failed:      ', imgURL)
        return False    
    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)

def addToDictionary(imgURL, imageFileName):
    _imgMap[imgURL] = os.path.abspath(imageFileName)
    
def getImageFromDictionary(imgURL):
    if imgURL in _imgMap.keys():
        return _imgMap[imgURL] 
    else:
        return ""
        
def getimageFileNameFull(imgURL, mdFileName):
        mdPath, mdFile = os.path.split(mdFileName)
        mdFileBase, mdExt = os.path.splitext(mdFile)
        
        if not os.path.exists(_imgRoot):
                  os.makedirs(_imgRoot)
        idx = len(next(os.walk(_imgRoot))[2])
        idx = str(idx).zfill(2)
         
        imgRoot, imgExt = os.path.splitext(imgURL)
        imageFileNameFull = _imgRoot + mdFileBase + '-' + str(idx).zfill(2) + imgExt
        
        # pathlib.Path(imageTargetFolder).mkdir(parents=True, exist_ok=True)
        return imageFileNameFull

def getImageTarget(imgFileName, mdFileName):     
    imgPath, imgName = os.path.split(imgFileName)
    imgName =  _imgRoot + imgName

    imgFileNameFull = os.path.abspath(imgName)
    mdFileNameFull = os.path.abspath(mdFileName) 
    # relPath = getRealRelPath(mdFileNameFull, imgFileNameFull)
    relPath = os.path.relpath(mdFileNameFull, imgFileNameFull)
    print("imgFileNameFull = ", imgFileNameFull)
    print("mdFileNameFull = ", mdFileNameFull)
    print("relPath = ", relPath)

    return relPath   


def updateImageRefsInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    print("mdFile = ", mdFileName)

    newMarkdown = []
    for line in mdLines:
        for match in re.finditer(_imgURLpattern, line):
            imgURL = match.group()
            imgFileName = getImageFromDictionary(imgURL)
            if (imgFileName == "") :
                 imgFileName = getimageFileNameFull(imgURL, mdFileName)
                 getImage(imgURL, imgFileName)
                 addToDictionary(imgURL, imgFileName)
            imgTarget = getImageTarget( mdFileName, imgFileName)
            print('')
            print('______________________________________________________')
            print("mdFileName = ", mdFileName)
            print("imgURL = ", imgURL)
            print("imgTarget = ", imgTarget)
            print("imageFileName = ", imgFileName)
            print('______________________________________________________')
            print('')
            line = line.replace(imgURL, imgTarget)
        newMarkdown.append(line)
            
    stringListToFile(newMarkdown, mdFileName)


for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
         print('')
         print(' ------------------------ processing ', mdFileName)
         # print("markdown source = ", filename)
         # print('markdown full:     ',  os.path.abspath(mdFileName))
         # print('Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         updateImageRefsInFile(os.path.abspath(mdFileName))         
         print('------------------------  end processing ', mdFileName)
         print('')
         # print("dest   = ", mdfn)

# print("_imgMap = ", _imgMap)