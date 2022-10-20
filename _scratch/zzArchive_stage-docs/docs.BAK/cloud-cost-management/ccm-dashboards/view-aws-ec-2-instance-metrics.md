---
title: View AWS EC2 Instance Metrics Dashboard
description: This topic describes how to view the AWS EC2 Instance Metrics Dashboard and get more information about that data.
tags: 
   - helpDocs
   - Dashboards
   - instance metrics
   - aws ec2
   - AWS
helpdocs_topic_id: mwhraec911
helpdocs_is_private: false
helpdocs_is_published: true
---

**Dashboards** are a collection of charts and data tables with filters that you can use to get at the data you're interested in. Dashboards serve as a platform for data modeling and analytics using a combination of available business metrics and operational data. You can use this data to make data-driven informed business decisions.

For information on core Dashboard functionality, see [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards).Harness provides pre-loaded **By Harness** (pre-defined) and **Custom** (user-defined) Dashboards to visualize cloud cost data across clusters and cloud accounts. Using the **AWS EC2** **Instance Metrics** **Dashboard** you can:

* Discover new analytical insights into your AWS EC2 instances metrics
* Track various cloud cost indicators across different zones and time range
* Explore the cloud cost data in a logical and structured manner
* View your cloud costs at a glance, understand what is costing the most, and analyze cost trends

This Dashboard will not be available if you have not selected **AWS ECS and Resource Inventory Management** feature when setting up [CCM for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).This topic describes how to view the **AWS EC2 Instance Metrics** **Dashboard** and get more information about that data.

![](https://files.helpdocs.io/i5nl071jo5/articles/mwhraec911/1627463943914/screenshot-2021-07-28-at-2-48-42-pm.png)In this topic:

* [Before You Begin](view-aws-ec-2-instance-metrics.md)
* [Prerequisites](view-aws-ec-2-instance-metrics.md)
* [Data Ingestion for Dashboard](view-aws-ec-2-instance-metrics.md)
* [Step: View AWS EC2 Instance Metrics Dashboard](view-aws-ec-2-instance-metrics.md)
* [See Also](view-aws-ec-2-instance-metrics.md)
* [Next Steps](view-aws-ec-2-instance-metrics.md)

### Before You Begin

* [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md)

### Prerequisites

* Review [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Ensure that you have **Dashboard-All View** permissions assigned. See [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md).
* Ensure that you have set up Cloud Cost Management (CCM) for the [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md) cloud provider.
* Ensure that you have selected **AWS ECS and Resource Inventory Management** feature when creating the AWS connector. See [Select Features](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).

### Data Ingestion for Dashboard

Once you have set up cost visibility for the [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md) cloud provider and the data is available in the Perspective, you can view the dashboard. The data in the Dashboard is updated dynamically.

### Step: View AWS EC2 Instance Metrics Dashboard

Perform the following steps to view AWS EC2 Instance Metrics Dashboard:

1. In Harness, click **Dashboards**.
2. In **All Dashboards**, click **AWS EC2 Instance Metrics Dashboard**.
3. Select **EC2 Instance Id** from the drop-down list for which you want to view the details. You can select multiple IDs.
4. In **Metrics start time date**, select the time duration. You can select the preset value or use custom.  
By default, the **Last 30 Days** is selected.
	1. **Presets**: Select a Preset filter. For example, Today, Yesterday, etc.![](https://files.helpdocs.io/i5nl071jo5/articles/mwhraec911/1627550101589/screenshot-2021-07-29-at-2-43-24-pm.png)
	2. **Custom**: Custom allows you to select the date range.![](https://files.helpdocs.io/i5nl071jo5/articles/mwhraec911/1627550206239/screenshot-2021-07-29-at-2-46-30-pm.png)
5. Select the Public IP Address.
6. Once you have selected all the filters, click **Update**.  
  
The **EC2 Instance Metrics Dashboard** is displayed.

### See Also

Once you have set up cost visibility for your [Kubernetes clusters](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md), [GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md), and [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud providers, you can create your own Dashboards. Refer to the following topics to create your own Dashboard and chart data.

* [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards)
* [Create Visualizations and Graphs](https://docs.harness.io/article/n2jqctdt7c-create-visualizations-and-graphs)

### Next Steps

* [Use Dashboard Actions](https://ngdocs.harness.io/article/y1oh7mkwmh-use-dashboard-actions)
* [Download Dashboard Data](https://ngdocs.harness.io/article/op59lb1pxv-download-dashboard-data)
* [Schedule and Share Dashboards](https://docs.harness.io/article/35gfke0rl8-share-dashboards)
* [Create Conditional Alerts](https://ngdocs.harness.io/article/ro0i58mvby-create-conditional-alerts)

