---
title: Use AutoStopping Rules Dashboard
description: AutoStopping Rules make sure that your non-production resources run only when used, and never when idle. This topic describes how to use AutoStopping Dashboard.
tags: 
   - helpDocs
   - Autostopping rules
helpdocs_topic_id: ehmi6kiynl
helpdocs_is_private: false
helpdocs_is_published: true
---

AutoStopping Rules make sure that your non-production resources run only when used, and never when idle. It also allows you to run your workloads on fully orchestrated spot instances without any worry of spot interruptions.

AutoStopping dashboard allows you to view a summary of all the AutoStopping rules you have created in a simple and intuitive interface. The following are the key features of the AutoStopping Rules dashboard:

* View total savings in your setup after AutoStopping rules are created
* View total spend in your setup after AutoStopping rules are created
* Number of instances managed using AutoStopping rules
* State of the instances where AutoStopping rules are applied
* Number of active AutoStopping rules in your setup

You can also perform the following actions from the AutoStopping dashboard view:

* Start the instances that are in a stopped state
* Edit or delete an AutoStopping rule
* Enable or disable an AutoStopping rule

![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627397248152/screenshot-2021-07-27-at-8-17-15-pm.png)In this topic:

* [Before You Begin](autostopping-dashboard.md)
* [Visual Summary](autostopping-dashboard.md)
* [View the AutoStopping Rules Dashboard](autostopping-dashboard.md)
* [Start the Instances from the Dashboard](autostopping-dashboard.md)
* [Enable or Disable an AutoStopping Rule from the Dashboard](autostopping-dashboard.md)
* [Edit an AutoStopping Rule from the Dashboard](autostopping-dashboard.md)
* [Delete an AutoStopping Rule from the Dashboard](autostopping-dashboard.md)

### Before You Begin

* [Create AutoStopping Rules for AWS](create-autostopping-rules-aws.md)
* [Create AutoStopping Rules for Azure](create-auto-stopping-rules-for-azure.md)

### Visual Summary

### View the AutoStopping Rules Dashboard

The **AutoStopping Summary of Rules dashboard** displays data as a chart and table. You can view, understand, and analyze your usage and cost data using either of them. However, the table allows you to view granular details.

1. In **AutoStopping Rules**, in **Summary of Rules**, click the instance for which you want to view the details.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627404676619/screenshot-2021-07-27-at-10-21-02-pm.png)You can view the details of the AutoStopping rule that you have created.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627404856146/screenshot-2021-07-27-at-10-22-03-pm.png)
2. In **Spend vs Saving**, view the spend and savings data of seven days for the selected rule. The savings are calculated as the following:

* The actual and potential costs of the VM are used to calculate savings.
	+ Your actual hourly cost multiplied by 24 equals your potential daily cost.
	+ The actual cost is the amount paid to the cloud provider for the number of hours actually used. This information comes from the AutoStopping usage records.  
	  
	
	```
	Potential cost = Actual hourly cost * 24
	```
	  
	With potential and actual cost, the savings are calculated.  
	  
	
	```
	Savings = Potential cost - Actual cost
	```
	  
	![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627408784246/screenshot-2021-07-27-at-11-29-12-pm.png)
1. In **Logs and Usage Time**, view usage details and logs for the selected rule.
	1. **Usage Time**: This shows the details of the time at which the rule started and ended for seven days.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627409105738/screenshot-2021-07-27-at-11-32-10-pm.png)
	2. **Logs**: This shows the different states of the rule with the timestamp. For example, active, warming up, and cooling down.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627409251009/screenshot-2021-07-27-at-11-36-50-pm.png)
2. In **Details**, click the instance to go to the cloud provider page to modify any of the settings.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627405699170/screenshot-2021-07-27-at-10-37-54-pm.png)

### Start the Instances from the Dashboard

You can start an instance from the Summary of Rules Page or from the details page of a selected rule.

#### From the Summary of Rules Page

1. In **AutoStopping Rules**, in **Summary of Rules**, click on the **Custom Domain** or **Hostname** of the selected instance.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627410890423/screenshot-2021-07-28-at-12-04-34-am.png)
2. The instance starts to warm up. This takes about 30 seconds.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627411081614/screenshot-2021-07-27-at-10-40-29-pm.png)
3. Once the instance is up and running, the status of the instance changes from stopped to running in the dashboard.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627411049681/screenshot-2021-07-28-at-12-07-13-am.png)

#### From the Details Page

1. In **AutoStopping Rules**, in **Summary of Rules**, click the instance that you want to delete.
2. In **Details**, click the **Hostname** or **Domain name** to warm up the instance.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627406033289/screenshot-2021-07-27-at-10-43-26-pm.png)

### Enable or Disable an AutoStopping Rule from the Dashboard

You can enable or disable an AutoStopping rule from the Summary of Rules Page or from the details page of a selected rule.

#### From the Summary of Rules Page

1. In **AutoStopping Rules**, in **Summary of Rules**, select the instance that you want to enable or disable.
2. Click the three-dot menu and click **Disable**.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627409668383/screenshot-2021-07-27-at-11-42-34-pm.png)
3. Click **Disable**.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627409822223/screenshot-2021-07-27-at-11-43-34-pm.png)

#### From the Details Page

1. In **AutoStopping Rules**, in **Summary of Rules**, click the instance that you want to enable or disable.
2. Click the Toggle button to disable or enable the rule.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627405485119/screenshot-2021-07-27-at-10-34-32-pm.png)

### Edit an AutoStopping Rule from the Dashboard

You can edit an AutoStopping rule from the Summary of Rules Page or from the details page of a selected rule.

#### From the Summary of Rules Page

1. In **AutoStopping Rules**, in **Summary of Rules**, select the instance that you want to enable or disable.
2. Click the three-dot menu and click **Edit**.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627409668383/screenshot-2021-07-27-at-11-42-34-pm.png)
3. The AutoStopping Rules setting appears. Follow the steps in [Create AutoStopping Rules for AWS](create-autostopping-rules-aws.md) and [Create AutoStopping Rules for Azure](create-auto-stopping-rules-for-azure.md).

#### From the Details Page

1. In **AutoStopping Rules**, in **Summary of Rules**, click the instance that you want to edit.
2. Click the Edit button. The AutoStopping Rules setting appears. Follow the steps in [Create AutoStopping Rules for AWS](create-autostopping-rules-aws.md) and [Create AutoStopping Rules for Azure](create-auto-stopping-rules-for-azure.md).![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627405485119/screenshot-2021-07-27-at-10-34-32-pm.png)

### Delete an AutoStopping Rule from the Dashboard

You can delete an AutoStopping rule from the Summary of Rules Page or from the details page of a selected rule.

#### From the Summary of Rules Page

1. In **AutoStopping Rules**, in **Summary of Rules**, select the instance that you want to enable or disable.
2. Click the three-dot menu and click **Delete**.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627409668383/screenshot-2021-07-27-at-11-42-34-pm.png)
3. Click **Delete**.

#### From the Details Page

1. In **AutoStopping Rules**, in **Summary of Rules**, click the instance that you want to delete.
2. Click the **Delete** button.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627405485119/screenshot-2021-07-27-at-10-34-32-pm.png)
3. Click **Delete**.![](https://files.helpdocs.io/i5nl071jo5/articles/ehmi6kiynl/1627410384338/screenshot-2021-07-27-at-11-56-09-pm.png)

