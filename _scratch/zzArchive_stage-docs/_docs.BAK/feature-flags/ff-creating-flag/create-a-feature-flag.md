---
title: Create a Feature Flag
description: This topic describes how to create a feature flag in Harness.
tags: 
   - helpDocs
   - feature flag
helpdocs_topic_id: 1j7pdkqh7j
helpdocs_is_private: false
helpdocs_is_published: true
---

Feature Flags allow you to toggle features in your code on or off, which
allows you to progressively roll out features to particular users or
groups. By using Feature Flags, you can manage continuous delivery and
control who sees which features and when.

This topic describes how to create a Feature Flag in the Harness
platform. 

::: note-callout
A Feature Flag is available only for the Project the Flag is created in,
so you'll need to create any relevant Flags you want to use in each
Project you want to use them for.\
\
You can use the same Flags across multiple Environments within a single
project, but the Flag status in each Environment is independent.
:::

### Before you begin

Before you create a Feature Flag, you must have:

1.  [Created a
    Project](create-a-project.md){target="_blank"}
2.  [Created an
    Environment](create-an-environment.md){target="_blank"}
3.  [Created an SDK
    Key](create-an-sdk-key.md){target="_blank"}

### How Feature Flag Variations work

When you create a Feature Flag, you also create different options to
label the logic of that Flag. These are called Flag Variations, for
example, a simple Boolean flag would have only two Variations, `true`
and `false`. However, there are two different types of Feature Flags you
can create:

-   **Boolean**: Has only two Variations; true and false.

![](https://files.helpdocs.io/kw8ldg1itf/articles/1j7pdkqh7j/1657792983322/3-zc-1-tte-bs-tuwxyzstj-mua-wc-kyi-5-jdmp-2-f-vf-pg-yr-p-29-og-90-ggy-0-ozzmwd-pxo-1-n-ym-8-f-7-jg-ms-5-zob-zs-xk-a-0-c-6-ug-bdk-6-zz-9-n-fnp-l-81-is-5-i-iox-6-oqv-0-w-c-9-okfm-h-9-hgtjvi-p-1-t-83-waezfq-6-ka){style="max-width:700px;display:block;margin-left:0;margin-right:auto"
hd-width="700px" hd-align="left"}

*Figure 1: Variations of a boolean Flag*

-   **Multivariate**: Has multiple Variations, you can add as many
    custom Variations as you like. 

![](https://files.helpdocs.io/kw8ldg1itf/articles/1j7pdkqh7j/1657793005472/wfc-7-xo-44-fi-9-l-f-k-qlk-xpz-l-48-eo-qwm-pwtz-urf-3-zkapra-qntl-7-z-82-ghir-2-way-nndo-1-o-qsbp-af-n-4-nge-tv-2-gc-4-l-ajh-ndt-9-huxwvmv-vg-0-p-kebrpy-5-v-iju-41-b-1-t-dq-00-dry-93-kqazkl-ghbtk-vyi-a){style="max-width:700px;display:block;margin-left:0;margin-right:auto"
hd-width="700px" hd-align="left"}

*Figure 2: Variations of a multivariate Flag*

### Create a boolean Flag 

1.  In **Feature Flags**, click **+ New Flag**.
2.  Select **Boolean**.
3.  In **About the Flag**, in **Name**, enter a name for your Flag and
    click **Next**.

::: note-callout
When you name a Flag, Harness automatically generates its identifier.
You can edit the Identifier when you are creating the Flag, but not
after it is saved. If you rename the Flag, the Identifier remains the
same. For more information, go to [Entity Identifier
Reference](https://ngdocs.harness.io/article/li0my8tcz3-entity-identifier-reference).
:::

1.  To make the Feature Flag permanent, select the **This is a permanent
    flag** checkbox. Permanent Flags are flags you intend to stay in
    your system indefinitely, so we will never mark them as potentially
    stale. 
2.  Click **Next**.
3.  In **Variation** **settings**, in **Flag Type**, select **Boolean**.
4.  In the **Name** fields, enter the name for the true and false
    variations, for example, **True** and **False**.
5.  In **Default rules for the flag**, select which variation of the
    flag to serve when the flag is ON or OFF, for example, True when the
    flag is ON and False when the flag is OFF.

![](https://files.helpdocs.io/kw8ldg1itf/articles/1j7pdkqh7j/1657792275423/swu-5-cng-svlpvqq-3-k-zccmk-hwaq-89-h-3-s-tj-1-tfu-ypvgn-dskrc-3-oriv-ic-ph-krek-x-6-vp-edibu-git-4-xe-v-8-i-jlvaiad-cmgkj-za-9-fk-cyvn-eqzoa-rs-5-f-9-i-zn-hu-u-30-w-c-2-psaq-6-a-8-jf-ty-2-fr-hp-gou-97-dg){style="max-height:70%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="70%" hd-width="70%" hd-align="left"}

*Figure 3: Variation settings*

1.  Click **Save and Close**. The Feature Flag is created and is set to
    **OFF** by default.

![](./static/create-a-feature-flag-01.png){style="max-height:70%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="70%" hd-width="70%" hd-align="left"}

*Figure 4: A boolean Flag*

After you have created your Boolean Flag, you can then:

-   [Manage the Variations of the Feature
    Flag](../update-feature-flags/manage-variations.md){target="_blank"}
-   [Add Flag
    Prerequisites](../ff-adding-prereqs/add-prerequisites-to-feature-flag.md){target="_blank"}
-   [Targeting Users with
    Flags](../ff-target-management/targeting-users-with-flags.md){target="_blank"}

### Create a multivariate Flag 

Multivariate Feature Flags allow you to serve a different Variation of a
Flag to multiple user groups at one time.  For example, a multivariate
Flag could have the following Variations:

-   Variation 1 set to OFF 
-   Variation 2 set to ON
-   Variation 3 set to be served only when a user has a certain email
    address

There is no limit to the amount of Variations that you can add to a
multivariate Flag, and you can use strings, numbers, or JSON to define
the different Variants. 

To create a multivariate Flag:

1.  In **Feature Flags**, click **+ New Flag**.
2.  Select **Multivariate**.
3.  In **About the Flag**, in **Name**, enter a name for your Flag and
    click **Next**.
4.  To make the Feature Flag permanent, select the **This is a permanent
    flag** checkbox. Permanent Flags are flags you intend to stay in
    your system indefinitely, so we will never mark them as potentially
    stale. For example, if you are offering a premium feature to some of
    your customers but not others, you can use a permanent flag to
    manage who sees this feature indefinitely.
5.  In **Variation settings**, in **Flag Type**, select **Multivariate**
    and then select the **Data Type**. You can select, **String**,
    **JSON**, or **Number**.
6.  Enter a **Name** and **Value** for each Variation you want to use.
7.  In **Default rules for the flag**, define which Variation you will
    see by default when the Flag is ON or OFF.

![](https://files.helpdocs.io/kw8ldg1itf/articles/1j7pdkqh7j/1657793372053/x-yvg-3-xsxw-lpt-01-rnmbg-8-ji-gn-8-jq-ew-1-tqc-pd-ug-qi-ty-56-f-5-z-e-ta-vwt-3-tnt-lylu-9-vma-qfem-9-ozyfgam-tord-k-0-jp-3-v-8-mw-k-sw-7-pvt-djij-smd-rx-5-bds-7-bpu-17-ak-lj-samy-s-1-v-cj-qcix-9-cy-xby-q){style="max-height:70%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="70%" hd-width="70%" hd-align="left"}

*Figure 5: Variation settings of a multivariate fFag*

After you have created your multivariate Flag, you can then:

-   [Manage the Variations of the Feature
    Flag](../update-feature-flags/manage-variations.md){target="_blank"}
-   [Add Flag
    Prerequisites](../ff-adding-prereqs/add-prerequisites-to-feature-flag.md){target="_blank"}
-   [Target Users with
    Flags](../ff-target-management/targeting-users-with-flags.md){target="_blank"}
