import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml

# _imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')
_imgURLpattern = re.compile('(https?:\/\/files.helpdocs.io\/.*?\.(?:png|jpg))')


_mdRoot = './docs/'
# _imgRoot = './OUT_markdown/MODULE_NAME/static/'
_imgRefs = {}


def getImage(imgURL, imageFileNameFull, mdFile):
    
    res = requests.get(imgURL, stream = True)

    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        # print('Image downloaded:           ',imageFileNameFull)
        addImageToMap(imgURL, imageFileNameFull, mdFile)
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

def addImageToMap(imgURL, imgFile, mdFile):
    imgPath, imgFile = os.path.split(imgFile)
    imgRelPath = os.path.relpath(_mdRoot, imgPath)
    imgTarget = imgRelPath + imgFile
    
    if imgURL in _imgRefs.keys():
        refsList = _imgRefs[imgURL] 
        print('-------------------------')
        print('[WARNING] Image URL also referenced in topics:      ', imgURL)
        print('Image filename:      ', imgFile)
        print('Topics list:')
        print(*refsList, sep = "\n")
        print('-------------------------')
    else:
        refsList = []
        
    refsList.append(mdFile)     
    _imgRefs[imgURL] = refsList
            
    return refsList
    
        
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
             imgURL = imgURL.strip('()')
             imgFileName = getimageFileNameFull(imgURL, mdFileName)
             if getImage(imgURL, imgFileName, mdFileName) != False: 
                imgTarget = getImageTarget(imgFileName)
                
                # print('')
                # print('______________________________________________________')
                # print("mdFileName = ", mdFileName)
                # print("imgURL = ", imgURL)
                # print("imgTarget = ", imgTarget)
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

print("_imgRefs = ", _imgRefs)