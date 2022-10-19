---
title: Create an Application Gateway for Azure
description: Describes how to create a new Application Gateway for Azure.
tags: 
   - helpDocs
   - azure
   - Autostopping rules
   - Gateway
helpdocs_topic_id: d43tsblpma
helpdocs_is_private: false
helpdocs_is_published: true
---

Azure Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. Application Gateway can make routing decisions based on additional attributes of an HTTP request, for example, URI path or host headers.

### Before You Begin

* [Connect to an Azure Connector](../cloud-cost-management/add-connectors/add-azure-connector.md)
* [Create AutoStopping Rules for Azure](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md)

### Create a New Application Gateway

Perform the following steps to create a new Application Gateway in Azure.

1. In **Cloud Costs**, click **New AutoStopping Rule**.[![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)
2. In **AutoStopping Rules**, select **Azure**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping rules.[![](https://files.helpdocs.io/i5nl071jo5/articles/r5x5pvuqfn/1641314863202/screenshot-2022-01-04-at-10-17-19-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/r5x5pvuqfn/1641314863202/screenshot-2022-01-04-at-10-17-19-pm.png)
3. If you have already linked your Azure account and want to use that account, then select the Azure account from the list.
4. If you have not added your cloud account, click **New Connector**. For the detailed steps, see [Connect to an Azure Connector](../cloud-cost-management/add-connectors/add-azure-connector.md).  
[![](https://files.helpdocs.io/i5nl071jo5/articles/r5x5pvuqfn/1641313959022/screenshot-2022-01-04-at-10-02-26-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/r5x5pvuqfn/1641313959022/screenshot-2022-01-04-at-10-02-26-pm.png)
5. Define an AutoStopping Rule. See [Step 2: Add a New AutoStopping Rule](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md).
6. Select the resources to be managed by the AutoStopping Rule. See [Step: Select the Resources to be Managed by the AutoStopping Rule](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md).
7. Select the instance fulfillment type. See [Step 3: Select the Instance Fulfillment Type](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-azure.md).
8. (Optional) Set up advanced configuration. See [Step: Set Up Advanced Configuration](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).
9. In **Setup Access**, select **DNS Link**.
10. In **Select Application Gateway**, click **New Application Gateway** to add an application gateway.
11. In **Create a new Application Gateway**, in **Provide a name for the Load balancer**, enter a name for your application gateway. This name will appear in your application gateway list.
12. In Enter Domain Name, enter a domain name. For example, `autostopping.yourcompany.com`.  
![](https://files.helpdocs.io/i5nl071jo5/articles/d43tsblpma/1643369405229/screenshot-2022-01-28-at-4-59-45-pm.png)
13. Click **Continue**.
14. Select region from the drop-down list to install the Access Point.
15. Select a **Resource Group** from the drop-down list.
16. (Optional) Upload a **Certificate**.
17. Select **Virtual Network**.
18. Select **Subnet**.
19. Select **Frontend IP**.
20. Select **SKU**.
21. Once you're done, click **Save**.  
  
Your application gateway is listed under the **Application Gateway**.

