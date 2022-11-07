---
title: Trigger Pipelines using Git Event Payload Conditions
description: You can trigger Pipelines in response to Git events that match specific payload conditions you set up in the Harness Trigger. For example, when a pull request or push event occurs on a Git repo and y…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: 10y3mvkdvk
helpdocs_category_id: oya6qhmmaw
helpdocs_is_private: false
helpdocs_is_published: true
---

You can trigger Pipelines in response to Git events that match specific payload conditions you set up in the Harness Trigger.

For example, when a pull request or push event occurs on a Git repo and your Trigger settings match the payload conditions, a CI or CD Pipeline can execute.

In this example, we create a Custom Trigger for GitHub payload conditions.

This topic covers payload conditions in detail. For a general overview of creating Triggers using Git Events, see [Trigger Pipelines using Git Events](https://ngdocs.harness.io/article/hndnde8usz-triggering-pipelines).For general Triggers reference, see [Triggers Reference](https://ngdocs.harness.io/article/rset0jry8q-triggers-reference).

### Before You Begin

* [Learn Harness' Key Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)
* [Kubernetes CD Quickstart](https://ngdocs.harness.io/article/knunou9j30-kubernetes-cd-quickstart)
* [CI Pipeline Quickstart](https://ngdocs.harness.io/article/x0d77ktjw8-ci-pipeline-quickstart)
* [Trigger Pipelines using Git Events](https://ngdocs.harness.io/article/hndnde8usz-triggering-pipelines)

### Limitations

* Currently, Harness supports Git-based Triggers for the most common Git providers. Harness includes a Custom Trigger for other repo providers.
* The **IN** and **NOT IN** operators do not support Regex.

#### Important Notes

* All Triggers in a Harness account have the same URL. This means that you must set up your Trigger Conditions carefully to ensure that a Pipeline triggers Builds for relevant events only.
* If a Build does not start in response to an incoming event, do the following:
	+ Check the execution history (click Execution History in the top right of the Pipeline Studio).
	+ Verify that the runtime inputs are correct.
	+ Check the payloads sent from the Git provider and compare the relevant fields with the Conditions in your Triggers. For example, in GitHub you can view the full payload of each event sent from a specific Webhook.

### Step 1: Add a Trigger to a Pipeline

1. Open your Harness Pipeline in **Pipeline Studio**.
2. Click **Triggers**.
3. Click **New Trigger**.
4. Choose your Git SaaS provider, such as **GitHub** or **BitBucket**, or **Custom** if you are using a different provider.

### Step 2: Configure the Trigger

In the Configuration tab of the new Trigger, specify the following:

* **Name** and **Description**
* **Payload Type:** This should match your Git SaaS provider.
* **Connector:** A [Connector](https://ngdocs.harness.io/category/xyexvcc206) to your Git SaaS provider. (This is required for all Git trigger types except **Custom**.) In the Credentials page of the Connector setup wizard, make sure that API access is selected with the correct permissions.  
A Connector is required for all Git trigger types except Custom. For Custom Triggers, you set up the external tool to send paylods to to the Trigger URL. The specific steps to do this vary depending on the external tool
* **Event:** Select the Git event type for the Webhook.  
If the event type you select results in the **Actions** settings appearing, select the actions for the Webhook or select **Any Actions**.
* **Auto-abort Previous Execution:** Use this option if you want to override active Pipeline executions. When the branch of interest is updated, the Pipeline aborts any active Builds on the branch before it launches the new Build.

### Step 3: Set Trigger Conditions

Conditions specify criteria in addition to events and actions.

Conditions help to form the overall set of criteria to trigger a Pipeline based on changes in a given source.

Conditions support Harness built-in expressions for accessing Trigger settings, Git payload data, and headers.

#### Option 1: Branches and Changed Files

You can configure Triggers based on the source branches, target branches, and changed files in a Git merge.

If you want to specify multiple paths, use the Regex operator.![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1653322170386/trigger-conditions-v-2.png)#### Option 2: Header Condition

In the Header condition, enter the Git Webhook Header data that matches your value. 

The header expression format is `<+trigger.header['key-name']>`. 

For example: `<+trigger.header['X-GitHub-Event']>`.

Refer to [Built-in Git Trigger and Payload Expressions](/article/rset0jry8q-triggers-reference#built_in_git_trigger_and_payload_expressions) for more trigger expressions in Harness.

#### Option 3: Payload Condition

Conditions based on the values of the JSON payload. Harness treats the JSON payload as a data model and parses the payload and listens for events on a JSON payload key.

To reference payload values, you use `<+eventPayload.` followed by the path to the key name.

For example: `<+eventPayload.repository.full_name>`

For details on Payload Condition, see [Payload Condition](https://ngdocs.harness.io/article/rset0jry8q-triggers-reference#payload_conditions).

#### Option 4: JEXL Condition

JEXL expressions are also supported. For example: `<+eventPayload.repository.owner.name> == "repositoryOwnerName"`

JEXL expressions are also supported. Here are some examples:

* `<+trigger.payload.pull_request.diff_url>.contains("triggerNgDemo")`
* `<+trigger.payload.pull_request.diff_url>.contains("triggerNgDemo") || <+trigger.payload.repository.owner.name> == "wings-software"`
* `<+trigger.payload.pull_request.diff_url>.contains("triggerNgDemo") && (<+trigger.payload.repository.owner.name> == "wings-software" || <+trigger.payload.repository.owner.name> == "harness")`

For details on Trigger settings, see [Triggers Reference](https://ngdocs.harness.io/article/rset0jry8q-triggers-reference).

If you select multiple conditions, the conditions are ANDed together (boolean AND operation). All Conditions must match an event payload for it to execute the Trigger. If you select any one condition, Trigger will execute based on the condition you entered.![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1653320703452/trigger-conditions-anded.png)Click **Continue**.

### Step 4: Set Pipeline Input

Pipelines often have [Runtime Inputs](https://ngdocs.harness.io/article/f6yobn7iq0-runtime-inputs) like codebase branch names or artifact versions and tags.

Provide values for the inputs. You can also use [Input Sets](https://ngdocs.harness.io/article/3fqwa8et3d-input-sets).

Click **Create Trigger**.

The Trigger is now added to the Triggers page.

### Step 5: Register Webhook in the Git Provider

When you create or edit the custom webhook trigger, you need to copy the webook URL and add it to your repo webhooks. However, make sure you have the following permissions for GitHub Personal Access Token for webhook registration to work:

* Scopes: select all the repo, user, and admin:repo\_hook options

![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1638175305017/eu-ok-5-sb-rdm-9-hx-ynbpl-9-w-2-sg-35-h-4-hlgr-4-ply-swfg-n-2-wr-ykdjg-0-h-qe-mbkn-yjziwz-g-09-w-6-op-84-p-rt-uk-pjc-so-9-bpql-ykk-0-q-5-th-v-9-phmn-59-zztzytxfg-8-b-cjeoeyhh-hwlm-z-8-z-rzcrk)You should also be repo admin.

1. In the **Pipeline Studio**, click **Triggers.**
2. Select your Custom Webhook.
3. Click on Webhook URL icon.
4. Click the link button to copy the webhook URL.![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1649719755964/trigger-copy-url.png)
5. Log in to your repo in the Git provider and navigate to its Webhook settings.   
All Webhook URLs in an account have the same format: `https://app.harness.io/gateway/ng/api/webhook?accountIdentifier=ACCOUNT_ID`
6. Create a new webhook and paste the URL you copied from Harness in Step 4.
7. Make sure that the content type of the outbound requests is **Application/json**.
8. Make sure that **Enable verification** is enabled.
9. Select the events that you would like to trigger this webhook.  
In this example, we select **Just the push event**. It means that this webhook will only be triggered if there is a push event.
10. Click **Update webhook**.

![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1638177750696/image.png)### Step 6: Test Trigger

Make a change on the repo and push the changes to Github and see if it executes the Trigger. For example, change a file, commit it on the main branch, and make a push event.

In your Git provider repo, you can see that the request and response were successful.

![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1638177429905/image.png)Note that the webhook conditions specified in [Step 3](/article/10y3mvkdvk-trigger-pipelines-using-custom-payload-conditions#step_3_set_trigger_conditions) match the Payload data. As a result, the Pipeline was triggered.

In Harness, view the **Pipeline execution**.

In Harness CI, click **Builds** (1). You can see the source branch (2), target branch (3), and the push request comment and number (4).

![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1656340605211/webhook-connector-build-fields.png)Click the push request number and it opens the Git provider repo at the push request.

If you open the Trigger in the Pipeline, you will see a status in **Last Activation Details**.

![](https://files.helpdocs.io/i5nl071jo5/articles/10y3mvkdvk/1638175614859/o-yjs-8-uq-ol-39-bla-kznpgmzg-9-t-mzw-yq-8-rr-ecox-msgyc-7-r-hptet-z-o-vryzzo-8-2-wah-2-h-r-f-1-y-0-o-vlt-41-c-z-c-ls-9-scwzn-qlln-1-mw-9-kznb-p-esbf-5-iz-84-zax-1-k-jsi-2-d-w-ufl-utqbbw)Activation indicates that the Trigger was successful in requesting Pipeline execution.

### See Also

* [Triggers Reference](https://ngdocs.harness.io/article/rset0jry8q-triggers-reference)
* [Harness Git Sync Overview](https://ngdocs.harness.io/article/utikdyxgfz)
* [Trigger Pipelines Using Git Events](https://ngdocs.harness.io/article/hndnde8usz)

