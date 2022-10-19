import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml

_imageURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')
_imageRefsYamlFileName = './_data/_image-refs.STO.yml'
_rootFolder = './OUT_markdown'


_DH_REPO_ROOT = os.path.abspath(os.path.join('.', os.pardir))
_commonImagesFolder = _DH_REPO_ROOT + "/_docs_convert/OUT_markdown/static/common/"

def getStringFromFile(fileName):
    with open(fileName, 'r') as f:
        str = f.read()
    return str
    
def updateFile(str, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)
    else:
        print(fileName, "  not found")

    file_new = open(fileName, "w")
    file_new.write(str)
    file_new.close()    

def getimageFileNameFull(imageURL, mdFileName):
        mdPath, mdFileName = os.path.split(mdFileName)
        mdFileName, mdExt = os.path.splitext(mdFileName)
        
        if getNumRefs(imageURL) > 1:
            imageTargetFolder = _commonImagesFolder 
            print(imageURL, " has multiple references!")
        else:
            imageTargetFolder = mdPath + '/static/'
        
        # https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python
        # print("imageTargetFolder = ", imageTargetFolder)
        if not os.path.exists(imageTargetFolder):
                  os.makedirs(imageTargetFolder)
        idx = len(next(os.walk(imageTargetFolder))[2])
        idx = str(idx).zfill(2)
        # print("idx =", idx)   
         
        imgRoot, imgExt = os.path.splitext(imageURL)
        imageFileNameFull = imageTargetFolder + mdFileName + '-' + str(idx).zfill(2) + imgExt
        
        pathlib.Path(imageTargetFolder).mkdir(parents=True, exist_ok=True)
        print('image filename full:        ', imageFileNameFull)
        return imageFileNameFull

def getFileNameRelative(imgFileName, mdFileName): 
    imgFileNameFull = os.path.abspath(imgFileName)
    mdFileNameFull = os.path.abspath(mdFileName) 
    relPath = os.path.relpath(imgFileNameFull, mdFileNameFull)
    print('filename rel:              ', relPath)
    return relPath

def getFileNameFromRoot(fileNameFull): 
    return fileNameFull.replace(_DH_REPO_ROOT,'/' )

def getNumRefs(imageURL):
    with open(_imageRefsYamlFileName , 'r') as inFile:
        data = yaml.safe_load(inFile)
        return len(data[imageURL])
        
def fileIsInDocs(fileName):
    p, f = os.path.split(imageFileName)
    docsFolder = _DH_REPO_ROOT + '/docs'
    for root, dirs, files in os.walk(docsFolder):  
        if f in files:
            print("file is in docs/: ", fileName)
            return True
    return False

def getImageTarget(imageURL, imageFileNameFull): 
    imgFileNamePath, imgFileName = os.path.split(imageFileNameFull)
    if getNumRefs(imageURL) > 1:
        imgTarget = '/static/common/'  + imgFileName
    else: 
        imgTarget = './static/' + imgFileName 
    return imgTarget   

def getImage(imageURL, imageFileNameFull):
    
    res = requests.get(imageURL, stream = True)

    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image downloaded:           ',imageFileNameFull)
        return imageFileNameFull
    else:
        print('Image download failed:      ', imageURL)
        return False    
    
def updateImageRefsInFile(mdFileName): 
    mdString = getStringFromFile(mdFileName)

    for i, line in enumerate(open(mdFileName)):
        for match in re.finditer(_imageURLpattern, line):
            imageURL = match.group()
            imageFileNameFull = getimageFileNameFull(imageURL, mdFileName )
            
            if (os.path.exists(imageFileNameFull)) == False:
                getImage(imageURL, imageFileNameFull)
            
            imgTarget = getImageTarget(imageURL, imageFileNameFull)
            
            mdString = mdString.replace(imageURL, imgTarget)
            
    updateFile(mdString, mdFileName)

# updateImageRefsInFile(_mdFileName)

for mdFileName in glob.iglob(_rootFolder + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
         print('')
         print('------------------------  ')
         # print("markdown source = ", filename)
         print('markdown full:     ',  os.path.abspath(mdFileName))
         # print('Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         updateImageRefsInFile(os.path.abspath(mdFileName))         
         print('------------------------  ')
         # print("dest   = ", mdfn)
