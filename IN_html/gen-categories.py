
# NOTE -- This script requires the following:
# python3 -- to check if installed, run:
# $ python3 --version

# Once you install python3, you also need to install the following libraries:
# pip3 install markdownify
# pip3 install pyyaml


import glob
import os
import re 
import pathlib
import markdownify
import yaml  
import json
# pip3 install markdownify
# pip3 install pyyaml

_htmlSourceRoot  = './'
_mdfTargetRoot = '../OUT_markdown/MODULE_NAME/' 
_domFileName = '../_data/_dom.LATEST.html'

_categoryDict = {
  "label": "Label TBD", 
  "collapsible": "true",
  "collapsed": "true",
  "className": "red",
  "link": {
    "type": "generated-index",
    "title": "Title TBD"
  },
  "customProps": {
      "position" : "To position the category, enter a number and move this to the root level.",
      "helpdocs_category_id" : "HelpDocs category hash string TBD"
  }
}

topicIDlist = []
topicsPublished = 0
topicsPrivate = 0
topicsInDOM= 0
filesProcessed = 0
filesSkipped = 0

'''
# GENERATE MARKDOWN USING PANDOC
# https://boisgera.github.io/pandoc/markdown/ 
# https://docs.python.org/3/library/subprocess.html#replacing-os-system       
def createMarkdown(htmlFileName, markdownFileName, frontMatterString):
     # generate strict markdown
     # execArgs = ["pandoc", "-s", "-o", markdownFileName, htmlFileName]
     # generate markdown with default settings
     execArgs = ["pandoc", "-o", markdownFileName, htmlFileName]
     result = subprocess.run(execArgs,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
     print(result.stderr)
     with open(markdownFileName, 'r') as f:
         mdString = f.read()
     os.remove(markdownFileName)
     with open(markdownFileName,'w') as f:
            f.write(frontMatterString)
            f.write(mdString)    
     return True
'''

def getMetaDataFilename(filename):
    parts = filename.split('/')
    
    metaTargetPath = _mdfTargetRoot + parts[-3] + '/'
    pathlib.Path(metaTargetPath).mkdir(parents=True, exist_ok=True) 
    
    mdfn = metaTargetPath + '_category_.json'
    return mdfn

def createCategory(metaData, ymlFileName, categoryDict):
    
        metaDataFileName = getMetaDataFilename(ymlFileName)

        # update the category dictionary with the title and category id from the metadata file 
        # print("[DEBUG] metaData", metaData)
        if 'title' in metaData:
            categoryDict['label'] = metaData['title'] 
            newLink = categoryDict['link']
            newLink['title'] = metaData['title']
            categoryDict['link'] = newLink
            # print("[DEBUG] metaData['title'] ", metaData['title'])

        if 'category_id' in metaData:
            newProps = categoryDict['customProps']
            newProps['helpdocs_category_id'] = metaData['category_id']
            categoryDict['customProps'] = newProps
            # print("[DEBUG] metaData['category_id'] ", metaData['category_id'])

        if 'parent_category_id' in metaData:            
            newProps = categoryDict['customProps']
            newProps['helpdocs_parent_category_id'] = metaData['parent_category_id']
            categoryDict['customProps'] = newProps
            # print("[DEBUG] metaData['category_id'] ", metaData['category_id'])
                
        # save the category json to the category file
        # print('[DEBUG] categoryDict = ', categoryDict)
        print('[INFO] saving category: ', metaDataFileName)
        with open(metaDataFileName, 'w') as fp:
            json.dump(categoryDict, fp)            
    

for yamlFileName in glob.iglob(_htmlSourceRoot + '**/**', recursive=True):
    if yamlFileName.endswith('.yaml'):
         with open(yamlFileName, "r") as stream:
                 metaData = yaml.safe_load(stream)
                 if metaData['type'] == 'category':
                     createCategory(metaData, yamlFileName, _categoryDict)