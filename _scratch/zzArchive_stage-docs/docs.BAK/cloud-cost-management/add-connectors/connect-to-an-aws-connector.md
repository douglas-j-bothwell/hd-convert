---
title: Create an AWS Connector for AutoStopping Rules
description: Connectors allow Harness to connect to your deployment environments, such as Kubernetes Clusters, AWS, Google Cloud Platform, Azure, etc. This topic describes how to link your AWS cloud account to Harness.
tags: 
   - helpDocs
   - AWS
   - Autostopping rules
helpdocs_topic_id: hiyi6xvj36
helpdocs_is_private: false
helpdocs_is_published: true
---

Connectors allow Harness to connect to your deployment environments, such as Kubernetes Clusters, AWS, Google Cloud Platform, Azure, etc. To create an AutoStopping Rule for your AWS instances, you first need to connect Harness to your AWS account. This topic describes how to connect your AWS cloud account to Harness.

In this topic:

* [Before You Begin](connect-to-an-aws-connector.md)
* [Add an AWS Connector](connect-to-an-aws-connector.md)
	+ [Step 1: Overview](connect-to-an-aws-connector.md)
	+ [Step 2: Cost and Usage Report](connect-to-an-aws-connector.md)
	+ [Step 3: Select Features](connect-to-an-aws-connector.md)
	+ [Step 4: Create Cross-Account Role](connect-to-an-aws-connector.md)
	+ [Step 5: Test Connection](connect-to-an-aws-connector.md)
* [Next Steps](connect-to-an-aws-connector.md)

### Before You Begin

* [AutoStopping Rules Overview](auto-stopping-rules.md)

### Add an AWS Connector

Perform the following steps to add an AWS connector for AutoStopping Rules:

1. In **Cloud Costs**, click **New AutoStopping Rule**.![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)
2. In **AutoStopping Rules**, select **AWS**. It is the cloud account in which your workloads are running that you want to manage using AutoStopping Rules.![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1633498726320/screenshot-2021-10-06-at-11-08-02-am.png)
3. Click **Connect to your AWS account** drop-down list and then click **New Connector**.

#### Step 1: Overview

1. In **AWS Connector**, in **Overview**, enter the **Connector** **Name**. The name will appear in CCM Perspectives to identify this cloud provider.
2. In **Specify the AWS account ID**, enter your AWS account ID and click **Continue**. To find your AWS account ID, see [Finding your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html#FindingYourAWSId).![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1633511261805/screenshot-2021-10-06-at-2-37-16-pm.png)

#### Step 2: Cost and Usage Report

Cost and Usage Report (CUR) provides detailed billing data across AWS accounts to help you analyze your spending. You need to enter the **cost and usage report name** and **cost and usage S3 bucket name** in Harness. To get these details, do the following:

1. In **Cost and Usage Report**, click **Launch AWS console** to log into your AWS account.
2. In **AWS Cost and Usage Reports**, click **Create Report**.[![](https://files.helpdocs.io/kw8ldg1itf/articles/5ql31pdjcm/1593247638364/screenshot-2020-06-27-at-12-47-26-pm.png)](https://files.helpdocs.io/kw8ldg1itf/articles/5ql31pdjcm/1593247638364/screenshot-2020-06-27-at-12-47-26-pm.png)
3. Enter the **Report Name**. This is the CUR name that you need to enter in Harness.
4. In **Additional report details**, select the checkbox **Include resource IDs** to include the IDs of each individual resource in the report.
5. In **Data refresh settings**, select the checkbox **Automatically refresh your Cost & Usage Report when charges are detected for previous months with closed bills**.
6. Click **Next**.  
  
When you are done with the **Report content** step, it will look something like this:![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1632799614933/screenshot-2021-09-28-at-8-56-20-am.png)
7. In the **S3 bucket**, click **Configure**.
8. In **Configure S3 Bucket**, in **Create a bucket**, enter the **S3 bucket name**. This is the cost and usage S3 bucket name that you need to enter in Harness. For more information on S3 bucket naming requirements, see [Amazon S3 Bucket Naming Requirements](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html).
9. Select **Region** from the drop-down list and click **Next**. It is recommended to select **US East** (**N. Virginia**).![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625817602710/screenshot-2021-07-09-at-1-29-03-pm.png)
10. In **Verify policy**, select the checkbox **I have confirmed that this policy is correct** and click **Save**.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625817842853/screenshot-2021-07-09-at-1-31-11-pm.png)
11. Enter the report path prefix that you want to be prepended to the name of your report.
12. Select **Hourly** in **Time granularity**.
13. Select **Overwrite Existing Report** in **Report versioning**.
14. Do not select any value in **Enable report data integration for**.
15. Select **GZIP** in the **Compression type**.
16. Click **Next**.  
  
When you are done with the **Delivery options** step, it will look something like this:![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625850563649/screenshot-2021-07-09-at-1-35-53-pm.png)
17. Review your report details and click **Review and Complete**.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625823491297/screenshot-2021-07-09-at-1-37-00-pm.png)Your report is listed in AWS Cost and Usage Reports.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625818364978/screenshot-2021-07-09-at-1-37-51-pm.png)
18. Enter the **Cost and Usage Report Name** (as entered in step 3) and **Cost and Usage S3 Bucket Name** (as entered in step 8) in Harness.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625818328989/screenshot-2021-07-09-at-1-41-28-pm.png)

#### Step 3: Select Features

Select the Cloud Cost Management features that you would like to use on your AWS account. Based on your selection Harness requires specific permissions for the cross-account role. See [Review: AWS Access Permissions](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).

![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1633512792813/screenshot-2021-10-06-at-3-02-51-pm.png)CCM offers the following features:



|  |  |
| --- | --- |
| **Cost Visibility (Required)** | This feature is available by default and requires access to the CUR report. Provides the following capabilities:* Insights into AWS costs by services, accounts, etc.
* Root cost analysis using cost perspectives
* Cost anomaly detection
* Governance using budgets and forecasts
* Alert users using Email and Slack notification
 |
| **AWS ECS and Resource Inventory Management (Optional)** | This feature provides visibility into your EC2, EBS volumes, and ECS costs. The insights provided by inventory management can be consumed by Finance teams to understand the resource utilization across the board.* Breakdown by ECS cluster cost, Service, Task, Launch Type (EC2, Fargate)
* Insight into EC2 instances and their utilization
* Access to AWS EC2 Inventory Cost and EBS Volumes and Snapshots inventory dashboards. For more information, see [View AWS EC2 Inventory Cost Dashboard](../ccm-dashboards/view-aws-ec-2-inventory-cost-dashboard.md), [Orphaned EBS Volumes and Snapshots Dashboard](../ccm-dashboards/orphaned-ebs-volumes-and-snapshots-dashboard.md), and [View AWS EC2 Instance Metrics Dashboard](../ccm-dashboards/view-aws-ec-2-instance-metrics.md).
 |
| **AWS resource optimization using AutoStopping rules (Required for AutoStopping Rules)** | This feature allows you to enable Intelligent Cloud AutoStopping for your AWS instances and auto-scaling groups. For more information, see [Create AutoStopping Rules for AWS](create-auto-stopping-rules/create-autostopping-rules-aws.md).* Orchestrate VMs and ASGs based on idleness
* Run your workloads on fully orchestrated spot instances
* Granular savings visibility
 |

Make your selection and click **Continue**.

#### Step 4: Create Cross-Account Role

Harness uses the secure cross-account role to access your AWS account. The role includes a restricted policy to access the cost and usage reports and resources for the sole purpose of cost analysis and cost optimization.

1. In **Create Cross Account Role**, click **Launch Template in AWS console**.
2. In **Quick create stack**, in **Capabilities**, select the acknowledgment, and click **Create stack**.It is recommended that you do not modify any value in the **Quick create stack** page.  
  
  
The value for `BillingEnabled`, `EventsEnabled`, and `OptimizationEnabled` varies depending on the features that you have selected in the [Select Features step](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md).![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625849363280/screenshot-2021-07-09-at-10-18-58-pm.png)
3. In the **Stacks** page, from the **Outputs** tab copy the **Value** of **CrossAccountRoleArn Key**.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625824586201/screenshot-2021-07-09-at-3-26-06-pm.png)
4. In **Role ARN**, enter the **Cross-Account Role ARN** that you copied from the **Output**s tab (previous step) in Harness.
5. The **External ID** is generated dynamically for your account. For example, `harness:111111111111:lnFZRF6jQO6tQnB9xxXXXx` .Do not modify the value of **External ID**.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625826333902/screenshot-2021-07-09-at-3-54-52-pm.png)
6. Click **Save and Continue**.

#### Step 5: Test Connection

The validation and verification happen in this step. Once the validation and verification are completed, click **Finish**.

![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1625826679832/screenshot-2021-07-09-at-2-04-39-pm.png)Your connector is now listed under **Connect to your AWS account** drop-down list.

![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1633513671896/screenshot-2021-10-06-at-3-17-26-pm.png)### Step: Create Multiple Connectors in an AWS Account

Harness CCM also provides the flexibility to create multiple Connectors using a stack set configured at the master account level. It involves the following steps:

* Create a stack set
* Create an API Key in Harness
* Add an Admin Role
* Run the cURL Command to create connectors using the Roles created in the AWS accounts via API

#### Step 1: Create a Stack Set in AWS

Perform the following steps to create a stack set in AWS:

1. Launch create stack set template using the following link:  
<https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacksets/create>
2. In **Choose a template**, in **Permissions**, select **Service-managed permissions**.
3. In **Prerequisite - Prepare template**, select **Template is ready**.
4. In the **Specify template**, in the **Template source**, select **Amazon S3 URL**.
5. In the **Amazon S3 URL** enter the following URL and click **Next**.  
`https://continuous-efficiency-prod.s3.us-east-2.amazonaws.com/setup/ngv1/HarnessAWSTemplate.yaml`![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1651723129898/screenshot-2022-05-05-at-9-28-24-am.png)
6. In **Specify StackSet details**, in **StackSet** **name**, enter a stack set name. For example, `harness-ce-iam-stackset`.
7. In **Parameters**, specify the following details:
	1. Set **BillingEnabled** to false.
	2. Leave the **BucketName** empty.
	3. Set **EventsEnabled** to true.
	4. In **ExternalID** enter your <*Harness Account ID>*, for example, `harness:111122225555` .
	5. In **LambdaExecutionRoleName**, enter Lambda execution role name, for example, `HarnessCELambdaExecutionRole`. The Lambda execution role name must begin with `Harness`.
	6. Set **OptimizationEnabled** to true.
	7. **PrincipalBilling** is auto-generated for your AWS account. Do not edit the Principal Billing details. For example, `arn:aws:iam::123451231355:root`.
	8. In **RoleName**, enter the role name, for example, `HarnessCERole`. The role name must begin with Harness e.g., HarnessCERole, HarnessManagedRole.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1651678007697/screenshot-2022-05-04-at-8-56-33-pm.png)
8. Once you've entered all the details, click **Next**.
9. In **Configure StackSet options**, in **Managed execution**, select **Active** and click **Next**.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1651723477788/screenshot-2022-05-05-at-9-34-16-am.png)
10. In **Set deployment options**, in **Add stacks to stack set**, select **Deploy new stacks**.
11. In **Deployment targets**, select **Deploy to organization** (recommended). You can select **Deploy to Organizational Units (OUs)** to limit the monitoring clusters to a particular OU or a subset of linked accounts.
12. In **Automatic deployment**, select **Enabled**.
13. In **Account removal behavior**, select **Delete Stacks**.
14. Select a **region** from the drop-down list and click **Next**.
15. In **Deployment Options**, in **Region Concurrency**, select **Sequential**.![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1651723676530/screenshot-2022-05-05-at-9-37-41-am.png)
16. Review the details, select acknowledgment, and click **Submit**.

#### Step 2: Create an API Key in Harness

1. In Harness, click **Home**.
2. In **Account Setup**, click **Access Control**.
3. Click **Service Accounts** and then click the service account to which you want to add a new API Key. For step-by-step instructions to add a new Service Account, see [Add and Manage Service Accounts](https://ngdocs.harness.io/article/e5p4hdq6bd).
4. In the Service Account's settings page, click **API Key**.
5. In the **New API Key** settings, enter **Name, Description,** and **Tags**.
6. Click **Save**. The new API Key is created.  
  
Once you've created an API Key for your Service Account, generate a Token for this API Key.
7. To generate a Token for this API Key, click **Token** below the API Key you just created.
	1. In the **New Token** settings, enter Name, Description, and Tags.
	2. To set an expiration date for this token, select **Set Expiration Date**.
	3. Enter date in **Expiration Date (mm/dd/yyyy)**.
	4. Click **Generate Token**.
	5. Your new Token is generated.[![](https://files.helpdocs.io/i5nl071jo5/articles/tdoad7xrh9/1625893969426/screenshot-2021-07-10-at-10-33-16-am.png)](https://files.helpdocs.io/i5nl071jo5/articles/tdoad7xrh9/1625893969426/screenshot-2021-07-10-at-10-33-16-am.png)You cannot see this token value after you close this dialog. Make sure to copy and store the generated token value securely.

You need to enter this Token when running your cURL command.

#### Step 3: Add an Admin Role to the Service Account

Ensure that you've added the Admin role to this Service Account. For more information, see [Add and Manage Roles](https://docs.harness.io/article/tsons9mu0v-add-manage-roles).

![](https://files.helpdocs.io/i5nl071jo5/articles/80vbt5jv0q/1651680903213/screenshot-2022-05-04-at-9-44-50-pm.png)#### Step 4: Run the cURL Command

Run the following command for each AWS Account ID and IAM Role Pair:


```
curl -i -X POST \  
  'https://app.harness.io/gateway/ng/api/connectors?accountIdentifier=<CustomerHarnessAccountID>' \  
  -H 'Content-Type: application/json' \  
  -H 'x-api-key: <Enter your API Key Token>' \  
  -d '{  
  "connector":{  
    "name":"AWSConnector-<AWSAccountId>",  
    "identifier":"AWSConnector_<AWSAccountId>",  
    "spec":{  
      "crossAccountAccess":{  
        "crossAccountRoleArn":"<Enter the Role Created in the Account>",  
        "externalId":"<Enter ExternalID oused when creating the IAM Role>"  
      },  
      "awsAccountId":"<AWSAccountId>",  
      "curAttributes":{  
        "reportName":"",  
        "s3BucketName":""  
      },  
      "featuresEnabled":[  
        "VISIBILITY",  
        "OPTIMIZATION"  
      ]  
    },  
    "type":"CEAws"  
  }  
}'
```
### Next Steps

* [Create AutoStopping Rules for AWS](create-auto-stopping-rules/create-autostopping-rules-aws.md)
* [Use AutoStopping Rules Dashboard](create-auto-stopping-rules/autostopping-dashboard.md)

