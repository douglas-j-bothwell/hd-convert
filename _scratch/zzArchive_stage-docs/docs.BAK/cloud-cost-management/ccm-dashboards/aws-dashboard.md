---
title: View AWS Cost Dashboard
description: This topic describes how to view By Harness AWS Cost Dashboard and get more information about that data.
tags: 
   - helpDocs
   - Dashboards
   - AWS
helpdocs_topic_id: u3yxrebj6r
helpdocs_is_private: false
helpdocs_is_published: true
---

Dashboards help you model and analyze business metrics and operational data. You can use this data to make data-driven business decisions. Using charts, data tables, and filters, Dashboards help you get the most useful cost data.

For information on core Dashboard functionality, see [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards).Harness provides pre-loaded **By Harness** (pre-defined) and **Custom** (user-defined) Dashboards to visualize cloud cost data across clusters and cloud accounts. Using the **AWS Cost Dashboard** you can:

* Discover new analytical insights into your AWS cloud costs
* Track various cloud cost indicators across different zones and time range
* Explore the cloud cost data in a logical and structured manner
* View your cloud costs at a glance, understand what is costing the most, and analyze cost trends

This topic describes how to view the **By Harness AWS Cost Dashboard** and get more information about that data.

![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626148311517/screenshot-2021-07-13-at-9-21-29-am.png)In this topic:

* [Prerequisites](aws-dashboard.md)
* [Data Ingestion for Dashboard](aws-dashboard.md)
* [Step: View AWS Cost Dashboard](aws-dashboard.md)
* [See Also](aws-dashboard.md)
* [Next Steps](aws-dashboard.md)

### Prerequisites

* Review [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).
* Ensure that you have **Dashboard-All View** permissions assigned. See [Manage Access Control for CCM Dashboards](manage-access-control-for-ccm-dashboards.md).
* Ensure that you have set up Cloud Cost Management (CCM) for the [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md) cloud provider.
* Ensure that you have added all the required permissions for your cloud provider. The data available in the Dashboard depends on the permissions you provided to the AWS cloud provider when setting up the CCM. For more information, see [Select Features](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).

### Data Ingestion for Dashboard

Once you have set up cost visibility for the [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md) cloud provider and the data is available in the Perspective, you can view **AWS Cost Dashboard**. The data in the Dashboard is updated dynamically.

### Step: View AWS Cost Dashboard

Perform the following steps to view AWS Cost Dashboard:

1. In Harness, click **Dashboards**.
2. In **All Dashboards**, select **By Harness** and click **AWS Cost Dashboard**.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626149925113/screenshot-2021-07-13-at-9-48-12-am.png)The AWS Cost Dashboard is displayed:  
  


|  |  |  |
| --- | --- | --- |
| **Dimensions** | **Description** | **Context and Visibility** |
| Total Cost | The total AWS cost with cost trend. |  |
| Forecasted Cost | The forecasted cloud cost with cost trend. Forecasted cost is the prediction based on your historical cost data and it is predicted for the same future time period as your selected time range. |  |
| Cost by AWS Account | The cost of each AWS account you are using to connect Harness to AWS via a Harness AWS Cloud Provider. |  |
| Top Cost Trend by Services | The top AWS services by cost increase or decrease |  |
| Historical and Forecasted Cost | The historical and forecasted AWS cost. Forecasted cost is the prediction based on your historical cost data and it is predicted for the same future time period as your selected time range. |  |
| Current Period vs Last Period | The cost of the current and previous time range. |  |
| Most Expensive Services by Month | Top five services that incurred the maximum cost per month. |  |
3. Select **Time Range** to filter the data based on pre-defined time range filters. The available filters are:
	* Last 7 Days
	* Last 30 Days
	* Last 90 Days
	* Last year
4. Once you have selected the Time Range filter, click **Reload**. The data is refreshed with the latest data from the database.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626184742941/screenshot-2021-07-13-at-7-28-38-pm.png)
5. Hover on the chart to see the cost details.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626519581838/screenshot-2021-07-17-at-4-29-20-pm.png)
6. In **Cost by AWS** **Account**, click the up or down arrow button to scroll up or down the list. The list shows the percentage of each AWS account with respect to the cost contribution.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626519875067/screenshot-2021-07-17-at-4-34-16-pm.png)
7. In **Historical and Forecasted Cost**, click on the chart to further drill into the cost details **by Time Period/Time**.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626614366421/screenshot-2021-07-18-at-6-48-40-pm.png)The cost for the selected Time period is displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626614553289/screenshot-2021-07-18-at-6-50-07-pm.png)
8. In **Most Expensive Services by Month**, click on the chart to further drill into the cost details:
	* by Time Period/Week
	* by Time Period/Date
	* by Time Period/Time![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626615522170/screenshot-2021-07-18-at-7-07-25-pm.png)The cost data for the selected filter is displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626615590200/screenshot-2021-07-18-at-7-09-37-pm.png)
9. You can further drill into **by Time Period/Date** and **by Time Period/Time** cost details in the resulting dashboard.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626615883478/screenshot-2021-07-18-at-7-13-16-pm.png)The cost data for the selected filter is displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626615991842/screenshot-2021-07-18-at-7-15-43-pm.png)
10. You can further drill into **by Time Period/Time** cost details in the resulting dashboard.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626616072829/screenshot-2021-07-18-at-7-17-00-pm.png)The cost data for the selected filter is displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626616128994/screenshot-2021-07-18-at-7-18-30-pm.png)
11. Click **Back** to go back to the previous page in the Dashboard.
12. Click **Download** to download the Dashboard. See [Download Dashboard Data](https://docs.harness.io/article/op59lb1pxv-download-dashboard-data).
13. Click the **Filter** icon to hide or show the filters.![](https://files.helpdocs.io/i5nl071jo5/articles/u3yxrebj6r/1626185013021/screenshot-2021-07-13-at-7-33-22-pm.png)

### See Also

Once you have set up cost visibility for your [Kubernetes clusters](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), [AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md), [GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md), and [Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md) cloud providers, you can create your own Dashboards. Refer to the following topics to create your own Dashboard and chart data.

* [Create Dashboards](https://docs.harness.io/article/ardf4nbvcy-create-dashboards)
* [Create Visualizations and Graphs](https://docs.harness.io/article/n2jqctdt7c-create-visualizations-and-graphs)

### Next Steps

* [Use Dashboard Actions](https://ngdocs.harness.io/article/y1oh7mkwmh-use-dashboard-actions)
* [Download Dashboard Data](https://ngdocs.harness.io/article/op59lb1pxv-download-dashboard-data)
* [Create Conditional Alerts](https://docs.harness.io/article/ro0i58mvby-create-conditional-alerts)
* [Schedule and Share Dashboards](https://docs.harness.io/article/35gfke0rl8-share-dashboards)

