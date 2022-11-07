---
title: Add Folders to Existing Git Experience Repos (Deprecated)
description: You can add multiple folders as Harness Folders. This allows you to save Pipelines or resources to separate .harness folders in your repo.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: ottiky0sge
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see [Harness Git Experience Quickstart](/article/grfeel98am).​When you [enable Harness Git Experience](/article/hzajxmb3oj-enable-git-experience-in-a-project) in your Project, you select a repo folder as the **Harness Folder** (named **.harness**). The Harness Folder identifies where Harness should save and look for your Project's Pipelines and resources in the repo.

When you save a Pipeline or resource the Harness Folder is used. You can tell Harness to add the Pipeline or resource to a subfolder of the Harness Folder.

You can add multiple folders as Harness Folders. This allows you to save Pipelines or resources to separate .harness folders in your repo.

This topic describes how to add new .harness folders to the repo you have set up in your Project's Git Experience.

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/ottiky0sge-add-folders-to-existing-git-experience-repos#before_you_begin)
* [Limitations](https://ngdocs.harness.io/article/ottiky0sge-add-folders-to-existing-git-experience-repos#limitations)
* [Step: Add a New Harness Folder](https://ngdocs.harness.io/article/ottiky0sge-add-folders-to-existing-git-experience-repos#step_add_a_new_harness_folder)
* [See Also](https://ngdocs.harness.io/article/ottiky0sge-add-folders-to-existing-git-experience-repos#see_also)

### Before You Begin

Make sure that you've added a Source Code Manager (SCM) and enabled Harness Git Experience in your Project.

* [Harness Git Experience Quickstart](/article/dm69dkv34g-harness-git-experience-quickstart)
* [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers)
* [Enable Git Experience in a Project](/article/hzajxmb3oj-enable-git-experience-in-a-project)

### Limitations

Do not enable Harness Git Experience on a Project that already has Pipelines and resources. You must enable Harness Git Experience on a new Project when you first create the Project.

This is a temporary limitation.

### Step: Add a New Harness Folder

In your Project, click **Project Setup**, and then click **Git Management**.

The repos that have been added to Git Management are displayed.

![](https://files.helpdocs.io/i5nl071jo5/articles/ottiky0sge/1624387284001/clean-shot-2021-06-22-at-11-41-10.png)Click **Add Folder** for the repo where you want to add a new **.harness** folder.

In **Add new .harness folder**, in **Path to the Harness folder**, enter the full path from the repo root to where you want to add a new **.harness** folder.

The folder you added when you set up the repo in Git Management is the default folder for this repo. The default folder is simply the first folder that appears in **Harness Folder** settings when you save a Pipeline or resource.

Select **Make this a default folder for this repository** to make the new folder the default folder.

When you are done, the folder setting will look something like this:

![](https://files.helpdocs.io/i5nl071jo5/articles/ottiky0sge/1624387697165/clean-shot-2021-06-22-at-11-48-07.png)Click **Add Folder**.

Now the folder is listed in the repo's row in Git Management.

![](https://files.helpdocs.io/i5nl071jo5/articles/ottiky0sge/1624387780415/clean-shot-2021-06-22-at-11-49-19.png)Now when you save a Pipeline or resource, you can select the new folder.

![](https://files.helpdocs.io/i5nl071jo5/articles/ottiky0sge/1624388330955/clean-shot-2021-06-22-at-11-57-44.png)### See Also

See [Git Experience How-tos](/article/soavr3jh0i-git-experience-how-tos).

