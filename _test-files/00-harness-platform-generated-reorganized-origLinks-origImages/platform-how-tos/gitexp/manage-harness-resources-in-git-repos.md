---
title: Manage Project Resources in Git Repos (Deprecated)
description: Create Project resources and store their YAML files in your Git repo's branches and folders.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: auqv67yr6x
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see [Harness Git Experience Quickstart](/article/grfeel98am).​​​Once you have [enabled Harness Git Experience](/article/hzajxmb3oj-enable-git-experience-in-a-project) in your Project, you can create Pipelines and resources and store their YAML files in your Git repo's branches and folders. Git is the single source of truth. The Pipelines and resources are stored in the repo first, and then synced with Harness.

This topic provides an example of adding a Connector and storing it in the Git repo set up in the Harness Git Experience for the Project. The process is the same for Pipelines and other resources.

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/auqv67yr6x-manage-harness-resources-in-git-repos#before_you_begin)
* [Limitations](https://ngdocs.harness.io/article/auqv67yr6x-manage-harness-resources-in-git-repos#limitations)
* [Step 1: Create the Resource](https://ngdocs.harness.io/article/auqv67yr6x-manage-harness-resources-in-git-repos#step_1_create_the_resource)
* [Step 2: Save Connectors to Git](https://ngdocs.harness.io/article/auqv67yr6x-manage-harness-resources-in-git-repos#step_2_save_connectors_to_git)
* [See Also](https://ngdocs.harness.io/article/auqv67yr6x-manage-harness-resources-in-git-repos#see_also)

### Before You Begin

Make sure that you've added a Source Code Manager (SCM) and enabled Harness Git Experience in your Project.

* [Harness Git Experience Quickstart](/article/dm69dkv34g-harness-git-experience-quickstart)
* [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers)
* [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project)

### Limitations

Do not enable Harness Git Experience on a Project that already has Pipelines and resources. You must enable Harness Git Experience on a new Project when you first create the Project.

This is a temporary limitation.

### Step 1: Create the Resource

You can't save Project resources to Git until you have added a SCM to your Harness account and enabled Harness Git Experience in your Project.

* [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers)
* [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project)

In your Harness Project, click **Project Setup**, and then click **Connectors**. We'll be adding a Connector in this topic, but the process is the same for other resources.

At the top of the page is **All Repositories**.

![](https://files.helpdocs.io/i5nl071jo5/articles/auqv67yr6x/1624308554527/clean-shot-2021-06-21-at-13-49-03.png)You select the repo and branch here to display the Connectors stored in them. It does not affect the repo and branch where you create a new Connector. You will select that repo and branch in the Connector settings next.

Click **New Connector**.

For this example, click **Docker Registry**. The **Docker Registry Connector** settings appear.

![](https://files.helpdocs.io/i5nl071jo5/articles/auqv67yr6x/1624308509894/clean-shot-2021-06-21-at-13-48-19.png)Enter a name for the Connector, such as **DockerHub Anonymous**.

In **Git Repository Details**, select the repo and branch where you want to store this Connector. The repos displayed here are the ones set up in **Git Management**.

Click **Continue**.

In **Docker Registry URL**, enter `https://registry.hub.docker.com/v2/`.

In **Provider Type**, select **DockerHub**.

In **Authentication**, select **Anonymous**.

![](https://files.helpdocs.io/i5nl071jo5/articles/auqv67yr6x/1624308859833/clean-shot-2021-06-21-at-13-54-12.png)Click **Continue**.

In **Set Up Delegates**, select **Connect via any available delegate**. If you need to install a Delegate, see [Delegate Installation Overview](/article/re8kk0ex4k-delegate-installation-overview) or [Install a Kubernetes Delegate](/article/f9bd10b3nj-install-a-kubernetes-delegate).

Click **Save and Continue**.

The **Save Connectors to Git** settings appear. Now you can specify the Harness Folder for the Connector's YAML file.

### Step 2: Save Connectors to Git

The Save Connectors to Git settings let you pick the folder, file path, filename, and branch for the Connector YAML file and commit.

![](https://files.helpdocs.io/i5nl071jo5/articles/auqv67yr6x/1624310975497/clean-shot-2021-06-21-at-14-29-14.png)In **Save Connectors to Git** you select the folder where you want to store the Connector's YAML file. This is called the Harness Folder.

The **Harness Folder** is the default folder for this Connector. If a Pipeline stored in another repo/branch uses this Connector, Harness will use the Connector YAML file in this default folder at Pipeline execution.

In **Harness Folder**, select one of the folders set up in the Project's Git Experience settings. See [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project).

The YAML file for the Pipeline will be saved to this folder.

In **File Path**, enter a name for the YAML file, such as `DockerHub_Anonymous.yaml`. Harness will generate a name automatically from the Connector name, but you can add your own.

To enter a subfolder of the Harness Folder you selected, enter the folder name in front of the file name like `connectors/DockerHub_Anonymous.yaml`.

In this example, we use `connectors/DockerHub_Anonymous.yaml`.

In **Commit Details**, enter a message.

In **Select Branch to Commit**, commit to an existing or new branch.

* **Existing branch:** you can start a pull request if you like.
* **New branch:** enter the new branch name. You can start a pull request if you like.

Click **Save**.

The Connector is saved to the repo, branch, folder, and file.

In your Git repo, locate the branch, folder, and file.

Harness created a **.harness** folder under the folder you selected in **Harness Folder.**

If you added a folder to **File Path**, open that folder.

Click the YAML file for your Connector. The YAML is displayed.

### See Also

See [Git Experience How-tos](/article/soavr3jh0i-git-experience-how-tos).

