---
title: Manage Input Sets and Overlays in Git Repos (Deprecated)
description: Add an Input Set to your Git repo as part of Harness Git Experience.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: 041lpndoma
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see [Harness Git Experience Quickstart](/article/grfeel98am).​​Once you have [enabled Harness Git Experience](/article/hzajxmb3oj-enable-git-experience-in-a-project) in your Project, you can create Pipelines and resources and store their YAML files in your Git repo's branches and folders. Git is the single source of truth. The Pipelines and resources are stored in the repo first, and then synced with Harness.

Pipeline Input Sets and Overlays can be stored in Git also. They can be stored in repos, branches, and folders separate from the Pipeline where they were created.

This topic covers adding an Input Set to your Git repo as part of Harness Git Experience. It does not cover Input Sets and Overlays in detail. For details on those, see [Run Pipelines using Input Sets and Overlays](/article/gfk52g74xt-run-pipelines-using-input-sets-and-overlays).

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/041lpndoma-manage-harness-input-sets-and-overlays-in-git-repos#before_you_begin)
* [Limitations](https://ngdocs.harness.io/article/041lpndoma-manage-harness-input-sets-and-overlays-in-git-repos#limitations)
* [Step 1: Create a Pipeline](https://ngdocs.harness.io/article/041lpndoma-manage-harness-input-sets-and-overlays-in-git-repos#step_1_create_a_pipeline)
* [Step 2: Create an Input Set](https://ngdocs.harness.io/article/041lpndoma-manage-harness-input-sets-and-overlays-in-git-repos#step_2_create_an_input_set)
* [Step 3: Save Input Set to Git](https://ngdocs.harness.io/article/041lpndoma-manage-harness-input-sets-and-overlays-in-git-repos#step_3_save_input_set_to_git)
* [See Also](https://ngdocs.harness.io/article/041lpndoma-manage-harness-input-sets-and-overlays-in-git-repos#see_also)

### Before You Begin

Make sure that you've added a Source Code Manager (SCM) and enabled Harness Git Experience in your Project.

* [Harness Git Experience Quickstart](/article/dm69dkv34g-harness-git-experience-quickstart)
* [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers)
* [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project)

### Limitations

* Do not enable Harness Git Experience on a Project that already has Pipelines and resources. You must enable Harness Git Experience on a new Project when you first create the Project.  
This is a temporary limitation.

### Step 1: Create a Pipeline

Before you can add an Input Set to Git, you need to create and save its Pipeline. This topic does not covering adding a Pipeline to Git.

Follow the steps in [Manage Pipelines in Git Repos](/article/77xsb39287-manage-harness-pipelines-in-git-repos) to set up a Pipeline and save it to a Git repo, branch, and folder.

Now that you have your Pipeline set up, let's create the Input Set.

### Step 2: Create an Input Set

In your Pipeline, click **Input Sets**.

The **New Input Set** settings appear, including the **Git Repository Details** settings.

![](https://files.helpdocs.io/i5nl071jo5/articles/041lpndoma/1624384843044/clean-shot-2021-06-22-at-10-55-56.png)In **Repository name**, select the repo where you want to store this Input Set. This is not the actual repo name, it is the name you gave to the repo connection when you added it in the Project's Git Experience settings.

In **Select a Brach**, select repo branch to use.

Configure the rest of the Input Set and click **Save**.

**Save Input Sets to Git** appears.

### Step 3: Save Input Set to Git

In **Save Input Sets to Git**, you define the Harness Folder, subfolder(s), and file path for the Input Set YAML file. You also select the branch for the commit.

In **Harness Folder**, select one of the folders set up in the Project's Git Experience settings. See [Enable Git Experience in a Project](https://ngdocs.harness.io/article/hzajxmb3oj-enable-git-experience-in-a-project).

The YAML file for the Input Set will be saved to this folder. But you can add subfolders in **File Path**.

In **File Path**, enter a name for the YAML file, such as `GitExpInputSet.yaml`. Harness will generate one automatically from the Input Set name, but you can add your own.

To enter a subfolder of the Harness Folder you selected, enter the folder name in front of the file name like `inputsets/GitExpInputSet.yaml`.

In **Commit Details**, enter a message.

In **Select Branch to Commit**, commit to an existing or new branch.

* **Existing branch:** you can start a pull request if you like.
* **New branch:** enter the new branch name. You can start a pull request if you like.

Here's a simple example:

![](https://files.helpdocs.io/i5nl071jo5/articles/041lpndoma/1624385649029/clean-shot-2021-06-22-at-11-13-58.png)Click **Save**.

The Input Set is saved to the repo, branch, folder, and file.

In your Git repo, locate the branch, folder, and file.

Harness created a **.harness** folder under the folder you selected in **Harness Folder.**

If you added a folder to **File Path**, open that folder.

Click the YAML file for your Input Set. The YAML is displayed.

### See Also

See [Git Experience How-tos](/article/soavr3jh0i-git-experience-how-tos).

