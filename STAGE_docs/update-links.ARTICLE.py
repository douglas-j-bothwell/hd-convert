import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import pprint

'''
https://regex101.com/
test strings:
(https://ngdocs.harness.io/article/e7yidxmtmj-add-azure-connector#before_you_begin)
(/article/e7yidxmtmj)
(https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) or a [Canary Deployment](https://www.infoworld.com/article/3644449/how-canary-releases-enable-continuous-deployment.html)
(https://app.harness.io/auth/#/signup/?module=cf).  Creating and executing a Feature Flag for the React app is pretty straightforward. Depending on your language, Feature Flags requires the use of a corresponding SDK (software development kit), which is installed as a dependency in your application.  Since this example application is React, we can leverage the [JavaScript Feature Flags SDK](https://docs.harness.io/article/bmlvsxhp13-java-script-sdk-references)
Since this example application is React, we can leverage the [JavaScript Feature Flags SDK](https://docs.harness.io/article/bmlvsxhp13-java-script-sdk-references)
Since this example application is React, we can leverage the [JavaScript Feature Flags SDK](/article/e7yidxmtmj)
(/article/ltt65r6k39-set-up-cost-visibility-for-kubernetes), [AWS](/article/80vbt5jv0q-set-up-cost-visibility-for-aws), [GCP](/article/kxnsritjls-set-up-cost-visibility-for-gcp), and [Azure](/article/v682mz6qfd-set-up-cost-visibility-for-azure)
'''

'''
(.*?\/article\/[^)]*?)\)
(https://ngdocs.harness.io/article/e7yidxmtmj-add-azure-connector#before_you_begin)
(/article/e7yidxmtmj)
(https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) or a [Canary Deployment](https://www.infoworld.com/article/3644449/how-canary-releases-enable-continuous-deployment.html)
'''

_topicLinkRE = re.compile('\((https:\/\/n?g?docs.harness.io\/article\/|/article\/).*?\)')
_categoryLinkRE = re.compile('\((https:\/\/n?g?docs.harness.io\/category\/|/category\/).*?\)')
# _topicCategoryURL_RE = re.compile('\(\/category\/.*?\.*?\)')
# _topicLinkRE = re.compile('\((.*\/article\/[^)]*)\)')

_topicIDRE = re.compile('helpdocs_topic_id:.*$')
_mdRoot = './docs/'
_topicMap = {}

def getTopicMap(mdFileName):
    topicMap = {}
    for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
        if mdFileName.endswith('.md'):
            topicID = getTopicID(mdFileName)
            if topicID != False:
                topicMap[topicID] = mdFileName
    return topicMap

def getTopicID(mdFileName):
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
        # print("mdFile = ", mdFileName)
        for line in mdLines:
           for match in re.finditer(_topicIDRE, line):
              tLine = match.group()
              tLineElements = tLine.split()
              if len(tLineElements) > 1:
                  # print("[DEBUG] .md found. tLineElements = ", tLineElements )
                  topicID = tLineElements[1]
                  return topicID
    return False  
    
def getTopicFromID(topicID):
    if topicID in _topicMap.keys():
        return _topicMap[topicID]
    return False        

def getTopicFileFromURL(reMatch):
    # print("[DEBUG] Start URL string: ", reMatch)
    reMatchElements = reMatch.split("/article/")
    if len(reMatchElements) == 2:
        afterArticleString = reMatchElements[1]
        afterArticleString.strip(')')
        strList = afterArticleString.split('-')
        topicID = strList[0]
        # print("[DEBUG] urlString to getTopicFromID:\t", topicID)
        topicFile = getTopicFromID(topicID)
        if topicFile != False: 
            return topicFile               
    return False 
    

def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)
        
def getSectionTag(reMatch):
    
    reMatchElements = reMatch.split("#")
    if len(reMatchElements) == 2:
        sectionTag = reMatchElements[1]
        sectionTag = sectionTag.replace('_', '-')
        sectionTag = sectionTag.strip(')')
        print("[DEBUG4] section tag in ", reMatch, " found, returning ", sectionTag)
        return sectionTag
    return False


def getHelpDocsID(reMatch, splitOn):
    
    reMatchElements = reMatch.split(splitOn)
    # print("[DEBUG] Start URL string: ", reMatch)
    # if (1 == 1):    # for debugging
    if len(reMatchElements) == 2:
        afterArticleString = reMatchElements[1]
        split_string = re.split(r'[-#/]', afterArticleString)
        hd_ID = split_string[0]
        hd_ID = hd_ID.strip(')')
        # print( "[DEBUG] split_string = ", split_string )
        # print( "[DEBUG] hd_ID = ", hd_ID  )
        return hd_ID
    print("[DEBUG2] split on ", splitOn, " failed, returning FALSE")
    return False 
    

def updateLine(mdFileName, line, idx, aDict):
    newLine = line
    for match in re.finditer(_topicLinkRE, line):
         curLink = match.group()
         curLinkPlusDomain = False 
         newLinkLocalTarget = False
         # print ("[DEBUG1] curLink = ", curLink)
         # print("[DEBUG1] line ", idx, '\t', line)
         
         # step 1 -- If curLink does not include the domain, create curLinkPlusDomain
         #        before: (/article/ljlkj) 
         #        after:  (https://docs.harness.io/article/ljlkj)
         if ("docs.harness.io" in curLink) == False:
             curLinkPlusDomain = curLink.replace("(", "(https://docs.harness.io")
             # print("[INFO1] adding docs.harness.io to link.", idx, '\t', line)
             # print("[DEBUG1]Line ", idx, " link updated: ",  curLink, " > ", curLinkPlusDomain)    

         hd_ID = getHelpDocsID(curLink, "/article/")
         print("[DEBUG1] HelpDocs ID = ", hd_ID)
         if hd_ID in aDict: 
             newLinkLocalTarget = aDict[hd_ID]
             print("[DEBUG3] newLinkLocalTarget found:\t", newLinkLocalTarget)                                  
             srcPath, srcFile = os.path.split(mdFileName)
             relPath = os.path.relpath(newLinkLocalTarget, srcPath)
         
         # step 3 -- if we created a new link, update the line.
         if newLinkLocalTarget != False:
            sectionTag = getSectionTag(curLink)
            if sectionTag != False:
                sectionTag = newLinkLocalTarget + '#' + sectionTag                
                print("[WARNING3] Original link points to subsection, tag might be incorrect: ", sectionTag) 
                newLinkLocalTarget = '(' + relPath + sectionTag + ')'
            else:
                newLinkLocalTarget = '(' + relPath +  ')'                  
            newLine = newLine.replace(curLink, newLinkLocalTarget)
         else:
            if curLinkPlusDomain != False: 
                newLine = newLine.replace(curLink, curLinkPlusDomain)     
         if newLine != line:                
            print("\n[UPDATE_LINK_SUCCESS3] line updated:")
            print("\tline ", idx, "original:\t", line)
            print("\tline ", idx, "upated:\t", newLine)
            # else: 
                # print("[DEBUG1] Link not updated: ", curLink)
    return newLine

def updateTopic(mdFileName, aDict):
    updated = False
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
        print("\n\n[INFO] processing file ", mdFileName)
        idx = 1
        newMarkdown = []
        topicUpdated = False 
        for line in mdLines:
            newLine = updateLine(mdFileName, line, idx, aDict)
            newMarkdown.append(newLine)
            if (line != newLine):
                topicUpdated = True
            idx += 1
        stringListToFile(newMarkdown, mdFileName)

        if topicUpdated == True:
            print("[INFO1] File updated: ", mdFileName)
        else:
            print("[INFO1] File not updated: ", mdFileName)
        
        # print('[DEBUG] ======================================================\n')



_topicMap = getTopicMap(_mdRoot)

for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
        updateTopic(mdFileName, _topicMap)
        # updateLinksCategory(mdFileName)
        


pp = pprint.PrettyPrinter(depth=4)
pp.pprint(_topicMap)