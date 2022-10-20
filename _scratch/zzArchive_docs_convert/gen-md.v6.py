
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
isPublished = 0
isPrivate = 0

def getMarkdownFilename(filename):
    parts = filename.split('/')
    
    mdfTargetPath = _mdfTargetRoot + parts[-3] + '/'
    pathlib.Path(mdfTargetPath).mkdir(parents=True, exist_ok=True) 
    print("folder exists: ", mdfTargetPath)
    
    mdfn = mdfTargetPath + parts[-2] + '.md'
    return mdfn

def getMetaDataFilename(filename):
    metaDirName = os.path.dirname(os.path.abspath(filename))
    metaYAMLfile = metaDirName + '/metadata.yaml'
    return metaYAMLfile
    
def isPublishedAndFeatured(ymlFile):
    with open(ymlFile, "r") as stream:
        ymlData = yaml.safe_load(stream)
    print("checking topic ID ", ymlData['article_id'])
    # if (ymlData['is_published'] == True and ymlData['is_featured'] == True ):
    if (ymlData['is_featured'] == "true" ):
        return True
    else:
        return False

def addIDtoList(topicID):
    if topicID in topicIDlist:
        print("duplicate topic: ", topicID)
        return False
    else:
        topicIDlist.append(topicID) 
        return True      

def topicIsInDOM(metaDataFileName, domFileName):
    with open(metaDataFileName, "r") as metaData:
        ymlData = yaml.safe_load(metaData)
        print("testing articleID ", ymlData['article_id'])
        print("published ", ymlData['is_published'])
        print("private ", ymlData['is_private'])
        print("feature ", ymlData['is_featured'])
        if (ymlData['is_published'] == "true"):
            isPublished += 1
        if (ymlData['is_private'] == "true"):
            isPrivate += 1
        lineNum = 0
        isInDOM = False
        isUnique = False
        with open(domFileName, 'rt') as f:
             dom = f.readlines()
             for line in dom:
                 lineNum += 1
                 if ymlData['article_id'] in line:
                        print("articleID  is in DOM ", lineNum, ": ", line)
                        isInDOM = True
        # 
        if (isInDOM == True):
            isUnique = addIDtoList(ymlData['article_id'])
            if (isUnique == False):
                print("articleID is a dup")
                return False
        else:
            print("articleID is not in DOM")
            return False 
        return True
        
def getFrontMatterStringFromMetadata(ymlFile):
    with open(ymlFile, "r") as stream:
        ymlData = yaml.safe_load(stream)
    
    frontMatter = "---\n"
    frontMatter = frontMatter + "title: " + ymlData['title'] + '\n'
    frontMatter = frontMatter + "description: " + ymlData['short_version'] + '\n'
    
    frontMatter = frontMatter + "tags: " + '\n'
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
    
# https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
def addFrontMatterToMarkdown(string, originalfile):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.remove(originalfile)
    os.rename('newfile.txt',originalfile)    

filesProcessed = 0
filesSkipped = 0
for filename in glob.iglob(_htmlSourceRoot + '**/**', recursive=True):
    if filename.endswith('.html'):
         metaDataFileName = getMetaDataFilename(filename)
         # if (isPublishedAndFeatured(metaDataFileName)):
         if topicIsInDOM(metaDataFileName, _domFileName):
             markdownFileName = getMarkdownFilename(filename)
             # print("source.html = ", filename)
             # print("meta.yml   = ", metaDataFileName)
             # print("dest.md   = ", markdownFileName)
             
             h = markdownify.markdownify(open(filename), heading_style="ATX")
              
             f = open(markdownFileName, "w")
             f.write(h)
             f.close()
             # print("create file ", markdownFileName)
             
             frontMatterString = getFrontMatterStringFromMetadata(metaDataFileName)
             addFrontMatterToMarkdown(frontMatterString, markdownFileName)
             filesProcessed +=1
             # print('++++++++++++++++++++++++++++++++')             
         else: 
             # print("not published: ", filename)
             filesSkipped +=1
             print('--------------------------------')         
         
             
         
         # h = markdownify.markdownify(open(filename), heading_style="ATX")
         
         # f = open(mdfn, "w")
         # f.write(h)
         # f.close()
         # print("create file ", mdfn)
         
         
         
         # print('')
         # print('metaDirName =', metaDirName)
         # print('metaDirFile =', metaDirFile)
         # showFileCommand = "cat " + metaDirFile
         # os.system(showFileCommand)
         # print('')
         
         
print("\n FILES PROCESSED: ", filesProcessed)
print("\n FILES SKIPPED: ", filesSkipped)
print("\n UNIQUE TOPIC IDS: ", len(topicIDlist))
print("\n isPublished: ", isPublished)
print("\n isPrivate: ", isPrivate)