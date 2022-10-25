import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import pprint

_imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')

'''
_imageRefsFile = '../_data/_image-refs.TEST.yml'
with open(_imageRefsFile , 'r') as inFile:
    _imgRefsDict = yaml.safe_load(inFile)
'''

_mdRoot = './docs/'
_imgMap = {}


def getImage(imgURL, imageFileNameFull, mdFile):
    
    addImageRefToCatalog(imgURL, mdFile)
    
    res = requests.get(imgURL, stream = True)
    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        # # print('[DEBUG] Image downloaded:           ',imageFileNameFull)
        return os.path.abspath(imageFileNameFull)
    else:
        print('[WARNING2] Image download failed:      ', imgURL)
        return False    
    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)

'''        
def getRefsListForURL(imgURL):
    if imgURL in _imgMap.keys():
        return _imgMap[imgURL] 
    emptyList = []
    return emptyList
'''

def addImageRefToCatalog(imgURL, mdFile):
    if imgURL in _imgMap.keys():
        mdFileList = _imgMap[imgURL]
    else:
        mdFileList = []
    mdFileList.append(mdFile)
    if len(mdFileList) > 1:
        print('-------------------------')
        print('[WARNING1] Image URL referenced in multiple topics:      ', imgURL)
        # print('Image filename:      ', imageFileNameFull)
        print('Topics list:')
        print(mdFileList)
        print('-------------------------')
    _imgMap[imgURL] = mdFileList
    return mdFileList
        
def getimageFileNameFull(imageURL, mdFileName):
        mdPath, mdFileName = os.path.split(mdFileName)
        mdFileName, mdExt = os.path.splitext(mdFileName)
        
        imageTargetFolder = mdPath + '/static/'
        
        if not os.path.exists(imageTargetFolder):
                  os.makedirs(imageTargetFolder)
        idx = len(next(os.walk(imageTargetFolder))[2])
        idx = str(idx).zfill(2)
         
        imgRoot, imgExt = os.path.splitext(imageURL)
        imageFileNameFull = imageTargetFolder + mdFileName + '-' + str(idx).zfill(2) + imgExt
        
        return imageFileNameFull

def getImageTarget(imgFileName):     
    imgPath, imgName = os.path.split(imgFileName)
    return "./static/" + imgName   

def updateImageRefsInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    # # print("[DEBUG] mdFile = ", mdFileName)

    newMarkdown = []
    idx = 1
    for line in mdLines:
        for match in re.finditer(_imgURLpattern, line):
             imgURL = match.group()
             imgFileName = getimageFileNameFull(imgURL, mdFileName)
             if getImage(imgURL, imgFileName, mdFileName) != False: 
                imgTarget = getImageTarget(imgFileName)
                # print('')
                # print('______________________________________________________')
                # print("[DEBUG] mdFileName = ", mdFileName)
                # print("[DEBUG] imgURL = ", imgURL)
                # print("[DEBUG] imgTarget = ", imgTarget)
                # print("imageFileName = ", imgFileName)
                # print('______________________________________________________')
                # print('')
                line = line.replace(imgURL, imgTarget)
             else:
                print("[WARNING2] Image not downloaded, reference not updated:")
                print("\t URL  ", imgURL)
                print("\t file ", os.path.basename(mdFileName))
                print("\t line ", idx, ": ", line)
                print('')
        newMarkdown.append(line)
        idx += 1
            
    stringListToFile(newMarkdown, mdFileName)

for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
         print('')
         # print('[DEBUG]  ------------------------ processing ', os.path.basename(mdFileName))
         # # print("[DEBUG] markdown source = ", filename)
         # # print('[DEBUG] markdown full:     ',  os.path.abspath(mdFileName))
         # # print('[DEBUG] Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         updateImageRefsInFile(os.path.abspath(mdFileName))         
         # print('[DEBUG] ------------------------  end processing ', os.path.basename(mdFileName))
         print('')
         # print("dest   = ", mdfn)

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(_imgMap)