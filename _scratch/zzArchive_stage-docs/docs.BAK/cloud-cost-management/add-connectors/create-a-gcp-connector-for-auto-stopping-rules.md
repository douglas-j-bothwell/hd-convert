---
title: Create a GCP Connector for AutoStopping Rules
description: This topic describes how to add a GCP connector for creating AutoStopping Rules.
tags: 
   - helpDocs
   - GCP connector
   - gcp
   - Autostopping rules
helpdocs_topic_id: cfojlhnf8s
helpdocs_is_private: true
helpdocs_is_published: true
---

Currently, this feature is in Beta and behind Feature Flag. Contact [Harness Support](mailto:support@harness.io) to enable the feature.  
Connectors allow Harness to connect to your deployment environments, such as Kubernetes Clusters, AWS, Google Cloud Platform, Azure, etc. To create an AutoStopping Rule for your GCP instances, you first need to connect Harness to your GCP account.

This topic describes how to connect your GCP cloud account to Harness.

In this topic:

* [Before You Begin](create-a-gcp-connector-for-auto-stopping-rules.md)
* [Add a GCP Connector](create-a-gcp-connector-for-auto-stopping-rules.md)
* [Step 1: Overview](create-a-gcp-connector-for-auto-stopping-rules.md)
* [Step 2: GCP Billing Export](create-a-gcp-connector-for-auto-stopping-rules.md)
* [Step 3: Grant Permissions](create-a-gcp-connector-for-auto-stopping-rules.md)
* [Step 4: Test Connection](create-a-gcp-connector-for-auto-stopping-rules.md)
* [Next Steps](create-a-gcp-connector-for-auto-stopping-rules.md)

### Before You Begin

* [AutoStopping Rules Overview](auto-stopping-rules.md)

### Add a GCP Connector

Perform the following steps to add a GCP connector for AutoStopping Rules:

1. In **Cloud Costs**, click **New AutoStopping Rule**.[![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)
2. In **AutoStopping Rules**, select **GCP**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping Rules.![](https://files.helpdocs.io/i5nl071jo5/articles/cfojlhnf8s/1634627802704/screenshot-2021-10-19-at-12-46-27-pm.png)
3. Click **Connect to your GCP account** drop-down list and then click **New Connector**.

### Step 1: Overview

1. In **Overview**, in **Connector Name**, enter a name that describes this account.
2. In **Specify Project ID**, enter the project ID and click **Continue**. For more information on how to get a project ID, see [Create a BigQuery dataset](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset).![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1625854255149/screenshot-2021-07-09-at-11-39-30-pm.png)

### Step 2: GCP Billing Export

Cloud Billing export to BigQuery enables you to export detailed Google Cloud billing data (such as usage and cost estimate data) automatically throughout the day to a BigQuery dataset that you specify.

1. In **GCP Billing Export**, click **Launch GCP console**.
2. In the GCP **Explorer** window, in the pinned projects section, click **your project ID** to open the project. If you see an overflow menu (:) next to your project ID, click the menu and select **Open**.
3. Click **Create dataset**. For more information, see [Create a BigQuery dataset](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset).![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626001265234/screenshot-2021-07-11-at-4-30-50-pm.png)
4. Enter a **Dataset ID**.  
You need to enter Dataset ID in Harness.
5. Select a **Data location**.
6. Set the **Default table expiration** to **Never**.
7. Set the **Encryption** option to **Google-managed key**.
8. To save, click **CREATE DATASET**.
9. Enter the **Dataset ID** in Harness and click **Continue**. When you are done it will look something like this:![](https://files.helpdocs.io/i5nl071jo5/articles/kxnsritjls/1626006563019/screenshot-2021-07-11-at-5-59-08-pm.png)

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

### Next Steps

* [Create AutoStopping Rules for GCP](create-auto-stopping-rules/create-auto-stopping-rules-for-gcp.md)

