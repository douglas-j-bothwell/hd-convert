---
title: Analyze Cost for AWS Using Perspectives
description: This topic describes how to analyze costs for AWS using Perspectives.
tags: 
   - helpDocs
   - perspectives
   - AWS
helpdocs_topic_id: 1nf0qcz4o0
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Cloud Cost Management (CCM) allows you to view your AWS costs at a glance, understand what is costing the most, and analyze cost trends. CCM Perspectives displays the data for all your Amazon Web Services (ECS, EC2, and so on) and also helps you get details of:

* AWS cloud cost spending trend
* AWS service costing the most in the selected time range, for example, EC2 spent last month
* Primary cost contributor, for example, region, account, instance type, or usage type
* AWS spending by region, for example, US East or US West

![](https://files.helpdocs.io/i5nl071jo5/articles/1nf0qcz4o0/1628001917245/screenshot-2021-08-03-at-8-14-46-pm.png)### Before You Begin

* [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)

### Step: Analyze AWS Cost

The Perspectives provides deep insights into your AWS costs. The cost includes all the applicable credits and discounts.

1. In **Cloud Costs**, click **Perspectives**,and then click **AWS**. The AWS services are displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/1nf0qcz4o0/1627976784816/screenshot-2021-08-03-at-12-54-49-pm.png)
2. Select the **date range** for the costs you want to analyze.![](https://files.helpdocs.io/i5nl071jo5/articles/1nf0qcz4o0/1628002093381/screenshot-2021-08-03-at-8-17-59-pm.png)
3. You can use the following options to Group By:
	* **AWS**: Under AWS, you can Group by:
		+ **Service**: Each of your active [AWS services](https://aws.amazon.com/) is displayed.
		+ **Account**: Each AWS account you are using to connect Harness to AWS via a Harness AWS Cloud Provider. This displays the Account Name along with the Account ID (if the Account Name is available, else only the Account ID is displayed).  
		![](https://files.helpdocs.io/i5nl071jo5/articles/1nf0qcz4o0/1651761463647/screenshot-2022-05-05-at-8-07-26-pm.png)
		+ **I****nstance Type**: Each [Amazon EC2 instance type](https://aws.amazon.com/ec2/instance-types/) you are using.
		+ **Usage Type**: Usage types are the units that each service uses to measure the usage of a specific type of resource. For example, the BoxUsage:t2.micro(Hrs) usage type filters by the running hours of Amazon EC2 t2.micro instances.
	* **Region**: Each AWS region you are currently running services in.
	* **Product**: Each of your active products with its cloud costs.
	* **Label**: Each label that you assign to your AWS resources. You can select a label name to get further granular details of your label.
	* **Tags**: Each [tag](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) that you assign to your AWS resources. You can select a **Tag name** to get further granular details of your tags.For tags to appear in the Perspective, you must activate the user-defined cost allocation tags in the AWS Billing and Cost Management console. For more information, see [Activating User-Defined Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html).In CCM, the tag keys are updated as the following:
		+ For the user-defined tags, `user_` prefix is added.
		+ For the AWS system tags, `aws_` prefix is added.
		+ The characters that do not follow regex `[a-zA-Z0-9_]` are changed to `_`.
		+ The tags are case-sensitive. If the tags are specified as `UserName` and `username`, then the number suffix `_<Number>`is added to the tag. For example, `UserName` and `username_1`.

### Option: Add Filter

Perform the following steps to add filters.

1. In **Cloud Costs**, click **Perspectives**,and then click **AWS**.
2. Click **add filter**.![](https://files.helpdocs.io/i5nl071jo5/articles/1nf0qcz4o0/1628002479897/screenshot-2021-08-03-at-8-24-24-pm.png)
3. Select AWS, Region, Product, or Label.
4. Select the operator. The supported operators are:
	* **IN: The exact match operation is used to filter for the value specified.**
	* **NOT IN: The exact match operation is used to filter for the value that is not specified.**
5. Select value for your filter. You can select multiple values. You can also filter and customize your result using the search option.![](https://files.helpdocs.io/i5nl071jo5/articles/1nf0qcz4o0/1628002564030/screenshot-2021-08-03-at-8-25-48-pm.png)

### Next Steps

* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

