---
title: Delegate Requirements and Limitations
description: This topic lists the limitations and requirements of the Harness Delegate. Before You Begin. Delegates Overview. Delegate Limitations. Deployment limits --  Deployment limits are set by account type.. Y…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: k7sbhe419w
helpdocs_category_id: c3plipcrqq
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic lists the limitations and requirements of the Harness Delegate.

### Before You Begin

* [Delegates Overview](/article/2k7lnc7lvl-delegates-overview)

### Delegate Limitations

* **Deployment limits:** Deployment limits are set by account type**.**
* You might need to install multiple Delegates depending on how many Continuous Delivery tasks you do concurrently, and on the compute resources you are providing to each Delegate. Typically, you will need one Delegate for every 300-500 service instances across your applications.  
A service instance is when you use Harness to deploy the underlying infrastructure for the instance.  
For example, an instance of a Kubernetes workload where Harness creates the pods, or an instance of an ECS task where Harness creates the service for the task.

### System Requirements

The Delegate is installed in your network and connects to the Harness Manager.

One Delegate size does not fit all use cases, so Harness let's you pick from several options:

![](https://files.helpdocs.io/i5nl071jo5/articles/2k7lnc7lvl/1625084105662/clean-shot-2021-06-30-at-13-14-58.png)Remember that the memory and CPU requirements are for the Delegate only. You Delegate host/pod/container will need more computing resources for its operations systems and other services such as Docker or Kubernetes.

The Delegate runs on a Linux/UNIX server or container.

Ensure that you provide the minimum memory for the Delegate and enough memory for the host/node system. For example, an AWS EC2 instance type such as m5a.xlarge has 16GB of RAM, 8 for the Delegate and 8 for the remaining operations.

The ​Shell Script Delegate requires cURL 7.64.1 or later.

Access to artifact servers, deployment environments, and cloud providers. As shown in the following illustration:

![](https://files.helpdocs.io/i5nl071jo5/articles/k7sbhe419w/1625096729943/image.png)### Allowlist Harness Domains and IPs

Harness SaaS Delegates only need outbound access to the Harness domain name (most commonly, **app.harness.io)** and, optionally, to **logging.googleapis.com**. The URL logging.googleapis.com is used to provide logs to Harness support.

See [Allowlist Harness Domains and IPs](/article/ooelo06uy5-whitelist-harness-domains-and-ips).

### Network Requirements

The following network requirements are for connectivity between the Harness Delegate you run in your network and the **Harness Manager** (SaaS or On-Prem), and for your browser connection to the Harness Manager.

All network connections from your local network to Harness SaaS are outbound-only.* HTTPS port 443 outbound from the Delegate to Harness.
* HTTP/2 for gRPC (gRPC Remote Procedure Calls)
* Delegate requirements: The Delegate will need API/SSH/HTTP access to the providers you add to Harness, such as:
	+ Cloud Providers.
	+ Verification Providers.
	+ Artifact Servers (repos).
	+ Source repositories.
	+ Collaboration Providers.
	+ SSH access to target physical and virtual servers.

#### gRPC Limitations

If you do not enable gRPC connections, the following limitations apply:

* [Cloud Cost Management (CCM)](/category/exgoemqhji-ccm) will not collect events.
* If the `ARTIFACT_PERPETUAL_TASK` feature flag is enabled in your account, Harness performs perpetual artifact collection. If you do not enable gRPC connections, this will not work.

Contact [Harness Support](mailto:support@harness.io) to enable or disable feature flags.### Permissions and Ports

See [Permissions and Ports for Harness Connections](/article/ga1155j91x-permissions-and-ports-for-harness-connections).

### Add Certificates and Other Software to Delegate

For steps on adding certs or other software to the Delegate, see [Common Delegate Initialization Scripts](/article/auveebqv37-common-delegate-profile-scripts).

### Delegate Access Requirements

* The Harness Delegate does NOT require root account access, but the Kubernetes and Docker Delegates run as root by default. If you do not need to install applications using Delegate Profiles, then you can use a non-root account or install the application without the Delegate.  
See [Non-Root Delegate Installation](/article/h2kydm6qme-non-root-delegate-installation).
* If you do not run the Delegate as root, be aware that you cannot install any software using a [Delegate Initialization Script](/article/auveebqv37-common-delegate-profile-scripts).

