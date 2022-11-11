import re
import os
import pathlib 
import requests # request img from web
import shutil # save img locally
import glob
import yaml
import json
import pprint



# _topicCategoryURL_RE = re.compile('\(\/category\/.*?\.*?\)')
# _topicLinkRE = re.compile('\((.*\/article\/[^)]*)\)')
# _topicIDRE = re.compile('helpdocs_category_id:.*$')

_topicLinkRE = re.compile('\((https:\/\/n?g?docs.harness.io\/article\/|/article\/).*?\)')
_categoryLinkRE = re.compile('\((https:\/\/n?g?docs.harness.io\/category\/|/category\/).*?\)')
_categoriesDataFile = '../_data/category-mappings.LATEST.json'
_mdRoot = './docs/'
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

def updateLine(mdFileName, line, idx, cDict):
    newLine = line
    linkIsInDictionary = False
    linkNeedsDomain = True
    for match in re.finditer(_categoryLinkRE, line):
         curLink = match.group()
         hd_ID = getHelpDocsID(curLink, "/category/", cDict)
         
         # case 1: found category ID in catalog, replace current link with (/catagory/<developer-hub-category-string>)
         if hd_ID != False: 
            newLinkLocalTarget = cDict[hd_ID]
            newLinkLocalTarget = '(' + newLinkLocalTarget + ')'
            newLine = newLine.replace(curLink, newLinkLocalTarget) 
            # print("[DEBUG7] Category ID found. curLink = ", curLink, " helpdocs ID = ", hd_ID, "\tnewLinkLocalTarget = ", newLinkLocalTarget)
            continue
         else:
            # case 1: category has no local equivalent and no linkNeedsDomain, add domain to current link so it points to the HD target 
            if ("docs.harness.io" in curLink) == False: 
                curLinkPlusDomain = curLink.replace("(", "(https://docs.harness.io")     
                newLine = newLine.replace(curLink, curLinkPlusDomain)
                # print("[DEBUG7] Adding domain. curLink = ", curLink, "\tcurLinkPlusDomain = ", curLinkPlusDomain)
                continue
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
                print("\n[UPDATE_LINK_SUCCESS7] link updated in ", mdFileName)
                print('\tline ', idx, 'original: ', line)
                print('\tline ', idx, 'updated : ', newLine)     
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


with open(_categoriesDataFile, 'w') as fp:
    json.dump(_categoryMap, fp)
