---
title: Set Up Cloud Cost Management for Kubernetes
description: This topic describes how to connect your Kubernetes cluster to CCM.
tags: 
   - helpDocs
   - cloud cost management
   - kubernetes
helpdocs_topic_id: ltt65r6k39
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Cloud Cost Management (CCM) monitors the cloud costs of your Kubernetes clusters, namespaces, nodes, workloads, and labels. CCM also allows you to optimize your Kubernetes cluster resources using intelligent cloud AutoStopping rules.

You need to provide different permissions depending on the features that you enable for your Kubernetes clusters. CCM offers the following features:



|  |  |
| --- | --- |
| **Cost Visibility (Required)** | This feature is available by default and provides the following capabilities:* Insights into cluster costs by pods, namespace, workloads, etc.
* Idle and unallocated cluster costs
* Workload recommendations
* Root cost analysis using cost perspectives
* Cost anomaly detection
* Governance using budgets and forecasts
* Alert users using Email and Slack notification

For [AWS](set-up-cost-visibility-for-aws.md) and [Azure](set-up-cost-visibility-for-azure.md) if the cloud connectors are set up, then the cost will be trued-up to the pricing received from the CUR/billing export. However, for [GCP](set-up-cost-visibility-for-gcp.md) the list pricing is used. |
| **Kubernetes optimization using AutoStopping rules (Optional)** | This feature allows you to enable Intelligent Cloud AutoStopping for Kubernetes. For more information, see [Create AutoStopping Rules for AWS](../add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).* Works for custom resources, EKS, AKS, GKE, etc.
* Orchestrate VMs based on idleness
* Provides granular savings visibility
 |

This topic describes how to connect your Kubernetes cluster to CCM. 

Once you enable CCM, for the first cluster the data is available within a few minutes for viewing and analysis. However, you will not see the idle cost because of the lack of utilization data. CCM generates the last 30 days of the cost data based on the first events. From the second cluster onwards, it takes about 2–3 hours for the data to be available for viewing and analysis.  
  
  
If you are using an EKS connector, the data generation is delayed. AWS ingests data at the source (S3 bucket) four times a day. CCM takes about two hours to make the data available for viewing and analysis once it is available at the source.In this topic:

* [Review: Kubernetes Connector Requirements and Workflow](set-up-cost-visibility-for-kubernetes.md)
* [Visual Summary](set-up-cost-visibility-for-kubernetes.md)
* [Prerequisites](set-up-cost-visibility-for-kubernetes.md)
* [Step: Connect Your Kubernetes Cluster to CCM](set-up-cost-visibility-for-kubernetes.md)
	+ [Step 1: Overview](set-up-cost-visibility-for-kubernetes.md)
	+ [Step 2: Feature Selection](set-up-cost-visibility-for-kubernetes.md)
	+ [(Optional) Step 3: Create a Secret](set-up-cost-visibility-for-kubernetes.md)
	+ [Step 4: Provide Permissions](set-up-cost-visibility-for-kubernetes.md)
* [Next Steps](set-up-cost-visibility-for-kubernetes.md)

### Review: Kubernetes Connector Requirements and Workflow

For CCM, Kubernetes connectors are available only at the Account level in Harness. To set up the CCM K8s Connector, you need to create the following:

1. **Cloud Provider Kubernetes Connector**. You need to create a Kubernetes Cloud Provider Connector for each Kubernetes cluster. One connector can access only one cluster. See [Add a Kubernetes Cluster Connector](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector).  
  
If you have already created a Cloud Provider Connector, you may reference the same connector in the CCM and create a connector for CCM.
	1. **Harness Delegate**. You need to set up Harness Delegate for each Cloud Provider (K8s cluster) connector. Delegate is installed when adding a Connector. See [Install a Kubernetes Delegate](https://docs.harness.io/article/f9bd10b3nj-install-a-kubernetes-delegate). Delegate is responsible for collecting metrics from the K8s connector.
2. **CCM Connector**. For the CCM Kubernetes connector, you need to first create a [Cloud Provider K8s Connector](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector) and then create a K8s Cloud Cost Management Connector. You simply create a CCM Connector Reference to Cloud Provider Kubernetes Connector.
	* Create a CCM Connector Reference to Cloud Provider Kubernetes Connector
	* For each cluster, you need to create a CCM Kubernetes connector.CCM can now connect to the K8s connector and collect CCM metrics for deep cloud cost visibility.

In Harness, the ratio of Delegates to Connectors is 1:2. If you have 20 clusters you will need 20 Delegates and 40 Connectors (1 Cloud Provider K8s Connector and 1 CCM Connector each).  
  
  
Alternatively, if you wish to use a single Delegate to access multiple Kubernetes clusters, you need to specify the Kubernetes master node URL. See [Master URL](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector#step_2_enter_credentials).### Visual Summary

Here's a visual representation of the CCM Kubernetes connector requirements and workflow:

![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1638960162116/image-16.png)### Prerequisites

Make sure you have the following set up before you create a Kubernetes connector for CCM:

* Ensure that you have access to your Kubernetes cluster.

* Ensure that you have added a **Kubernetes Cluster** in **Cloud Providers Connector.** See [Add a Kubernetes Cluster Connector](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector) and also [review Kubernetes Connector Requirements and workflow](set-up-cost-visibility-for-kubernetes.md).  
Set up your Kubernetes ClusterYou'll need a target Kubernetes cluster for the Harness Delegate and deployment. Ensure your cluster meets the following requirements:


	+ **Number of nodes:** 2.
	+ **vCPUs, Memory, Disk Size:** 4vCPUs, 16GB memory, 100GB disk. In GKE, the **e2-standard-4** machine type is enough for this quickstart.
	+ **Networking:** outbound HTTPS for the Harness connection to **app.harness.io**, **github.com**, and **hub.docker.com**. Allow TCP port 22 for SSH.
	+ A **Kubernetes service account** with permission to create entities in the target namespace is required. The set of permissions should include `list`, `get`, `create`, and `delete` permissions. In general, the cluster-admin permission or namespace admin permission is enough.  
	For more information, see [User-Facing Roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) from Kubernetes.  
  
Delegate SizeYour Kubernetes cluster must have unallocated resources required to run the Harness Delegate workload:


	+ Laptop - 1.6GB memory, 0.5CPU
	+ Small - 3.3GB memory, 1CPU
	+ Medium - 6.6GB memory, 2CPU
	+ Large - 13.2GB memory, 4CPU**Important:** these sizing requirements are for the Delegate only. Your cluster will require more memory for Kubernetes, the operating system, and other services. Ensure that the cluster has enough memory, storage, and CPU for all of its resource consumers.  
Delegate PermissionsYou can choose one of the following permissions for CCM:

**Install Delegate with cluster-wide read/write access**

Creates a new namespace called "harness-delegate-ng" with the service account bound to Cluster Admin role. This Delegate will be able to read tasks (capture change events etc., needed for Harness Cloud Cost Management) anywhere on the K8s cluster where the Delegate is installed.

**Install Delegate with cluster-wide read access**

(Requires read-only Cluster Admin role) Creates a new namespace called "harness-delegate-ng" with the service account bound to Cluster Admin role. This Delegate will be able to perform read-only tasks (capture change events etc., needed for Harness Cloud Cost Management) anywhere on the K8s cluster where the Delegate is installed.

* **Metrics Server**: Metrics Server must be running on the Kubernetes cluster where your Harness Kubernetes Delegate is installed. Before enabling CCM for Kubernetes, you must ensure the utilization data for pods and nodes is available.  
Metrics Server is installed by default on GKE and AKS clusters, however, you need to install it on the AWS EKS cluster.Metrics Server is a cluster-wide aggregator of resource usage data. It collects resource metrics from kubelets and exposes them in the Kubernetes API server through Metrics API. CCM polls the utilization data every minute on the Delegate. The metrics are aggregated for 20 minutes and then CCM keeps one data point per 20 minutes. For more information, see [Installing the Kubernetes Metrics Server](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html) from AWS.  
  
To install metrics server on your EKS clusters, run the following command:  
  

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.5.0/components.yaml  

```

### Step: Connect Your Kubernetes Cluster to CCM

Perform the following steps to connect your Kubernetes cluster to CCM.

#### Step 1: Overview

1. In Harness, click **Account Setup**.
2. In **Account Setup**, in **Account Resources**, click **Connectors**.![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1630563523009/screenshot-2021-09-02-at-11-22-27-am.png)
3. In **Connectors**, click **+ Connector**.
4. In **Cloud Costs**, click **Kubernetes**.![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1625556708941/screenshot-2021-07-06-at-1-01-31-pm.png)
5. In **Kubernetes Connector**, in **Overview**, from the **Reference an existing connector** drop-down list, select your Cloud Provider Kubernetes Connector.
	1. If you do not have Cloud Provider Kubernetes Connector already created, click **Create a new connector**. See [Add a Kubernetes Cluster Connector](https://docs.harness.io/article/1gaud2efd4-add-a-kubernetes-cluster-connector) and also [review Kubernetes Connector Requirements and workflow](set-up-cost-visibility-for-kubernetes.md).
6. The **Name** for your connector is automatically populated. You can choose to edit the name. The name will appear in the Perspectives to identify this cluster.![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1642010369558/screenshot-2022-01-12-at-11-29-02-pm.png)
7. Click **Save and Continue**.

#### Step 2: Feature Selection

In **Choose Requirements**, select the Cloud Cost Management features that you would like to enable for your Kubernetes clusters. Based on your selection Harness requires specific permissions.

![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1627543037017/screenshot-2021-07-29-at-12-45-15-pm.png)You need to provide different permissions depending on the features that you enable for your Kubernetes clusters. CCM offers the following features:



|  |  |
| --- | --- |
| **Cost Visibility (Required)** | This feature is available by default and provides the following capabilities:* Insights into cluster costs by pods, namespace, workloads, etc.
* Idle and unallocated cluster costs
* Workload recommendations
* Root cost analysis using cost perspectives
* Cost anomaly detection
* Governance using budgets and forecasts
* Alert users using Email and Slack notification
 |
| **Kubernetes optimization using AutoStopping rules (Optional)** | This feature allows you to enable Intelligent Cloud AutoStopping for Kubernetes. For more information, see [Create AutoStopping Rules for AWS](../add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).* Works for custom resources, EKS, AKS, GKE, etc.
* Orchestrate VMs based on idleness
* Provides granular savings visibility
 |

Make your selection and click **Continue**.

#### (Optional) Step 3: Create a Secret

The secret creation settings appear only if you have selected **Kubernetes Optimization by AutoStopping** feature in the **Feature Selection** step. In this step, you are providing permissions for intelligent cloud AutoStopping rules. For more information, see [Create AutoStopping Rules for AWS](../add-connectors/create-auto-stopping-rules/create-autostopping-rules-aws.md).

1. In **Secret creation**, click create an API key here and create an API key. See [Create an API Key](https://docs.harness.io/article/tdoad7xrh9-add-and-manage-api-keys).
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

#### Step 4: Provide Permissions

If the cluster does not already have additional permissions, you will apply them in this step. See Delegate Permissions in the [Prerequisites](set-up-cost-visibility-for-kubernetes.md) for additional details.

1. In **Provide Permissions**, click **Download YAML**.
2. Copy the downloaded YAML to a machine where you have `kubectl`installed and have access to your Kubernetes cluster.
3. Run the following command to apply the Harness Delegate permissions to your Kubernetes Cluster.  
  

```
$ kubectl apply -f ccm-kubernetes.yaml
```
4. Click **Done** and **Continue**.
5. In **Verify connection**, once the Test Connection succeeds, click **Finish**.  
  
The Connector is now listed in **Connectors**.![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1627494459373/screenshot-2021-07-28-at-11-14-46-pm.png)

### Troubleshooting

In **Verify connection** step if you get `few of the visibility permissions are missing` error message, you need to review the CCM permissions required for Harness Delegate.

![](https://files.helpdocs.io/i5nl071jo5/articles/ltt65r6k39/1638981660952/screenshot-2021-12-08-at-10-07-55-pm.png)Verify that you have all the required permissions for the Service account using the following commands:


```
kubectl auth can-i watch pods   
--as=system:serviceaccount:<your-namespace>:<your-service-account>   
--all-namespaces  
kubectl auth can-i watch nodes   
--as=system:serviceaccount:<your-namespace>:<your-service-account>   
--all-namespaces
```

```
  
kubectl auth can-i get nodemetrics   
--as=system:serviceaccount:<your-namespace>:<your-service-account>   
--all-namespaces  
kubectl auth can-i get podmetrics   
--as=system:serviceaccount:<your-namespace>:<your-service-account>   
--all-namespaces
```
Here is an example showing the commands and output using the default Delegate Service account name and namespace:


```
$ kubectl auth can-i watch pods --as=system:serviceaccount:harness-delegate:default --all-namespaces  
yes  
$ kubectl auth can-i watch nodes --as=system:serviceaccount:harness-delegate:default --all-namespaces                                                                      
yes  
$ kubectl auth can-i watch nodemetrics --as=system:serviceaccount:harness-delegate:default --all-namespaces                                                                
yes  
$ kubectl auth can-i watch podmetrics --as=system:serviceaccount:harness-delegate:default --all-namespaces   
yes
```
### Next Steps

* [Optimize Cloud Costs with AutoStopping Rules]**TODO:** Update category link **TODO:** Update category link **TODO:** Update category link (/category/e04ek5vxtx-optimize-cloud-costs-with-intelligent-cloud-auto-stopping-rules)
* [Root Cost Analysis]**TODO:** Update category link **TODO:** Update category link **TODO:** Update category link (/category/jkwta6oexk-root-cost-analysis)
* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

