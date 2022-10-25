#bin/bash

echo "Contents of IN_html:"
ls ./IN_html

# [[ $junk -eq 2 ]]
echo "Enter a new branch to check out (NOT main) and press [ENTER]:"
read newBranch 
echo "New branch = $newBranch"
if [newBranch == "main"]; then
  echo "New branch is main. NOT RECOMMENDED."
  # exit 1
fi

# git checkout -b newBranch

cd ./IN_html

rm ../_logs/gen-markdown.log
echo "Starting python script: " 
python3 gen-md.MARKDOWNIFY.py > ../_logs/gen-markdown.log
echo "python script ended."
echo "Contents of OUT_markdown/MODULE_NAME:"
ls ../OUT_markdown/MODULE_NAME

