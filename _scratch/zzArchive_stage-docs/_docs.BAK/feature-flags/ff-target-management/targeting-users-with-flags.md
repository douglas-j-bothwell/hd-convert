---
title: Target Users with Flags
description: This topic describes how to use targeting rules to control variations that you want to serve to your users.
tags: 
   - helpDocs
   - feature flag
   - Target Users
helpdocs_topic_id: xf3hmxbaji
helpdocs_is_private: false
helpdocs_is_published: true
---

Feature Flag Targeting allows you to serve a particular Variation of a
Flag to specific Target when the Flag is enabled. Targets are anything
that can be uniquely identified, we refer to these Targets as users, but
they could also be apps, machines, resources, emails etc. 

For example:

1.  You have a new feature you want your QA team to test before a
    general roll-out.
2.  You create a Boolean Feature Flag for the new feature.
3.  You add Targeting to the Flag so that the QA team are served the
    True Variation when the Flag is enabled, and the Non-QA team are
    served the False Variation. 
4.  You enable the Feature Flag. 
5.  The feature is available to the QA team but is not available to the
    Non-QA team.  

::: note-callout
A Flag can have values in each Environment. For example, if you have a
QA Environment and a Production Environment within a single Project on
the Harness Platform, the Flag could be toggled ON in QA but toggled OFF
in Production. 
:::

This topic describes how to set up Targeting for a Feature Flag you've
created. 

::: note-callout
To edit the default Variations that are served to Targets, go to
[Changing the Variations of Your
Flags](../update-feature-flags/manage-variations.md){target="_blank"}.
:::

### Target specific users or Target Groups when a Flag is enabled

To target specific users, you first need to add them as a Target or
Target Group on the Harness platform. To do this, go to [Adding
Targets](add-targets.md){target="_blank"} and [Managing
Target Groups](add-target-groups.md){target="_blank"}. 

After you have added the Target or Target Group, you can then choose the
Variation to serve them when the Feature Flag is Enabled:

-   **True**: The Targets are served the default True variation.
-   **False**: The Targets are served the default False variation.
-   **Percentage rollout**: You select a percentage of Targets to be
    served each Variation. For example, to increment how many users a
    feature is available for over time, you could use a percentage roll
    out to give 10% of users access to a feature, then 50%, then 100%.
    The users are selected randomly from the Target Group you target,
    and when you increase the percentage, all original users maintain
    their access to the feature. 

    ::: note-callout
    We can only ensure that identifiable Targets maintain their access,
    we can\'t maintain access for anonymous users.
    :::

To add specific Targets: 

1.  Go to the Feature Flag you want to add Targets for and in the
    **Targeting** tab, under **Specific Targeting**, click **+ Add
    Targeting**.
2.  Select which Variation you want to serve to the Target.

If you select one of the default Variations, for example, True or False:

-   Select the Target(s) or Target Group(s), then Click **Save**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/xf3hmxbaji/1657801967037/6-dmgi-6-k-cbcz-84-tcb-2-b-8-k-wy-yit-0-lm-12-c-u-8-qhs-5-pa-u-9-vg-mcfi-559-rx-g-2-g-3-jc-9-i-3-ax-6-s-6-dm-rl-7-x-o-91-al-qij-qesu-r-0-rh-3-bj-ad-7-nz-ua-4-lz-yr-5-q-2-d-kefck-edh-bvge-8-v-ndtl-gv-pn-9-y-cfw-7-tq-zjs-eg){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

*Figure 1: Adding Targets and Target Groups to serve a Variation to*

If you want to use a Percentage Rollout:

1.  Select the Target Group.

::: note-callout
You can only use Percentage Rollouts on a single Target Group for each
Flag. 
:::

1.  Enter the percentage of each Variation you want to serve, then click
    **Save**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/xf3hmxbaji/1657801873792/uidb-21-dgq-us-y-5-b-pg-ddo-ow-3-o-x-eq-xdgkjrgu-9-ya-yxs-ikw-e-32-hk-fe-2-x-9-fsdgz-p-bqkl-3-yvnd-sy-aqxzioaea-qk-qtml-dzhe-hed-61-x-lzu-osgss-as-pz-rbcj-7-f-dcc-9-hqf-i-9-rof-7-xlk-xb-6-w-knys-5-jma){style="max-height:50%;max-width:50%"
hd-height="50%" hd-width="50%"}

*Figure 2: Using a percentage rollout for the Target Group*[*\
*](../update-feature-flags/manage-variations.md){target="_blank"}
