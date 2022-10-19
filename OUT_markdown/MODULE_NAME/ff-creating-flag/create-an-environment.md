---
title: Create an Environment
description: Once you've created a Project, you need to create an Environment before you create a Feature Flag. Feature Flags can be used independently across multiple Environments within a single Project, for ex…
tags: 
   - helpDocs
helpdocs_topic_id: nh1n5qtjmm
helpdocs_is_private: false
helpdocs_is_published: true
---

Once you've created a Project, you need to create an Environment before you create a Feature Flag. Feature Flags can be used independently across multiple Environments within a single Project, for example:

* In Project X you have two Environments, `Environment_A` and `Environment_B`.
* You create `Flag_1`.
* In `Environment_A` you could have `Flag_1` toggled `on`, but in `Environment_B`, `Flag_1` is toggled `off`.

![A side by side screenshot that shows the same Flag in two environments. One is toggled on and one is toggled off.  ](https://files.helpdocs.io/kw8ldg1itf/articles/nh1n5qtjmm/1658140835837/screenshot-2022-07-18-at-11-40-20.png)*Figure 1: Flag\_1 in different Environments* 

This topic describes how to create an Environment in the Harness platform. 

To read more about the Harness Platform, see [Harness Platform](https://harness.helpdocs.io/category/3fso53aw1u-howto-general).### Before you begin

Before you create a Feature Flag, you must have:

1. [Created an Organization](/article/36fw2u92i4-create-an-organization)
2. [Created a Project](/article/47fkt1ric5-create-a-project)

### Create an Environment

1. In your Project, in **Environments**, click **Create an Environment**.
2. Enter a **Name** for your Environment.
3. Select the **Environment type** and click **Create**.

![A screenshot of the Create an Environment form. ](https://files.helpdocs.io/kw8ldg1itf/articles/1j7pdkqh7j/1657791107725/snsf-vsm-3-a-7-x-3-ybi-1-zly-djz-9-wsq-t-4-m-1-ddid-1-m-omofj-av-7-k-e-8-urw-az-9-xrsh-c-8-g-1-fb-kg-mc-q-b-m-3-qnc-ogmiidj-9-id-ifl-dji-kfr-6-wmeb-4-x-s-di-7-aw-mu-ja-34-hc-kr-1-b-3-zyd-w-0-zxx-p-8-se-3-h-4-o-7-pnpk-q)*Figure 2: Create an Environment form*

1. Your environment is created and you can find it listed in **Environments**.

### Next step

* [Create an SDK Key](/article/8ja1j98xgp-create-an-sdk-key) to authorize your application's access to the Feature Flag client.

