import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import pprint

_imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')
# _imgURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')

_imageRefsFile = '../_data/_image-refs.TEST.yml'
with open(_imageRefsFile , 'r') as inFile:
    _imgRefsDict = yaml.safe_load(inFile)

_mdRoot = './docs/'
# _imgRoot = './OUT_markdown/MODULE_NAME/static/'
_imgMap = {}

# for each markdown file:
#     for each line in file:
#         for each image URL in line:
#             imageFileName = getFileFromURL(imgURL)
#             if imageFileName == "": 
#                 imageFileName = getImage(imgURL)
#             addToImageMap(imgURL, imageFileName)
#             imgTarget = getImageTarget(mdFileName, imgFileName)




def getImage(imgURL, imageFileNameFull):
    
    refsList = getRefsListForURL(imgURL)
    if len(refsList) > 1:
        print('-------------------------')
        print('[WARNING] Image URL referenced in multiple topics:      ', imgURL)
        print('Image filename:      ', imageFileNameFull)
        print('Topics list:')
        print(refsList)
        print('-------------------------')
    
    res = requests.get(imgURL, stream = True)

    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        # print('Image downloaded:           ',imageFileNameFull)
        return os.path.abspath(imageFileNameFull)
    else:
        print('[WARNING] Image download failed:      ', imgURL)
        return False    
    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)
        
def getRefsListForURL(imgURL):
    if imgURL in _imgRefsDict.keys():
        return _imgRefsDict[imgURL] 
    emptyList = []
    return emptyList
    
        
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
    idx = 1
    for line in mdLines:
        for match in re.finditer(_imgURLpattern, line):
             imgURL = match.group()
             imgFileName = getimageFileNameFull(imgURL, mdFileName)
             if getImage(imgURL, imgFileName) != False: 
                imgTarget = getImageTarget(imgFileName)
                # print('')
                # print('______________________________________________________')
                # print("mdFileName = ", mdFileName)
                print("imgURL = ", imgURL)
                print("imgTarget = ", imgTarget)
                # print("imageFileName = ", imgFileName)
                #print('______________________________________________________')
                # print('')
                line = line.replace(imgURL, imgTarget)
             else:
                print("[WARNING] Image not downloaded, reference not updated:")
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
         print(' ------------------------ processing ', os.path.basename(mdFileName))
         # print("markdown source = ", filename)
         # print('markdown full:     ',  os.path.abspath(mdFileName))
         # print('Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         updateImageRefsInFile(os.path.abspath(mdFileName))         
         print('------------------------  end processing ', os.path.basename(mdFileName))
         print('')
         # print("dest   = ", mdfn)

# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(_imgMap)