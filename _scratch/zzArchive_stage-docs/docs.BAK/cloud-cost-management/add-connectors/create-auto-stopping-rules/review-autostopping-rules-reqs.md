---
title: Review AutoStopping Rules Requirements
description: This topic covers the requirements for creating AutoStopping Rules on all supported cloud platforms.
tags: 
   - helpDocs
   - Autostopping rules
   - prerequisites
   - ec2 vms
   - auto scaling groups
   - AWS
   - kubernetes
helpdocs_topic_id: hlbi19ol2o
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic covers the requirements for creating [AutoStopping Rules](../auto-stopping-rules.md) on all supported cloud platforms. Before you begin creating AutoStopping Rules, make sure you've reviewed the following:

* Prerequisites
* Questionnaire about your cloud setup and resources

### AWS: EC2 VMs and Auto Scaling Groups

Review the following prerequisites and set up related questions.

#### Prerequisites

The following prerequisites are needed:

* Ensure that you have AWS EC2 VMs or Auto Scaling Groups created
* Ensure that you have access to CUR. See [Review: Cost and Usage Reports (CUR) and CCM Requirements](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Permissions to create a cross-account role. See [AWS Access Permissions](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)

#### Questionnaire



|  |
| --- |
| How are the VMs accessed?1. DNS link
2. SSH
3. RDP
 |
| What is the protocol used for accessing these VMs?1. HTTP/HTTPS
2. TCP (SSH, RDP, etc.)
 |
| Do you use a load balancer like ALB for non-prod workloads? |
| Do you use Route53 to manage DNS? |
| What is the life cycle of these VMS?1. Short-lived and dynamically created (ephemeral instances, created via deployment scripts, etc..)
2. Long-lived static environments
 |
| Do you use AWS Gov Cloud? |
| Are these VMs shut down during non-working hours? |
| Do you use Reserved instances for non-prod workloads? |
| Do you use Spot instances? |
| What is the platform type that you use?1. Windows
2. Linux
 |
| How many developers access the instances? |
| What is the number of instances? |

### Amazon ECS

Review the following prerequisites.

#### Prerequisites

The following prerequisites are needed:

* Access to CUR. See [Review: Cost and Usage Reports (CUR) and CCM Requirements](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Permissions to create a cross-account role. See [AWS Access Permissions](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Permissions for AWS ECS and Resource Inventory Management. See [AWS ECS and Resource Inventory Management](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* Permissions for AWS Resource Optimization Using AutoStopping Rules. See [AWS Resource Optimization Using AutoStopping Rules](../../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* HTTP/HTTPS-based applications running on ECS
* ECS running on EC2 nodes or Fargate

### Azure

Review the following prerequisites and set up related questions.

#### Prerequisites

The following prerequisites are needed:

* Ensure that you have Azure on-demand VMs created
* Make sure that you have the **Application Administrator** role assigned for your Azure AD. Users in this role can create and manage all aspects of enterprise applications, application registrations, and application proxy settings. See [Application Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#application-administrator)
* Many Azure CLI commands act within a subscription. Ensure that you have selected the right subscription before executing the commands. If you need to switch the subscription, use the following command:  
`az account set -s <`*`subs id/name`*`>`  
For more information, see [Manage Subscriptions](https://docs.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)
* Permissions to create an application gateway:
	+ A dedicated subnet with no other resources
	+ A public IP belonging to the same VPN as the application gateway
		- SKU: Basic for V1 Application gateway and Standard for V2 application gateway
		- Type: Static or Dynamic
* Permissions to create Azure function and a dedicated storage account
* SSL certificate in **\*.pfx** format to support HTTPS traffic if required. You can use a wild card certificate or specific to the domain certificate

#### Questionnaire



|  |
| --- |
| How are the VMs accessed?1. DNS link
2. SSH
3. RDP
 |
| What is the protocol used for accessing these VMs?1. HTTP/HTTPS
2. TCP (SSH, RDP, etc.)
 |
| Do you use an ApplicationGateway or WAF for non-prod workloads?  |
| Are the VMs publicly accessible? |
| What DNS provider do you currently use? |
| What is the life cycle of these VMS?1. Short-lived and dynamically created (ephemeral instances, created via deployment scripts, etc..)
2. Long-lived static environments
 |
| Are these VMs shut down during non-working hours? |
| Do you use Reserved Instances for non-prod workloads? |
| Do you use Spot instances? |
| What is the platform type that you use?1. Windows
2. Linux
 |
| How many developers access the instances? |
| What is the number of instances? |

### Kubernetes Clusters

Review the following prerequisites and set up related questions.

#### Prerequisites

The following prerequisites are needed:

* Ingress controller installed. For example, Nginx, Istio, Kong, etc.
* Ensure that you have Cluster Autoscaler enabled for EKS with managed node groups
* For EKS:
	+ Ensure that you have access to (Cost Usage Report) CUR. See [Review: Cost and Usage Reports (CUR) and CCM Requirements](https://newdocs.helpdocs.io/article/80vbt5jv0q-set-up-cost-visibility-for-aws#review_cost_and_usage_reports_cur_and_ccm_requirements)
	+ Permissions to create a cross-account role. See [AWS Access Permissions](https://newdocs.helpdocs.io/article/80vbt5jv0q-set-up-cost-visibility-for-aws#aws_resource_optimization_using_auto_stopping_rules)

#### Questionnaire



|  |
| --- |
| What is the Kubernetes version? |
| Do you use Fargate on Kubernetes? |
| Do you have Cluster Autoscaler? |
| Do you use Helm to install your apps? |
| Do you use an ingress controller? If yes, which one? |
| Do you use end-to-end TLS for your Kubernetes workloads or does the TLS get terminated at the ingress controller? |

### Google Cloud Platform (GCP)

Review the following prerequisites and set up related questions.

#### Prerequisites

The following prerequisites are needed:

#### Questionnaire



|  |
| --- |
| How are the VMs accessed?1. DNS link
2. SSH
3. RDP
 |
| What is the protocol used for accessing these VMs?1. HTTP/HTTPS
2. TCP (SSH, RDP, etc.)
 |
| Are the VMs publicly accessible? |
| What DNS provider do you currently use? |
| What is the life cycle of these VMS?1. Short-lived and dynamically created (ephemeral instances, created via deployment scripts, etc..)
2. Long-lived static environments
 |
| Are these VMs shut down during non-working hours? |
| Do you use Reserved Instances for non-prod workloads? |
| Do you use preemptible (spot) VM instances? |
| What is the platform type that you use?1. Windows
2. Linux
 |
| How many developers access the instances? |
| What is the number of instances? |

### Next Steps

* [AutoStopping Rules]**TODO:** Update category link **TODO:** Update category link **TODO:** Update category link **TODO:** Update category link (/category/biypfy9p1i-create-auto-stopping-rules)

