import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import pprint

_imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')

# _imgURLpattern = re.compile('https:\/\/files.helpdocs.io[%5E/s)/]]*')

'''
_imageRefsFile = '../_data/_image-refs.TEST.yml'
with open(_imageRefsFile , 'r') as inFile:
    _imgRefsDict = yaml.safe_load(inFile)
'''
_mdRoot = './docs/'
_imgMap = {}
_download_cmds = []

# Given an image URL, an image filename, and a markdown file, do the following:
# 1. Add the URL and markdown to the image catalog.
# 2. Download the image and save it using the image filename, then return the full path to the new image file. 
# 3. If the file can't be downloaded:
#    a) Generate a curl command that MIGHT work if it's edited manually. 
#    b) Return False. 
# This catalog gets printed out at the end of the script.
# Print a warning if the same URL is referenced in multiple files. 
def getImage(imgURL, imageFileNameFull, mdFile):
    
    addImageRefToCatalog(imgURL, mdFile)
    
    res = requests.get(imgURL, stream = True)
    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        # # print('[DEBUG] Image downloaded:           ',imageFileNameFull)
        return os.path.abspath(imageFileNameFull)
    else:
        # '''
        print('[WARNING2] Image download failed:      ', imgURL)
        print('\tTry the curl command, see end of log')
        commentString = "# file not downloaded in " + mdFile
        _download_cmds.append(commentString)
        commandString = "curl -o LOCAL_IMAGE_FILENAME " + imageFileNameFull + " " + imgURL 
        _download_cmds.append(commandString)
        # '''
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

# For every image URL found by the regex, add the URL and markdown files referencing that URL to a catalog. 
# This catalog gets printed out at the end of the script.
# Print a warning if the same URL is referenced in multiple files. 
def addImageRefToCatalog(imgURL, mdFile):
    if imgURL in _imgMap.keys():
        mdFileList = _imgMap[imgURL]
    else:
        mdFileList = []
    mdFileList.append(mdFile)
    # '''
    if len(mdFileList) > 1:
        print('-------------------------')
        print('[WARNING1] Image URL referenced in multiple topics:      ', imgURL)
        print('Image filename:      ', imgURL)
        print('Topics list:')
        print(mdFileList)
        print('-------------------------')
    # '''
    _imgMap[imgURL] = mdFileList
    return mdFileList
        
# Given a markdown filename, return the full path to a new image that is yet to be downloaded.
# The main loop will use this path when it downloads and save the image
# Each image is saved in a .static/ subfolder of the markdown file that references it.
# For example:
# ../set-up-test-intelligence
#    set-up-test-intelligence.md
#    /static/
#    set-up-test-intelligence-01.png
#    set-up-test-intelligence-02.png
#    ...
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

# Given the full path to an image file, return the local target to use 
# in the markdown file that will reference it.
# For example, ./static/run-ci-scripts-003.png
def getImageTarget(imgFileName):     
    imgPath, imgName = os.path.split(imgFileName)
    return "./static/" + imgName   

# Given a markdown file, apply the _imgURLpattern regex.
# For each match in the file, do the following: 
#     1. Get the filename for the downloaded image (getimageFileNameFull). 
#        Each filename is based on the markdown file referencing that image and a calculated index.
#        The image gets saved in a ./static subfolder under the markdown file will reference it.
#        For example, ./static/run-ci-scripts-003.png
#     2. Download and save the target (getImage)
#        Returns the full path to the downloaded image, or False if it couldn't be downloaded. 
#     3. If the file was downloaded, image the image reference in the markdown (getImage)
#        For example, ./static/run-ci-scripts-003.png

def updateImageRefsInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    # print("[DEBUG] mdFile = ", mdFileName)

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
                # print("[ERROR2] Image not downloaded, reference not updated:")
                
                print("\t Failed download: ", imgURL)
                # print("\t file ", os.path.basename(mdFileName))
                # print("\t line ", idx, ": ", line)
                # print('')
        newMarkdown.append(line)
        idx += 1
            
    stringListToFile(newMarkdown, mdFileName)



# MAIN LOOP 
# For each markdown file in the .docs folder, run updateImageRefsInFile
for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
         # print('[DEBUG]  ------------------------ processing ', os.path.basename(mdFileName))
         # # print("[DEBUG] markdown source = ", filename)
         # # print('[DEBUG] markdown full:     ',  os.path.abspath(mdFileName))
         # # print('[DEBUG] Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         updateImageRefsInFile(os.path.abspath(mdFileName))         
         # print('[DEBUG] ------------------------  end processing ', os.path.basename(mdFileName))
         # print('')
         # print("dest   = ", mdfn)


# print("Try the following commands to download these image files: ")
# pp1 = pprint.PrettyPrinter(depth=4)
for line in _download_cmds:
    print(line)

pp2 = pprint.PrettyPrinter(depth=4)
pp2.pprint(_imgMap)