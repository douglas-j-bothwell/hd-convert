---
title: Enable or Disable Your Flags
description: This topic describes how to turn on or off a flag in a specific environment.
tags: 
   - helpDocs
   - feature flag
   - Enable
   - Disable
helpdocs_topic_id: 0tlih9lee5
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to turn a Feature Flag `on` or `off`. Flags you
create are available in all Environments, but the state of the Flag is
independent, which means the same Flag can be turned on in
`Environment_A` and turned off in `Environment_B`.

Before enabling or disabling a Flag, consider the following:

-   Remember to check which Environment you are in before toggling any
    Flags to ensure you are enabling or disabling the feature in the
    correct Environment.
-   By default, Flags are disabled on creation, so you need to enable
    them when you are ready to use them in your application.
-   When a Flag is disabled, the off Variation (which is the default
    variation) is served to all users. The Flag does not evaluate any
    Targets or Target Rules until you enable it.

### Enable or disable Flags from the Feature Flag dashboard

To enable or disable a Flag from the Feature Flag dashboard:

1.  In your Harness Project, go to **Feature Flags**. A list of all your
    Flags is displayed.
2.  Toggle the button next to the Flag name to turn the Flag on or off.
3.  Check the details are correct, then click **Confirm**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/0tlih9lee5/1660497799236/2022-08-14-18-18-05.png){style="display:block;margin-left:0;margin-right:auto"
hd-align="left"}

*Figure 1: Confirm the Flag should be turned on*

### Enable or disable Feature Flags from the Targeting tab

To enable or disable a Flag from the Feature Flag from the Targeting
tab:

1.  In your Harness Project, go to **Feature Flags**. A list of all your
    Flags is displayed.
2.  Click the Flag you want to enable or disable, then click Targeting.
3.  Depending on the action you want to take, toggle **Flag Enabled** or
    **Flag Disabled**.
4.  Click **Save.**

![](https://files.helpdocs.io/kw8ldg1itf/articles/0tlih9lee5/1660498131563/2022-08-14-18-26-56.png){style="display:block;margin-left:0;margin-right:auto"
hd-align="left"}

*Figure 2: The Targeting tab of a Flag*