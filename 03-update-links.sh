#bin/bash

echo "========================================"
echo "Running ./STAGE_docs/get-images.DEV.py:"
echo "========================================"
ls ./IN_html

cd ./STAGE_docs/

rm ../_logs/update-links.log
echo "Starting python script: " 
python3 update-links.DEV.py > ../_logs/update-links.log
echo "python script ended, images updated."
echo "========================================"
