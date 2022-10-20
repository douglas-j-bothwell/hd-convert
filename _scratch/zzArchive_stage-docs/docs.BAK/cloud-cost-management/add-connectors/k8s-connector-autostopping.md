---
title: Create a Kubernetes Connector for AutoStopping Rules
description: This topic describes how to create a Kubernetes connector for AutoStopping Rules.
tags: 
   - helpDocs
   - kubernetes
   - cloud cost management
   - Autostopping rules
   - Connectors
helpdocs_topic_id: dfwoqnacnw
helpdocs_is_private: true
helpdocs_is_published: true
---

Currently, this feature is in Beta.Connectors allow Harness to connect to your deployment environments, such as Kubernetes Clusters, AWS, Google Cloud Platform, Azure, etc. To create an AutoStopping Rule for your Kubernetes clusters, you first need to connect Harness to your cluster.

This topic describes how to connect your Kubernetes cluster to Harness for creating AutoStopping Rules.

In this topic:

* [Before You Begin](k8s-connector-autostopping.md)
* [Review: Kubernetes Coverage](k8s-connector-autostopping.md)
* [Review: Kuberenetes Cluster Connector Options](https://newdocs.helpdocs.io/article/dfwoqnacnw-k8s-connector-autostopping#review_kuberenetes_cluster_connector_options)
* [Connect Your Kubernetes Cluster Connector to CCM for AutoStopping Rules](k8s-connector-autostopping.md)
* [Step 1: Overview](k8s-connector-autostopping.md)
* [Step 2: Select Features](k8s-connector-autostopping.md)
* [Step 3: Create a Secret](k8s-connector-autostopping.md)
* [Step 4: Provide Permissions](k8s-connector-autostopping.md)
* [Next Step](k8s-connector-autostopping.md)

### Before You Begin

Make sure you have the following set up before you create a Kubernetes connector for AutoStopping Rules:

* Ensure that you have access to your Kubernetes cluster.
* Ensure that you've added a cloud provider connector depending on the type of Kubernetes cluster for which you want to create an AutoStopping Rules:  

	+ EKS (AWS): [Create an AWS Connector for AutoStopping Rules](https://newdocs.helpdocs.io/article/hiyi6xvj36-connect-to-an-aws-connector)
	+ AKS (Azure): [Create an Azure Connector for AutoStopping Rules](https://newdocs.helpdocs.io/article/e7yidxmtmj-add-azure-connector)
	+ GKE (GCP): [Create a GCP Connector for AutoStopping Rules](https://newdocs.helpdocs.io/article/cfojlhnf8s-create-a-gcp-connector-for-auto-stopping-rules)

* Ensure that you have added a **Kubernetes Cluster** in **Cloud Providers Connector.** See [Add a Kubernetes Cluster Connector](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector).  
Set up your Kubernetes ClusterYou'll need a target Kubernetes cluster for the Harness Delegate and deployment. Ensure your cluster meets the following requirements:


	+ **Number of nodes:** 2.
	+ **vCPUs, Memory, Disk Size:** 4vCPUs, 16GB memory, 100GB disk.
	+ **Networking:** outbound HTTPS for the Harness connection to **app.harness.io**, **github.com**, and **hub.docker.com**. Allow TCP port 22 for SSH.
	+ A **Kubernetes service account** with permission to create entities in the target namespace is required. The set of permissions should include `list`, `get`, `create`, and `delete` permissions. In general, the cluster-admin permission or namespace admin permission is enough.  
	For more information, see [User-Facing Roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) from Kubernetes.  
Delegate SizeYour Kubernetes cluster must have unallocated resources required to run the Harness Delegate workload:


	+ Laptop - 1.6GB memory, 0.5CPU
	+ Small - 3.3GB memory, 1CPU
	+ Medium - 6.6GB memory, 2CPU
	+ Large - 13.2GB memory, 4CPU**Important:** these sizing requirements are for the Delegate only. Your cluster will require more memory for Kubernetes, the operating system, and other services. Ensure that the cluster has enough memory, storage, and CPU for all of its resource consumers.

* Make sure you are a member of the Harness Administrator Group in the Harness FirstGen version. This is required to [create an API key](k8s-connector-autostopping.md).
* **Metrics Server**: Metrics Server must be running on the Kubernetes cluster where your Harness Kubernetes Delegate is installed. Before enabling CCM for Kubernetes, you must ensure the utilization data for pods and nodes is available.Metrics Server is installed by default on GKE and AKS clusters, however, you need to install it on the AWS EKS cluster.Metrics Server is a cluster-wide aggregator of resource usage data. It collects resource metrics from kubelets and exposes them in the Kubernetes API server through Metrics API. CCM polls the utilization data every minute on the Delegate. The metrics are aggregated for 20 minutes and then CCM keeps one data point per 20 minutes. For more information, see [Installing the Kubernetes Metrics Server](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html) from AWS.  
  
To install a metrics server on your EKS clusters, run the following command:  
  

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.5.0/components.yaml
```

### Review: Kubernetes Coverage

The following section lists the support for Kubernetes clusters for AutoStopping Rules:

* EKS (AWS)
* GKE (GCP)
* AKS (Azure)
* kOps

### Review: Kuberenetes Cluster Connector Setup Options

There are two ways to add a Kubernetes cluster connector:

* **When Setting Up the Connectors**: You can create Connectors from the Account Resources option in the Account Setup. See [Connect Your Kuberenetes Cluster to CCM](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md).
* **When Creating an AutoStopping Rule**: You can also add a Connector inline when creating an AutoStopping Rule. If you've added a Kubernetes Connector already as described in the [Connect Your Kuberenetes Cluster to CCM](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md), you can simply select your Kubernetes Connector for which you want to create AutoStopping Rules. This topic explains how to add a Kuberenetes cluster inline when creating an AutoStopping Rule.  
![](https://files.helpdocs.io/i5nl071jo5/articles/dfwoqnacnw/1648552153026/screenshot-2022-03-29-at-4-38-24-pm.png)

### Connect Your Kubernetes Cluster Connector to CCM for AutoStopping Rules

Perform the following steps to connect your Kubernetes cluster connector inline when creating AutoStopping Rules:

1. In **Cloud Costs**, in **AutoStopping Rules**, click **New AutoStopping Rule**.![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1627917097777/screenshot-2021-08-02-at-8-40-48-pm.png)
2. In **AutoStopping Rules**, select the cloud account. It is the cloud account in which your workloads are running that you want to manage using AutoStopping Rules.  
  
You can select any of the following cloud account types:  
- AWS  
- Azure  
- GCP![](https://files.helpdocs.io/i5nl071jo5/articles/hiyi6xvj36/1633498726320/screenshot-2021-10-06-at-11-08-02-am.png)

1. Click **Connect to your** ***Cloud Account*** drop-down list. The name of the drop-down list depends on the cloud account type selection. For example, if you select AWS, then the label reads as **Connect to your AWS account**.
2. In **Create or Select an Existing Connector** page, select your Conenctor from the list.  
  
If you have not created a cloud provider connector already, click **New Connector**. Refer to the following topics to add your cloud account Connector (depending on the type of cloud account you have selected):  

	* AWS: [Create an AWS Connector for AutoStopping Rules](connect-to-an-aws-connector.md)
	* Azure: [Create an Azure Connector for AutoStopping Rules](add-azure-connector.md)
	* GCP: [Create a GCP Connector for AutoStopping Rules](create-a-gcp-connector-for-auto-stopping-rules.md)  
	![](https://files.helpdocs.io/i5nl071jo5/articles/dfwoqnacnw/1646452284485/screenshot-2022-03-05-at-9-21-07-am.png)
3. Once you've created your cloud account type Connector, select the Connector, and click **Apply Selected**.![](https://files.helpdocs.io/i5nl071jo5/articles/dfwoqnacnw/1646452660948/screenshot-2022-03-05-at-9-27-12-am.png)
4. In **Let's get you started** page, click **Next**.
5. In **Configurations**, in **Define your AutoStopping rule**, in **Name your Rule**, enter a name for your rule. This is the name of your AutoStopping rule.
6. In **Idle time**, enter the idle time in minutes. This is the time that the AutoStopping rule will wait before stopping the idle instances.
7. In **Resources to be managed by the AutoStopping rules** step, select **Kubernetes Cluster** and then click **Add a cluster**.![](https://files.helpdocs.io/i5nl071jo5/articles/dfwoqnacnw/1633588288644/screenshot-2021-10-07-at-12-01-09-pm.png)
8. Click **Create a new connector**.

### Step 1: Overview

1. In **Kubernetes Connector**, in **Overview**, enter the **Name** for your connector. The name will appear in [AutoStopping Dashboard](create-auto-stopping-rules/autostopping-dashboard.md) to identify this cluster.
2. In **Reference an existing connector**, select your Kubernetes cluster connector from the drop-down list. See [Add a Kubernetes Cluster Connector](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector).![](https://files.helpdocs.io/i5nl071jo5/articles/dfwoqnacnw/1633678412639/screenshot-2021-10-08-at-1-03-12-pm.png)
3. Click **Save and Continue**.

### Step 2: Select Features

1. In **Choose Requirements**, select the Cloud Cost Management features that you would like to enable for your Kubernetes clusters. Based on your selection Harness requires specific permissions.  
To create AutoStopping Rules for your Kubernetes connector, ensure that you have selected Cost Visibility and AutoStopping both.![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1627543037017/screenshot-2021-07-29-at-12-45-15-pm.png)You need to provide different permissions depending on the features that you enable for your Kubernetes clusters. CCM offers the following features:  


|  |  |
| --- | --- |
| **Cost Visibility (Required)** | This feature is available by default and provides the following capabilities:
	* Insights into cluster costs by pods, namespace, workloads, etc.
	* Idle and unallocated cluster costs
	* Workload recommendations
	* Root cost analysis using cost perspectives
	* Cost anomaly detection
	* Governance using budgets and forecasts
	* Alert users using Email and Slack notification |
| **Kubernetes optimization using AutoStopping rules (Required for AutoStopping Rules)** | This feature allows you to enable Intelligent Cloud AutoStopping for Kubernetes. For more information, see [Create AutoStopping Rules for AWS](create-auto-stopping-rules/create-autostopping-rules-aws.md).
	* Works for custom resources, EKS, AKS, GKE, etc.
	* Orchestrate VMs based on idleness
	* Provides granular savings visibility |
2. Click **Continue**.

### Step 3: Create a Secret

The secret creation settings appear only if you have selected **Kubernetes Optimization by AutoStopping** feature in the **Feature Selection** step. In this step, you are providing permissions for intelligent cloud AutoStopping rules. For more information, see [Create AutoStopping Rules for Kubernetes](create-auto-stopping-rules/create-autostopping-rules-for-kubernetes.md).

1. In **Secret creation**, click create an API key here and create an API key. See [Create an API Key](https://docs.harness.io/article/smloyragsm-api-keys).You must be logged into the Harness FirstGen version as a member of the Administrators User Group to create an API key. For details about Harness' role-based access control, see [Managing Users and Groups (RBAC)](https://docs.harness.io/article/ven0bvulsj-users-and-permissions).
2. Run the following commands in your Kubernetes cluster:
	1. Create a namespace.  
	
	```
	kubectl create namespace harness-autostopping
	```
	2. In the following YAML, add the API token that you created (in step 1) and run the command in your K8s cluster.  
	
	```
	apiVersion: v1  
	data:  
	    token: <*paste token here*>  
	kind: Secret  
	metadata:  
	    name: harness-api-key  
	    namespace: harness-autostopping  
	type: Opaque
	```
	3. Run the following command:  
	
	```
	kubectl apply -f secret.yaml
	```
3. Click **Continue**.

### Step 4: Provide Permissions

1. In **Provide Permissions**, click **Download YAML**.
2. Copy the downloaded YAML to a machine where you have `kubectl`installed and have access to your Kubernetes cluster.
3. Run the following command to apply the Harness Delegate to your Kubernetes Cluster.  

```
kubectl apply -f ccm-kubernetes.yaml
```
4. Click **Done** and **Continue**.
5. In **Verify connection**, once the Test Connection succeeds, click **Finish**.  
  
The Connector is now listed in **Connectors**.

### Next Step

* [Create AutoStopping Rules for a Kubernetes Cluster](create-auto-stopping-rules/create-autostopping-rules-for-kubernetes.md)

