import re
import os
import pathlib
import requests # request img from web
import shutil # save img locally
import glob
import yaml

_imageURLpattern = re.compile('(https?:\/\/.*\.(?:png|jpg))')
_markdownFilesRoot = './OUT_markdown'
_imageRefsYaml = './_image-refs.v2.yml'


def addURLtoDictionary(imageURL, mdFileName, imageURLsDict ): 
        listWithNewFile = [mdFileName]
        if imageURL not in imageURLsDict:
            imageURLsDict[imageURL] = []
        print('ADDING imageURL ', imageURLsDict[imageURL], 'in file ', mdFileName, ' to list ', imageURLsDict[imageURL])
        imageURLsDict[imageURL] = imageURLsDict[imageURL] + listWithNewFile
        return imageURLsDict
        
    
def addImageRefsFromMarkdownFile(mdFileName, imageURLsDict): 
    for i, line in enumerate(open(mdFileName)):
        for match in re.finditer(_imageURLpattern, line):
            imageURL = match.group()
            imageURLsDict = addURLtoDictionary(imageURL, mdFileName, imageURLsDict)            
            # print('imageURL ', imageURLsDict[imageURL], 'in file ', mdFileName, 'imageURL added to list ', imageURLsDict[imageURL])
    return imageURLsDict
            
# imageURLdict = yaml.safe_load(rd)
# print(imageURLdict)
imageURLsDict = {}

for mdFilename in glob.iglob(_markdownFilesRoot + '**/**', recursive=True):
    if mdFilename.endswith('.md'):
        imageURLsDict = addImageRefsFromMarkdownFile(mdFilename, imageURLsDict)
        
        
print("publishing imageURLdict to YAML: ===============================================")
# print(imageURLsDict)

with open(r'./image-references-db.yaml', 'w') as file:
    documents = yaml.dump(imageURLsDict, file)
    
with open(r'./image-references-db.yaml', 'r') as inFile:
    with open(r'./image-refs-count.csv', 'w') as outFile:
        data = yaml.safe_load(inFile)
        for key in data:
            numRefs = len(data[key])
            outString = str(numRefs) + ',' + key + '\n'
            print(outString)
            outFile.write(outString)
    outFile.close()
inFile.close()
         