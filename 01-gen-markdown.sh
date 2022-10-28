#bin/bash

'''
# [[ $junk -eq 2 ]]
echo "Enter a new branch to check out (NOT main) and press [ENTER]:"
read newBranch 
echo "New branch = $newBranch"
if [newBranch == "main"]; then
  echo "New branch is main. NOT RECOMMENDED."
  # exit 1
fi
'''

# download a helpdocs page that includes the sidebar menu
# the gen-md.*.py scripts use this to determine if a topic is in the public docs
rm ./_data/_dom.LATEST.html
curl https://docs.harness.io/category/zgffarnh1m-ci-category --output ./_data/_dom.LATEST.html

echo "Contents of IN_html:"
ls ./IN_html
cd ./IN_html

rm ../_logs/gen-markdown.log
echo "Starting python script: " 
python3 gen-md.MARKDOWNIFY.v2.py > ../_logs/gen-markdown.log
echo "python script ended."
echo "Contents of OUT_markdown/MODULE_NAME:"
ls ../OUT_markdown/MODULE_NAME

