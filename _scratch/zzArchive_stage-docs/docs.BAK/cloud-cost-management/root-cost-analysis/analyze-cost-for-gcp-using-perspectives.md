---
title: Analyze Cost for GCP ​Using Perspectives
description: This topic describes how to analyze costs for GCP using Perspectives.
tags: 
   - helpDocs
   - perspectives
   - gcp
helpdocs_topic_id: ryhe4aut1y
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Cloud Cost Management (CCM) allows you to view your Google Cloud Platform (GCP) costs, understand what is costing the most, and analyze cost trends. CE displays data for all your GCP products (such as Compute Engine, Cloud Storage, BigQuery, and so on), projects, SKUs, location, and labels and also provides details on:

* GCP cloud cost spending trends
* The GCP products costing the most in a selected time range. For example, how much Compute Engine cost last week
* Primary cost contributors, such as product, project, SKUs, or region
* GCP spendings by region, such as us-west1 or us-east4![](https://files.helpdocs.io/i5nl071jo5/articles/ryhe4aut1y/1628002773158/screenshot-2021-08-03-at-8-29-10-pm.png)

Time periods in the GCP Cloud Billing report use the Pacific Time Zone (PST) and observe daylight saving time shifts. However, Harness CCM explorer uses the UTC time zone. You may notice some cloud cost differences between Harness CCM explorer and the GCP Cloud Billing report due to the time zone difference.### Before You Begin

* [Set Up Cloud Cost Management for GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md)

### Step: Analyze GCP Cost

The Perspectives provides deep insights into your GCP costs. The cost includes all the applicable credits and discounts.

1. In **Cloud Costs**, click **Perspectives**,and then click **GCP**. The GCP products are displayed.![](https://files.helpdocs.io/i5nl071jo5/articles/ryhe4aut1y/1628002870176/screenshot-2021-08-03-at-8-30-51-pm.png)
2. Select the **date range** for the costs you want to analyze.![](https://files.helpdocs.io/i5nl071jo5/articles/ryhe4aut1y/1628003030686/screenshot-2021-08-03-at-8-33-30-pm.png)
3. You can use the following options to Group By:
	* **GCP**: Under AWS, you can Group by:
		+ **Products**: Each of your active products with their cloud costs is displayed.
		+ **Projects**: Each of your Cloud projects with their cloud costs is displayed.
		+ **SKUs**: Each [SKU](https://cloud.google.com/skus) you are using.
	* **Region**: Each GCP region you are currently running services in.
	* **Product**: Each of your active products with its cloud costs.
	* **Label**: Each [label](https://cloud.google.com/resource-manager/docs/creating-managing-labels) that you are using to organize your Google Cloud instances.

### Option: Add Filter

Perform the following steps to add filters.

1. In **Cloud Costs**, click **Perspectives**,and then click **GCP**.
2. Click **add filter**.![](https://files.helpdocs.io/i5nl071jo5/articles/ryhe4aut1y/1628003311712/screenshot-2021-08-03-at-8-36-28-pm.png)
3. Select GCP, Region, Product, or Label.
4. Select the operator. The supported operators are:
	* **IN: The exact match operation is used to filter for the value specified.**
	* **NOT IN: The exact match operation is used to filter for the value that is not specified.**
5. Select value for your filter. You can select multiple values. You can also filter and customize your result using the search option.![](https://files.helpdocs.io/i5nl071jo5/articles/ryhe4aut1y/1628003383249/screenshot-2021-08-03-at-8-39-19-pm.png)

### Next Steps

* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

