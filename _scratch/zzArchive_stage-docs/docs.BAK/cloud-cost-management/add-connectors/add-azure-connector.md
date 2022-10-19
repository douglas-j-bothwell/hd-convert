---
title: Create an Azure Connector for AutoStopping Rules
description: Connectors allow Harness to connect to your deployment environments, such as Kubernetes Clusters, AWS, Google Cloud Platform, Azure, etc. To create an AutoStopping Rule for your Azure instances, you…
tags: 
   - helpDocs
helpdocs_topic_id: e7yidxmtmj
helpdocs_is_private: false
helpdocs_is_published: true
---

Connectors allow Harness to connect to your deployment environments, such as Kubernetes Clusters, AWS, Google Cloud Platform, Azure, etc. To create an AutoStopping Rule for your Azure instances, you first need to connect Harness to your Azure account. This topic describes how to connect your Azure cloud account to Harness.

In this topic:

* [Before You Begin](add-azure-connector.md)
* [Prerequisites](add-azure-connector.md)
* [Add Your Azure Cloud Account](add-azure-connector.md)
* [Step 1: Connector Overview](add-azure-connector.md)
* [Step 2: Azure Billing Exports](add-azure-connector.md)
* [Step 3: Select Features](add-azure-connector.md)
* [Step 4: Create Service Principal and Assign Permissions](add-azure-connector.md)
* [Step 5: Test Connection](add-azure-connector.md)
* [Next Steps](add-azure-connector.md)

### Before You Begin

* [AutoStopping Rules Overview](auto-stopping-rules.md)

### Prerequisites

* Make sure that you have the **Application Administrator** role assigned for your Azure AD. Users in this role can create and manage all aspects of enterprise applications, application registrations, and application proxy settings. See [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#application-administrator).
* Many Azure CLI commands act within a subscription. Ensure that you have selected the right subscription before executing the commands. If you need to switch the subscription, use the following command:  
`az account set -s <`*`subs id/name`*`>`  
For more information, see [Manage Subscriptions](https://docs.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli).

### Add Your Azure Cloud Account

Perform the following steps to link your Azure cloud account to Harness.

1. In **Cloud Costs**, click **New AutoStopping Rule**.![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)
2. In **AutoStopping Rules**, select **Azure**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping rules.  
![](https://files.helpdocs.io/i5nl071jo5/articles/e7yidxmtmj/1633514921522/screenshot-2021-10-06-at-3-38-05-pm.png)
3. Click **Connect to your Azure account** drop-down list and then click **New Connector**.

### Step 1: Connector Overview

1. In **Azure Connector**, in **Overview**, enter a name for the Azure Connector.
2. In **Specify Azure Tenant ID**, enter the Tenant ID of your Azure AD account. A tenant represents an organization. It's a dedicated instance of Azure AD that an organization or app developer receives at the beginning of a relationship with Microsoft.  
  
Each Azure AD tenant is distinct and separate from other Azure AD tenants.  
  
To find your tenant ID, do the following:  

	1. Launch Azure Active Directory.
	2. Copy the tenant ID from the **Tenant information**.![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614751699244/screenshot-2021-03-03-at-11-38-01-am.png)If you don't find the tenant ID in the Azure console, run the `az account show` command using Azure CLI.
3. In **Specify Azure Subscription ID**, enter the **Azure Subscription ID** and click **Continue**. To find your Subscription ID, do the following:
	1. Launch Azure Active Directory.
	2. In **Product + services**, click **Azure subscriptions**.
	3. Copy the **Subscription ID** for your subscription.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626018851340/screenshot-2021-07-11-at-9-21-20-pm.png)If you don't find the Subscription ID in the Azure console, you can use Azure CLI. See [List your Azure subscriptions with CLI](https://docs.microsoft.com/en-us/azure/media-services/latest/setup-azure-subscription-how-to?tabs=cli).
4. Click **Continue**.

### Step 2: Azure Billing Exports

Billing export is used to get insights into your cloud infrastructure and Azure services such as Storage account, Virtual machines, Containers, etc.

You need to enter the following details in Harness:

* Storage Account Name
* Storage Container
* Storage Directory
* Report Name

To fetch these details, perform the following steps:

1. In **Azure Billing Exports**, click **Launch Azure Billing Exports**.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626069021464/screenshot-2021-07-12-at-11-20-06-am.png)

1. In the Azure Cost Management portal, in **Settings**, in **Exports**, click **Add** to create a new export.
2. In **Export details**, provide the following details:
	1. Enter **Name** for your export.
	2. In **Export type**, select **Daily export of month-to-date costs**.
	3. In the **Start date**, leave the date as the current date.  
	  
	For example, if you are creating a new export on March 1, 2021, select the date as **Mon Mar 01 2021**.
3. In the **Storage**, you can select **Use existing** or **Create new**.
	1. If you select **Use existing**, enter the following details:
		1. In **Subscription**, select the **Subscription** of your storage account.
		2. In the **Storage account**, select the storage account where the data needs to be exported.
		3. In **Container**, enter the container name where the report is to be stored.
		4. In **Directory**, enter the directory path where the export is to be stored.![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614752219755/screenshot-2021-03-03-at-11-46-42-am.png)
	2. If you select **Create new**, enter the following details:
		1. In **Subscription**, select the **Subscription** of your storage account.
		2. In the **Resource group**, select the group to place the storage account. You can also create a new resource group.  
		  
		A resource group is a container that holds related resources for an Azure solution.
		3. In **Account name**, enter the name for your storage account.
		4. In **Location**, select the region for your storage account.
		5. In **Container**, enter the container name where the report is to be stored.
		6. In **Directory**, enter the directory path where the export is to be stored.![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614664583414/screenshot-2021-03-02-at-11-21-47-am.png)
4. Once you are done, click **Create**.  
  
Your export report is listed in the **Exports** list.![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614753836168/screenshot-2021-03-03-at-12-13-32-pm.png)
5. Click the export that you created in the previous step and click **Run now**.![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1616754471022/screenshot-2021-03-26-at-3-55-57-pm.png)
6. In the Azure Cost Management portal, click the billing export that you created in the [enable export billing step](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md).![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614753782707/screenshot-2021-03-03-at-12-12-44-pm.png)
7. Enter the following details in Harness:
	1. In the **Storage account name**, enter the account name.
	2. In **Storage Container**, enter the container name.
	3. In **Storage Directory**, enter the directory name.
	4. In **Report Name**, enter the report name.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626070931659/screenshot-2021-07-12-at-11-51-46-am.png)
8. Click **Continue**.

### Step 3: Select Features

1. Select **Cost Visibility** and **Azure resource optimization using AutoStopping rules** in **Create Cross Account Role**.  
![](https://files.helpdocs.io/i5nl071jo5/articles/e7yidxmtmj/1633515334115/screenshot-2021-10-06-at-3-44-38-pm.png)  
CCM offers the following features:  


|  |  |
| --- | --- |
| **Cost Visibility** | This feature is available by default and requires access to the access billing export. Provides the following capabilities:
	* Insights into Azure costs by services, accounts, etc.
	* Root cost analysis using cost perspectives
	* Cost anomaly detection
	* Governance using budgets and forecasts
	* Alert users using Email and Slack notification |
| **Azure resource optimization using AutoStopping rules** | This feature allows you to enable intelligent cloud AutoStopping for your Azure instances. For more information, see [Create AutoStopping Rules for Azure](create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md).
	* Orchestrate VMs based on idleness
	* Provide granular savings visibility |
2. Make your selection and click **Continue**.

### Step 4: Create Service Principal and Assign Permissions

Harness uses a multi-tenant app to sync billing export data from the source storage account to Harness and to perform cost optimization functions. This involves the following steps:

* Register the Harness CCM application into your Azure account.
* Provide read permissions to the storage account in which the billing data export is available and/or contributor role on the subscription where the optimization feature is to be performed.

Create service principal and assign permissions by running the following commands in the bash terminal or in the Azure cloud shell.

#### Step 1: Register the Harness Application

Run the following **bash** commands using your **bash** terminal or Azure cloud shell:

1. `az ad sp create --id <>`  
  
**Required Parameter**  
`--id`  
This is a common ID for Harness CCM client application. Use `10034206-24bf-442b-968c-70a9c896a2f6`If you see the following error proceed with [Step 2: Assign Permissions to the Storage Account](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md).  
  
`Another object with the same value for property servicePrincipalNames already exists.`  
  
The error means that your Harness CCM application is already registered into your Azure account.#### Step 2: Assign Permissions to the Storage Account

Run the following **bash** commands using your **bash** terminal or Azure cloud shell:
2. `SCOPE=`az storage account show --name <storage account name> --query "id" | xargs``: Provides scope for your storage account. Each role assignment in Azure needs a scope on which the permissions or role is applied. The output of this command is used in the next step.  
  
**Required Parameter**  
`--name`  
The name of your storage account.  
  
Here's a screenshot with the Storage account name for your reference.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626083213255/screenshot-2021-07-12-at-3-16-08-pm.png)**Response**  

```
$ SCOPE=`az storage account show --name test --query "id" | xargs`  
  
$ echo $SCOPE  
/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/<resourcegroupname>/providers/Microsoft.Storage/storageAccounts/<storage account name>
```
3. `az role assignment create --assignee 10034206-24bf-442b-968c-70a9c896a2f6 --role 'Storage Blob Data Reader' --scope $SCOPE`: Provides Storage Blob Data Reader permission to the Harness application on the scope fetched in the previous step.  
  
**Required Parameter**  
`--assignee`  
  
This is the ID of the Harness CCM client application. Use `10034206-24bf-442b-968c-70a9c896a2f6`
4. Run the following command:  

```
az role assignment create --assignee 10034206-24bf-442b-968c-70a9c896a2f6 --role 'Contributor' --scope /subscriptions/123e4567-e89b-12d3-a456-9AC7CBDCEE52
```
5. Once you are done, click **Continue** in Harness.

### Step 5: Test Connection

The validation and verification happen in this step. Once the validation and verification are completed, click **Finish**.

### Next Steps

* [Create AutoStopping Rules for Azure](create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md)
* [Use AutoStopping Rules Dashboard](create-auto-stopping-rules/autostopping-dashboard.md)

