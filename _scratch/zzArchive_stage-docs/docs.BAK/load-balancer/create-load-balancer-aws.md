---
title: Create an Application Load Balancer for AWS
description: Describes how to create a new Application Load Balancer for AWS.
tags: 
   - helpDocs
   - Load Balancer
   - Autostopping rules
   - AWS
helpdocs_topic_id: eba1bn2jm6
helpdocs_is_private: false
helpdocs_is_published: true
---

A load balancer serves as the single point of contact for clients. The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases the availability of your application.

An Application Load Balancer makes routing decisions at the application layer (HTTP/HTTPS), supports path-based routing, and can route requests to one or more ports on each container instance in your cluster.

This topic describes how to create a new application load balancer for creating AutoStopping Rules for AWS. 

In this topic:

* [Before You Begin](create-load-balancer-aws.md)
* [Why do You Need a Load Balancer?](create-load-balancer-aws.md)
* [Create a New Application Load Balancer](create-load-balancer-aws.md)
	+ [Configure DNS Using Route 53](create-load-balancer-aws.md)
	+ [Configure DNS Using other DNS Providers](create-load-balancer-aws.md)

### Before You Begin

* [Connect to an AWS Connector](../cloud-cost-management/add-connectors/connect-to-an-aws-connector.md)
* [Create AutoStopping Rules for AWS](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md)

### Why do You Need a Load Balancer?

AutoStopping integrates with the cloud provider's native load balancing technologies (Application Load Balancer, Azure AppGateway, etc.) to provide start and stop capability for the AutoStopping-managed cloud services.

![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643089567315/screenshot-2022-01-20-at-12-04-39-pm.png)* The rule requires a load balancer to direct traffic/shut down appropriate instances. Each load balancer is identified by its DNS hostname `(autostopping.example.com`, `www.example.com`, etc.).
* AutoStopping can use the same load balancer for multiple AutoStopping rules. This means multiple instances can be added under one single load balancer and AutoStopping will manage the traffic based on the HTTP host details.
* DNS configuration for load balancer is a one-time setup.
* When configuring a load balancer, it is required to choose a domain name. This domain name will be used for all the AutoStopping rules created under this load balancer. For example:  
  

```
*.autostopping.example.com -> Load balancer IP
```

### Create a New Application Load Balancer

A DNS link allows you to access the resources managed by the AutoStopping rule using an HTTP or HTTPS URL. Select DNS Link if the underlying application running on the resources managed by this AutoStopping Rule is currently accessed by an HTTP or HTTPS URL.

Perform the following steps to create a new Application Load Balancer in AWS.

1. In **Cloud Costs**, click **New AutoStopping Rule**.

1. In **AutoStopping Rules**, select **AWS**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping rules.[![](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1634476693199/screenshot-2021-10-17-at-6-47-51-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1634476693199/screenshot-2021-10-17-at-6-47-51-pm.png)
2. If you have already linked your AWS account and want to use that account, then select the AWS account from the **Connect to your AWS account** drop-down list.
3. If you have not added your cloud account, click **Connect to your AWS account** drop-down list and then click **New Connector**. For the detailed steps, see [Connect to an AWS Connector](../cloud-cost-management/add-connectors/connect-to-an-aws-connector.md).[![](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1641315189370/screenshot-2022-01-04-at-10-22-55-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1641315189370/screenshot-2022-01-04-at-10-22-55-pm.png)
4. Define an AutoStopping Rule. See [Step: Define an AutoStopping Rule](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).
5. Select the resources to be managed by the AutoStopping Rule. See [Step: Select the Resources to be Managed by the AutoStopping Rule](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).
6. (Optional) Set up advanced configuration. See [Step: Set Up Advanced Configuration](../cloud-cost-management/add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).
7. In **Setup Access**, select **DNS Link**.
8. In **Select a load balancer**, click **New Load Balancer** to add a load balancer.![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643309101396/screenshot-2022-01-28-at-12-14-43-am.png)
9. In **Create a new Load Balancer**, in **Provide a name for the Load balancer**, enter a name for your load balancer. This name will appear in your load balancer list.

The Application Load Balancer (ALB) does not have a domain name associated with it. The AutoStopping Rule directs traffic to resources through the load balancer. Hence the load balancer requires a domain name to be accessed by the rule. You can configure DNS using **Route 53** or **Others** DNS providers to do the mapping.

#### Configure DNS Using Route 53

AutoStopping Rule has first-class integration with Route 53. 

This will only work if Route 53 is in the same AWS account as the instance you want to include in the AutoStopping rule.1. In **Select your preferred DNS provider and perform the mapping**, select **Route 53**.
2. Select the correct Route 53 hosted zone from the drop-down list.![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643310060101/screenshot-2022-01-28-at-12-30-40-am.png)
3. In **Enter Domain name**, enter the domain name. For example, `autostopping`.![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643310193120/screenshot-2022-01-28-at-12-32-41-am.png)
4. Click **Continue**.
5. Select region from the drop-down list to install the Access Point.
6. Select a certificate from the drop-down list.
7. Select VPC.
8. Select security groups.
9. Click **Save Load Balancer**.![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643311129011/screenshot-2022-01-28-at-12-48-23-am.png)Once you save your load balancer, AutoStopping Rule will create an entry similar to the following example in your Route 53 account.  
  

```
A record: *.autostopping.yourdomain.com<lightwing.io> -> up-a1thp0i3k1k7ment50l0-4225468.ap-south-1.elb.amazonaws.com
```

#### Configure DNS Using other DNS Providers

1. In **Select your preferred DNS provider and perform the mapping**, select **Others**.
2. In **Enter Domain name**, enter the domain name. For example, `autostopping.yourcompany.com`.![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1643311246089/screenshot-2022-01-28-at-12-50-26-am.png)
3. Click **Continue**.
4. Select region from the drop-down list to install the Access Point.
5. (Optional) Select a certificate from the drop-down list.
6. Select VPC.
7. Select security groups.
8. Once you're done, click **Save Load Balancer**.![](https://files.helpdocs.io/i5nl071jo5/articles/eba1bn2jm6/1621444257244/screenshot-2021-05-19-at-10-36-59-pm.png)
9. In your DNS provider’s configuration page, add CNAME record.  See [Add DNS CNAME record](https://docs.aws.amazon.com/managedservices/latest/ctexguide/ex-dirserv-cname-record-add-col.html). For example:  
  

```
*.autostopping.test.com -> Load balancer DNS address
```

Your Load Balancer is now listed.

