
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
_mdfTargetRoot = './OUT_markdown/' 

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
    
def isPublished(ymlFile):
    with open(ymlFile, "r") as stream:
        ymlData = yaml.safe_load(stream)
    if (ymlData['is_published'] == True and ymlData['is_private'] == False ):
        return True
    else:
        return False
        
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
    
# https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
def addFrontMatterToMarkdown(string, originalfile):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.remove(originalfile)
    os.rename('newfile.txt',originalfile)    

filesProcessed = 0
for filename in glob.iglob(_htmlSourceRoot + '**/**', recursive=True):
    if filename.endswith('.html'):
         metaDataFileName = getMetaDataFilename(filename)
         if (isPublished(metaDataFileName)):
             markdownFileName = getMarkdownFilename(filename)
             print("source.html = ", filename)
             print("meta.yml   = ", metaDataFileName)
             print("dest.md   = ", markdownFileName)
             
             h = markdownify.markdownify(open(filename), heading_style="ATX")
              
             f = open(markdownFileName, "w")
             f.write(h)
             f.close()
             print("create file ", markdownFileName)
             
             frontMatterString = getFrontMatterStringFromMetadata(metaDataFileName)
             addFrontMatterToMarkdown(frontMatterString, markdownFileName)
             filesProcessed +=1
             print('++++++++++++++++++++++++++++++++')             
         else: 
             print("not published: ", filename)
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