---
title: Trigger Pipelines using Git Events
description: You can trigger Pipelines in response to Git events automatically. For example, when a pull request or push event occurs on a Git repo, a CI or CD Pipeline can execute. Triggers enable event driven C…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: hndnde8usz
helpdocs_category_id: oya6qhmmaw
helpdocs_is_private: false
helpdocs_is_published: true
---

You can trigger Pipelines in response to Git events automatically.

For example, when a pull request or push event occurs on a Git repo, a CI or CD Pipeline can execute.

Triggers enable event driven CI/CD and support the practice of every commit building and/or deploying to a target environment.

For general Triggers reference, see [Triggers Reference](/article/rset0jry8q-triggers-reference).### Before You Begin

* [Learn Harness' Key Concepts](/article/hv2758ro4e-learn-harness-key-concepts)
* [Kubernetes CD Quickstart](/article/knunou9j30-kubernetes-cd-quickstart)
* [CI Pipeline Quickstart](/article/x0d77ktjw8-ci-pipeline-quickstart)

### Limitations

* Currently, Harness supports Git-based Triggers for the most common Git providers. Harness includes a Custom Trigger for other repo providers.
* The **IN** and **NOT IN** operators do not support Regex.
* In Harness, you can select who is able to create and use Triggers within Harness, but you must use your repos' RBAC to control who can initiate the Git events that start the Harness Trigger.

### Visual Summary

Here's a two minute video showing you how to create and run a Trigger in response to Git events.

### Step 1: Set Up Your Codebase

For a Trigger to process Git events, the Pipeline must have a Codebase object that points to the Git repo that sends the events.

The first Build Step in your Pipeline specifies the codebase to build. If your Pipeline doesn't include a Build Step, click **Add Stage**, select **Build**, and specify the Codebase. Select **Clone Codebase** and specify the Connector and source repo for the events.

To edit an existing Codebase, click **Codebase** on the right side of the Pipeline Studio.

See [Create and Configure a Codebase](https://ngdocs.harness.io/article/mozd8b49td).

### Step 2: Add a Trigger to a Pipeline

Open your Harness Pipeline in Pipeline Studio.

Click **Triggers**.

Click **New Trigger**.

Click one of the Git-based Trigger types. In this example, we'll use GitHub.

### Step 3: Set up Webhook Listener

Enter a name for the Trigger.

In **Payload Type**, select your Git provider. This setting is populated with the provider you selected automatically.

Select or create a Connector to the Git account for the Trigger repo. See [Code Repo Connectors](/category/xyexvcc206-ref-source-repo-provider).

* **If you set up an account-level Code Repo Connector:** in **Repository Name**, enter the name of the repo in the account in the Connector.
* **If you set up a repo-level Code Repo Connector:** the repo name cannot be edited.

In **Event**, select the Git event for the Webhook.

If the event you select results in the **Actions** settings appearing, select the actions for the Webhook or select **Any Actions**.

For details on these settings, see [Triggers Reference](/article/rset0jry8q-triggers-reference).

For details on the payloads of the different repo Webhooks, see GitHub [Event Types & Payloads](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads), Bitbucket [Event Payloads](https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html), and Gitlab [Events](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#events).### Option: Auto-abort Previous Execution

Use this option if you want to override active Pipeline executions whenever the branch is updated.

If you select this option, when the branch you specified in the **Connector** is updated, then any active Pipeline executions using the branch and this Trigger are cancelled.

The updated branch will initiate a new Trigger execution.

### Option: Polling Frequency

Currently, this feature is behind the feature flag `GIT_WEBHOOK_POLLING`. Contact [Harness Support](mailto:support@harness.io) to enable the feature.By default, Harness Git-based triggers listen to Git events using webhooks. 

Sometimes webhook events can be missed due to a firewall or a network issue and cannot reach Harness.

To prevent webhook issues from happening, enter an polling interval in **Polling Frequency**.

Permitted values:

* minimum value: `2m`.
* maxium value: `1h`.

### Option: Set Trigger Conditions

Conditions specify criteria in addition to events and actions.

Conditions help to form the overall set of criteria to trigger a Pipeline based on changes in a given source.

For example:

* Execute Pipeline if the source/target branch name matches a pattern.
* Execute Pipeline if the event is sent for file changes from specific directories in the Git repo. This is very useful when working with a monorepo (mono repository). It ensures that only specific Pipelines are triggered in response to a change.

Conditions support Harness built-in expressions for accessing Trigger settings, Git payload data and headers.

![](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1624919275031/clean-shot-2021-06-28-at-15-27-08.png)JEXL expressions are also supported.

For details on these settings, see [Triggers Reference](/article/rset0jry8q-triggers-reference).

Conditions are ANDed together (boolean AND operation). All Conditions must match an event payload for it to execute the Trigger.### Step 3: Set Pipeline Input

Pipelines often have [Runtime Inputs](/article/f6yobn7iq0-runtime-inputs) like codebase branch names or artifact versions and tags.

Provide values for the inputs. You can also use [Input Sets](/article/3fqwa8et3d-input-sets).

Click **Create Trigger**.

The Trigger is now added to the Triggers page.

### Review: Automatic Webhook Registration

When you create or edit the Trigger, Harness registers the webhook in your Git provider automatically. You don't need to copy it and add it to your repo webhooks. However, make sure you have the following permission for GitHub Personal Access Token for automatic webhook registration to work:

* **Scopes:** select all the **repo**, **user**, and **admin:repo\_hook** options

![](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1637177263636/clean-shot-2021-11-17-at-11-26-59.png)You should also be repo admin.

### Step 4: Test Trigger

Make a change on the repo and see if it executes the Trigger. For example, change a file, commit it on a branch, and make a pull request.

In your Git provider repo, you can see that the request and response were successful.

![](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1614104307757/image.png)In Harness, view the Pipeline execution.

In Harness CI, click **Builds**.

You can see the source and target branches. You can also see the pull request comment and number.

![](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1614104376860/image.png)Click the pull request number and it opens the Git provider repo at the pull request.

If you open the Trigger in the Pipeline you will see a status in **Last Activation Details**.

![](https://files.helpdocs.io/i5nl071jo5/articles/hndnde8usz/1624922961169/clean-shot-2021-06-28-at-16-29-13.png)Activation means the Trigger was able to request Pipeline execution. It does not mean that the Webhook didn't work.

### See Also

* [Triggers Reference](/article/rset0jry8q-triggers-reference)

