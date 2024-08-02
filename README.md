This folder contains a set of scripts for converting our Harness docs from the [HelpDocs platform](https://www.helpdocs.io/) to the new [Harness Developer Hub](https://github.com/harness/developer-hub).

# Migration Workflow for Docs Team 

To migrate your section of the docs over to the Developer Hub platform, do the following.

## Set up your Local Environment

1) You will be using this repo in conjunction with the developer-hub repo. I recommend you create a folder with the two repos side-by-side, at a location where the paths won't get too long (for example, '~'). For example:
 
 ```
 /users/myusername
     docs-migrate/
         developer-hub/
         hd-convert     
 ``` 
 
2) `cd` to your `docs-migrate` folder and clone the repos:
 
      a) `git clone https://github.com/harness/developer-hub.git`
      
      b) `git clone https://github.com/douglas-j-bothwell/hd-convert.git`
      
3) `cd` into the `hd-convert` folder and create a branch. For example: `git checkout -b platform-docs-migrate-v1`
   
:information_source: You won't be making changes to this repo. This is primarily a best-practice thing. When it comes time to push your updates to the Developer Hub, you will create a fork of the [developer-hub](https://github.com/harness/developer-hub) repo, copy in your changes, and then create a Pull Request. 
        <br>
   
:information_source: I recommend keeping the developer-hub repo in the `main` branch. The purpose of this local copy is to make sure you have the latest/greatest content from the remote. You'll be pulling from the remote a lot, especially if you're migrating a big chunk of docs. 
   
4) You should now be in the root of the hd-convert repo. Run the following command to ensure that you can run the shells scripts:

        sudo chmod +x *.sh
        
5) Run the following script. This script installs Homebrew, Node, Python3, and some Python libraries: 

        ./00_init.sh
        
## Convert HTML to Markdown 

#### Download HTML docs from Harness

1) Log in to HelpDocs and go to ***Settings*** > ***Migrations***. 

2) In ***Export & Backup***, click the ***ZIP*** menu and choose ***Download as ZIP***.

3) Save an unzipped copy of the archive in the `hd_convert/_data` folder. 

:exclamation: Important notes:

* In many cases, the exported archive doesn't maintain the directory structure of the public doc set. You might need to arrange the relevant folders into the structure that you want in the developer-hub docs set. You need to do this BEFORE you run the scripts to update the article and category links. 

* The archive also includes stuff that doesn't appear in the public docs, such as empty folders and files whose status is Private rather than Published.

#### Convert the HTML Topics to Markdown

1) Copy the folders to convert into `IN_html`. (You can arrange the folders now do it in the next step.)

2) Run the following script: `./01-gen-markdown.sh`

3) When the script finishes, check the resulting output in `OUT_markdown/MODULE_NAME`.

:exclamation: Important notes:

* By default, the script generates markdown only for HTML topics in the public docs (specifically in the left-side TOC menu).

* Each markdown topic has a frontmatter section at the top.

* A colon in the frontmatter will cause Docusaurus to choke. For this reason, it replaces any colon (***:***) in the description with an em dash between two spaces (*** &#8212; ***).

* The frontmatter also includes a commented-out line (`# sidebar_position: 2`) that you can use to position the topics within within their parent in the TOC. 

#### Review the Markdown Output

At this point, it's good practice to eyeball the generated topics and compare each topic with its source on [https://docs.harness.io/](https://docs.harness.io/).




 

    

