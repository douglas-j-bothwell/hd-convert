#bin/bash

echo "========================================"
echo "Running ./STAGE_docs/update-links.CATEGORY.sh:"
echo "========================================"
ls ./IN_html

cd ./STAGE_docs/

rm ./_logs/update-links.CATEGORY.log
rm ./_data/category-mappings.LATEST.json

echo "Starting python script: hd-convert/_logs/update-links.CATEGORY.log " 
python3  update-links.CATEGORY.py > ../_logs/update-links.CATEGORY.log
echo "python script ended, links updated."
echo "========================================"
