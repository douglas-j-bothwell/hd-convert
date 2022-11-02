---
title: Change the Variations of Your Flags
description: This topic describes how to edit the default variations of your feature flag.
tags: 
   - helpDocs
   - feature flag
   - variation
# sidebar_position: 2
helpdocs_topic_id: 8bf3us11kz
helpdocs_category_id: skrwlcueml
helpdocs_is_private: false
helpdocs_is_published: true
---

When you create a Feature Flag, it has default Variations that are served when the Flag is toggled `ON` or `OFF`. You can accept these default Variations or you can change them. 

For example:

* A Boolean Flag could have `false` set as its default `OFF` Variation and `true` set as its default `ON` Variation. You could change the `ON` Variation to `feature_enabled` and the `OFF` Variation to `feature_disabled`.
* A Multivariate Flag could have `Variation_1` set as its default `OFF` variation and `Variation_2` set as its default `ON` variation, with `Variation_3` configured to be served only when a user has a certain email address.

You can edit the Variations of your Flags on the Harness Platform even after using the Harness Feature Flag SDKs in your application.This topic describes how to edit the default Variations of your Feature Flag and how to edit the Variations that are served for your current Environment.

### Edit the default Flag Variations

When you change the default Variation of a Flag, the change is applied to **only** the current Environment you are in and any new Environments you create.  
To change the Variations in other pre-existing Environments, follow the steps in Option 1: Edit the Variations for a Specific Environment.1. Go to the Feature Flag you want to edit the Variations for.
2. In **Variations**, click the edit icon.

![A screenshot of a flag with the edit icon next to the Variations heading highlighted.](https://files.helpdocs.io/kw8ldg1itf/articles/8bf3us11kz/1657794955710/screenshot-2022-07-14-at-11-35-08.png)*Figure 1: The edit Variations icon*

1. In **Edit Variations**, you can add or delete a Variation and also edit the following:
* **Name**: The name of the Variation, for example `Enabled`.
* **Value**: The value of the Variation, for example `Feature_Enabled`.
* **Description**: An optional description for the Variation.
* **Default rules for the flag**: The rules that are served by default for this Flag, for example, when the Flag is enabled, serve the `Enabled` Variation.

![A screenshot of the Edit Variations page. ](https://files.helpdocs.io/kw8ldg1itf/articles/8bf3us11kz/1657795766706/screenshot-2022-07-14-at-11-37-02.png)*Figure 2: The Edit Variations form*

### Edit the Variations served for your current Environment

1. Go to the Feature Flag you want to edit the Variations for.
2. In the **Targeting** tab, under **When the Default Flag is Enabled** and **When the Default Flag is Disabled**, select the Variations you want to set as the default.

![A screenshot of the Targeting tab of a Flag, which highlights where you can change which Flag Variation is served. ](https://files.helpdocs.io/kw8ldg1itf/articles/8bf3us11kz/1657794755459/p-0-gv-4-ni-0-fhujgg-i-my-l-he-sa-lqj-slb-iuhv-cg-3-jv-f-26-n-04-su-yebvk-4-r-1-yw-7-fsbr-1-crz-bn-2-f-cjn-vw-lzh-yaohzih-iauih-ag-4-vpecpiap-jci-twek-gw-s-4-g-6-ox-4-l-7-n-ubcosn-qe-njf-caux-kw-9-xor-is-eg)*Figure 3: Variations when the Flag is enabled and disabled*

For information about Specific Targeting, go to [Targeting Users with Flags](/article/xf3hmxbaji-targeting-users-with-flags)1. Click **Save** to save your changes.

