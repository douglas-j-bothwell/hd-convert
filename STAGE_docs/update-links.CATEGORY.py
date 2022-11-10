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
    print("[DEBUG1] Start URL string: ", reMatch)
    if len(reMatchElements) == 2:
        afterArticleString = reMatchElements[1]
        afterArticleString.strip(')')
        strList = afterArticleString.split('-')
        hd_ID = strList[0]
        hd_ID = hd_ID.strip(')')
        print("[DEBUG1] extracted hd_ID = ", hd_ID)        
        if hd_ID in cDict: 
            print("[DEBUG1] hd_ID is in Dict ", hd_ID)
            return hd_ID
    return False 
    
def stringListToFile(strList, fileName):
    if (os.path.exists(fileName)):
        os.remove(fileName)

    with open(fileName, 'w') as f:
        f.writelines(strList)

def updateLineWithDomain(mdFileName, line, idx, cDict):
    newLine = line
    linkIsInDictionary = False
    linkNeedsDomain = True
    for match in re.finditer(_categoryLinkRE, line):
         curLink = match.group()
         if curLink in cDict.values(): 
             linkIsInDictionary = True
             print("[DEBUG5] Skipping, link ", curLink, " is in dictionary with value ", cDict(curLink))
         if "docs.harness.io" in curLink:
             linkNeedsDomain = False
             print("[DEBUG5] Skipping, link already has domain: ", curLink,)
         if linkIsInDictionary == False and linkNeedsDomain == True:
            print("\n[WARNING] The following link might need updating:")
            print('\tFile: ', mdFileName)
            print('\tline ', idx, 'original: ', line)
            print("\t You need to add \'https://docs.harness.io\' to this link the category ID isn't in the following dictionary:")
            print(cDict)
            print('-----------------')
            '''
            curLinkPlusDomain = curLink.replace("(", "(https://docs.harness.io")     
            newLine = newLine.replace(curLink, curLinkPlusDomain)
            print("\n[UPDATE_LINK_SUCCESS1] Added domain to link:")
            print('\tline ', idx, 'original: ', line)
            print('\tline ', idx, 'updated : ', newLine)
            ''' 
         
    return newLine        


def updateLineWithLocalTarget(mdFileName, line, idx, cDict):
    newLine = line
    for match in re.finditer(_categoryLinkRE, line):
         curLink = match.group()
         newLinkLocalTarget = False
         skipUpdate = False
         hd_ID = getHelpDocsID(curLink, "/category/", cDict)
         print ("[DEBUG2] curLink = ", curLink)
         print("[DEBUG2] line ", idx, '\t', line)

         if hd_ID != False: 
            newLinkLocalTarget = cDict[hd_ID]
            newLinkLocalTarget = '(' + newLinkLocalTarget + ')' 
            print("[DEBUG3] Category ID found. curLink = ", curLink, " helpdocs ID = ", hd_ID, "\tnewLinkLocalTarget = ", newLinkLocalTarget)
                     
         # if we found a local category, replace curLink with newLinkLocalTarget.
         # print("[DEBUG1] line ", idx, '\t', line)
         if newLinkLocalTarget != False:
            # curLink = curLink.replace("(https://docs.harness.io", "")
            newLine = newLine.replace(curLink, newLinkLocalTarget)
            print("[DEBUG3] After replace. curLink = ", curLink, "\tnewLinkLocalTarget = ", newLinkLocalTarget)
            print("\n[UPDATE_LINK_SUCCESS2] Replaced with local target:", idx)
            print('\tline ', idx, 'original: ', line)
            print('\tline ', idx, 'updated : ', newLine) 
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
            newLine = updateLineWithDomain(mdFileName, line, idx, cDict)
            newLine = updateLineWithLocalTarget(mdFileName, newLine, idx, cDict)
            
            newMarkdown.append(newLine)
            if (line != newLine):
                print("[DEBUG4] newLine updated: ", newLine)
                topicUpdated = True
            idx += 1
        stringListToFile(newMarkdown, mdFileName)

        if topicUpdated == True:
            print("[INFO1] File updated: ", mdFileName)
        '''
        else:
            print("[INFO1] File not updated: ", mdFileName)
        '''
        
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