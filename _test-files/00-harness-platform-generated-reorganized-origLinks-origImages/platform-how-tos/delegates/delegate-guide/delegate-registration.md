---
title: Delegate Registration and Verification
description: To set up a Harness Delegate, you install the Delegate in your environment and the Delegate automatically registers with your Harness account. The Delegate config file (for example, Kubernetes Delega…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: 39tx85rekj
helpdocs_category_id: m9iau0y3hv
helpdocs_is_private: false
helpdocs_is_published: true
---

To set up a Harness Delegate, you install the Delegate in your environment and the Delegate automatically registers with your Harness account.

The Delegate config file (for example, Kubernetes Delegate YAML file) contains your Harness account Id. That's how the Delegate knows where to register.

### Installing and Registering Delegates

To install a Delegate, follow the steps in the relevant Delegate installation topic, such as [Install a Kubernetes Delegate](/article/f9bd10b3nj-install-a-kubernetes-delegate) or [Install a Docker Delegate](/article/cya29w2b99-install-a-docker-delegate).

Once you have installed the Delegate in your environment, click **Verify** in the Delegate wizard and Harness will verify that it is receiving heartbeats from the Delegate.

![](https://files.helpdocs.io/i5nl071jo5/articles/39tx85rekj/1645743199994/clean-shot-2022-02-24-at-14-53-07-2-x.png)This means Harness is waiting for the Delegate you installed to register.

Registration can take a few minutes. 

Once the Delegate registers, the **Verify** screen will indicate that the Delegate is running.

### Verifying Delegate Registration Manually

The Verify screen also includes troubleshooting steps. 

Here are a few of the steps for the Kubernetes Delegate.

Check the status of the Delegate on your cluster:


```
kubectl describe pod <your-delegate-pod> -n harness-delegate
```
Check the Delegate logs:


```
kubectl logs -f <harness-delegate> -n harness-delegate
```
If the pod isn't up, you might see the following error in your cluster:


```
CrashLoopBackOff: Kubernetes Cluster Resources are not available.
```
Make sure the Kubernetes Cluster Resources (CPU, Memory) are enough.

If the Delegate didn’t reach a healthy state, try this:


```
kubectl describe pod <your-delegate-pod> -n harness-delegate
```
