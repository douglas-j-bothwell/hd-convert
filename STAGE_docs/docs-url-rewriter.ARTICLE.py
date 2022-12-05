#JSON to URL Re-write Converter
#@Author Ravi Lachhman - ravi.lachhman@harness.io
#@Date Dec 1, 2022

import os
import json

JSON_file_path = "../_data/article-mappings.LATEST.json"
nginx_file_path = "../_data/_article-redirects.LATEST.txt"

with open(JSON_file_path) as json_file:
    data = json.load(json_file)

#Load JSON
if os.path.exists(JSON_file_path):
            with open(JSON_file_path) as f:
                json_data = json.load(f)
else:
    print('File does not exist'.format(JSON_file_path))

#Create File
articleList = open(nginx_file_path, 'a')


#Create URL List
for key, value in json_data.items():
    fromHelpDocsDomain = "https://docs.harness.io/article/" + key + "*"
    toDeveloperHubDomain = "https://developer.harness.io" + value[1:-3]
    articleList.write(fromHelpDocsDomain + ' ' + toDeveloperHubDomain + '\n')

print('File write underway'.format(nginx_file_path))

#Close File
articleList.close()
print('Job Complete')
