---
title: Diagnose and Fix Git Sync Errors (Deprecated)
description: Helps you diagnose errors you might encounter during the Harness Git sync process.
tags: 
   - helpDocs
   - git sync
   - Platform
# sidebar_position: 2
helpdocs_topic_id: 24ehx5oa94
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see [Harness Git Experience Quickstart](/article/grfeel98am).​Harness Git Experience provides seamless integration between your Git repos and your Harness Projects, Pipelines, and resources. You can work entirely from Git or use a hybrid method of Git and the Harness Manager. You can sync your Git repo with Harness to simply use the YAML files in your source repo when making changes to Harness.

This topic helps you diagnose and fix errors you might encounter during the Git to Harness sync process.

In this topic:

* [Before You Begin](#before_you_begin)
* [Review: Error Categories](#review_error_categories)
* [Git to Harness Sync Errors](#git_to_harness_sync_errors)
* [Connectivity Issues](#connectivity_issues)
* [Step: Diagnose Git to Harness Sync Errors](#step_diagnose_git_to_harness_sync_errors)
* [Step: Diagnose Connectivity Issues](#step_diagnose_connectivity_issues)

### Before You Begin

* [Learn Harness' Key Concepts](/article/hv2758ro4e-learn-harness-key-concepts)
* [Harness Git Experience Overview](/article/utikdyxgfz-harness-git-experience-overview)
* [Git Experience How-to](/article/soavr3jh0i-git-experience-how-tos)

### Review: Error Categories

As a part of the Harness Git Experience, you can make changes in configuration either from the Harness side or from the Git repo side. If you are making a change from the Git side, then there is a chance that you can give the wrong YAML input.

You might encounter one of the following Git Sync errors:

* Git to Harness Sync Errors
* Connectivity Issues

### Git to Harness Sync Errors

You can find all the errors that you encounter while syncing your Harness entities from your Git repo under this category.

These errors can occur due to one of the following reasons:

* The YAML syntax is not correct.
* Semantic errors, like an entity with the same name or identifier, already exists.
* Invalid references in the YAML, like when the identifier refers to a secret in your Connector that does not exist.
* Mandatory fields are missing in YAML.

To fix an error, try one of the following:

* Make the entity change from the Harness Manager UI.
* Fix the YAML from Git.

If an entity has errors because of Git to Harness Sync issues, Harness marks it as **INVALID**.

![](https://files.helpdocs.io/i5nl071jo5/articles/24ehx5oa94/1639479298137/screenshot-2021-12-14-at-4-21-09-pm.png)Clicking on this connector takes you to the YAML view.

The visual view is disabled for any connector that is marked invalid.### Connectivity Issues

All connection or network-related errors that occur during the Git Sync process appear under this category. Connectivity issues might occur for the following reasons:

* Your Git credentials are invalid. In such a scenario, Harness cannot connect to your Git repo, resulting in a connectivity error.
* If you enable Git Experience using Delegates as the connectivity mode, and the Delegates are not available, then errors can occur.

### Step: Diagnose Git to Harness Sync Errors

In Project Setup, click Git Management.

Click Errors.

Errors are listed based on commit Ids or file names.

Select Commits to list errors by commit Ids.

Select Files to list errors by file name.

![](https://files.helpdocs.io/i5nl071jo5/articles/24ehx5oa94/1638885932290/screenshot-2021-12-07-at-6-27-41-pm.png)Filter errors for a specific repository. Select a repo and branch to view repo-specific errors.

Click **View Content** in the **Files** view to see the content of the error encountered. You can see the content of the file where the error has occurred.

![](https://files.helpdocs.io/i5nl071jo5/articles/24ehx5oa94/1638961409840/screenshot-2021-12-08-at-4-32-37-pm.png)### Step: Diagnose Connectivity Issues

In **Project Setup**, click **Git Management**.

Click **Errors** and then click **Connectivity Errors**.

