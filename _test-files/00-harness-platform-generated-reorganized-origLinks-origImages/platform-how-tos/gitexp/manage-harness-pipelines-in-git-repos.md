---
title: Manage Pipelines in Git Repos (Deprecated)
description: Create Pipelines and resources and store their YAML files in your Git repo's branches and folders.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: 77xsb39287
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see Harness Git Experience Quickstart.​​Once you have [enabled Harness Git Experience](/article/hzajxmb3oj-enable-git-experience-in-a-project) in your Project, you can create Pipelines and resources and store their YAML files in your Git repo's branches and folders. Git is the single source of truth. The Pipelines and resources are stored in the repo first, and then synced with Harness.

This topic provides an example of adding a Pipeline and storing it in the Git repo set up in the Harness Git Experience for the Project. The process is the same for other resources.

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#before_you_begin)
* [Limitations](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#limitations)
* [Visual Summary](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#visual_summary)
* [Step 1: Create the Pipeline](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#step_1_create_the_pipeline)
* [Step 2: Save Pipeline to Git](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#step_2_save_pipeline_to_git)
* [Step 3: View the Pipeline in Git](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#step_3_view_the_pipeline_in_git)
* [Step 4: View the Pipeline in Git Experience](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#step_4_view_the_pipeline_in_git_experience)
* [See Also](https://ngdocs.harness.io/article/77xsb39287-manage-harness-pipelines-in-git-repos#see_also)

### Before You Begin

Make sure that you've added a Source Code Manager (SCM) and enabled Harness Git Experience in your Project.

* [Harness Git Experience Quickstart](/article/dm69dkv34g-harness-git-experience-quickstart)
* [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers)
* [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project)

### Limitations

Do not enable Harness Git Experience on a Project that already has Pipelines and resources. You must enable Harness Git Experience on a new Project when you first create the Project.

This is a temporary limitation.

### Step 1: Create the Pipeline

You can't save Pipelines to Git until you have added a SCM to your Harness account and enabled Harness Git Experience in your Project.

* [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers)
* [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project)

In your Harness Project, click **Builds**. If you don't have the **Builds** module, use another module.

In **Builds**, click **Pipelines**.

At the top of the page is **All Repositories**.

![](https://files.helpdocs.io/i5nl071jo5/articles/77xsb39287/1623969465388/clean-shot-2021-06-17-at-15-37-38.png)You select the repo and branch here to display the Pipelines stored in them. It does not affect the repo and branch where you create a new Pipeline. You will select that repo and branch in the **Create New Pipeline** settings next.

Click **+Pipelines** to create a new Pipeline. The **Create New Pipeline** settings appear.

Give the Pipeline a name such as **Example**.

In **Git Repository Details**, select the repo and branch where you want to store the Pipeline YAML file in. You will select a folder in that repo and branch later.

Click **Start**.

We're simply demonstrating Harness Git Experience so we'll create a very simple Pipeline.

Click **Add Stage** and then click **Build**.

In **About Your Stage**, enter the name **helloworld**.

Disable **Clone Codebase**.

Click **Set Up Stage**.

Next, you can just paste the following YAML into the Pipeline to create a very simple Pipeline.

Click **YAML** and then paste in the follow YAML.


```
pipeline:  
    name: Example  
    identifier: Example  
    projectIdentifier: GitExp_Doc_Example  
    orgIdentifier: default  
    tags: {}  
    stages:  
        - stage:  
              name: helloworld  
              identifier: helloworld  
              description: ""  
              type: CI  
              spec:  
                  cloneCodebase: true  
                  execution:  
                      steps:  
                          - step:  
                                type: Run  
                                name: example  
                                identifier: example  
                                spec:  
                                    connectorRef: <+input>  
                                    image: <+input>  
                                    command: echo "hello world"  
                                    privileged: false  
                  serviceDependencies: []  
                  infrastructure:  
                      type: KubernetesDirect  
                      spec:  
                          connectorRef: <+input>  
                          namespace: default
```
Replace `projectIdentifier: GitExp_Doc_Example` with identifier of your Project.

You can see the Project ID right after `projects` in the URL of the page:

`https://app.harness.io/.../projects/GitExp_Doc_Example/...`

Click **Save**.

The Pipeline is ready. Now we can save it to Git.

### Step 2: Save Pipeline to Git

When you click **Save**, the **Save Pipelines to Git** settings appear.

In **Harness Folder**, select one of the folders set up in the Project's Git Experience settings. See [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project).

The YAML file for the Pipeline will be saved to this folder. But you can add subfolders in **File Path**.

In **File Path**, enter a name for the YAML file, such as `Example.yaml`. Harness will generate one automatically from the Pipeline name, but you can add your own.

To enter a subfolder of the Harness Folder you selected, enter the folder name in front of the file name like `mybuilds/Example.yaml`.

In this example, we use `mybuilds/Example.yaml`.

In **Commit Details**, enter a message.

In **Select Branch to Commit**, commit to an existing or new branch.

* **Existing branch:** you can start a pull request if you like.
* **New branch:** enter the new branch name. You can start a pull request if you like.

Here's a simple example:

![](https://files.helpdocs.io/i5nl071jo5/articles/77xsb39287/1623972190240/clean-shot-2021-06-17-at-16-23-01.png)Click **Save**.

![](https://files.helpdocs.io/i5nl071jo5/articles/77xsb39287/1623973042485/clean-shot-2021-06-17-at-16-37-14.png)The Pipeline is saved to the repo branch and folder.

### Step 3: View the Pipeline in Git

In your Git repo, locate the branch, folder, and file.

Harness created a **.harness** folder under the folder you selected in **Harness Folder.**

If you added a folder to **File Path**, open that folder.

Click the YAML file for your Pipeline. The YAML is displayed.

![](https://files.helpdocs.io/i5nl071jo5/articles/77xsb39287/1623973191351/clean-shot-2021-06-17-at-16-39-31.png)### Step 4: View the Pipeline in Git Experience

In your Harness Project, click **Project Setup**, and then click **Git Management**.

In **Git Management**, click **Entities**.

In **Entities by repositories**, expand the Project name.

The Pipeline is listed along with its file path in the repo.

![](https://files.helpdocs.io/i5nl071jo5/articles/77xsb39287/1623973642993/clean-shot-2021-06-17-at-16-47-11.png)Now you have a Pipeline stored in Git.

### See Also

See [Git Experience How-tos](/article/soavr3jh0i-git-experience-how-tos).

