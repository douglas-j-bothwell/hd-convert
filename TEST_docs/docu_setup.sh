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


#Access
http://localhost:3000