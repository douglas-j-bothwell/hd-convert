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
_linksNotUpdated = []

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
    
def getHelpDocsID(reMatch, splitOn, cDict):
    
    reMatchElements = reMatch.split(splitOn)
    # print("[DEBUG] Start URL string: ", reMatch)
    if len(reMatchElements) == 2:
        afterArticleString = reMatchElements[1]
        afterArticleString.strip(')')
        strList = afterArticleString.split('-')
        hd_ID = strList[0]
        # print("[DEBUG] extracted hd_ID = ", hd_ID)
        if hd_ID in cDict: 
            return hd_ID
    return False 
    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)
        
def updateLine(mdFileName, line, idx, cDict):
    newLine = line
    for match in re.finditer(_categoryLinkRE, line):
         curLink = match.group()
         newLine = newLine
         newLinkLocalTarget = False
         skipUpdate = False
         hd_ID = getHelpDocsID(curLink, "/category/", cDict)
         print ("[DEBUG1] curLink = ", curLink)
         # print("[DEBUG1] line ", idx, '\t', line)

         if hd_ID != False: 
            newLinkLocalTarget = cDict[hd_ID]
            newLinkLocalTarget = '(' + newLinkLocalTarget + ')' 
            print("[DEBUG] Category ID found. helpdocs ID = ", hd_ID, "\tnewLinkLocalTarget = ", newLinkLocalTarget)
                     
         # step 2 -- if we found a local category, replace curLink with newLinkLocalTarget.
         # print("[DEBUG1] line ", idx, '\t', line)
         if newLinkLocalTarget != False:
            newLine = line.replace(curLink, newLinkLocalTarget)
            print("\n[UPDATE_LINK_SUCCESS1] Replaced with local target on line ", idx)
            print('\toriginal: ', line)
            print('\tupdated:  ', newLine) 
         else:
            # step 3 -- if there's no local category, but the current link needs the domain, replace curLink with curLinkPlusDomain. 
            print("\n[WARNING] Skipping link on line ", idx, ", you might need to update it manually. Remove this link, check if the category link is already in the catalog (see end of log), or add the domain https:/docs.harness.io to the link. ")
            print('\toriginal: ', line)
            if curLink not in _linksNotUpdated:
                _linksNotUpdated.append(curLink)
    return newLine

def updateTopic(mdFileName, cDict):
    updated = False
    with open(mdFileName, "r") as mdFile:
        mdLines = mdFile.readlines()
        print("\n\n[INFO] processing file ", mdFileName)
        idx = 1
        newMarkdown = []
        topicUpdated = False 
        for line in mdLines:
            newLine = updateLine(mdFileName, line, idx, cDict)
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



_categoryMap = getCategoryMap(_mdRoot)
        
for mdFileName in glob.iglob(_mdRoot + '**/**', recursive=True):
    if mdFileName.endswith('.md'):
        updateTopic(mdFileName, _categoryMap)


"\n\n[DEBUG] ntopicMap ="
pp1 = pprint.PrettyPrinter(depth=4)
pp1.pprint(_categoryMap)

"\n\\n[DEBUG] links not updated ="
pp2 = pprint.PrettyPrinter(depth=4)
pp2.pprint(_linksNotUpdated)