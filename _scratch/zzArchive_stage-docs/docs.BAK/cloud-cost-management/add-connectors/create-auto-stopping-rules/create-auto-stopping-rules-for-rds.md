---
title: Create AutoStopping Rules for RDS
description: This topic describes how to create AutoStopping Rules for Amazon Relational Database Service (RDS).
tags: 
   - helpDocs
   - Autostopping rules
   - Amazon RDS
helpdocs_topic_id: ryk2e3ujpn
helpdocs_is_private: false
helpdocs_is_published: true
---

AutoStopping Rule is a dynamic and powerful resource orchestrator for non-production workloads. For more information, see [AutoStopping Rules Overview](../auto-stopping-rules.md).

This topic describes how to create AutoStopping Rules for Amazon Relational Database Service (RDS).

### Before You Begin

* [Create an AWS Connector for AutoStopping Rules](../connect-to-an-aws-connector.md)

### Prerequisites

* Access to CUR. See [Review: Cost and Usage Reports (CUR) and CCM Requirements](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Permissions to create a cross-account role. See [AWS Access Permissions](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Permissions for AWS Resource Optimization Using AutoStopping Rules. See[AWS Resource Optimization Using AutoStopping Rules](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* The database that will be onboarded must be able to start and stop. Harness AutoStopping cannot manage certain DB instances, such as serverless ones, because they cannot be started or stopped.

### Review: Use Cases for Using AutoStopping for RDS

This section describes some of the most common scenarios where you can use AutoStopping Rules with RDS.

#### EC2 Rule With RDS Dependency

This is an ideal use case when a web server or an application server connects to an RDS database to access/store data.

![](https://files.helpdocs.io/i5nl071jo5/articles/ryk2e3ujpn/1649666383865/screenshot-2022-04-11-at-2-09-07-pm.png)In this scenario, if there is no traffic to the application server (EC2 instance), the AutoStopping Rule will stop both the application server and the RDS database that it connects to. When the application server receives traffic, the Rule will start the RDS instance first, followed by the EC2 instance. This results in substantial cost savings for both instances. 

You can achieve this by simply creating an EC2 AutoStopping Rule and adding an RDS Rule as a dependency.

#### Query the Archived Database Using Your Own Database Client

See [Use Harness AutoStopping CLI to Keep the RDS Instance(s) Running](create-auto-stopping-rules-for-rds.md).

### Step 1: Add a Cloud Provider

Perform the following steps to link your AWS cloud account to Harness.

1. In **Cloud Costs**, click **New AutoStopping Rule**.[![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)
2. In **AutoStopping Rules**, select **AWS**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping rules.[![](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1634476693199/screenshot-2021-10-17-at-6-47-51-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1634476693199/screenshot-2021-10-17-at-6-47-51-pm.png)
3. If you have already linked your AWS account and want to use that account, then select the AWS account from the **Connect to your AWS account** drop-down list.
4. If you have not added your cloud account, click **Connect to your AWS account** drop-down list and then click **New Connector**. For the detailed steps, see [Connect to an AWS Connector](../connect-to-an-aws-connector.md).[![](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1641315189370/screenshot-2022-01-04-at-10-22-55-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1641315189370/screenshot-2022-01-04-at-10-22-55-pm.png)

### Step 2: Add a New AutoStopping Rule for RDS

Creating AutoStopping Rules for Amazon RDS involves the following steps:

#### Define an AutoStopping Rule

1. In **Cloud Costs,** in **AutoStopping Rules**, click **New AutoStopping Rule**.
2. In the cloud account type, select **AWS**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping rules.
3. Select your AWS account from the **Connect to your AWS account** drop-down list and click **Next**. If you have not added an AWS cloud account, see [Connect to an AWS Connector](https://newdocs.helpdocs.io/article/hiyi6xvj36-connect-to-an-aws-connector).[![](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1634480750909/screenshot-2021-10-17-at-7-55-31-pm.png)](https://files.helpdocs.io/i5nl071jo5/articles/7025n9ml7z/1634480750909/screenshot-2021-10-17-at-7-55-31-pm.png)
4. In **Define your AutoStopping rule**, in **Name your Rule**, enter a name for your rule. This is the name of your AutoStopping rule.
5. In **Idle time**, enter the idle time in minutes. This is the time that the AutoStopping rule will wait before stopping the idle instances.

#### Select the Resources to be Managed by the AutoStopping Rule

Select the cloud resources that you want to manage using this rule. AutoStopping Rule will monitor the selected resources and stop them when they are idle beyond the configured idle time.

1. In **Select the resources to be managed by the rule**, select **RDS** and then click Add RDS instance.![](https://files.helpdocs.io/i5nl071jo5/articles/ryk2e3ujpn/1651841971040/screenshot-2022-05-06-at-6-29-10-pm.png)
2. In **Select RDS Instance**, do the following:
	1. Select the region where your instance is hosted from the drop-down list.
	2. Select the RDS instance for which you want to enable AutoStopping Rule and click **Add Selected**.![](https://files.helpdocs.io/i5nl071jo5/articles/ryk2e3ujpn/1651842989997/screenshot-2022-05-06-at-6-46-19-pm.png)
	3. Once you've made all the selections, click **Add Selected**.
3. Click **Next**.

#### (Optional) Set Up Advanced Configuration

In this step, you can configure the following settings:

* **Add Dependency**: Set dependencies between two or more AutoStopping Rules when you want one Rule to make one or more Rules to be active based on the traffic that it receives. See [Add Dependency](https://newdocs.helpdocs.io/article/7025n9ml7z-create-autostopping-rules-aws#add_dependency).
* **Fixed Schedules**: Create fixed uptime or downtime schedules for the resources managed by this AutoStopping Rule. When a resource is configured to go up or down on a fixed schedule, it is unaffected by activity or idleness during that time period. See [Fixed Schedules](https://newdocs.helpdocs.io/article/7025n9ml7z-create-autostopping-rules-aws#fixed_schedules).

### Review

In Review, verify all the configuration details and click **Save Rule**. To edit any of the configuration settings, click **EDIT** and modify the settings.

Your AutoStopping rule is listed under the [AutoStopping Rules dashboard](autostopping-dashboard.md).

### Use Harness AutoStopping CLI to Keep the RDS Instance(s) Running

You can also use Harness AutoStopping CLI to query the archived database using your own database client. Basically you're leveraging Harness CLI to keep the RDS instance(s) running.

1. From the AutoStopping dashboard, click on the RDS rule.
2. In **Download CLI**, select your operating system to download the Harness CLI for your system.![](https://files.helpdocs.io/i5nl071jo5/articles/ryk2e3ujpn/1652071260888/screenshot-2022-05-09-at-10-09-42-am.png)
3. Click **Download CLI**.
4. Run the following command to connect to an RDS database.  

```
harness connect --host hostname --port 5432
```
  
The above command will start the RDS database if it is not running and set up a secure tunnel to it. This command will output the connection details to which you can connect your database client.
5. As an example, in the case of Postgres, the following command can be used to connect to the database.  

```
psql -h localhost -p port-received-from-above -u postgres
```
  
As soon as your database client is disconnected, AutoStopping will consider it as idleness and shut down the database after the configured idle time.

