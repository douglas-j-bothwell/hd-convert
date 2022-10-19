---
title: Use Cost Categories
description: CCM Cost Categories let you view costs according to meaningful categories, such as departments and teams. You can then use Cost Categories in Perspectives to filter across accounts, products, etc. In…
tags: 
   - helpDocs
helpdocs_topic_id: 6lle2diqeg
helpdocs_is_private: false
helpdocs_is_published: true
---

CCM Cost Categories let you view costs according to meaningful categories, such as departments and teams. You can then use Cost Categories in Perspectives to filter across accounts, products, etc.

Instead of viewing costs based purely on different data sources, Cost Categories free you to view spending across data sources according to different business contexts.

### Prerequisites and Permissions

To use Cost Categories, your Harness User account must belong to a User Group with the following Role permissions:

* **Cloud Cost Management**: **Cost Categories**: **Create/Edit**

For more details, go to [CCM Roles and Permissions](../ccm-ref/ccm-roles-and-permissions.md).

### Visual Summary

How to create a Cost Category:

How to use a Cost Category:

### Cost Categories Summary

Cost Categories let you take data across multiple sources and attribute it to business contexts, like Departments, Teams, and spend categories.

For example, if your business is organized by teams with multiple accounts, you can create a Cost Category named Teams and map costs to each team from all your accounts.

Your Teams cost category shows you what each team is spending across AWS, GCP, Clusters, etc.

A Cost Category is composed of one or more buckets. A bucket is one or more filters that collect data sources.

For example, a Departments Cost Category would have separate buckets for each department. Each bucket collects the data sources that belong to each department.

Once you have Cost Categories, you can use them in Perspective filters and Group By.

You can even use Cost Categories to define Perspectives. The Cost Categories used in Perspectives are updated separately from the Perspectives. This allows you to update a single Cost Category and have the result automatically reflected in all the Perspectives that use that Cost Category. 

### Creating Cost Categories

You can create a Cost Category 

1. In your Harness account, click **Cloud Costs**, click **Setup**, and then click **Cost Categories**.
2. Click **New Cost Category**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660601654669/image.png)You can also create a new Cost Category when you create a Perspective.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660601751071/image.png)The new Cost Category appears.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660601946083/image.png)1. In the new Cost Category, enter a name. For example, if this Cost Category is for departments, name it **Departments**.

#### Cost Buckets

1. Click **New Cost Bucket**.
2. Enter a name for the cost bucket, such as the name of a department.
3. Define the data sources for the Cost Category.
4. Add a new row for each data source until the Cost Category correctly includes all of the costs for this Cost Category.

Typically, you want to create multiple cost buckets in the Cost Category. For example, if the Cost Category is for Departments, you would create a cost bucket for each department. 

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660603191200/image.png)##### AND and OR

The AND and OR operators are used to filter data based on more than one condition:

* AND: use AND to filter data sources that include both criteria.
* OR: use OR to filter data source that include one of the criteria.

You can use AND and OR together.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660602731116/image.png)#### Manage Unallocated Costs

When used in a Perspective as a filter or **Group By**, the Cost Category shows data that matches its filters. 

Unallocated Costs are costs that do not match the Cost Categories in the Perspective graph and rows.

In **Manage Unallocated Costs**, you can choose to show or ignore unallocated costs, and choose a name for how those costs are displayed.

### Using Cost Categories

Cost Categories can be used in Perspectives in the following ways.

#### Group By

Select a Cost Category in **Group By**:

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660603345738/image.png)#### Filter

Select one of more Cost Categories as a filter.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660603414002/image.png)You can use Group By and filters together. For example, your filter could select **Manufacturing** from the Department Cost Category, and then you can select **GCP: SKUs** in **Group By**.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660603664673/image.png)#### Perspectives

When creating a Perspective, you can define a rule using Cost Categories.

![](https://files.helpdocs.io/kw8ldg1itf/articles/6lle2diqeg/1660603793646/image.png)The benefit of using a Cost Category as a rule in a Perspective is that the Cost Category definition is separated from all the Perspectives that use it.

When you change the definition of the Cost Category, it automatically changes what is displayed by all the Perspectives that use that Cost Category.

For example, if a new product is added to the Manufacturing department, you can simply update the Manufacturing bucket in the Departments Cost Category, and that change is automatically reflected in all the Perspectives that use that Cost Category.

### See Also

* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

