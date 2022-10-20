---
title: Set Up Cloud Cost Management for Azure
description: This topic describes how to set up cost visibility for Azure.
tags: 
   - helpDocs
   - azure
   - cloud cost management
   - cloud cost
helpdocs_topic_id: v682mz6qfd
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Cloud Cost Management (CCM) monitors the cloud costs of your Azure services. Connect your Azure account and set up Billing Export to get insights into your cloud infrastructure and Azure services such as Storage accounts, Virtual machines, Containers, and so on. CCM also allows you to optimize your instances and AKS clusters using intelligent cloud [AutoStopping rules](../add-connectors/auto-stopping-rules.md).

You can set up CCM for your Azure resources, in a simple two-step process:

1. [Provide access to the Azure billing export](set-up-cost-visibility-for-azure.md).
2. [Create service principal and assign permissions](set-up-cost-visibility-for-azure.md). The permissions are assigned based on the CCM features that you want to enable for your Azure account. CCM offers the following features:  
  


|  |  |
| --- | --- |
| **Cost Visibility (Required)** | This feature is available by default and requires access to the billing export. Provides the following capabilities:
	* Insights into Azure costs by services, accounts, etc.
	* Root cost analysis using cost perspectives
	* Cost anomaly detection
	* Governance using budgets and forecasts
	* Alert users using Email and Slack notificationThis feature will give you cost insights that are derived from the billing export. For deep Kubernetes visibility and rightsizing recommendations based on the historical utilization and usage metrics, set up Kubernetes connectors. See [Set Up Cloud Cost Management for Kubernetes](set-up-cost-visibility-for-kubernetes.md). |
| **Azure resource optimization using AutoStopping rules (Optional)** | This feature allows you to enable intelligent cloud AutoStopping for your Azure instances. For more information, see [Create AutoStopping Rules for Azure](../add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md).
	* Orchestrate VMs based on idleness
	* Provide granular savings visibility |

After enabling CCM, it takes about 24 hours for the data to be available for viewing and analysis.In this topic:

* [Before You Begin](set-up-cost-visibility-for-azure.md)
* [Review: Azure Connector Requirements](set-up-cost-visibility-for-azure.md)
* [Connect CCM to Your Azure Account](set-up-cost-visibility-for-azure.md)
* [Step 1: Overview](set-up-cost-visibility-for-azure.md)
* [Step 2: Azure Billing Exports](set-up-cost-visibility-for-azure.md)
* [Step 3: Select Features](set-up-cost-visibility-for-azure.md)
* [Step 4: Create Service Principal and Assign Permissions](set-up-cost-visibility-for-azure.md)
* [Step 5: Test Connection](set-up-cost-visibility-for-azure.md)
* [Troubleshooting](set-up-cost-visibility-for-azure.md)
* [Next Steps](set-up-cost-visibility-for-azure.md)

### Before You Begin

* [Review: Azure Connector Requirements](set-up-cost-visibility-for-azure.md)
* Review [prerequisites](set-up-cost-visibility-for-azure.md) for creating Service Principal and assigning permissions

### Review: Azure Connector Requirements

* The same connector cannot be used in NextGen and FirstGen. For information on creating an Azure connector in the FirstGen see [Set Up Cost Visibility for Azure](https://docs.harness.io/article/7idbmchsim-set-up-cost-visibility-for-azure).
* For CCM, Azure connectors are available only at the Account level in Harness.
* You can create multiple Azure connectors for each Harness Account.
* You can create multiple Azure connectors per Azure Tenant with unique subscription IDs.
* If you have separate billing exports for each of your subscriptions in your Azure account, set up separate connectors in Harness to view the cloud cost of all the subscriptions in CCM.

### Prerequisites

* Make sure that you have the **Application Administrator** role assigned for your Azure AD. Users in this role can create and manage all aspects of enterprise applications, application registrations, and application proxy settings. See [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#application-administrator).
* Many Azure CLI commands act within a subscription. Ensure that you have selected the right subscription before executing the commands. If you need to switch the subscription, use the following command:  
`az account set -s <`*`subs id/name`*`>`  
  
For more information, see [Manage Subscriptions](https://docs.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli).

### Connect CCM to Your Azure Account

To enable CCM for your Azure services (such as Storage accounts, Virtual machines, Containers, and so on), you simply need to connect Harness to your Azure account.

Perform the following steps to connect to your Azure account:

### Step 1: Overview

1. In **Account Setup**, in **Account Resources**, click **Connectors**.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1630563084139/screenshot-2021-09-02-at-11-22-27-am.png)
2. In **Connectors**, click **+ Connector**.
3. In **Cloud Costs**, click **Azure**.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626011530252/screenshot-2021-07-11-at-7-21-49-pm.png)
4. In **Azure Connector**, in **Overview**, enter a name for the Azure Connector.
5. In **Specify Azure Tenant ID**, enter the Tenant ID of your Azure AD account. A tenant represents an organization. It's a dedicated instance of Azure AD that an organization or app developer receives at the beginning of a relationship with Microsoft.  
  
Each Azure AD tenant is distinct and separate from other Azure AD tenants.  
  
To find your tenant ID, do the following:  

	1. Launch Azure Active Directory.
	2. Copy the tenant ID from the **Tenant information**.![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614751699244/screenshot-2021-03-03-at-11-38-01-am.png)If you don't find the tenant ID in the Azure console, run the `az account show` command using Azure CLI.
6. In **Specify Azure Subscription ID**, enter the **Azure Subscription ID** and click **Continue**. To find your Subscription ID, do the following:
	1. Launch Azure Active Directory.
	2. In **Product + services**, click **Azure subscriptions**.
	3. Copy the **Subscription ID** for your subscription.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626018851340/screenshot-2021-07-11-at-9-21-20-pm.png)If you don't find the Subscription ID in the Azure console, you can use Azure CLI. See [List your Azure subscriptions with CLI](https://docs.microsoft.com/en-us/azure/media-services/latest/setup-azure-subscription-how-to?tabs=cli).
7. Click **Continue**.

### Step 2: Azure Billing Exports

Billing export is used to get insights into your cloud infrastructure and Azure services such as Storage accounts, Virtual machines, Containers, etc.

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
6. In the Azure Cost Management portal, click the billing export that you created in the [enable export billing step](set-up-cost-visibility-for-azure.md).![](https://files.helpdocs.io/kw8ldg1itf/articles/7idbmchsim/1614753782707/screenshot-2021-03-03-at-12-12-44-pm.png)
7. Enter the following details in Harness:
	1. In the **Storage account name**, enter the account name.
	2. In **Storage Container**, enter the container name.
	3. In **Storage Directory**, enter the directory name.
	4. In **Report Name**, enter the report name.![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626070931659/screenshot-2021-07-12-at-11-51-46-am.png)
8. Click **Continue**.

### Step 3: Select Features

Select the Cloud Cost Management features that you would like to enable for your Azure account. Based on your selection Harness requires specific permissions for the storage account.

![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1627478411396/screenshot-2021-07-28-at-6-48-56-pm.png)CCM offers the following features:



|  |  |
| --- | --- |
| **Cost Visibility (Required)** | This feature is available by default and requires access to the access billing export. Provides the following capabilities:* Insights into Azure costs by services, accounts, etc.
* Root cost analysis using cost perspectives
* Cost anomaly detection
* Governance using budgets and forecasts
* Alert users using Email and Slack notification

This feature will give you cost insights that are derived from the billing export. For deep Kubernetes visibility and rightsizing recommendations based on the historical utilization and usage metrics, set up Kubernetes connectors. See [Set Up Cloud Cost Management for Kubernetes](set-up-cost-visibility-for-kubernetes.md). |
| **Azure resource optimization using AutoStopping rules (Optional)** | This feature allows you to enable intelligent cloud AutoStopping for your Azure instances. For more information, see [Create AutoStopping Rules for Azure](../add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md).* Orchestrate VMs based on idleness
* Provide granular savings visibility
 |

Make your selection and click **Continue**.

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
This is a common ID for Harness CCM client application. Use `10034206-24bf-442b-968c-70a9c896a2f6`If you see the following error proceed with [Step 2: Assign Permissions to the Storage Account](set-up-cost-visibility-for-azure.md).  
  
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
4. (Optional) You need to run this command only if you have selected **Azure Optimization by AutoStopping** in [Step 3: Select Features](set-up-cost-visibility-for-azure.md).  

```
az role assignment create --assignee 10034206-24bf-442b-968c-70a9c896a2f6 --role 'Contributor' --scope /subscriptions/123e4567-e89b-12d3-a456-9AC7CBDCEE52
```
5. Once you are done, click **Continue** in Harness.

### Step 5: Test Connection

The validation and verification happen in this step. Once the validation and verification are completed, click **Finish**.

Your connector is listed in the **Connectors**.

![](https://files.helpdocs.io/i5nl071jo5/articles/v682mz6qfd/1626084326416/screenshot-2021-07-12-at-3-34-31-pm.png)### Troubleshooting

1. If you get the `When using this permission, the backing application of the service principal being created must in the local tenant` error, check if you have the **Application Administrator** role assigned for your Azure AD. Users in this role can create and manage all aspects of enterprise applications, application registrations, and application proxy settings. For more information, see [Prerequisites](set-up-cost-visibility-for-azure.md) and [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#application-administrator).

### Next Steps

* [Analyze Cost for Azure Using Perspectives](../root-cost-analysis/analyze-cost-for-azure.md)
* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

