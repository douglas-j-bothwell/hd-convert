---
title: Filter Flags by State
description: To help manage your Feature Flags, you can use the filter tiles on the Harness Platform to filter your Flags based on the following states&#58; Figure 1&#58; The Flag overview dashboard State Description All…
tags: 
   - helpDocs
helpdocs_topic_id: 2s5qt02s74
helpdocs_is_private: false
helpdocs_is_published: true
---

To help manage your Feature Flags, you can use the filter tiles on the Harness Platform to filter your Flags based on the following states: 

![A screenshot of the Feature Flag states dashboard. ](https://files.helpdocs.io/kw8ldg1itf/articles/2s5qt02s74/1657802380832/uevlqjl-nh-7-urh-kh-jr-3-ee-yqq-hb-vx-55-pvt-pwb-hu-0-lxxrf-sa-w-13-hpp-it-ese-yx-6-oy-fsdrl-awq-pq-7-lz-2-o-qma-2-zco-yc-8-p-8-lz-pniyc-jngl-3-jea-qbdo-8-ibjqs-ulo-gbix-l-wntb-dxghbgoqjl-hygeh-1-qnc)*Figure 1: The Flag overview dashboard*



|  |  |
| --- | --- |
| **State** | **Description** |
| All Flags | All of the Flags that you’ve created. |
| Enabled Flags | Flags that are currently toggled on.  |
| Permanent Flags | Flags you intend to stay in your systems indefinitely and that you marked as permanent when creating them. Permanent flags are never marked as stale. |
| Recently Changed Flags | Flags that have been changed in the last 24 hours. Changes include enabling or disabling a Flag, or adding new Rules or Targets. |
| Active Flags | Flags that have been evaluated in the last 7 days |
| Potentially Stale Flags | Flags are marked as potentially stale if in the past 60 days:* They haven't been changed or evaluated.
* Their default rules or target rules haven’t been added to or updated.
* They haven’t been toggled on or off.
 |

A Flag can be marked as both Active and Potentially Stale if it has been Evaluated via an SDK but no other changes have been made in over 60 days.  For example, if you Evaluated `Flag_A` yesterday using an SDK, but haven’t made any changes on the Harness Platform in over three months, the Flag will be marked as Active and Potentially Stale on the Platform. ### Filter your Flags

To view filter your Flags:

1. Go to your project on the Harness Platform.
2. Click on **Feature Flags**.
3. Click on the filter you want to use.
4. A list of the relevant Flags are displayed.

![A screenshot of the Permanent Flags tile selected to filter for permanent flags.](https://files.helpdocs.io/kw8ldg1itf/articles/2s5qt02s74/1657802369150/1-tjm-8-zvkw-6-o-8-bb-8-otdcf-2-it-19-r-k-4-dett-0-h-mb-49-roeuc-xucugqvlvoje-hsdo-wx-bot-mn-1-jl-xy-at-fui-ktkb-z-1-iy-71-et-jnqe-ljj-is-7-exf-lgs-cj-2-ebi-tmbbsc-2-cmnf-9-p-aj-k-3-uom-8-qk-502-x-ma-1-ow)*Figure 2: A filtered list of Flags*

 

