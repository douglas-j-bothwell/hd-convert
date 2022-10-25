cd ..

if [ -d "./developer-hub" ] 
then
    echo "updating main branch of developer hub:"
    cd ./developer-hub 
    git checkout main
    git pull 
    cd ..
else
    echo "cloning developer hub:"
    git clone https://github.com/harness/developer-hub.git
fi

echo "current directory:"
pwd
echo ""

if [ -d "./TEST" ] 
then
    echo "deleting ..TEST/"
    rm ./TEST 
fi

mkdir ./TEST 
echo "copy developer-hub repo to TEST folder:"
cp -rf ./developer-hub ./TEST

echo "cd-ing into ./TEST/developer-hub"
cd ./TEST/developer-hub
echo "pwd:"
pwd
echo ""

echo "start automated setup...."
# install node and yarn as described here: https://harness.atlassian.net/wiki/spaces/PD/pages/21172979350/Authoring+Experience
#Install Latest Node
brew install node

#If a Specific Version of Node is Required
node --version
brew search node
brew unlink node
brew install node@16
brew link node@16
brew link --overwrite node@16
brew switch

#Run 
#https://github.com/facebook/docusaurus/issues/2848

cd developer-hub

#Install Yarn
npm install --global yarn

#Validate Install
yarn --version

yarn
yarn start
