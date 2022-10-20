---
title: Add Targets
description: This topic describes how to add targets to your environment.
tags: 
   - helpDocs
   - feature flag
   - Target Users
helpdocs_topic_id: dbk9uoaid3
helpdocs_is_private: false
helpdocs_is_published: true
---

Targets are used to control which users see which Variation of a Feature
Flag, for example, if you want to do internal testing or a beta program
before a broader roll out, you can enable the Flag for some users and
not others. While we refer to targeting users, when you create a Target
you give it a name and a unique identifier, so a Target can be anything
that can be uniquely identified. For example, a Target can be a user, an
application, a system, a machine, or any resource uniquely identified by
an IP address, email ID, user ID, etc.

This topic describes how to add Targets to an Environment. After you've
added the Target, you can add it to a [Target
Group](add-target-groups.md)
or to a [Feature
Flag](targeting-users-with-flags.md). 

::: note-callout
You can add a Target using Harness UI. Alternatively, you can add a
Target and define its attributes in your application\'s code directly
[using a Feature Flag
SDK]**TODO:** Update category link **TODO:** Update category link **TODO:** Update category link (/category/rtce97j1wu-ff-sdks){target="_blank"}. The Targets added
in your code are discovered automatically and populated in the Harness
UI.
:::

### Regex requirements for Target names and identifiers

A Target is identified by a name and an identifier. The name and
identifier you enter must conform to the following regex:

##### **Name**

Regex: `[\\p{L}\\d .@_-]`

Must consist of only alphabetical characters, numbers, and the following
symbols: 

-   . (period)
-   @ (at sign)
-   \- (dash)
-   \_ (underscore)

The characters can be lowercase or uppercase and can include accented
letters, for example `Café_123`.

##### **Identifier**

Regex: `[A-Za-z0-9.@_-]`

Must consist of only alphabetical characters, numbers, and the following
symbols: 

-   . (period)
-   @ (at sign)
-   \- (dash)
-   \_ (underscore)

The characters can be lowercase or uppercase but cannot include accented
letters, for example `CF.789`.

### Add a Target

::: note-callout
A Target is identified by a name and an identifier. Make sure your
Target names and identifiers conform to the regex explained in [Review
Regex Requirements for Target Names and
Identifiers](add-targets.md).
:::

To add a Target:

1.  In **Feature Flags**, in **Target Management**, select **Targets**.
2.  Click **+ Target**.
3.  In **Add Target(s)**, select **Add a Target**.
4.  In **Name**, enter the name that will appear in the Target
    Management page so you can identify this Target.
5.  In **Identifier**, enter a unique identifier for your Target. When
    [Targeting Users with
    Flags](targeting-users-with-flags.md){target="_blank"}
    or [Managing Target
    Groups](add-target-groups.md){target="_blank"}, the
    Targets are identified by the identifier you give them.
6.  You can add multiple Targets. Click **+** to add more Targets.

![](https://files.helpdocs.io/kw8ldg1itf/articles/dbk9uoaid3/1657788769441/ilf-3-ztwgfw-e-2-ttg-xzy-4-hkz-1-okc-qllrc-ql-qzdgk-6-r-htr-gup-eh-fajb-7-zcd-9-im-zk-2-n-uhet-m-3-m-rn-yk-vq-4-sb-fkk-40-w-di-den-0-q-6-h-1-cayyg-zpvc-wjze-wyb-1-wwia-4-zraplyzunv-vkynp-bq-7-cskkwkap-sa){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

*Figure 1: Adding Targets*

1.  When you've added all the Targets, Click **Add**.

### Upload a List of Targets

This option allows you to import a list of Targets in CSV format. To do
this:

1.  In **Feature Flags**, in **Target Management**, select **Targets**.
2.  Click **+ Target**.
3.  In **Add Target(s)**, select **Upload a list of Targets**.
4.  Upload your CSV file as per the template below. The CSV file must
    have only the Name and Identifier; do not include any headings, for
    example:

  ---------- ----
  Target_4   T4
  Target_5   T5
  Target_6   T6
  ---------- ----

1.  Click **Add**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/dbk9uoaid3/1657788967458/g-ufv-nuvlh-zukkrfc-925-li-ivswrge-sxoj-psi-d-2-tni-3-f-70-rtw-5-jabhsae-5-lq-z-06-kj-9-vyhl-ulhb-n-finhv-f-1-z-kpn-6-jlg-ve-9-g-m-ebwlz-9-uk-con-kyo-9-yh-bvxkgqc-ogmgc-nr-9-cq-4-zh-n-4-aowa-3-a-5-q){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

*Figure 2: Adding Targets from a CSV file*

1.  The list of Targets is added.

![](https://files.helpdocs.io/kw8ldg1itf/articles/dbk9uoaid3/1657788983463/syp-a-7-lg-ny-um-ajj-7-ti-2-dq-p-1-cd-ybi-drm-ttd-7-rcnq-lxn-9-dzfvciw-hgq-emrf-9-z-wl-lyn-t-64-fkw-4-p-3-wqz-gqd-4-u-5-xu-xak-d-atjr-vj-5-nbrg-l-9-r-4-aocc-fwxvp-985-assz-m-6-zgu-8-o-anjj-9-i-nvicr-4-utqi-rg){style="max-height:70%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="70%" hd-width="70%" hd-align="left"}

*Figure 3: The list of Targets added to the Harness Platform*

### Next steps

After your have created a Target, you can:

-   [Add them to Target
    Groups](add-target-groups.md){target="_blank"}
-   [Target Users with
    Flags](targeting-users-with-flags.md){target="_blank"}