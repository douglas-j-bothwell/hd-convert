
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

    
def topicIsPublished(metaDict):
    # print( metaDict['article_id'], "[DEBUG] is published: ", metaDict['is_published'])
    if (metaDict['is_published'] == "true" ):
        topicsPublished += 1
        return True
    else:
        return False
        
def topicIsPrivate(metaDict):
    # print( metaDict['article_id'], "[DEBUG] is private: ", metaDict['is_private'])
    if (metaDict['is_private'] == "true" ):
        print("private ", ymlData['is_private'])
        topicsPrivate += 1
        return True
    else:
        return False

def getTopicRefsInDOM(metaDict, dom):
     refsInDOM = 0
     lineNum = 0
     # print("[DEBUG] testing topic ID ", metaDict['article_id'])
     for line in dom:
         lineNum += 1
         if metaDict['article_id'] in line:
                # print("[DEBUG] articleID in DOM ", lineNum, ": ", line)
                refsInDOM += 1
     # if (refsInDOM > 1):
         # print("[DEBUG] multiple refs in DOM")
     #print('[DEBUG] refsInDOM', str(refsInDOM))
     return refsInDOM

def addIDtoList(topicID):
    if topicID in topicIDlist:
        print("[DEBUG] duplicate topic: ", topicID)
        return False
    else:
        topicIDlist.append(topicID) 
        return True      

def getDOMstring(domFileName):
    with open(domFileName, 'rt') as f:
        dom = f.readlines()
    return dom

def getMarkdownFilename(filename):
    parts = filename.split('/')
    
    mdfTargetPath = _mdfTargetRoot + parts[-3] + '/'
    pathlib.Path(mdfTargetPath).mkdir(parents=True, exist_ok=True) 
    # print("folder exists: ", mdfTargetPath)
    
    mdfn = mdfTargetPath + parts[-2] + '.md'
    return mdfn

def getMetaDataFilename(filename):
    metaDirName = os.path.dirname(os.path.abspath(filename))
    metaYAMLfile = metaDirName + '/metadata.yaml'
    return metaYAMLfile        

def getFrontMatterDict(ymlFile):
    with open(ymlFile, "r") as stream:
        ymlData = yaml.safe_load(stream)
    return ymlData

def getBooleanFromString(inString):
    if (inString == "true"):
        return "True" 
    return "False"

# given the metadata.yaml for the HTML topic, generate a frontmatter string 
# that gets added to the top of the generated markdown file
def getFrontMatterString(ymlData):
        frontMatter = "---\n"
        
        frontMatter = frontMatter + "title: " + ymlData['title'] + '\n'

        # need to replace colon character with ' — ' in description value, 
        # since the frontmatter is YAML. Otherwise Docusaurus chokes.
        description = ymlData['short_version']
        description = description.replace(':',' &#8212; ' )
        frontMatter = frontMatter + "description: " + description + '\n'
        
        frontMatter = frontMatter + "tags: " + '\n'
        frontMatter = frontMatter + "   - helpDocs" + '\n'
        tags = ymlData['tags']
        for t in tags:
            frontMatter = frontMatter + "   - " + t + '\n'
        
        frontMatter = frontMatter + "# sidebar_position: 2\n"
        frontMatter = frontMatter + "helpdocs_topic_id: " + ymlData['article_id'] + '\n'
        frontMatter = frontMatter + "helpdocs_category_id: " + ymlData['category_id'] + '\n'
        frontMatter = frontMatter + "helpdocs_is_private: " + str(ymlData['is_private']).lower() + '\n'
        frontMatter = frontMatter + "helpdocs_is_published: " + str(ymlData['is_published']).lower() + '\n'
        frontMatter = frontMatter + "---\n\n"
        
        # print(frontMatter)
        return frontMatter

def createCategory(htmlFile, mdFile, categoryDict):

        print("[DEBUG] htmlFile = ", htmlFile)
        print("[DEBUG] mdFile = ", mdFile)
        
        # if the category file already exists in the markdown folder, nothing to do.
        mdPath = os.path.dirname(mdFile)
        catJSON = mdPath + '/_category_.json'
        if os.path.exists(catJSON) == True:
            return    
            
        # the metadata file with the category title is in the parent folder (..) of the html file.
        htmlPath = os.path.dirname(htmlFile)
        metadataFile = os.path.abspath(os.path.join(htmlPath, os.pardir)) + '/metadata.yaml'
        print("[DEBUG] metadataFile ", metadataFile)

        # update the category dictionary with the title and category id from the metadata file 
        with open(metadataFile, "r") as stream:
            ymlData = yaml.safe_load(stream)
            print("[DEBUG] ymlData", ymlData)
            if 'title' in ymlData:
                print("[DEBUG] ymlData['title'] ", ymlData['title'])
                categoryDict['label'] = ymlData['title'] 
                newLink = categoryDict['link']
                newLink['title'] = ymlData['title']
                categoryDict['link'] = newLink
            if 'category_id' in ymlData:
                print("[DEBUG] ymlData['category_id'] ", ymlData['category_id'])
                newProps = categoryDict['customProps']
                newProps['helpdocs_category_id'] = ymlData['category_id']
                categoryDict['customProps'] = newProps
                
        # save the category json to the markdown folder
        print("[DEBUG] categoryDict = ", categoryDict)
        with open(catJSON, 'w') as fp:
            json.dump(categoryDict, fp)            

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
    
# '''
# GENERATE MARKDOWN USING MARKDOWNIFY    
def createMarkdown(htmlFileName, markdownFileName, frontMatterString):
     with open(markdownFileName,'w') as f:
            f.write(frontMatterString)
            md = markdownify.markdownify(open(htmlFileName), heading_style="ATX")  
            f.write(md)    
     return True
# '''    

domString = getDOMstring(_domFileName)

for htmlFileName in glob.iglob(_htmlSourceRoot + '**/**', recursive=True):
    if htmlFileName.endswith('.html'):

         metaDataFileName = getMetaDataFilename(htmlFileName)
         markdownFileName = getMarkdownFilename(htmlFileName)
         fmDict = getFrontMatterDict(metaDataFileName)
         fmString = getFrontMatterString(fmDict)

         # By default, this script generates markdown for public topics only
         #             i.e, topics included in the sidebar TOC for docs.harness.io
         # Use 'if (1 == 1):' to generate markdowns for ALL topics whether
         # they're published or not
         # if (1 == 1):    
         if getTopicRefsInDOM(fmDict, domString) > 0:             
             createMarkdown(htmlFileName, markdownFileName, fmString)
             createCategory(htmlFileName, markdownFileName, _categoryDict)
             filesProcessed +=1
             # topicIsPublished(fmDict)
             # topicIsPrivate(fmDict)
             # print('[DEBUG] ++++++++++++++++++++++++++++++++') 
             # print('')               
         else: 
             # print("not published: ", filename)
             filesSkipped +=1
             # print('[DEBUG] --------------------------------')         
             # print('') 
                 
         
print("\n FILES PROCESSED: ", filesProcessed)
print("\n FILES SKIPPED: ", filesSkipped)
print("\n UNIQUE TOPIC IDS: ", len(topicIDlist))
print("\n topicsPublished: ", topicsPublished)
print("\n isPrivate: ", topicsPrivate)