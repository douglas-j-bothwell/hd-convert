---
title: Configure Git Sync in Harness (Deprecated)
description: Harness Git Experience syncs your Harness Projects and all of their Pipelines and resources with one or more Git repos.
tags: 
   - helpDocs
   - 2-way sync to github
   - gitsync
# sidebar_position: 2
helpdocs_topic_id: hzajxmb3oj
helpdocs_category_id: 236edhb63y
helpdocs_is_private: false
helpdocs_is_published: true
---

This version of Harness Git Experience has been deprecated. To try out the latest version of Git Experience, see [Harness Git Experience Quickstart.​​](/article/grfeel98am)​Harness Git Experience syncs one or more Git repositories with your Harness Projects, including all of their Pipelines and their [resources](#review_git_sync_requirements). When you push changes to your Git repository, the changes are pushed to your Harness entities as well, and vice versa.

This topic explains how to configure the integration between your Git repositories and Harness Projects, Pipelines, and resources.

### Before You Begin

* [Harness Git Experience Overview](/article/utikdyxgfz-harness-git-experience-overview)
* [Harness Git Experience Quickstart](/article/dm69dkv34g-harness-git-experience-quickstart)

### Limitations

* Git Sync in Harness is limited to the following Git providers:
	+ GitHub
	+ Bitbucket cloud. Bitbucket on-prem is not supported.Harness only supports BitBucket cloud.
* In the Git Connectors, all Projects that connect to a given Git repo must use the same Connection Type: SSH or HTTP. For more information, see [Connection Type](/article/tbm2hw6pr6-git-connector-settings-reference#connection_type).  
Let us take an example where Project1 and Project2 connect to repo Repo1. In this case, the Git connectors for both projects must use the same Connection Type.
* Do not change any Types or Identifiers (Account Id, Org Id, Project Id, Connectors, etc) for any Harness entities. Ids are immutable and if they are out of sync, Harness Git Experience will not work.
* Do not delete the branch that you used to enable Git sync. Deleting this branch will cause inconsistencies in the Harness Git Experience.
* Harness Git Experience is not enabled for Pipeline Triggers at this time. Pipelines with Harness Git Experience enabled can use default Triggers, but not Triggers added to Pipelines in Git branches.

### Review: Git Sync Requirements

* You can sync the following Harness resources with your Git repo:
	+ Pipelines
	+ Connectors
	+ Input Sets
	+ Templates
	+ Feature Flags
* Only the resources created at the Project [scope](/article/vz5cq0nfg2-rbac-in-harness#scope) can be synced to Git. Resources created at the Account or Org scope will not be synced.

### Review: Harness to Git Sync

For Git-enabled projects, Git is the source of truth. Harness changes don't take effect until they're committed to Git.

Harness to Git flow can be triggered for the following scenarios:

* When a new entity is created.
* When an existing entity is modified.
* When Git is enabled on an existing Project with existing entities.

### Review: Git to Harness Sync

When you enable Git to create and manage the config in Harness, any change done in Git is synced to Harness.

* Git to Harness flow is initiated only for those repos and branches which exist in Harness.
* You must manually sync every new branch in Git, to push subsequent changes automatically.
* Git to Harness is synced using the webhook that is automatically registered for each Project when Git Experience is enabled. However, make sure you have the following permissions for the GitHub Personal Access Token for automatic webhook registration to work:
	+ **Scopes:** select all the **repo**, **user**, and **admin:repo\_hook** options![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1649752379250/webhook-permissions.png)You should also be the repo admin.
* Although Webhooks are applied automatically by Harness, you can do it manually in case the automatic Webhook registration doesn't work.  
You obtain the Webhook to use in your repo by clicking the **Webhook** icon.[![](https://files.helpdocs.io/i5nl071jo5/articles/rset0jry8q/1613777651302/image.png)](https://files.helpdocs.io/i5nl071jo5/articles/rset0jry8q/1613777651302/image.png)Log into your repo in the Git provider and navigate to its Webhook settings. For example, here's the **Webhooks** section of GitHub.[![](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1614103358723/image.png)](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1614103358723/image.png)Add a Webhook.  
In the Webhook settings, paste the Webhook URL you copied from Harness into the payload URL setting in the repo.  
Make sure that you select JSON for the content type. For example, in GitHub, you select **application/json** in **Content type**.

### Prerequisites

* You must have valid Git credentials and a repo within this Git account.
* Make sure that you have **Project Administrator** permissions in Harness to create a Project and enable Git Experience on Projects. See [Permissions Reference](/article/yaornnqh0z-permissions-reference).
* Make sure you have a Git Source Code Manager in your Harness account. A **Harness SCM** is required to sync entities from Harness to Git. For detailed steps to add an SCM, see [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers). If you try to enable Harness Git Experience without first setting up an SCM, Harness will warn you and require you to set one up.

### Step 1: Add a Harness SCM

Once you have [set up a Harness SCM](/article/p92awqts2x-add-source-code-managers), you can enable Git Experience in your Harness Project.

This topic uses GitHub as the SCM to explain Git Experience.

Once enabled, you can add your Pipelines and resources and select the repos and folders where their YAML files are stored.

See [Add Source Code Managers](/article/p92awqts2x-add-source-code-managers).

Harness only supports BitBucket cloud.### Step 2: Create a Repo

In the Git provider, you want to use for syncing your Project, create a repo(s) for the Project. If you wish to use an existing repo, skip this step.

* You can use multiple repos in the Harness Git Experience for a Project. For example, you could add Pipelines to one repo and Connectors to another.
* Make sure your repo has at least one branch, such as main or master. For most Git providers, you can simply add a README file to the repo, and the branch is created.

Here's a new GitHub repo named **GitExpDocExample**.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1623794233271/clean-shot-2021-06-15-at-14-56-29-2-x.png)### Step 3: Create a New Project

You can enable Git Management for new as well as existing Projects.

If you wish to enable Git Management for an existing Project, skip this step.

In Harness, create a new Project. See [Create Organizations and Projects](/article/36fw2u92i4-create-an-organization).

Here's a new Project named **GitExp Doc Example**.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1647344213610/screenshot-2022-03-15-at-4-28-44-pm.png)Add any team members as contributors.

When you're done you'll have a new Project containing the modules according to your license.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1647344025380/screenshot-2022-03-15-at-4-38-04-pm.png)### Step 4: Enable Harness Git Experience

In your **Project**, select a module such as CI or CD.

Click **Project Setup**, and then click **Git Management**.

The **Enable Git Experience** settings appear.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1647344138133/enable-git-ex.png)Click **Enable Git Experience**.

### Step 5: Configure Harness Folder

Harness requires a Git folder to sync your projects and resources. All the configurations are stored in the Harness Folder. The Harness Folder is created in the Git directory you select and is named **.harness**.

You can have multiple Harness Folders to store configs.

For example: If you have two Connectors in a single Project you can have one Harness folder for each Connector or a common Harness Folder for the entire Project.

Later, when you add Pipelines and resources to this Project, you can specify their default folders. When a Pipeline in one repo needs to access a Connector/Secret/etc in another repo at runtime, the Pipeline will always use the Connector/Secret/etc in their default branch and folder.

You can add the Project's Harness Folder at the root of your repo or in a subfolder.

Create the folder in your repo before setting up the Harness Folder. You will enter the name of the folder in Harness. Harness does not create the folder for you.In **Repository Display Name**, enter a name for the repo. It doesn't have to be the same as the Git repo name. The name you enter here will appear in Harness only. It will identify the Project repo.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1645807144900/screenshot-2022-02-24-at-7-08-43-pm.png)For example, here's the **Repository Display Name** `GitExpDocExample` after Harness Git Experience is enabled:

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1645850354392/screenshot-2022-02-26-at-10-08-15-am.png)In **Select the Connector to your GitHub**, select, or create a Git Connector to the repo for your Project. For steps, see [Code Repo Connectors](https://ngdocs.harness.io/category/xyexvcc206-ref-source-repo-provider).

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1645807740225/screenshot-2022-02-25-at-10-18-03-pm.png)**Important:** The Connector must use the **Enable API access** option and Username and **Token** authentication. Harness requires the token for API access. Generate the token in your account on the Git provider and add it to Harness as a Secret. Next, use the token in the credentials for the Git Connector.Here's an example of a GitHub Connector with all the correct settings:

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1646118159190/screenshot-2022-03-01-at-12-30-59-pm.png)Once you add a Connector, enter the **Repository Name** with which you want to establish a connection.

You should see the Repo URL below the repository name.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1645808825077/screenshot-2022-02-25-at-10-35-17-pm.png)Click **Test Connection**. Once Harness verifies the connection, you will see **Connection Successful**.

In **Select Harness Folder**, enter the name of the folder in your repo where you want to sync.

In **Select Default Branch**, select the branch that you want to use, such as **main**.

Click **Continue**.

### Step 6: Select Connectivity Mode

In **Select Connectivity Mode**, you have two options:

* **Connect Through Manager:** Harness SaaS will connect to your Git repo whenever you make a change and Git and Harness sync.
* **Connect Through Delegate:** Harness will make all connections using the Harness Delegate. This option is used for Harness On-Prem frequently, but can be used for Harness SaaS as well. See [Harness On-Premise Overview](/article/tb4e039h8x-harness-on-premise-overview).

**Secrets:** If you select **Connect Through Manager**, the secrets are decrypted on the Delegate and are available on the Harness Manager. This is different from **Connect Through Delegate** where the Harness Delegate decrypts the secrets. The secrets are then used in the context of the Delegate that sits in your private network. See [Harness Secrets Manager Overview](/article/hngrlb7rd6-harness-secret-manager-overview).If you select **Connect Through Manager** then click **Save and Continue**.

If you select **Connect Through Delegate**, select/add the Delegate you want to use. See [Delegate Installation Overview](/article/re8kk0ex4k-delegate-installation-overview).

Harness Git Experience is enabled and the new repo and folder are listed.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1646271046149/screenshot-2022-03-03-at-6-57-47-am.png)### Step 7: Select the Branch to Sync

Perform this step if you are enabling Git Experience for an existing Project that already has Pipeline or Harness resources. This will establish a full sync of your Harness Project and its resources with Git.

The settings for this stage will not be available if you are enabling Git Experience for a new Project.You can select or create a specific branch in your Git repo to sync these resources. You can also start a pull request to merge these changes. Click **Save**.

The SCM user profile credentials of the user who initiated the sync will be used to sync all resources to Git.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1645712473597/screenshot-2022-02-24-at-7-14-47-pm.png)If you use a Git connector at Project scope to enable Git experience, then the connector will be synced as well. Make sure you merge this connector to the default branch so that it is not accidentally deleted in the non-default branch.To view the sync status, click **Config** in **Git Management**.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1648642579038/screenshot-2022-03-30-at-5-44-47-pm.png)You can check the status of any entity's sync under **Sync Status**. An entity can have any of the following sync statuses:

* SUCCESS
* FAILED
* QUEUED

Your Harness entities will appear in the Harness Folder under the selected branch in your Git Repo after the sync is complete.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1646271186903/screenshot-2022-03-03-at-7-01-24-am.png)To resync any entities that failed to sync, click **Resync**.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1648641932295/screenshot-2022-03-30-at-5-30-37-pm.png)### Step 8: Review the Harness Git Experience in your Project

Harness does not automatically add a folder to your repo until you create a Pipeline or resource like a Connector in your Project.

You can see the repo setting in your Project before creating Pipelines and resources.

In your Project, click one of your modules. In this example, we'll use **Builds**.

Click **Pipelines**.

At the top of the page, you can see **All Repositories**.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1623967095819/clean-shot-2021-06-17-at-14-58-04.png)Click **All Repositories** and select the name of the repo you entered in the **Repository name** earlier.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1623967195652/clean-shot-2021-06-17-at-14-58-35.png)You can now select any branch from the repo.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1623967244297/clean-shot-2021-06-17-at-15-00-25.png)Harness Git Experience is enabled.

![](https://files.helpdocs.io/i5nl071jo5/articles/hzajxmb3oj/1646271358018/screenshot-2022-03-03-at-7-04-03-am.png)### Next Steps

Now that you've enabled Harness Git Experience in your Project, you can start creating Pipelines and resources and syncing them with Git.

See [Git Experience How-tos](/article/soavr3jh0i-git-experience-how-tos).

