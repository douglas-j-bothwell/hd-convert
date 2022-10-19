---
title: Add or Exclude a Target in a Target Group
description: While we refer to targeting users, when you create a Target you give it a name and a unique identifier, so a Target can be anything that can be uniquely identified. For example, a Target can be a use…
tags: 
   - helpDocs
helpdocs_topic_id: 5qz1qrugyk
helpdocs_is_private: false
helpdocs_is_published: true
---

While we refer to targeting users, when you create a Target you give it a name and a unique identifier, so a Target can be anything that can be uniquely identified. For example, a Target can be a user, an application, a system, a machine, or any resource uniquely identified by an IP address, email ID, user ID, etc.Target Groups are a collection of [Targets](/article/dbk9uoaid3-add-targets) that allow you to serve Feature Flag Variations to a list of users in bulk. You can group Targets into a group either by picking individual Targets or by defining rules that automatically map Targets to a Target Group. For example, you can add individual Targets `joe@harness.io` and `jane@harness.io` to the QA internal users group or you can define a rule that all the emails ending with `@harness.io` are added to the QA internal users group.

You can also do the opposite and exclude specific Targets from a Target Group.  

This topic describes how to add a Target Group to your Environment, add Targets to the group, and apply the Target Group to a Feature Flag. 

### Before you begin

Make sure you've [created Targets to add to the Target Group](/article/dbk9uoaid3-add-targets).

### Create a Target Group and add Targets

To create a Target Group:

1. In **Feature Flags**, click **Target Management**, then click **Target Groups**.
2. Click **+ New Target Group**.
3. In **Create a Target Group**, enter a Name for your group and click **Create**.
4. (Optional) In **Description**, add a description of the group.

After you have created a Target Group, you need to add Targets to it. You can add Targets to a Target Group by selecting them individually or by setting conditions to add all Targets that meet those criteria. 

#### Add Targets from the Target Group page

You can add individual Targets from the Targets page or the Target Groups page. 

1. In **Target Management**, in **Target Groups**, select the Target Group you want to add Targets to.

![A screenshot of the Target Management page with a Target Group highlighted](https://files.helpdocs.io/kw8ldg1itf/articles/5qz1qrugyk/1660640966178/mc-5-n-7-vdm-0-o-9-j-9-qpr-wr-61-uz-09-ez-k-2-p-5-ndg-t-tjv-klau-1-omo-mxi-7-wam-fxtzp-p-d-1-hzgjo-ei-b-70-ws-uil-1-tl-2-qms-w-9-i-9-yedr-c-3-hyx-vne-3-qx-8-k-p-0-fzx-vvynz-la-9-krdf-y-9-ntoj-68-sovfh-mwbzi-6-j-4-g)*Figure 1: The Target Management page with the Target Groups tab selected*

1. In **Criteria**, click **Edit**.

![The edit button next to Criteria. ](https://files.helpdocs.io/kw8ldg1itf/articles/5qz1qrugyk/1658507048170/v-cx-995-q-a-2-vd-z-0-lie-qgbbaby-qeakz-mi-jzqou-1-f-3-q-ur-0-ellfydr-fp-4-d-8-rbs-v-5-dju-3-y-272-mujkx-hfb-wct-r-12-jbh-ee-2-ljm-pk-96-sq-8-js-tax-tglw-1-w-xt-gt-2-xvjg-4-sf-dn-6-q-3-u-2-nrse-4-pt-bandisb-w-6-nq)*Figure 2: Editing a Target Group*

You can include or exclude specific Targets, or you can set rules to add Targets based on conditions you set. 

##### Add or exclude specific Targets

* To add specific Targets, in **Include the following**, select the Targets.
* To exclude Targets, in **Exclude the following**, select the Targets.

![A screenshot of Targets added to the Target Group Criteria. ](https://files.helpdocs.io/kw8ldg1itf/articles/5qz1qrugyk/1658507117889/b-skzqa-1-wz-qm-7-o-4-dv-1-flyyx-u-1-ar-fwm-sfu-oc-6-ue-2-f-pscxfdz-5-kz-28-bh-65-z-g-6-hvwje-jju-dorh-kk-6-yke-kd-xnaszwz-sds-wukpa-rk-l-0-xm-tiv-0-jkps-ofsu-8-ku-md-t-autvty-8-t-n-75-awlosyk-cw-msj-2-w)*Figure 3: Adding Targets to a Target Group*

##### Add Targets based on conditions

When you create a Target based on Conditions, on the Target overview page the Group isn't displayed under the **Target Groups** column.In addition to targeting individual users, Harness Feature Flags also allows you to target a group based on the conditions you set. You can add conditions by constructing rules using the following:

* The name or identifier of the Target.
* An operator.
* Text that must match the Target name or identifier.

The following operators are supported:



|  |  |  |
| --- | --- | --- |
| **Operator** | **Attribute Type** | **Definition** |
| **starts with** | String | Matches the prefix of a string. If you enter multiple string values, only the first is matched. |
| **ends with** | String | Matches the suffix of a string. If you enter multiple string values, only the first is matched. |
| **contains** | String | Matches a part of a string. If you enter multiple string values, only the first is matched. |
| **equals** | Number or string | Matches the string or number. If you enter multiple string values, only the first is matched. |
| **equals (sensitive)** | Number or string | Matches the number or string and is case-sensitive. If you enter multiple string values, only the first is matched.For example,  the string HELLO is different from the string hello.  |
| **in** | Number or string | Acts as an “or” operator, so you can add multiple values at once. |

 

For example, you could set a rule to add all Targets whose identifiers end in `@harness.io`. 

To add Targets based on conditions:

1. In **T****arget Group Criteria**, click **+ Add Rule**.
2. In the first drop-down menu, select whether the condition applies to the Target Name or Identifier.
3. In the second drop-down menu, select the operator to apply to the Target Name or Identifier.
4. In the search bar, enter the value you want the Target Name or Identifier to match and click the **+** button to add it. The following shows an example of a rule that adds all Targets with a Target Identifier ending in harness.io to the Target Group.

![An example of the Target Group Criteria page with a condition added.](https://files.helpdocs.io/kw8ldg1itf/articles/5qz1qrugyk/1658507144015/k-n-8-jkn-m-0-mnlud-ec-5-g-wzi-yargn-fyu-p-tnumr-wfx-139-erilrfn-w-6-h-jh-an-hr-2-etk-c-2-h-82-k-xls-gdggc-st-zdmldfq-t-4-s-47-d-zybc-duepwgg-hbpp-4-hov-x-5-i-ppb-5-nig-are-0-js-7-ipd-5-lqud-rsym-9-e-gm-ry-q)*Figure 5: Adding Targets based on a condition*

1. Click **Save**. Targets that meet the criteria are now included in the Target Group.

![The Target Group page with the new condition displayed.](https://files.helpdocs.io/kw8ldg1itf/articles/5qz1qrugyk/1658507164912/mbz-va-wj-sif-ko-6-tpg-doehr-53-ku-kd-6-ph-0-m-80-k-6-mf-w-37-z-fe-0-h-88039-pi-dfa-rk-ln-hl-79-l-19-qz-s-506-jjcos-1-eubr-ykv-qoi-ko-lt-8-y-3-ongxax-xlx-8-icl-st-f-3-p-lvni-u-6-tq-7-igtq-4-msvg-8-a-qfwvy-mq)*Figure 6: Viewing the condition for adding a Target*

When you add Targets based on conditions, on the **Target Management:Targets** page, the Target Group is **not** displayed in the **Target Groups** column.### Add or exclude Targets from Target settings

You can use Target Settings to include or exclude Targets from a Target Group. Complete the following steps to include or exclude Targets using the Target Settings:

1. In **Target Management**, in **Targets**, click the Target you want to add to a group.
2. Click **Target Groups**, then **Add to Target Groups** to add a specific Target, or click **Exclude from Target Groups** to exclude a specific Target. You can add or exclude the Target to multiple groups at once.

![A screenshot of a Target with the Target Groups tab opened.](https://files.helpdocs.io/kw8ldg1itf/articles/5qz1qrugyk/1658507195650/59-v-6-y-k-3-d-nxs-1-lr-gbg-jnpccp-uyxon-rl-i-6-tp-iedw-d-7-nr-tr-a-snsb-0-nv-dd-wb-wn-pzg-s-7-d-pb-7-c-ov-vanf-btf-8-s-tjaga-r-42-h-6-e-hm-6-tc-t-9-dgd-tj-9-zi-fl-mej-vkq-tdehb-g-9-li-0-b-wz-6-r-uft-2-qwvkm-iomzw)*Figure 7: Adding and excluding Targets from the Target's settings*

1. Select the Group(s) to add the Target to or to exclude a Target from, then click **Add to (1) Target Group**, or **Exclude from (1) Target Group**.
2. The Targets are now added to the Target Group.

### Next step

After you have added the Targets and Target Groups, you can then [use them on your Feature Flags.](/article/xf3hmxbaji-targeting-users-with-flags)

