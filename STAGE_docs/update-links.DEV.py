import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import pprint

# _topicLinkRE = re.compile('\((.*\/article\/[^)]*)\)')
_topicLinkRE = re.compile('\((https:\/\/n?g?docs.harness.io\/article\/|/article\/).*?\)')
# _topicLinkURL_RE = re.compile('\(https:\/\/n?g?docs.harness.io\/article\/.*?\)')
# _topicLinkArticle_RE = re.compile('\(\/article\/.*?\)')
_categoryLinkRE = re.compile('\((https:\/\/n?g?docs.harness.io\/category\/|/category\/).*?\)')
# _topicCategoryURL_RE = re.compile('\(\/category\/.*?\.*?\)')


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

_topicIDRE = re.compile('helpdocs_topic_id:.*$')
_mdRoot = './docs/'
_topicMap = {}

'''
(.*?\/article\/[^)]*?)\)
(https://ngdocs.harness.io/article/e7yidxmtmj-add-azure-connector#before_you_begin)
(/article/e7yidxmtmj)
(https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) or a [Canary Deployment](https://www.infoworld.com/article/3644449/how-canary-releases-enable-continuous-deployment.html)
'''

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

'''
(.*?\/article\/[^)]*?)\)
(https://ngdocs.harness.io/article/e7yidxmtmj-add-azure-connector#before_you_begin)
(/article/e7yidxmtmj)
(https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) or a [Canary Deployment](https://www.infoworld.com/article/3644449/how-canary-releases-enable-continuous-deployment.html)
'''
def getTopicFileFromURL(reMatch):
    # print("[DEBUG] Start URL string: ", reMatch)
    reMatchElements = reMatch.split("/article/")
    if len(reMatchElements) == 2:
        afterArticleString = reMatchElements[1]
        afterArticleString.strip(')')
        strList = afterArticleString.split('-')
        topicID = strList[0]
        # print("{DEBUG] urlString to getTopicFromID:\t", topicID)
        topicFile = getTopicFromID(topicID)
        if topicFile != False: 
            return topicFile               
    return False 
    
def urlPointsToSection(urlString):
    if "#" in urlString:
        return True 
    return False

def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)

def updateLinksArticle(mdFileName):
    updated = False
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
        # print('[DEBUG] updateLinksArticleURL ======================================================')
        # print("[DEBUG] processing file ", mdFileName)
        updated = False
        newMarkdown = []
        idx = 1
        for line in mdLines:
            for match in re.finditer(_topicLinkRE, line):
                 curLink = match.group()
                 newLink = getTopicFileFromURL(curLink)
                 # print("[DEBUG] line ", idx, "---------------------------------------------------------")
                 # print("[DEBUG] Link found. curLink = ", curLink)
                 # print("[DEBUG] Match found. newLink = ", newLink)
                 if newLink != False: 
                    srcPath, srcFile = os.path.split(mdFileName)
                    relPath = os.path.relpath(newLink, srcPath)
                    # print("[DEBUG] relPath = ", relPath)
                    newLink = '(' + relPath + ')'                  
                    line = line.replace(curLink, newLink)
                    print("[UPDATE_LINK_SUCCESS] Line ", idx, " updated:\t", line)
                    if urlPointsToSection(curLink):                     
                         print("[WARNING] Topic section removed from old link: ", curLink)
                    updated = True
                    # print('---------------------------------------------------------')
                 else:
                    if ("docs.harness.io" in curLink) == False:
                        newLink = curLink.replace("(", "(https://docs.harness.io")
                        # print("[INFO] Adding URL path to curLink ", curLink)
                        # print("[INFO] newLink = ", newLink)
                        line = line.replace(curLink, newLink)
                        print("[UPDATE_LINK_SUCCESS] Line ", idx, '\t', line)
                    else:
                        print("[INFO] Topic not found, retaining link to docs.harness.io ", curLink)
            newMarkdown.append(line)
            idx += 1
        stringListToFile(newMarkdown, mdFileName)
        '''
        if updated == True:
            print("[INFO] File updated: ", mdFileName)
        else:
            print("[INFO] File not updated: ", mdFileName)
        '''
        # print('[DEBUG] ======================================================\n')

def updateLinksCategory(mdFileName):
    updated = False
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
        print("[INFO] processing file ", mdFileName)
        newMarkdown = []
        idx = 1
        for line in mdLines:
            for match in re.finditer(_categoryLinkRE, line):
                catLink = match.group()
                newLink = catLink.replace("(/category/", "")
                newLink = newLink.replace(")", "")
                newLink = '**TODO:** Update category link ' + catLink
                line = line.replace(catLink, newLink)
                print("[WARNING2] Line ", idx, " Category link found, need to update:\t", line)
            newMarkdown.append(line)
            idx += 1
        stringListToFile(newMarkdown, mdFileName)


_topicMap = getTopicMap(_mdRoot)

for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
        updateLinksArticle(mdFileName)
        updateLinksCategory(mdFileName)
        


# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(_topicMap)