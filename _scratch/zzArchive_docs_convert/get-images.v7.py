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
        print('[WARNING]  Image download failed:      ', imgURL)
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
        
def getimageFileNameFull(imageURL, mdFileName):
        mdPath, mdFileName = os.path.split(mdFileName)
        mdFileName, mdExt = os.path.splitext(mdFileName)
        
        imageTargetFolder = mdPath + '/static/'
        
        if not os.path.exists(imageTargetFolder):
                  os.makedirs(imageTargetFolder)
        idx = len(next(os.walk(imageTargetFolder))[2])
        idx = str(idx).zfill(2)
        # print("idx =", idx)   
         
        imgRoot, imgExt = os.path.splitext(imageURL)
        imageFileNameFull = imageTargetFolder + mdFileName + '-' + str(idx).zfill(2) + imgExt
        
        # pathlib.Path(imageTargetFolder).mkdir(parents=True, exist_ok=True)
        #print('image full:        ', imageFileNameFull)
        return imageFileNameFull

def getImageTarget(imgFileName):     
    imgPath, imgName = os.path.split(imgFileName)
    return "./static/" + imgName   


def updateImageRefsInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    print("mdFile = ", mdFileName)

    newMarkdown = []
    for line in mdLines:
        for match in re.finditer(_imgURLpattern, line):
             imgURL = match.group()
             imgFileName = getimageFileNameFull(imgURL, mdFileName)
             if getImage(imgURL, imgFileName) != False: 
                # addToDictionary(imgURL, imgFileName)
                imgTarget = getImageTarget(imgFileName)
                print('')
                print('______________________________________________________')
                print("mdFileName = ", mdFileName)
                print("imgURL = ", imgURL)
                print("imgTarget = ", imgTarget)
                print("imageFileName = ", imgFileName)
                print('______________________________________________________')
                print('')
                line = line.replace(imgURL, imgTarget)
             else:
                print("[WARNING]  URL not converted, reference not updated:")
                print("\t ", imgURL)
                print("\t in file ", os.path.basename(mdFileName))
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