---
title: Use the Harness REST API
description: Use the Harness REST API to automate Harness operations.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: bn72tvbj6r
helpdocs_category_id: pm96bpz4kf
helpdocs_is_private: false
helpdocs_is_published: true
---

The Harness REST API lets you automate Harness operations, including your builds, deployments, feature flags, etc.

The Harness REST API reference docs are located at [https://harness.io/docs/api](https://harness.io/docs/api/).

![](https://files.helpdocs.io/i5nl071jo5/articles/bn72tvbj6r/1646331067659/clean-shot-2022-03-03-at-10-10-52.png)You can try the API within the reference docs, or anywhere else (Postman, etc), but you'll need an API key from your Harness account first.

When using the API key within the API reference docs, your credentials are saved until the end of the browser session.

### Step 1: Create a Harness API Key and PAT

The Harness API uses API keys to authenticate requests. You create the API key in your Harness Manager User Profile, add a Personal Access Token (PAT) to the key, and then use the PAT in your API requests.

For an overview of Harness API keys, see [Add and Manage API Keys](/article/tdoad7xrh9).Let's create the API key and its Personal Access Token.

Here's a quick visual summary:

![](https://files.helpdocs.io/i5nl071jo5/articles/f0aqiv3td7/1636407720427/clean-shot-2021-11-08-at-13-37-44.gif)#### Create API Key

In Harness, navigate to your **Profile**.

![](https://files.helpdocs.io/i5nl071jo5/articles/f0aqiv3td7/1636406930993/clean-shot-2021-11-08-at-13-28-24-2-x.png)In **My API Keys**, Click **API Key**. The API Key settings appear.

![](https://files.helpdocs.io/i5nl071jo5/articles/f0aqiv3td7/1636407815962/clean-shot-2021-11-08-at-13-43-23-2-x.png)Enter **Name, Description,** and **Tags** for your API.

Click **Save**. The new API Key is created.

#### Create Personal Access Token

Next, we'll add the Personal Access Token (PAT) that you will use when you make API requests.

Click **Token** below the API Key you just created.

![](https://files.helpdocs.io/i5nl071jo5/articles/f0aqiv3td7/1636408087557/clean-shot-2021-11-08-at-13-47-58-2-x.png)In the **New Token** settings, enter a Name, Description, and Tags.

To set an expiration date for this token, select **Set Expiration Date** and enter the date in **Expiration Date (mm/dd/yyyy)**.

Click **Generate Token**.

Your new token is generated.

![](https://files.helpdocs.io/i5nl071jo5/articles/f0aqiv3td7/1636390414362/clean-shot-2021-11-08-at-08-53-10.png)Please copy and store your token value somewhere safe. You won't be able to see it again.  
  
Your API keys carry many privileges, so be sure not to share them in publicly accessible areas. Make sure you always use the updated API Key value after you rotate the token. For more details, see [Rotate Token](https://ngdocs.harness.io/article/tdoad7xrh9-add-and-manage-api-keys#rotate_token).#### Service Account Tokens

You can also use a Service Account Tokens instead of PAT. See [Add and Manage Service Accounts](/article/e5p4hdq6bd).

### Step 2: Use the API

Now you're ready to use the Harness API in the reference docs or anywhere else.

See [https://harness.io/docs/api](https://harness.io/docs/api/).

