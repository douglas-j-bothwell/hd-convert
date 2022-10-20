---
title: View Multi-cloud Cost Overview Dashboard
description: This topic describes how to view By Harness Multi-cloud Cost Overview Dashboard and get more information about that data.
tags: 
   - helpDocs
   - Dashboards
   - multi-cloud
   - Multi-cloud Cost Overview
helpdocs_topic_id: ff5f08g4v4
helpdocs_is_private: false
helpdocs_is_published: true
---

**Dashboards** are a collection of charts and data tables with filters that you can use to get at the data you're interested in. Dashboards serve as a platform for data modeling and analytics using a combination of available business metrics and operational data. You can use this data to make data-driven informed business decisions.

For information on core Dashboard functionality, see [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards).Harness provides **By Harness** (pre-defined) and **Custom** (user-defined) Dashboards to visualize cloud cost data across cloud providers. Using the **Multi-cloud Cost Overview Dashboard** you can:

* Get a unified view of your cloud cost data across the cloud environment. For example, AWS, Azure, GCP, and Cluster
* Discover new analytical insights into your cluster costs across cloud providers
* Track various cloud cost indicators across different zones and time range
* Explore the cloud cost data in a logical and structured manner
* View your cloud costs at a glance, understand what is costing the most, and analyze cost trends

This topic describes how to view the **By Harness** **Multi-cloud Cost Overview** **Dashboard** and get more information about that data.

![](https://files.helpdocs.io/i5nl071jo5/articles/ff5f08g4v4/1626543604654/screenshot-2021-07-17-at-11-09-45-pm.png)In this topic:

* [Before You Begin](multi-cloud-cost-overview-dashboard.md)
* [Prerequisites](multi-cloud-cost-overview-dashboard.md)
* [Data Ingestion for Multi-cloud Cost Overview Dashboard](multi-cloud-cost-overview-dashboard.md)
* [Step: View Multi-cloud Cost Overview Dashboard](multi-cloud-cost-overview-dashboard.md)
* [See Also](multi-cloud-cost-overview-dashboard.md)
* [Next Steps](multi-cloud-cost-overview-dashboard.md)

### Before You Begin

* Review the following topics:
	+ [Set Up Cloud Cost Management for Kubernetes](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md)
	+ [Set Up Cloud Cost Management for GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md)
	+ [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
	+ [Set Up Cloud Cost Management for Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md)

### Prerequisites

* Ensure that you have **Dashboard-All View** permissions assigned. See [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md).
* Ensure that you have set up Cloud Cost Management (CCM) for the [Kubernetes clusters](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md), [GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md), and [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud accounts.
* Ensure that you have added all the required permissions for your cloud account. The data available in the Dashboard depends on the permissions you provided to the cloud accounts or clusters when setting up CCM.

### Data Ingestion for Multi-cloud Cost Overview Dashboard

Once you have set up cost visibility for your clusters and cloud accounts and the data is available in the Perspective, you can view the **Multi-cloud Cost Overview Dashboard**. The data in the Dashboard is updated dynamically.

### Step: View Multi-cloud Cost Overview Dashboard

Perform the following steps to view the Multi-cloud Cost Overview Dashboard:

1. In **Harness**, click **Dashboard****s**.
2. In **All Dashboards**, select **By Harness** and click **Multi-cloud Cost Overview Dashboard**.![](https://files.helpdocs.io/i5nl071jo5/articles/ff5f08g4v4/1626610296437/screenshot-2021-07-18-at-5-41-15-pm.png)The cost data is displayed.  


|  |  |
| --- | --- |
| **Dimension** | **Description** |
| Total Cost | The total cloud cost across clusters and cloud accounts with cost trend. |
| Forecasted Cost | The forecasted cluster and cloud accounts cost with cost trend. Forecasted cost is the prediction based on your historical cost data and it is predicted for the same future time period as your selected time range. |
| Cost by Cloud Providers | The cost of each cloud provider. For example, AWS, GCP, Azure, and Kubernetes cluster. |
| Cost by Services or Products | The cost of each Service and Product across cloud providers. |
| Weekly Cost Trend | The weekly cost trend across cloud providers. |
3. Select **Time Range** to filter the data based on pre-defined time range filters. The available filters are:
	* Last 7 Days
	* Last 30 Days
	* Last 90 Days
	* Last year
4. Once you have selected the **Time Range**, click **Reload**. The data is refreshed with the latest data from the database. By default, **Last 30 Days** is selected.![](https://files.helpdocs.io/i5nl071jo5/articles/ff5f08g4v4/1626611962109/screenshot-2021-07-18-at-6-09-07-pm.png)
5. Hover over the chart to see the cost details.![](https://files.helpdocs.io/i5nl071jo5/articles/ff5f08g4v4/1626612727480/screenshot-2021-07-18-at-6-21-50-pm.png)
6. In **Cost by Cloud Providers**, click the cloud provider to view the cost of a specific cloud provider. For example, click GCP to update the dashboard data only for GCP.
7. In the resulting dashboard, you can further refine your view. In **Weekly Cost Trend**, click **Time period/Week** for which you want to view the cost.
8. In **Cost by Services or Products**, hover over the chart to view the cost of **Products**. The applied filters are also displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/ff5f08g4v4/1626612939090/screenshot-2021-07-18-at-6-25-15-pm.png)
9. Click the **Filter** icon to hide or show the filters.![](https://files.helpdocs.io/i5nl071jo5/articles/ff5f08g4v4/1626613017735/screenshot-2021-07-18-at-6-26-31-pm.png)

### See Also

Once you have set up cost visibility for your [Kubernetes clusters](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md), [GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md), and [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud providers, you can create your own Dashboards. Refer to the following topics to create your own Dashboard and chart data.

* [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards)
* [Create Visualizations and Graphs](https://docs.harness.io/article/n2jqctdt7c-create-visualizations-and-graphs)

### Next Steps

* [Create Conditional Alerts](https://docs.harness.io/article/ro0i58mvby-create-conditional-alerts)
* [Schedule and Share Dashboards](https://docs.harness.io/article/35gfke0rl8-share-dashboards)
* [Use Dashboard Actions](https://docs.harness.io/article/y1oh7mkwmh-use-dashboard-actions)
* [Download Dashboard Data](https://docs.harness.io/article/op59lb1pxv-download-dashboard-data)

