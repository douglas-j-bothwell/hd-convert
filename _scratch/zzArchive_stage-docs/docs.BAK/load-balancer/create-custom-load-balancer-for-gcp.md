---
title: Create a Custom Load Balancer for GCP
description: This topic describes how to create a custom load balancer for GCP.
tags: 
   - helpDocs
   - gcp
   - Load Balancer
   - listener
   - Autostopping rules
helpdocs_topic_id: 61h8i4d4j2
helpdocs_is_private: false
helpdocs_is_published: true
---

Currently, this feature is in Beta and behind Feature Flag. Contact [Harness Support](mailto:support@harness.io) to enable the feature.A load balancer distributes user traffic across multiple instances of your applications. Load balancing reduces the chances of performance issues in your applications by spreading the load.

This topic describes how to create a custom load balancer for creating AutoStopping Rules for Google Compute Engine VM(s).

In this topic:

* [Before You Begin](create-custom-load-balancer-for-gcp.md)
* [Why do You Need a Custom Load Balancer?](create-custom-load-balancer-for-gcp.md)
* [How Does Custom Load Balancer Work?](create-custom-load-balancer-for-gcp.md)
* [Review: Custom Load Balancer Requirements](create-custom-load-balancer-for-gcp.md)
* [Create a Custom Load Balancer](create-custom-load-balancer-for-gcp.md)
	+ [Choose a Domain Name](create-custom-load-balancer-for-gcp.md)
	+ [Configure a Custom Load Balancer](create-custom-load-balancer-for-gcp.md)
* [Next Step](create-custom-load-balancer-for-gcp.md)

### Before You Begin

* [Create a GCP Connector for AutoStopping Rules](../cloud-cost-management/add-connectors/create-a-gcp-connector-for-auto-stopping-rules.md)
* [Create AutoStopping Rules for GCP](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-gcp.md)

### Why do You Need a Custom Load Balancer?

A single custom load balancer can be set up to handle multiple AutoStopping Rules from the same VPC. Since VPC spans multiple regions, it allows saving costs by using a single custom load balancer for multiple rules.

### How Does Custom Load Balancer Work?

Harness' intelligent cloud AutoStopping Rules use Envoy and other proprietary services for the custom load balancer that routes traffic to configured Google Compute Engine VMs.

Envoy consists of clusters and listeners. Listeners represent the incoming port through which requests are routed to clusters based on route configurations and route path matches.

![](https://files.helpdocs.io/i5nl071jo5/articles/61h8i4d4j2/1648745647724/screenshot-2022-03-31-at-10-23-46-pm.png)### Review: Custom Load Balancer Requirements

* Harness creates and manages a custom load balancer, allowing you to use your preferred instance type.
* The load balancer must be located in the same VPC as the virtual machines that it will manage.
* Multiple AutoStopping rules can use a single load balancer to manage virtual machines in different regions and zones but within the same VPC.

### Create a Custom Load Balancer

The following steps are involved to create a custom load balancer for GCP:

#### Choose a Domain Name

Perform the following steps to create a new custom load balancer for GCP.

1. In **Cloud Costs**, click **New AutoStopping Rule**.
2. In **AutoStopping Rules**, select **GCP**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping rules.![](https://files.helpdocs.io/i5nl071jo5/articles/cfojlhnf8s/1634627802704/screenshot-2021-10-19-at-12-46-27-pm.png)
3. If you have already linked your GCP account and want to use that account, then select the GCP account from the **Connect to your GCP account** drop-down list.
4. If you have not added your cloud account, click **Connect to your GCP account** drop-down list and then click **New Connector**. For the detailed steps, see [Create a GCP Connector](../cloud-cost-management/add-connectors/create-a-gcp-connector-for-auto-stopping-rules.md).
5. Define an AutoStopping Rule. See [Step: Define an AutoStopping Rule](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-gcp.md).
6. In Select the resources to be managed by the AutoStopping Rule, select **GCE VM(s)**. See [Step: Select the Resources to be Managed by the AutoStopping Rule](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-gcp.md).
7. (Optional) Set up advanced configuration. See [Step: Set Up Advanced Configuration](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-gcp.md).
8. In **Setup Access**, select **DNS Link**.
9. In **Select a load balancer**, click **New Load Balancer** to add a load balancer.[![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643309101396/screenshot-2022-01-28-at-12-14-43-am.png)](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643309101396/screenshot-2022-01-28-at-12-14-43-am.png)
10. In **Create a new Load Balancer**, in **Provide a name for the Load balancer**, enter a name for your load balancer. This name will appear in your load balancer list.
11. In **Enter Domain Name**, enter the domain name. A domain name is required to route traffic to the load balancer. For example, `autostopping.yourcompany.com`.![](https://files.helpdocs.io/i5nl071jo5/articles/61h8i4d4j2/1648750801172/screenshot-2022-03-31-at-11-49-41-pm.png)
12. Click **Continue**.

#### Configure a Custom Load Balancer

Harness creates and manages a custom load balancer, allowing you to use your preferred instance type. The load balancer must be located in the same VPC as the virtual machines that it will manage. Multiple AutoStopping rules can use a single load balancer to manage virtual machines in different regions and zones but within the same VPC.

Provide the following details to configure the custom load balancer:

1. Select a Region from the drop-down list to install the Access Point.
2. Select a **Zone** from the drop-down list.
3. Select **VPC**.
4. Select **Network tags**.
5. Select **Subnet**.
6. Select **Machine type**.
7. Once you're done, click **Save Load Balancer**.![](https://files.helpdocs.io/i5nl071jo5/articles/61h8i4d4j2/1648799139611/screenshot-2022-03-31-at-11-51-42-pm.png)Your load balancer is now listed.![](https://files.helpdocs.io/i5nl071jo5/articles/61h8i4d4j2/1648751071047/screenshot-2022-03-31-at-11-54-11-pm.png)

### Next Step

* [Create AutoStopping Rules for GCP](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-auto-stopping-rules-for-gcp.md)

