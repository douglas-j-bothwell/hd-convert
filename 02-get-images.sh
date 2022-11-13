#bin/bash

echo "========================================"
echo "Running ./STAGE_docs/get-images.DEV.py:"
echo "========================================"
ls ./IN_html

cd ./STAGE_docs/

rm ../_logs/get-images.log
rm ../data/image-mappings.LATEST.yml
echo "Starting python script: " 
python3 get-images.DEV.py > ../_logs/get-images.log
echo "python script ended, images updated."
echo "========================================"
