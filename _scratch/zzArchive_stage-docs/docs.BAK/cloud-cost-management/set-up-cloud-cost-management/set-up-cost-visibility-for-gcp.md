---
title: Set Up Cloud Cost Management for GCP
description: This topic describes how to set up cost visibility for GCP.
tags: 
   - helpDocs
   - cloud cost management
   - gcp
   - cloud cost
helpdocs_topic_id: kxnsritjls
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Cloud Cost Management (CCM) monitors the cloud costs of your GCP products, projects, SKUs, and location. As a first step, you connect Harness to your GCP account to get insights into your cloud infrastructure and GCP services, Compute Engine Cloud Storage, BigQuery, etc. CCM displays the data for your connected GCP services for further analysis.

After enabling CCM, it takes about 24 hours for the data to be available for viewing and analysis.In this topic:

* [Before You Begin](set-up-cost-visibility-for-gcp.md)
* [Connect Harness to Google Cloud Platform (GCP) Account](set-up-cost-visibility-for-gcp.md)
* [Step 1: Overview](set-up-cost-visibility-for-gcp.md)
* [Step 2: GCP Billing Export](set-up-cost-visibility-for-gcp.md)
* [Step 3: Grant Permissions](set-up-cost-visibility-for-gcp.md)
* [Step 4: Test Connection](set-up-cost-visibility-for-gcp.md)
* [Next Steps](set-up-cost-visibility-for-gcp.md)

### Before You Begin

* The same connector cannot be used in NextGen and FirstGen. For information on creating a GCP connector in the FirstGen see [Set Up Cost Visibility for GCP](https://docs.harness.io/article/x53e2by67m-enable-cloud-efficiency-for-google-cloud-platform-gcp).
* Review [Required permissions and roles](https://cloud.google.com/iam/docs/understanding-custom-roles#required_permissions_and_roles) to create an IAM role at the organization level
* Ensure that you have the following permissions to enable and configure the export of Google Cloud billing data to a BigQuery dataset:
	+ **Billing Account Administrator** role for the target Cloud Billing account
	+ [BigQuery User role for the Cloud project](https://cloud.google.com/bigquery/docs/dataset-access-controls) that contains the BigQuery dataset that will be used to store the Cloud Billing data

### Connect Harness to Google Cloud Platform (GCP) Account

Connect Harness to your GCP account to get insights into your cloud infrastructure and GCP services, Compute Engine Cloud Storage, BigQuery, etc. This will give you cost insights that are derived from the billing export. For deep Kubernetes visibility and rightsizing recommendations based on the historical utilization and usage metrics, set up Kubernetes connectors. See [Set Up Cloud Cost Management for Kubernetes](set-up-cost-visibility-for-kubernetes.md).

Time periods in the GCP Cloud Billing report use the Pacific Time Zone (PST) and observe daylight saving time shifts. However, Harness CCM explorer uses the UTC time zone. You may notice some cloud cost differences between Harness CCM explorer and the GCP Cloud Billing report due to the time zone difference.### Step 1: Overview

1. In **Account Setup**, in **Account Resources**, click **Connectors**.![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1630563180229/screenshot-2021-09-02-at-11-22-27-am.png)
2. In **Connectors**, click **+ Connector**.
3. In **Cloud Costs**, click **GCP**.![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626110343551/screenshot-2021-07-12-at-10-42-20-pm.png)
4. In **Overview**, in **Connector Name**, enter a name that describes this account.
5. In **Specify Project ID**, enter the project ID and click **Continue**. For more information on how to get a project ID, see [Create a BigQuery dataset](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset).![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1625854255149/screenshot-2021-07-09-at-11-39-30-pm.png)

### Step 2: GCP Billing Export

Cloud Billing export to BigQuery enables you to export detailed Google Cloud billing data (such as usage and cost estimate data) automatically throughout the day to a BigQuery dataset that you specify.

1. In **GCP Billing Export**, click **Launch GCP console**.
2. In the GCP **Explorer** window, in the pinned projects section, click **your project ID** to open the project. If you see an overflow menu (:) next to your project ID, click the menu and select **Open**.
3. Click **Create dataset**. For more information, see [Create a BigQuery dataset](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset).![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626001265234/screenshot-2021-07-11-at-4-30-50-pm.png)
4. Enter a **Dataset Name**.  
You need to enter Dataset Name in Harness.
5. Select a **Data location**.
6. Set the **Default table expiration** to **Never**.
7. Set the **Encryption** option to **Google-managed key**.
8. To save, click **CREATE DATASET**.
9. Enter the **Dataset Name** in Harness.![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1643738388698/screenshot-2022-02-01-at-11-29-32-pm.png)
10. Next, you need to enter the table name in Harness. From the GCP console, copy the table name where the billing export is available. In your BigQuery dataset, the table is named `gcp_billing_export_v1_<BILLING_ACCOUNT_ID>`.![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1642004505075/screenshot-2022-01-12-at-9-51-30-pm.png)Enter the **Table Name** in Harness.
11. Click **Continue**. When you are done it will look something like this:![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1642004600001/screenshot-2022-01-12-at-9-52-53-pm.png)

### Step 3: Grant Permissions

Cloud Billing Export to BigQuery helps you export detailed Google Cloud billing data (such as usage and cost estimate data) to a BigQuery dataset that you specify. The export happens throughout the day automatically. 

1. In **Grant permissions**, click **Open BigQuery Page**.
2. Log into the GCP console and go to the BigQuery page.
3. Select your project in the left panel.
4. Select your dataset. For more information on creating a dataset, see [Creating datasets](https://cloud.google.com/bigquery/docs/datasets).[![](https://files.helpdocs.io/kw8ldg1itf/articles/x53e2by67m/1595605703660/screenshot-2020-07-23-at-8-54-29-pm.png)](https://files.helpdocs.io/kw8ldg1itf/articles/x53e2by67m/1595605703660/screenshot-2020-07-23-at-8-54-29-pm.png)
5. Click **SHARE DATASET**.
6. In **Dataset permissions**, in **Add members**, enter the Harness service account as a member.  
  
Copy the service account detail from Harness. The service account is generated dynamically for your account.
7. In **Select a** **role**, select **BigQuery Data Viewer**, and then click **Add**.
8. Click **Done**.  
  
When you are done, it will look something like this:[![](https://files.helpdocs.io/kw8ldg1itf/articles/x53e2by67m/1595606637082/screenshot-2020-07-24-at-9-21-45-pm.png)](https://files.helpdocs.io/kw8ldg1itf/articles/x53e2by67m/1595606637082/screenshot-2020-07-24-at-9-21-45-pm.png)
9. Click **Continue** in Harness.![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626112117371/screenshot-2021-07-12-at-11-11-38-pm.png)

### Step 4: Test Connection

The validation and verification happen in this step. Once the validation and verification are completed, click **Finish**.

![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626111830795/screenshot-2021-07-12-at-11-13-37-pm.png)Your connector is now listed in the **Connectors**.

![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626111908041/screenshot-2021-07-12-at-11-14-32-pm.png)### Next Steps

* [Analyze Cost for GCP ​Using Perspectives](../root-cost-analysis/analyze-cost-for-gcp-using-perspectives.md)
* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

