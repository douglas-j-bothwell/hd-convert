import re
import os
import pathlib
import requests # request img from web
import shutil # save img locally
import glob

_imageURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')
_rootFolder = './DONT-RUN-ON-THE-WHOLE-DOC'

# _mdFileName = './delegates/secure-delegates-with-tokens.md'

def getimageFileNameFull(imageURL, mdFileName, idx):
        mdPath, mdFileName = os.path.split(mdFileName)
        mdFileName, mdExt = os.path.splitext(mdFileName)
        
        imgRoot, imgExt = os.path.splitext(imageURL)
        imageTargetFolder = mdPath + '/static/'
        imageTargetFile = mdFileName + '-' + str(idx).zfill(2) + imgExt
        
        pathlib.Path(imageTargetFolder).mkdir(parents=True, exist_ok=True)
        imageFileNameFull = imageTargetFolder + imageTargetFile
        print("imageFileNameFull: ", imageFileNameFull)
        return imageFileNameFull

def downloadAndSaveImage(imageURL, imageFileNameFull):
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
    print("cwd = ", os.getcwd())
    print("replacing image XREFs in file: ", mdFileName)
    print("imageURL = ", imageURL)
    print("imageFileNameFull = ", imageFileNameFull)
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
    idx = 0
    for i, line in enumerate(open(mdFileName)):
        for match in re.finditer(_imageURLpattern, line):
            imageURL = match.group()
            idx += 1
            imageFileNameFull = getimageFileNameFull(imageURL, mdFileName, idx )
            
            print('Found: ', imageURL)
            print('target file: ', imageFileNameFull)
            
            downloadAndSaveImage(imageURL, imageFileNameFull)
            
            imgFileNamePath, imgFileName = os.path.split(imageFileNameFull)
            imgTarget = './static/' + imgFileName
            print("imgTarget: ", imgTarget)
            replaceImageXrefInMarkdown(mdFileName, imageURL, imgTarget)

# updateImageRefsInFile(_mdFileName)

for filename in glob.iglob(_rootFolder + '**/**', recursive=True):
    if filename.endswith('.md'):
         print("source = ", filename)
         print('Absolute path of file:     ',  os.path.abspath(filename))
         print('Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         print('')
         updateImageRefsInFile(os.path.abspath(filename))         
         # print("dest   = ", mdfn)
