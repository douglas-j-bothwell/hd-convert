import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml

_imageURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')
_imageRefsYamlFileName = './_data/_image-refs.ALL.yml'
_rootFolder = './OUT_markdown'


_DH_REPO_ROOT = os.path.abspath(os.path.join('.', os.pardir))
_commonImagesFolder = _DH_REPO_ROOT + "/_docs_convert/OUT_markdown/static/common/"

# _mdFileName = './delegates/secure-delegates-with-tokens.md'

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
        print('image full:        ', imageFileNameFull)
        return imageFileNameFull

def getImageFileNameRelative(imgFileName, mdFileName): 
    imgFileNameFull = os.path.abspath(imgFileName)
    mdFileNameFull = os.path.abspath(mdFileName) 
    relPath = os.path.relpath(imgFileNameFull, mdFileNameFull)
    print("returning relative path to img: ", relPath)
    return relPath

def getNumRefs(imageURL):
    with open(_imageRefsYamlFileName , 'r') as inFile:
        data = yaml.safe_load(inFile)
        return len(data[imageURL])

def downloadAndSaveImage(imageURL, imageFileNameFull):
    print("testing file name: ", imageFileNameFull)
    print("file exists: ", str(os.path.isfile(imageFileNameFull)))
    return
    
    if os.path.isfile(imageFileNameFull):
       print('Image file exists: ',imageFileNameFull)
       return
    
    res = requests.get(imageURL, stream = True)

    if res.status_code == 200:
        with open(imageFileNameFull,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',imageFileNameFull)
    else:
        print('Image Couldn\'t be retrieved')
        
def replaceImageXrefInMarkdown(mdFileName, imageURL, imageFileNameFull):
    print('')
    # print("cwd = ", os.getcwd())
    # print("replacing image XREFs in file: ", mdFileName)
    # print("imageURL = ", imageURL)
    # print("imageFileNameFull = ", imageFileNameFull)
    print('')
    
    reading_file = open(mdFileName, "r")

    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace(imageURL, imageFileNameFull)
        new_file_content += new_line +"\n"
    reading_file.close()

    writing_file = open(mdFileName, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    print("File updated: ", mdFileName)
    
def updateImageRefsInFile(mdFileName): 
    # idx = 0
    for i, line in enumerate(open(mdFileName)):
        for match in re.finditer(_imageURLpattern, line):
            imageURL = match.group()
            imageFileNameFull = getimageFileNameFull(imageURL, mdFileName )
            # imgFileRefRelative = getImageFileNameRelative(imageFileNameFull, mdFileName)
            # print("imageFileNameFull: ", imageFileNameFull)
            # print("Relative path to img: ", imgFileRefRelative)

            
            # print('Found: ', imageURL)
            # print('target file: ', imageFileNameFull)
            
            downloadAndSaveImage(imageURL, imageFileNameFull)
            
            imgFileNamePath, imgFileName = os.path.split(imageFileNameFull)
            if getNumRefs(imageURL) > 1:
                imgTarget = '/static/common/'  + imgFileName
            else: 
                imgTarget = './static/' + imgFileName
            
            # print("imgTarget: ", imgTarget)
            replaceImageXrefInMarkdown(mdFileName, imageURL, imgTarget)

# updateImageRefsInFile(_mdFileName)

for filename in glob.iglob(_rootFolder + '**/**', recursive=True):
    if filename.endswith('.md'):
         print('')
         print('------------------------  ')
         # print("markdown source = ", filename)
         print('markdown full:     ',  os.path.abspath(filename))
         # print('Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         updateImageRefsInFile(os.path.abspath(filename))         
         print('------------------------  ')
         # print("dest   = ", mdfn)
