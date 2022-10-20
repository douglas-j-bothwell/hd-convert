---
title: View Azure Cost Dashboard
description: This topic describes how to view By Harness Azure Cost Dashboard and get more information about that data.
tags: 
   - helpDocs
   - Dashboards
   - Azure Cost Dashboard
helpdocs_topic_id: n7vpieto0n
helpdocs_is_private: false
helpdocs_is_published: true
---

**Dashboards** are a collection of charts and data tables with filters that you can use to get at the data you're interested in. Dashboards serve as a platform for data modeling and analytics using a combination of available business metrics and operational data. You can use this data to make data-driven informed business decisions.

For information on core Dashboard functionality, see [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards).Harness provides pre-loaded **By Harness** (pre-defined) and **Custom** (user-defined) Dashboards to visualize cloud cost data across clusters and cloud accounts. Using the **Azure Cost Dashboard** you can:

* Discover new analytical insights into your Azure cloud costs
* Track various cloud cost indicators across different zones and time range
* Explore the cloud cost data in a logical and structured manner
* View your cloud costs at a glance, understand what is costing the most, and analyze cost trends

This topic describes how to view **By Harness** **Azure Cost Dashboard** and get more information about that data.

![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626437641489/screenshot-2021-07-16-at-5-43-01-pm.png)In this topic:

* [Before You Begin](azure-cost-dashboard.md)
* [Prerequisites](azure-cost-dashboard.md)
* [Data Ingestion for Azure Cost Dashboard](azure-cost-dashboard.md)
* [Step: View Azure Cost Dashboard](azure-cost-dashboard.md)
* [See Also](azure-cost-dashboard.md)
* [Next Steps](azure-cost-dashboard.md)

### Before You Begin

* [Set Up Cloud Cost Management for Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md)
* [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md)

### Prerequisites

* Review [Set Up Cloud Cost Management for Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md)
* Ensure that you have **Dashboard-All View** permissions assigned. See [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md).
* Ensure that you have set up Cloud Cost Management (CCM) for the [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud provider.
* Ensure that you have added all the required permissions for your cloud provider. The data available in the Dashboard depends on the permissions you provided to the Azure cloud provider when setting up CCM. For more information, see [Select Features](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md).

### Data Ingestion for Azure Cost Dashboard

Once you have set up cost visibility for the [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud provider and the data is available in the Perspective, you can view **Azure Cost Dashboard**. The data in the Dashboard is updated dynamically.

### Step: View Azure Cost Dashboard

Perform the following steps to view Azure Cost Dashboard:

1. In Harness, click **Dashboards**.
2. In **All Dashboards**, select **By Harness** and click **Azure Cost Dashboard**.![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626506498841/screenshot-2021-07-17-at-12-51-25-pm.png)The Azure Cost Dashboard is displayed.  


|  |  |
| --- | --- |
| **Dimension** | **Description** |
| Total Cost | The total Azure cloud cost with cost trend. |
| Total Cost by Meter Category | The total cost of the meter. For example, Cloud services, Networking, and so on. |
| Total Cost by Region | The total cost of each Azure region you are currently running services in. |
| Total Cost by Month | The total Azure cloud cost by month. |
| Most Expensive Service by Month | The monthly cost of the most expensive Azure services, for example, Virtual Machines, Azure App Service, Azure DNS, etc. |
| Most Expensive Resource Types | The cost of the most expensive resource types. |
| Monthly Cost and Difference by Meter Category | The monthly meter cost and the differences in the cost from the previous month. |
| Monthly Cost by Instance ID | The monthly cost of the instance ID. Each VM in a scale set gets an instance ID that uniquely identifies it. |
| Monthly Cost by Service Name | The monthly cost of Azure services, for example, Virtual Machines, Azure App Service, Azure DNS, etc. |
| Monthly Cost by Resource Group | The monthly cost of the resource group. A resource group is a container that holds related resources that you want to manage as a group. |
3. Select **Time Range** to filter the data based on pre-defined time range filters. The available filters are:
	* Last 7 Days
	* Last 30 Days
	* Last 90 Days
	* Last year
4. Once you have selected the **Time Range**, click **Update**. The data is refreshed with the latest data from the database. By default, **Last 30 Days** is selected.![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626517615371/screenshot-2021-07-17-at-3-56-32-pm.png)
5. Hover on the chart to see the cost details.![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626517404771/screenshot-2021-07-17-at-3-53-09-pm.png)
6. In the **Cost by Meter Category** and **Total Cost by Region** click the up or down arrow button to scroll up or down the list. The list shows the percentage of each meter category with respect to the cost contribution.![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626520603289/screenshot-2021-07-17-at-4-46-24-pm.png)
7. You can further filter and customize your result in the Dashboard. Click on the individual dimension and field for which you want to see the data. For example, select **Virtual Machines** in **Azure Meter Category** and **US East** in the **Region**.  
  
The dashboard displays the data based on the set filter.![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626517335070/screenshot-2021-07-17-at-3-51-53-pm.png)
8. Click the Filter icon to hide or show the filters.![](https://files.helpdocs.io/i5nl071jo5/articles/n7vpieto0n/1626518792009/screenshot-2021-07-17-at-4-16-16-pm.png)

### See Also

Once you have set up cost visibility for your [Kubernetes clusters](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md), [GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md), and [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud providers, you can create your own Dashboards. Refer to the following topics to create your own Dashboard and chart data.

* [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards)
* [Create Visualizations and Graphs](https://docs.harness.io/article/n2jqctdt7c-create-visualizations-and-graphs)

### Next Steps

* [Use Dashboard Actions](https://docs.harness.io/article/y1oh7mkwmh-use-dashboard-actions)
* [Download Dashboard Data](https://docs.harness.io/article/op59lb1pxv-download-dashboard-data)
* [Create Conditional Alerts](https://docs.harness.io/article/ro0i58mvby-create-conditional-alerts)
* [Schedule and Share Dashboards](https://docs.harness.io/article/35gfke0rl8-share-dashboards)
* [View AWS Cost Dashboard](aws-dashboard.md)

