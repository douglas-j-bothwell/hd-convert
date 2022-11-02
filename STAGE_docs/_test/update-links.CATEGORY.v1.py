import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import json
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

_topicIDRE = re.compile('helpdocs_category_id:.*$')
_mdRoot = './docs/'
_topicMap = {}
_categoryMap = {}

def getCategoryMap(mdRoot):
    categoryDict = {}
    for jsonFileName in glob.iglob(mdRoot + '**/**', recursive=True):
        # print("[DEBUG] processing file ", jsonFileName)
        if jsonFileName.endswith('.json'):
            with open(jsonFileName, "r") as jsonFile:
                catDict = json.load(jsonFile)
                # print("[DEBUG] catDict = ", catDict )
                if 'label' in catDict:
                    newPath = catDict['label']
                    # print("[DEBUG] newPath (v1) = ", newPath )
                    if 'customProps' in catDict: 
                        cProps = catDict['customProps']
                        if 'helpdocs_category_id' in cProps:
                            newCatID = cProps['helpdocs_category_id']
                            newPath = '/category/' + newPath.replace(' ', '-').lower()
                            # print("[DEBUG] newPath (v2) = ", newPath )
                            # print("[DEBUG] newCatID = ", newCatID )
                            categoryDict[newCatID] = newPath
    return categoryDict
    
def getHelpDocsID(reMatch, splitOn):
    
    reMatchElements = reMatch.split(splitOn)
    # print("[DEBUG] Start URL string: ", reMatch)
    if len(reMatchElements) == 2:
        afterArticleString = reMatchElements[1]
        afterArticleString.strip(')')
        strList = afterArticleString.split('-')
        hd_ID = strList[0]
        print("[DEBUG] hd_ID = ", hd_ID)
        return hd_ID
    return False 
    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)

def updateLinksCategory(mdFileName, cDict):
    updated = False
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
        print("[INFO] processing file ", mdFileName)
        newMarkdown = []
        idx = 1
        updated = False
        for line in mdLines:
            for match in re.finditer(_categoryLinkRE, line):
                print("[INFO] Line ", idx, " Category link found, need to update:\t", line)
                curLink = match.group()
                hd_ID = getHelpDocsID(curLink, "/category/")
                if ("docs.harness.io" in curLink) == False:
                    newLink = curLink.replace("(", "(https://docs.harness.io")
                    print("[DEBUG] curLink = ", curLink)
                    print("[DEBUG] newLink = ", newLink)
                    print("[INFO] newLink now points to docs.harness.io ", idx, '\t', line)
                    updated = True
                if hd_ID in cDict: 
                    newLink = cDict[hd_ID]
                    newLink = '(' + newLink + ')' 
                    print("[INFO] Category ID found. newLink = ", newLink)
                    updated = True                 
                if updated == True:
                    line = line.replace(curLink, newLink)        
                    print("[UPDATE_LINK_SUCCESS] Line ", idx, " updated:\t", line)
                else: 
                    print("[INFO] Target not found in developer-hub retaining link to docs.harness.io ", curLink)
            newMarkdown.append(line)
            idx += 1
        stringListToFile(newMarkdown, mdFileName)

_categoryMap = getCategoryMap(_mdRoot)
        
for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
        updateLinksCategory(mdFileName, _categoryMap)


pp = pprint.PrettyPrinter(depth=4)
"\n\[DEBUG] ntopicMap ="
pp.pprint(_categoryMap)