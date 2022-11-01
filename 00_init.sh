
# install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Run these three commands in your terminal to add Homebrew to your PATH:
echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /Users/admin/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/admin/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

brew install node

brew install python3
pip3 install markdownify
pip3 install pyyaml


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
