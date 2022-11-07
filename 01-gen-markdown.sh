#bin/bash


# download a helpdocs page that includes the sidebar menu
# the gen-md.*.py scripts use this to determine if a topic is in the public docs
rm ./_data/_dom.LATEST.html
curl https://docs.harness.io/category/zgffarnh1m-ci-category --output ./_data/_dom.LATEST.html

echo "Contents of IN_html:"
ls ./IN_html
cd ./IN_html

rm ../_logs/01a-gen-markdown.log
rm ../_logs/01b-gen-categories.log

echo "Starting python script: " 
python3 gen-markdown.py > ../_logs/01a-gen-markdown.log
python3 gen-categories.py > ../_logs/01b-gen-categories.log

# python3 gen-md.md.DOM-ONLY.py > ../_logs/gen-markdown.log
echo "python script ended."
echo "Contents of OUT_markdown/MODULE_NAME:"
ls ../OUT_markdown/MODULE_NAME

