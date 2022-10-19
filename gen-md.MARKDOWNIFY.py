
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
# pip3 install markdownify
# pip3 install pyyaml

_htmlSourceRoot  = './IN_html/'
_mdfTargetRoot = './OUT_markdown/MODULE_NAME/' 
_domFileName = '_data/_dom.LATEST.html'

topicIDlist = []
topicsPublished = 0
topicsPrivate = 0
topicsInDOM= 0
filesProcessed = 0
filesSkipped = 0

    
def topicIsPublished(metaDict):
    print( metaDict['article_id'], " is published: ", metaDict['is_published'])
    if (metaDict['is_published'] == "true" ):
        topicsPublished += 1
        return True
    else:
        return False
        
def topicIsPrivate(metaDict):
    print( metaDict['article_id'], "is private: ", metaDict['is_private'])
    if (metaDict['is_private'] == "true" ):
        print("private ", ymlData['is_private'])
        topicsPrivate += 1
        return True
    else:
        return False

def getTopicRefsInDOM(metaDict, dom):
     refsInDOM = 0
     lineNum = 0
     print("testing topic ID ", metaDict['article_id'])
     for line in dom:
         lineNum += 1
         if metaDict['article_id'] in line:
                print("articleID in DOM ", lineNum, ": ", line)
                refsInDOM += 1
     if (refsInDOM > 1):
         print("[DEBUG] multiple refs in DOM")
     print('[DEBUG] refsInDOM', str(refsInDOM))
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

def getFrontMatterString(ymlData):
        frontMatter = "---\n"
        
        frontMatter = frontMatter + "title: " + ymlData['title'] + '\n'

        # need to replace colon character with entity in description value, 
        # since the frontmatter is YAML. Otherwise Docusaurus chokes.
        description = ymlData['short_version']
        description = description.replace(':','&#58;' )
        frontMatter = frontMatter + "description: " + description + '\n'
        
        frontMatter = frontMatter + "tags: " + '\n'
        frontMatter = frontMatter + "   - helpDocs" + '\n'
        tags = ymlData['tags']
        for t in tags:
            frontMatter = frontMatter + "   - " + t + '\n'
        
        frontMatter = frontMatter + "helpdocs_topic_id: " + ymlData['article_id'] + '\n'
        frontMatter = frontMatter + "helpdocs_is_private: " + str(ymlData['is_private']).lower() + '\n'
        frontMatter = frontMatter + "helpdocs_is_published: " + str(ymlData['is_published']).lower() + '\n'
        frontMatter = frontMatter + "---\n\n"
        
        # print(frontMatter)
        return frontMatter
        
def getBooleanFromString(inString):
    if (inString == "true"):
        return "True" 
    return "False"
        
def createMarkdown(htmlFileName, markdownFileName, frontMatterString):
     with open(markdownFileName,'w') as f:
            f.write(frontMatterString)
            md = markdownify.markdownify(open(htmlFileName), heading_style="ATX")  
            f.write(md)    
     return True
    
domString = getDOMstring(_domFileName)

for htmlFileName in glob.iglob(_htmlSourceRoot + '**/**', recursive=True):
    if htmlFileName.endswith('.html'):

         metaDataFileName = getMetaDataFilename(htmlFileName)
         markdownFileName = getMarkdownFilename(htmlFileName)
         fmDict = getFrontMatterDict(metaDataFileName)
         fmString = getFrontMatterString(fmDict)

         # if (1 == 1):             
         if getTopicRefsInDOM(fmDict, domString) > 0:             
             createMarkdown(htmlFileName, markdownFileName, fmString)
             filesProcessed +=1
             topicIsPublished(fmDict)
             topicIsPrivate(fmDict)
             print('++++++++++++++++++++++++++++++++') 
             print('')               
         else: 
             # print("not published: ", filename)
             filesSkipped +=1
             print('--------------------------------')         
             print('')               
         
         
print("\n FILES PROCESSED: ", filesProcessed)
print("\n FILES SKIPPED: ", filesSkipped)
print("\n UNIQUE TOPIC IDS: ", len(topicIDlist))
print("\n topicsPublished: ", topicsPublished)
print("\n isPrivate: ", topicsPrivate)