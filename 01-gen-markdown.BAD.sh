#! bin/bash

'''
npx create-docusaurus@latest developer-hub  classic

cd /Users/douglasbothwell/git_repos/__DEV_LED_PLATFORM/FORK/developer-hub/_docs_convert

python3 gen-md.MARKDOWNIFY.py > ./_logs/gen-md.MARKDOWNIFY.ff.txt

cd STAGE_docs

python3 update-links.DEV.py > ../_logs/update-links.ff.txt

python3 get-images.DEV.py > ../_logs/get-images.ff.txt
'''

echo "Contents of IN_html:"
ls IN_html


echo "Enter branch to check out and press [ENTER]:"
read newBranch
if [$newBranch == "main"]: then
  echo "cannot run this script in a main branch. Exiting."
  exit 1
fi

git checkout -b newBranch

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
python3 gen-md.MARKDOWNIFY.py > ./_logs/gen-markdown.$current_time.txt

echo "Contents of OUT_markdown/MODULE_NAME:"
ls OUT_markdown/MODULE_NAME