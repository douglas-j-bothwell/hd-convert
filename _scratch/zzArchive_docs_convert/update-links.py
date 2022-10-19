import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml

_hdRxArticlePattern = re.compile('\(.*\/article\/.*\)')
_hdRxCategories =  re.compile('\(.*\/category\/.*\)')
_mdRoot = './OUT_markdown/MODULE_NAME/'

_linksUpdated = 0
_categoryRefs = []


def updateLinksInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    print("mdFile = ", mdFileName)

    newMarkdown = []
    linksUpdated = 0
    lineNum = 1
    for line in mdLines:
        for match in re.finditer(_hdRxArticlePattern, line):
            hdLink = match.group()
            print("[WARNING] Link found:")
            print("\t URL  ", hdLink)
            print("\t file ", os.path.basename(mdFileName))
            print("\t line ", lineNum, ": ", line)
            print('')
            _categoryRefs = {}
        # newMarkdown.append(line)
        lineNum += 1
            
    return linksUpdated
    
def getCategoryLinksInFile(mdFileName): 
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
    print("mdFile = ", mdFileName)

    categoryRefs = {}
    lineNum = 1
    for line in mdLines:
        for match in re.finditer(_hdRxArticlePattern, line):
            hdLink = match.group()
            print("[WARNING] Link found:")
            print("\t URL  ", hdLink)
            print("\t file ", os.path.basename(mdFileName))
            print("\t line ", lineNum, ": ", line)
            print('')
            linksUpdated += 1
        lineNum += 1
            
    return linksUpdated
    
    
    

for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
         print('')
         print(' ------------------------ processing ', os.path.basename(mdFileName))
         # print("markdown source = ", filename)
         # print('markdown full:     ',  os.path.abspath(mdFileName))
         # print('Absolute directoryname: ', os.path.dirname(os.path.abspath(filename)))
         _linksUpdated += updateLinksInFile(os.path.abspath(mdFileName))         
         print('------------------------  end processing ', os.path.basename(mdFileName))
         print('')
         # print("dest   = ", mdfn)
         
print("_linksUpdated = ", _linksUpdated)