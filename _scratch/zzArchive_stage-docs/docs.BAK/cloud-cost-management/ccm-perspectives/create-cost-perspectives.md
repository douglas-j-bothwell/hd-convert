---
title: Create Cost Perspectives
description: Perspectives allow you to group your resources in ways that are more meaningful to your business needs.
tags: 
   - helpDocs
   - perspectives
   - cloud cost management
helpdocs_topic_id: dvspc6ub0v
helpdocs_is_private: false
helpdocs_is_published: true
---

You can add business context to your Harness Cloud Cost Management (CCM) data using Perspectives. Perspectives allow you to group your resources in ways that are more meaningful to your business needs.

### Before You Begin

* [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* [Set Up Cloud Cost Management for Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md)
* [Set Up Cloud Cost Management for GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md)
* [Set Up Cloud Cost Management for Kubernetes](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md)

### Cloud Costs Perspective Concepts

This section describes Perspective concepts.

#### Perspectives

Perspectives allow you to group your resources in ways that are more meaningful to your business needs.

For example, you can group and filter by Account, Environment, Service, Region, Product, Label, Namespace, Workload, etc., and create a Perspective for your business, finance, and engineering teams.

Here are some of the examples where you could use Perspectives:

* Build your own visual interface using flexible rules and filters. With Perspectives, business units can create views that align with their business needs based on groups of resources determined by different rules and filters.
* Create Perspectives broken down by project, team, department, or business unit to gain granular visibility into all your cloud environments. Perspectives provide a single-pane view of different products, for example, clusters, applications, AWS, GCP, and Azure.
* Schedule and share the reports with the key stakeholders for maximum business impact.
* Estimate costs consumed by specific teams, groups, departments, BUs, LOBs, cost-centers, etc.

#### Rule-Based Engine

Perspectives use a rule-based engine to organize and display your cloud costs. Each Perspective has a set of rules and each rule can have multiple conditions. The following operators are supported for each condition:

* **IN**: The exact match operation is used to filter for the exact value specified.
* **NOT IN**: The exact match operation is used to filter for all values except the one specified.
* **NULL**: Null means the selected filter has no value. If you select NULL for your filter, then the cost of the selected filter isn't included in the Perspective.  
For example, in **Rules for Perspective**, if you select `Label: kubernetes.io/name` as `NULL`, then your Perspective won't include the cost for the selected label (`kubernetes.io/name`). It will include the cost for all the other resources.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627987692207/screenshot-2021-08-03-at-4-17-28-pm.png)
* **NOT NULL**: Not null means that the selected filter has a value. If you select NOT NULL for your filter, then only the cost of the selected filter is included in the perspective.  
  
For example, in **Rules for Perspective**, if you select `Label: kubernetes.io/name` as `NOT_NULL`, then your Perspective will list the cost of the selected label only (`kubernetes.io/name`). It won't include the cost of any other resources.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627987755009/screenshot-2021-08-03-at-4-18-40-pm.png)

#### Filters

You can create a Perspective for your resources using rules and filters. The filters are used to group the resources. The following are the supported filters:

* **AWS**: CCM allows you to view your AWS costs at a glance, understand what is costing the most, and analyze cost trends. CE displays the data for all your Amazon Web Services (ECS, EC2, and so on). For more information, see [Analyze Cost for AWS Using Perspectives](../root-cost-analysis/analyze-cost-for-aws.md).
* **GCP**: CCM allows you to view your Google Cloud Platform (GCP) costs, understand what is costing the most, and analyze cost trends. CE displays data for all your GCP products (such as Compute Engine, Cloud Storage, BigQuery, and so on), projects, SKUs, and location. For more information, see [Analyze Cost for GCP ​Using Perspectives](../root-cost-analysis/analyze-cost-for-gcp-using-perspectives.md).
* **Azure**: CCM allows you to view your Azure costs at a glance, understand what is costing the most, and analyze cost trends. CE displays the data for all your Azure services (Storage accounts, Virtual machines, Containers, and so on). For more information, see [Analyze Cost for Azure Using Perspectives](../root-cost-analysis/analyze-cost-for-azure.md).
* **Cluster**: Total cost, Cost trend, Idle cost, and Unallocated cost for each cluster.
* **Region**: Each AWS, GCP, or Azure region you're currently running services in.
* **Product**: Each of your active products with its cloud costs.
* **Label**: Costs organized by the Kubernetes labels used in the workload manifests. In GCP, it refers to each [label](https://cloud.google.com/resource-manager/docs/creating-managing-labels) that you are using to organize your Google Cloud instances.

#### Preview

As you add your resources in the **Perspective Builder**, a **Preview** of your Perspective is displayed.

![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627988079256/screenshot-2021-08-03-at-4-24-14-pm.png)The following are the key advantages of Preview:

* Provides a quick visual representation of your resources in the Perspective without saving them.
* Allows you to group resources in the preview mode itself. You can group by **Common**, **Custom** (if Custom Fields are available), **Cluster**, **AWS**, **GCP**, and **Azure**.
* Helps you to review your changes faster.

**Grouped by** Product in Preview.### Create a Perspective

You can create a Perspective by grouping your resources the way you wish. For example, if you want to create a perspective for your CFO, first add default or custom filters and then further group by Service, Account, Workload, Namespace, etc. that you would want to include in your Perspective.

You can create up to 250 Perspectives.Perform the following steps to create a Perspective:

1. In **Cloud Costs**, click **Perspectives**.
2. In **Perspectives**, click **New Perspective**.
3. In **Perspective Builder**, enter a name for your perspective. By default, a unique name is entered in the field. You can edit the pre-populated name of the perspective.Perspective names mustn't include any special characters.
4. In **Perspective Builder**, in **Rules for Perspective**, click **+** **Add rule**.
5. Select **Common**, **Cluster**, **AWS**, **GCP**, **Azure**, **Region**, or **Product**.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627988670259/screenshot-2021-08-03-at-4-33-44-pm.png)As you add your resources in the Perspective Builder, a [Preview](create-cost-perspectives.md) is displayed of your Perspective.
6. Select the operator. The supported operators are:
	* **IN**: The exact match operation is used to filter for the exact value specified.
	* **NOT IN**: The exact match operation is used to filter for all values except the one that is specified.
	* **NULL**: Null means the selected filter has no value. If you select NULL for your filter, then the cost of the selected filter is not included in the perspective.  
	  
	For example, in **Rules for Perspective**, if you select `Label: kubernetes.io/name` as `NULL`, then your Perspective will not include the cost for the selected label (`kubernetes.io/name`). It will include the cost for all the other resources.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627987692207/screenshot-2021-08-03-at-4-17-28-pm.png)
	* **NOT NULL**: Not null means that the selected filter has value. If you select NOT NULL for your filter, then only the cost of the selected filter is included in the perspective.  
	  
	For example, in **Rules for Perspective**, if you select `Label: kubernetes.io/name` as `NOT_NULL`, then your perspective will list the cost of the selected label only (`kubernetes.io/name`). It will not include the cost of any other resources.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627987755009/screenshot-2021-08-03-at-4-18-40-pm.png)
7. Select value for your filter. You can select multiple values. You can also filter and customize your result using the search option.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1627989653941/screenshot-2021-08-03-at-4-50-35-pm.png)
8. Once you have added all the filters, click **Next** to add a report sharing schedule and budget.

### Budgets, Reports, and Alerts

For details on adding Budgets, Reports, and Alerts go to:

* [Create a Budget for Your Perspective](create-a-budget-perspective.md)
* [Share Your Cost Perspective Report](share-cost-perspective-report.md)
* [Detect Cloud Cost Anomalies with CCM](../ccm-cost-anomaly-detection/detect-cloud-cost-anomalies-with-ccm.md)

### Perspective Preferences

In **Preferences**, you have the following options.

##### Include Others

The graphs displayed in a Perspective show the top 12 costs only. In order to include the remaining data, Harness displays **Others**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/dvspc6ub0v/1659989014900/clean-shot-2022-08-08-at-13-03-19.png)**Others** is always the total cost minus the top 12 costs listed in the graph you are viewing.

Enable **Include Others** in **Preferences** to have it displayed in the Perspective chart.

You can also enable **Include Others** in the Perspective chart:

![](https://files.helpdocs.io/kw8ldg1itf/articles/dvspc6ub0v/1658441098475/clean-shot-2022-07-21-at-15-04-05.png)The **Include Others** option must be enabled in **Preferences** to make it persist in the Perspective.

##### Include Unallocated

In some graphs, you will also see an **Unallocated** item. This is included to help you see all of the costs. If you look at the Total Cost in the Perspective, it includes the costs of all items and the Unallocated cost.

![](https://files.helpdocs.io/kw8ldg1itf/articles/dvspc6ub0v/1659989214307/clean-shot-2022-08-08-at-13-06-37.png)The **Include Unallocated** option is only available in the chart when the **Group By** is using **Cluster** and the following options are selected:

* Namespace
* Namespace Id
* Workload
* Workload Id
* ECS Task
* ECS Task Id
* ECS Service Id
* ECS Service
* ECS Launch Type Id
* ECS Launch Type

##### Review: No Account/Project/etc

It's important to understand the difference between the **Others** and **No Account/Project/etc** categories.

When a Perspective includes multiple data sources (for example, AWS, GCP, and Cluster) and you select one data source in a Perspective **Group By**, such as **AWS: Account**, the costs for the AWS data source are displayed individually.

The costs for the other data sources (GCP, Cluster) are grouped under **No Account**.

Another example is if the **Group By** is **Project**. For example, if you selected GCP:Project then the **No Project** item in the graph represents the AWS and Cluster project costs.

### Edit a Perspective

To edit a Perspective, do the following:

1. Select the Perspective that you want to edit, and click **Edit**.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1639486323140/screenshot-2021-12-14-at-2-45-50-pm.png)
2. The **Perspective Builder** appears. Follow the steps in [Create Cost Perspectives](create-cost-perspectives.md) to edit the Perspective.

### Clone a Perspective

When you clone a Perspective, all its settings are cloned. You simply add a new name. Once it is cloned, you can edit it just as you would any Perspective. To clone a Perspective, do the following:

1. Select the Perspective that you want to clone, and click **Clone**.![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1639486244720/screenshot-2021-12-14-at-2-45-50-pm.png)
2. The cloned Perspective appears.

### Delete a Perspective

To delete a Perspective, do the following:

1. Select the Perspective that you want to delete, and click **Delete**.  
  
The Perspective is deleted and no longer appears in the Perspective dashboard.

### Organize Perspectives using Folders

You can organize Perspectives by adding them to folders.

Click **New folder**, name the folder, and then select the Perspectives you want to add.

![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1655760357029/clean-shot-2022-06-20-at-14-25-04.png)You can also add a Perspective to a folder when you create it or move it to a folder when you edit it.

![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1655760406777/clean-shot-2022-06-20-at-14-26-15.png)You can also move a Perspective to a folder from its more options (⋮) setting.

![](https://files.helpdocs.io/i5nl071jo5/articles/dvspc6ub0v/1655760552855/clean-shot-2022-06-20-at-14-28-25.png)### Next Steps

* [Create a Budget for Your Perspective](create-a-budget-perspective.md)
* [Share Your Cost Perspective Report](share-cost-perspective-report.md)
* [Analyze Cost for Kubernetes Using Perspectives](../root-cost-analysis/analyze-cost-for-k8s-ecs-using-perspectives.md)
* [Analyze Cost for AWS Using Perspectives](../root-cost-analysis/analyze-cost-for-aws.md)
* [Analyze Cost for GCP ​Using Perspectives](../root-cost-analysis/analyze-cost-for-gcp-using-perspectives.md)
* [Analyze Cost for Azure Using Perspectives](../root-cost-analysis/analyze-cost-for-azure.md)

