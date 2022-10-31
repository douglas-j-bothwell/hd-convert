#bin/bash

echo "========================================"
echo "Running ./STAGE_docs/get-images.DEV.py:"
echo "========================================"


cd ./STAGE_docs/

rm ../_logs/update-links.log
echo "Starting python script: " 
python3 update-links.ARTICLE.py > ../_logs/update-links.ARTICLE.log
echo "python script ended, links updated."
echo "========================================"
