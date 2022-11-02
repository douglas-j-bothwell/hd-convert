---
title: Add a Default Pipeline for Flag Changes
description: This feature is available to use only by Project Admins. You can add a Pipeline to your Flags that will be applied when you or your team make the following changes&#58; Enable or disable a Flag. Add Targ…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: sjzsn4etz9
helpdocs_category_id: fsgwbaegql
helpdocs_is_private: false
helpdocs_is_published: true
---

This feature is available to use only by Project Admins.You can add a Pipeline to your Flags that will be applied when you or your team make the following changes:

* Enable or disable a Flag
* Add Targeting rules to a Flag

Using a default Pipeline means that you can ensure your Flag changes can go through the process you want it to, allowing for better security and more consistent operations. For example, you can add an approval step so all your production Flag changes must be approved before they are executed, or you can send a Slack notification every time a Flag changes. 

### Before you begin

* You should understand how to create a Pipeline. For more information about Pipelines, go to [Pipelines and Stages](/category/kncngmy17o-pipelines).
* You should have a Project set up with Feature Flags added to it.

### Important things to consider

* Removing Targeting rules won’t execute the Pipeline. Currently, the Pipeline is only executed for the following changes:
	+ Enable or disable a Flag.
	+ Add Targeting rules to a Flag.
* You must include a Flag step and add the Flag Configuration.
* Currently, you can’t add Pipelines that include a build or deploy stage.

### Add a default Pipeline

To add a default Pipeline: 

1. Go to Feature Flags, then select **Pipelines**.
2. Click **+ Create a Pipeline** and enter the name and description for the Pipeline, then click **Start**.
3. Add a stage and select **Feature Flag**, name the Flag, then click **Set Up Stage**.
4. Click **Add Step**, then click **Flag Configuration**. Add the following for your Flag Configuration:
* In **Step Name**, add the name for the Pipeline step.
* In **Environment**, add the environment you want to use.
* In **Select Flag**, click the pin icon and change to **Runtime input**.

![A screenshot of the Pipeline with the Flag Configuration panel open.](https://files.helpdocs.io/kw8ldg1itf/articles/sjzsn4etz9/1665673820066/2-o-4-h-9-k-tsojs-w-6-jo-cpjkfds-0-tun-es-vfi-8-y-9-au-vp-8-x-rcb-jfd-3-n-871-s-yzlx-5-u-6-uejlm-12-kmvzd-9-a-5-kuh-5-l-gdhqxh-h-0-uohn-cb-0-a-iu-yu-8-pnk-4-z-fo-tt-0-fmze-8-m-8-fq-tqzml-ly-ua-pqfev-w-6-ugsqpl-oz-9-tbbjvu-nbsx-lni-2-es-bb-qtv-e-9-cfv-5-a-ve-vl-oik-vv-a-6-g)1. Click **Apply Changes**. After you have added the Flag Step, you can then add any other Pipeline stages or steps you want to include in your Pipeline, for example, a Jira approval stage.

Currently, you can’t include build or deploy stages.### Apply the default Pipeline to a Flag

After you have created the Pipeline, you need to apply it to your Feature Flag. To do this:

1. Go to **Feature Flags**.
2. Select the Flag you want to add the Pipeline to.
3. Click the **Flag Pipeline** tab, then click **Add Flag Pipeline**.  
![A screenshot of the Flag Pipeline tab](https://files.helpdocs.io/kw8ldg1itf/articles/sjzsn4etz9/1665673826400/pqm-mstcq-ehd-e-3-nhd-nveewdcf-gwv-wocja-nrzv-419-gz-pf-2-xll-0-g-um-43-ekyyjr-acychkuhi-2-x-3-f-birg-l-0-rpkeygy-5-n-8-u-1-emd-2-ya-m-03-ug-wuct-ckke-39-g-53-v-3-ac-lea-0-bxx-muo-or-5-drqbgsuy-smfgploqa-aqn-y-2-kzfz-3-vyea-i-063-igo-ksf-5-x-xtwjh-og)
4. Select the Pipeline you created and click **Set as Flag Pipeline**.
5. The Pipeline is now displayed under the Flag Pipeline tab.  
![A screenshot of the Flag Pipeline tab with a pipeline added.](https://files.helpdocs.io/kw8ldg1itf/articles/sjzsn4etz9/1665673832040/eem-b-g-wig-xqvz-adiztu-7-bk-smccin-uok-vg-6-ok-pwn-gfw-9-z-bx-qgmo-0-b-qyojx-4-mck-t-ynt-7-f-jqfh-x-5-u-kojjk-bo-1-xo-joqv-x-3-ega-y-4-l-ut-yk-1-h-1-zm-7-hh-jzo-2-x-5-o-dyn-gu-2-jxb-8-k-qz-2-j-rwy-vktjd-98-aqc-h-9-os-sq-8-g-dm-tc-ysq-2-n-7-1-oocux-tf-ih-pps-kwyw-sw)

### Trigger your Pipeline

Test your Pipeline is triggered and runs correctly by making a change to the Flag you applied it to. To do this:

1. Go to the Flag you applied the Pipeline to and toggle it on or off.
2. Go to the **Flag Pipeline** tab. Under the Pipeline, you can see the Pipeline running and the number of stages it needs to complete. If the Pipeline is waiting for a stage to be completed, for example, an approval, a WAITING tag is added.  
![The pipeline running with waiting tag to show it is in progress.](https://files.helpdocs.io/kw8ldg1itf/articles/sjzsn4etz9/1665673836401/1-lw-6-l-8-soe-0-lm-91-l-xe-6-z-8-vxs-7-bg-cq-rvxi-ww-3-aqwu-oay-jd-d-0-wa-vt-9-qzcu-3-zafy-iyn-0-g-65-tue-nkixtpz-u-72-t-0-w-86-v-6-gjp-bvnit-v-0-h-dfi-fl-vru-gjf-dim-fn-b-fop-ofl-uoet-2-wk-bg-2-s-27-f-mmd-sw-nke-0-ru-lts-te-r-2-nd-so-ir-0-art-y-02-yax-cf-41-eb-ijbfd-dt-a)
3. Once complete, a SUCCESS tag is added and you can view the details by clicking on Trigger Details.  
![An entry in the Flag Pipeline tab with a success tag to show the pipeline ran successfully. ](https://files.helpdocs.io/kw8ldg1itf/articles/sjzsn4etz9/1665673841149/myso-4-cf-7-l-xdiv-dcbq-gkk-6-vxn-8-u-tj-nzddx-s-0-nk-4-sg-o-2-qrvv-8-ke-gg-ty-4-wv-9-arh-juj-f-3-iq-nhuk-5-x-kb-l-3-rkt-3-ngdzu-94-i-1-cuu-g-5-ta-9-oxgc-lz-h-78-bg-4-h-p-3-vkws-4-b-v-1-zyk-0-fkk-1-v-5-u-5-ew-ks-h-0-gctld-zi-j-3-rmryr-gmf-38-xy-0-fim-ez-9-p-tpmi-suk-xe-zmvw)

 

 

 

