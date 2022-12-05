#bin/bash

echo "========================================"
echo "Running ./STAGE_docs/update-links.CATEGORY.sh:"
echo "========================================"
ls ./IN_html

cd ./STAGE_docs/

rm ../_logs/update-links.CATEGORY.log
rm ../_data/category-mappings.LATEST.json
rm ../_data/category-mappings.LATEST.txt

echo "Starting python scripts:  " 
python3  update-links.CATEGORY.py > ../_logs/update-links.CATEGORY.log
python3 docs-url-rewriter.CATEGORY.py
echo "python script ended, links updated."
echo "========================================"

