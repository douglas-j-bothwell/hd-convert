---
title: Create an SDK Key
description: After you’ve created your Environment , you need to create an SDK key for it. You need to use this SDK key in your application’s code to authenticate your connection to the Harness Feature Flag clien…
tags: 
   - helpDocs
helpdocs_topic_id: 8ja1j98xgp
helpdocs_is_private: false
helpdocs_is_published: true
---

After you've [created your
Environment](/article/nh1n5qtjmm-create-an-environment){target="_blank"},
you need to create an SDK key for it. You need to use this SDK key in
your application's code to authenticate your connection to the Harness
Feature Flag client. 

::: warning-callout
You can view and copy the SDK key only immediately after it is created.
For security, after you leave the page, the key is redacted and you
can't view it. Make sure you make a copy of the key to use in your
application.
:::

### Create an SDK Key

1.  In the Environment you created, in **Settings**, click **Create SDK
    Key**.
2.  In **Create SDK Key**, in **Name**, enter a name for your SDK key.
3.  In **Key Type**, select either **Client** or **Server** depending on
    the type of SDK you want to use. For more information about the SDK
    types Harness supports, go to [Chose a Client-side or Server-side
    SDK](/article/rvqprvbq8f-client-side-and-server-side-sdks){target="_blank"}.
    If your organization needs to rotate the keys, you can choose to add
    more than one key for the same Environment.
4.  Click **Create**.
5.  Copy and store your Secret.

::: warning-callout
You can view and copy the SDK key only immediately after it is created.
For security, after you leave the page, the key is redacted and you
can't view it. Make sure you make a copy of the key to use in your
application.
:::

### Next step

After you have created an SDK Key, you can then [Create a Feature
Flag](/article/1j7pdkqh7j-create-a-feature-flag){target="_blank"}.
