import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml

_imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')
# _imgURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')

_imageRefs = './_data/_image-refs.TEST.yml'

_mdRoot = './OUT_markdown/MODULE_NAME/'
_imgCommonRoot = './OUT_markdown/MODULE_NAME/static/common'

_imgMap = {}
# a set of key-value pairs, where
#     key = the HelpDocs image URL
#     val = relative path from the _mdRoot 

# for each markdown file:
#     for each line in file:
#         for each image URL in line:
#             imageFileName = getFileFromURL(imgURL)
#             if imageFileName == "": 
#                 imageFileName = getImage(imgURL)
#             addToImageMap(imgURL, imageFileName)
#             imgTarget = getImageTarget(mdFileName, imgFileName)

    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)

def getImage(imgURL, imageFileNameFull):
    
    res = requests.get(imgURL, stream = True)

    if res.status_code == 200:
        # with open(imageFileNameFull,'wb') as f:
            # shutil.copyfileobj(res.raw, f)
        print('Image downloaded:           ',imageFileNameFull)
        return os.path.abspath(imageFileNameFull)
    else:
        print('Image download failed:      ', imgURL)
        return False    

def addImageToMap(imgURL, imageFileName):
    imgPath, imgFile = os.path.split(imageFileName)
    imgRelPath = os.path.relpath(_mdRoot, imgPath)
    imgTarget = imgRelPath + imgFile
    
    _imgMap[imgURL] = imgTarget
    return imgTarget
    
def getImageFromMap(imgURL):
    if imgURL in _imgMap.keys():
        return _imgMap[imgURL] 
    else:
        return ""
        
def getNumImgRefs(imgURL):
    if imgURL in _imgMap.keys():
        refsList =  _imageRefs[imgURL]
        return len(refsList) 
    else:
        return 0
    

def getImageFileNameFull(imgURL, mdFileName):
        mdPath, mdFile = os.path.split(mdFileName)
        mdFileBase, mdExt = os.path.splitext(mdFile)
        
        if getNumImgRefs(imgURL) > 1:
            imgPath = os.path.abspath(_imgCommonRoot)
        else:
            imgPath = os.path.abspath(mdPath) + "/static/"
        
        if not os.path.exists(imgPath):
                  os.makedirs(imgPath)
        idx = len(next(os.walk(imgPath))[2])
        idx = str(idx).zfill(2)
         
        imgRoot, imgExt = os.path.splitext(imgURL)
        imageFileNameFull = imgPath + mdFileBase + '-' + str(idx).zfill(2) + imgExt
        
        # pathlib.Path(imageTargetFolder).mkdir(parents=True, exist_ok=True)
        return imageFileNameFull

def getImageTarget(imgFileName, mdFileName):     
    imgPath, imgName = os.path.split(imgFileName)

    imgPath = os.path.abspath(imgName)
    mdPath = os.path.abspath(mdFileName) 
    relPath = os.path.relpath(mdPath, imgPath)
    
    imgTarget = relPath + imgName
    
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("imgFileName = ", imgFileName)
    print("mdFileName = ", mdFileName)
    print("relPath = ", relPath)
    print("imgTarget = ", imgTarget)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')

    return relPath   

def updateImageRefsInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    print("mdFile = ", mdFileName)

    newMarkdown = []
    for line in mdLines:
        for match in re.finditer(_imgURLpattern, line):
            imgURL = match.group()
            imgFileName = getImageFromMap(imgURL)
            if (imgFileName == "") :
                 imgFileName = getImageFileNameFull(imgURL, mdFileName)
                 getImage(imgURL, imgFileName)
                 addImageToMap(imgURL, imgFileName)
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