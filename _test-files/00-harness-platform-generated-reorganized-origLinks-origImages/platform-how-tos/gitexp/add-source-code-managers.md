---
title: Add Source Code Managers (Deprecated)
description: Add one SCM to your account for each provider.
tags: 
   - helpDocs
   - gitsync
# sidebar_position: 2
helpdocs_topic_id: p92awqts2x
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see [Harness Git Experience Quickstart](/article/grfeel98am).​​​A Harness Source Code Manager (SCM) contains your personal account for a Git provider such as GitHub or AWS CodeCommit. You can add one SCM to your account for each provider.

When you have [Harness Git Experience](/article/utikdyxgfz-harness-git-experience-overview) enabled for a Project, Harness uses your SCM account information to identify the commits you make to and from Harness. An SCM is useful for auditing who is making changes to a Project and its Pipeline, Connectors, etc.

**A Harness SCM is mandatory for Harness Git Experience.** If you don’t have a SCM when you try to enable Harness Git Experience, Harness will warn you and require you set one up.

This topic walks you through setting up a SCM. If you are simply looking for descriptions of a SCM settings, see [Source Code Manager Settings](/article/kqik8km5eb-source-code-manager-settings).

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/p92awqts2x-add-source-code-managers#before_you_begin)
* [Limitations](https://ngdocs.harness.io/article/p92awqts2x-add-source-code-managers#limitations)
* [Step 1: Open Your Profile](https://ngdocs.harness.io/article/p92awqts2x-add-source-code-managers#step_1_open_your_profile)
* [Step 2: Add the SCM](https://ngdocs.harness.io/article/p92awqts2x-add-source-code-managers#step_2_add_the_scm)
* [Next Step](https://ngdocs.harness.io/article/p92awqts2x-add-source-code-managers#next_step)

### Before You Begin

* If you are new to Harness Git Experience, read [Harness Git Experience Overview](/article/utikdyxgfz-harness-git-experience-overview) and try the [Harness Git Experience Quickstart](/article/dm69dkv34g-harness-git-experience-quickstart).

### Limitations

* You can only add one SCM per Git provider. For example, you cannot add two GitHub SCMs.
* Git Sync in Harness is limited to the following Git providers:
	+ GitHub
	+ BitbucketHarness only supports BitBucket cloud.

### Step 1: Open Your Profile

In Harness, click your account profile at the bottom of the navigation.

![](https://files.helpdocs.io/i5nl071jo5/articles/p92awqts2x/1623783902526/clean-shot-2021-06-15-at-12-04-43-2-x.png)In **My Source Code Managers**, click **Add Source Code Manager**.

### Step 2: Add the SCM

In **Add a Source Code Manager**, enter a name for the SCM.

Select the SCM type, such as GitHub.

Enter the authentication credentials.

We'll use GitHub in this example, but you can find the settings for all of the SCMs in [Source Code Manager Settings](/article/kqik8km5eb-source-code-manager-settings).

Here's a GitHub example:

![](https://files.helpdocs.io/i5nl071jo5/articles/p92awqts2x/1623784292600/clean-shot-2021-06-15-at-12-10-59-2-x.png)Click **Add**. The new SCM is listed under **My Source Code Managers**.

### Next Step

Now that you have an SCM you can enable [Harness Git Experience](/article/soavr3jh0i-git-experience-how-tos).

