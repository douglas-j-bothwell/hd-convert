#bin/bash

echo "Contents of IN_html:"
ls ./IN_html

echo "Enter branch to check out and press [ENTER]:"
read newBranch 
echo "New branch = $newBranch"
if ((newBranch == "main")); then
  echo "cannot run this script in a main branch. Exiting."
  exit 1
fi

git checkout -b newBranch

cd ./IN_html

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo 
python3 gen-md.MARKDOWNIFY.py > gen-markdown.log

../_logs/gen-markdown.$current_time.txt

mv gen-markdown.log ../_logs/$(date -d "today" +"%Y%m%d%H%M").gen-markdown.log

echo "Contents of OUT_markdown/MODULE_NAME:"
ls ../OUT_markdown/MODULE_NAME