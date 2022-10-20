---
title: Use Multiple Tags in AWS Dashboards
description: This topic explains how to use multiple tags in AWS.
tags: 
   - helpDocs
   - AWS Dashboards
   - multiple tags
   - tags
helpdocs_topic_id: hmj2vg5thi
helpdocs_is_private: false
helpdocs_is_published: true
---

Multiple Tags in AWS Dashboards can be used to filter and visualize data based on unique Tags and their values. This can be used to drill down the data for specific key values. If you filter `AWS: Multiple Tags - Key 1` with the environment or application, then `Dimension Value 1` will contain the values for that specific Tag. For example, the cost of `XYZ` application in the `ABC` cost center in the `QA` environment only.

For information on core Dashboard functionality, see [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards).This topic explains how to use Multiple Tags in AWS Dashboards.

### Prerequisites

* Review [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).
* Ensure that you have **Dashboard-All View** permissions assigned. See [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md).
* Ensure that you have set up Cloud Cost Management (CCM) for the [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md) cloud provider.
* Ensure that you have added all the required permissions for your cloud provider. The data available in the Dashboard depends on the permissions you provided to the AWS cloud provider when setting up the CCM. For more information, see [Select Features](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).

### Data Ingestion for Dashboard

Once you have set up cost visibility for the [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md) cloud provider and the data is available in the Perspective, you can view **AWS Cost Dashboard**. The data in the Dashboard is updated dynamically.

### Step: Use Multiple Tags

1. Click **Edit Tile** in your AWS Dashboard.
2. In **All Fields**, click **AWS: Multiple Tags**.![](https://files.helpdocs.io/i5nl071jo5/articles/hmj2vg5thi/1651049378005/screenshot-2022-04-27-at-2-19-10-pm.png)
3. In **Filter-only fields**, click **Key 1** and select the filters. Depending on your requirement, you can select filters for **Key 2** and/or **Key 3** also.![](https://files.helpdocs.io/i5nl071jo5/articles/hmj2vg5thi/1651050698470/screenshot-2022-04-27-at-2-41-15-pm.png)
4. In **Dimensions**, click **Value 1**, **2**, and/or **3** (for which you want to visualize the data) and click **Run**. Data for all the specified Keys (Filter-only fields) and Values (Dimensions) are displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/hmj2vg5thi/1651051949678/screenshot-2022-04-27-at-3-02-07-pm.png)

### See Also

Once you have set up cost visibility for your [Kubernetes clusters](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md), [GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md), and [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud providers, you can create your own Dashboards. Refer to the following topics to create your own Dashboard and chart data.

* [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards)
* [Create Visualizations and Graphs](https://docs.harness.io/article/n2jqctdt7c-create-visualizations-and-graphs)

### Next Steps

* [Use Dashboard Actions](https://ngdocs.harness.io/article/y1oh7mkwmh-use-dashboard-actions)
* [Download Dashboard Data](https://ngdocs.harness.io/article/op59lb1pxv-download-dashboard-data)
* [Create Conditional Alerts](https://docs.harness.io/article/ro0i58mvby-create-conditional-alerts)
* [Schedule and Share Dashboards](https://docs.harness.io/article/35gfke0rl8-share-dashboards)
