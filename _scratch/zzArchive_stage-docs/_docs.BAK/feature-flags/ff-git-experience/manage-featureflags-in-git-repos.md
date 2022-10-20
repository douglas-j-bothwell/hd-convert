---
title: Manage Your Flags Using Git Experience
description: This topic describes how to manage feature flags using Git experience.
tags: 
   - helpDocs
   - git experience
   - feature flag
   - SCM
helpdocs_topic_id: 6f5eylg819
helpdocs_is_private: false
helpdocs_is_published: true
---

::: warning-callout
There is a known issue with this feature. When you turn on a Feature
Flag, some Target rules may be reordered in your Git repo. This doesn\'t
affect the functionality of your Feature Flag or Targets and we are
working to fix this issue as soon as possible.
:::

Using Harness Git Experience with Feature Flags allows you to manage
your Flags from a .yaml file in your Git repository. When you enable Git
Experience, changes you make to Flags on the Harness Platform are
committed on Git, and commits you make on Git are reflected in the
Harness Platform. This means you can work on Flags entirely from Git,
the Harness Platform, or both, and your changes will be synchronized in
both places. 

::: note-callout
In the unlikely circumstance that Harness and Git are connected but out
of sync, your Git file is the source of truth. Changes in the Harness
Platform don't take effect until you commit them to Git. 
:::

### Before you begin

You must set up Git Experience in your Project before you can use it
with Feature Flags.To do this:

-   [Add a Source Code Manager to your
    account.](https://docs.harness.io/article/p92awqts2x-add-source-code-managers){target="_blank"}
-   Follow the steps in [Configure GitSync in
    Harness](https://docs.harness.io/article/xl028jo9jk-git-experience-overview){target="_blank"}
    to enable Git Experience and create a Git repository that contains a
    folder called `.harness`. Harness will automatically create a
    `flags.yaml` file within this folder and this is where you manage
    your Feature Flags. 

Also ensure you read [How Git Experience works with Feature
Flags](#how-git-experience-works-with-feature-flags). 

### How Git Experience works with Feature Flags

When you set up Git Experience and enable it in your Feature Flag
Project, Harness automatically creates a `flags.yaml` file in the
`.harness` folder you created during the set up. All your Flag,
Environment, and Target information is stored in this file. 

For example, the following sample shows:

-   A non-permanent boolean Flag named `Flag_1.`
-   `Flag_1` sits within Environment `Env_1`.
-   The Variations of `Flag_1` within `Env_1`, and which Variations are
    set as default.
-   The current state of `Flag_1`, which is toggled `on`.
-   A Target with the ID `T_1`.
-   The Variation served to `T_1`. 

Example of a YAML file for Feature Flags

<div>

    featureFlags:
     flags:
      - flag: 
         name: Flag_1
         identifier: Flag_1 
         description: "GitExFlag" 
         permanent: false 
         spec: 
             type: boolean 
             default:
                 onVariation: "true" 
                 offVariation: "false"
             variations:
                - identifier: "true"
                  value: "true" 
                - identifier: "false" 
                  value: "false"   
          environments: 
             - identifier: Env_1 
               default:
                  onVariation: "true" 
                  offVariation: "false"
               state: "on"
    targetRules:
       - targets: 
              - identifier: T1
                variation: "false" 
    projectIdentifier: FF_Docs_Demo
    orgIdentifier: Docs

</div>

 The synchronization between the Harness Platform and the `flags.yaml`
file works in both directions:

-   When you update the Harness Platform, the changes are committed to
    Git.
-   When you commit changes to Git, the Harness Platform is updated. 

In the unlikely circumstance that Harness and Git are connected but out
of sync, your Git file is the source of truth. Changes in the Harness
Platform don't take effect until you commit them to Git. 

::: note-callout
If you don't see the changes you made in Git reflected on the Harness
Platform, refresh the page.
:::

### Turn syncing with Git on or off

The Git Experience icons are displayed on many pages, you can turn it on
or off from any page where it is displayed.

After you have enabled Git Experience and understand how it works with
Harness Feature Flags, you can turn the synchronization between the
Harness Platform and Git on or off by completing the following: 

1.  Go to the Project you enabled Git Experience for.
2.  Click **Feature Flags**. 
3.  In the top bar navigation, next to the New Flag button, the Git
    repository you connected is displayed. 
4.  Next to the Git repository, the branch you connected is displayed.
5.  Click the branch and toggle the sync on or off. You have the
    following options:

#### Sync with Git

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363427347/sffdw-fc-7-a-8-i-6-h-tf-nwtcl-7-xwsww-1-lwvn-vo-1-s-2-cb-gqx-0-c-2-wub-orvv-9-tv-6-nvsfgkzy-s-d-k-zkpat-mw-ae-nsvfv-wq-f-56-ruj-3-ok-ov-skhf-3-pr-smzcxc-zhb-dxp-b-4-zf-0-f-jo-uxue-413-jtasfsw-7-wsptog-zmp-rfl-8){style="max-height:30%;max-width:30%;display:block;margin-left:0;margin-right:auto"
hd-height="30%" hd-width="30%" hd-align="left"}

*Figure 1: Sync with Git turned on, auto-commit turned off*

This turns on syncing with Git. When you toggle only this button, each
time you make a change on the Harness Platform, you will be prompted to
confirm which branch you want to commit to in Git and to add a commit
message. For example: 

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363433369/lgkc-k-0-cpp-qlv-ul-9-qx-amsj-gs-7-rczgs-ny-g-1-iw-pvv-lkcchxazh-hho-wjm-6-mm-9-ilapf-73-ep-a-3-j-dqp-sdga-1-f-5-zlu-gf-2-q-vadm-chxoc-l-2-ds-6-qm-6-d-cepqol-nif-pq-mo-ze-vs-8-wk-fwpm-62-ot-kj-l-8-jbgmqhoi-r-3-u){style="max-height:30%;max-width:30%;display:block;margin-left:0;margin-right:auto"
hd-height="30%" hd-width="30%" hd-align="left"}

*Figure 2: Example commit message*

::: note-callout
If you select the checkbox Always commit to this branch and do not
prompt for commit message, the Auto-commit to the selected branch option
will be toggled on.
:::

When you are using this option, the branch icon is a gray circle:

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363420475/a-5-hsm-crm-k-937-o-r-8-xlfrxbu-2-i-9-bqqu-5-pho-oz-9-k-w-oc-ju-1-j-08-d-ho-cok-ntj-kod-cy-18-m-9-yd-ryio-8-ml-qp-n-6-cf-ufeddsb-7-c-o-4-r-0-vxe-2-xpqebf-ihy-yo-zk-yu-9-gl-j-0-ajt-54-v-ug-lq-7-ows-mkm-i-pd-olxgbms-lx-3-g){style="max-height:20%;max-width:20%;display:block;margin-left:0;margin-right:auto"
hd-height="20%" hd-width="20%" hd-align="left"}

*Figure 3: The branch icon when syncing with Git is enabled but
auto-commit is disabled*

#### Auto-commit to the selected branch

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363404738/va-stek-lvws-pbfsucq-m-jvm-v-b-7-jxqq-ycg-1-q-3-sgrw-s-2-q-rv-5-mpztz-xn-jnx-46-w-6-j-amizx-icxxb-q-6-h-8-qs-ls-rti-vyioawv-1-v-0-am-0-yk-ft-llkpmzmokk-g-mhpo-71-j-nkw-ogq-m-7-vf-9-ks-mnbit-b-z-2-tr-8-ni-znfs){style="max-height:30%;max-width:30%;display:block;margin-left:0;margin-right:auto"
hd-height="30%" hd-width="30%" hd-align="left"}

*Figure 4: Sync with Git turned on, auto-commit turned on*

This turns on Auto committing, which means you do not have to manually
enter a commit message and confirm the branch you want to commit to. Any
changes you make will automatically be synced to the flags.yaml file on
Git. Changes that are auto-committed have a \[AUTO-COMMIT\] prefix, for
example:

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363397830/i-n-57-k-2-qu-6-trdas-mq-7-gt-efcga-5-g-hi-l-1-zm-unrvr-x-4-bt-xv-pgm-ns-ks-ldcow-gok-gadwa-cyqptf-qw-h-67-qh-wvu-8-djrj-sssqj-3-h-vh-2-byj-zj-78-f-y-82-c-btst-s-mcn-88-jh-2-l-w-3-wq-n-3318-akzafb-d-61-tu-tj-nfidv-w-0-q){style="max-height:70%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="70%" hd-width="70%" hd-align="left"}

*Figure 5: An auto-commit message in GitHub*

Possible Auto-commit messages

<div>

\[AUTO-COMMIT\] Created feature flag\
\[AUTO-COMMIT\] Toggled feature flag\
\[AUTO-COMMIT\] Updated feature flag details\
\[AUTO-COMMIT\] Updated feature flag rules\
\[AUTO-COMMIT\] Updated feature flag targeting\
\[AUTO-COMMIT\] Updated feature flag variations\
\[AUTO-COMMIT\] Deleted feature flag variations\
\[AUTO-COMMIT\] Updated feature flag prerequisites\
\[AUTO-COMMIT\] Updated feature flag targets\
\[AUTO-COMMIT\] Deleted feature flag\
\[AUTO-COMMIT\] Added feature flag to targets

</div>

When you are using the auto-commit option, the branch icon is a blue
circle:

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363387801/kb-yln-cvxm-chef-ee-ur-4-f-5-kp-6-w-v-3-au-ib-tu-g-5-mvi-02-isss-ik-n-9-r-8-s-madh-2-y-1-u-4-j-vgf-5-ge-125-zvnt-xut-r-fg-r-ioog-v-elm-03-ue-s-9-f-t-8-c-etei-c-3-sx-glg-iv-3-hm-4-nah-dhi-pj-vn-6-uf-9-g-kxwss-coy-3-p-xhf-m){style="max-height:20%;max-width:20%;display:block;margin-left:0;margin-right:auto"
hd-height="20%" hd-width="20%" hd-align="left"}

*Figure 6:* *The branch icon when syncing with Git is enabled but
auto-commit is enabled*

### Turn off syncing with Git

To turn off syncing with Git, turn off the Sync with Git toggle. 

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363378146/tb-y-8-k-0-se-v-a-6-z-vhehj-tx-5-dxgk-gs-5-tz-cqn-7-oqf-67-q-60-qr-yjb-3-k-os-dlgnse-8-b-y-b-9-ieq-8-i-9-fv-2-h-64-y-8-s-5-iqbs-6-lqyezxu-m-5-v-oq-kz-5-l-peqel-40-x-3-v-pun-sfi-25-vz-pzt-51-d-9-eh-d-4-gk-7-hb-xg-jo-9-c-6-uj-u){style="max-height:30%;max-width:30%;display:block;margin-left:0;margin-right:auto"
hd-height="30%" hd-width="30%" hd-align="left"}

*Figure 7: Sync with Git turned off*

If you turn the toggle on again, your Flags will sync with Git again
right away. 

::: note-callout
The Auto-commit to selected branch toggle will be the same status as
before you turned off synching with Git. 
:::

When syncing is off, the branch icon is a red warning circle:

![](https://files.helpdocs.io/kw8ldg1itf/articles/6f5eylg819/1659363354344/v-he-9-f-avvn-xnm-po-21-klio-vz-h-4-x-ghnx-a-7-rbo-5-a-vueag-xpskowkqh-6-m-8-zffzo-db-so-7-yah-qep-r-5-b-zb-xpfzh-9-t-etk-3-fb-bv-xdrh-vp-3-om-u-7-pm-9-nb-8-j-5-tgm-k-p-2-b-0-umc-n-3-dgdf-qut-8-xu-s-37-cj-6-sfe-58-d-xg-7-nj-8){style="max-height:20%;max-width:20%;display:block;margin-left:0;margin-right:auto"
hd-height="20%" hd-width="20%" hd-align="left"}

*Figure 8:The branch icon when syncing with Git is disabled*

### See also

For more information about using Git Experience, go to [Git Experience
How-tos](https://docs.harness.io/article/soavr3jh0i-git-experience-how-tos).
