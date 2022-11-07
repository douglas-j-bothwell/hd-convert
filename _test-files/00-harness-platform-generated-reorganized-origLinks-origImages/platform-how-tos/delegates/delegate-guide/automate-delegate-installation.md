---
title: Automate delegate lnstallation
description: Automate Delegate installation and registration.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: 9deaame3qz
helpdocs_category_id: m9iau0y3hv
helpdocs_is_private: false
helpdocs_is_published: true
---

You can automate Delegate installation and registration by duplicating the downloaded Delegate config file, renaming the Delegate, and applying the new file. You can script this process to duplicate Delegates as needed.

When you apply the new Delegate file it will register with Harness under the new name.

This topic will describe how to duplicate, rename, and register a new Delegate manually, but you will likely want to script this process.

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#before_you_begin)
* [Review: Automation and High Availability (HA)](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#review_automation_and_high_availability_ha)
* [Limitations](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#limitations)
* [Step 1: Duplicate the Delegate Config File](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#step_1_duplicate_the_delegate_config_file)
* [Step 2: Rename the New Delegate](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#step_2_rename_the_new_delegate)
	+ [Kubernetes Delegate Renaming](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#kubernetes_delegate_renaming)
	+ [Docker Delegate Renaming](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#docker_delegate_renaming)
* [Step 3: Install the New Delegate](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#step_3_install_the_new_delegate)
* [See Also](https://ngdocs.harness.io/article/9deaame3qz-automate-delegate-installation#see_also)

### Before You Begin

* [Delegates Overview](/article/2k7lnc7lvl-delegates-overview)
* [Install a Kubernetes Delegate](/article/f9bd10b3nj-install-a-kubernetes-delegate)
* [Install the Harness Docker Delegate](/article/cya29w2b99-install-a-docker-delegate)

### Review: Automation and High Availability (HA)

Delegate Automation isn't required for all High Availability (HA) scenarios. Let's review Delegate HA and when automation might be beneficial.

You might need to install multiple Delegates depending on how many tasks you do concurrently, and on the compute resources you are providing to each Delegate. Typically, you will need one Delegate for every 300-500 service instances.

In addition to compute considerations, you can enable High Availability (HA) for Harness Delegates. HA simply involves installing multiple Delegates in your environment.

For example, in Kubernetes deployments, you can set up two Kubernetes Delegates, each in its own pod in the same target K8s cluster. Simply edit the Kubernetes Delegate spec you download from Harness, **harness-kubernetes.yaml**, to have multiple `replicas`:


```
...  
apiVersion: apps/v1beta1  
kind: StatefulSet  
metadata:  
  labels:  
    harness.io/app: harness-delegate  
    harness.io/account: xxxx  
    harness.io/name: test  
  name: test-zeaakf  
  namespace: harness-delegate  
spec:  
  replicas: 2  
  selector:  
    matchLabels:  
      harness.io/app: harness-delegate  
...
```
In this case, you do not need automation. Simply adding more `replicas` will accomplish HA.

For the Kubernetes Delegate, you only need one Delegate in the cluster. Simply increase the number of replicas, and nothing else. Do not add another Delegate to the cluster in an attempt to achieve HA.If you want to install Kubernetes Delegates in separate clusters, do not use the same **harness-kubernetes.yaml** and name for both Delegates. Download a new Kubernetes YAML spec from Harness for each Delegate you want to install. This will avoid name conflicts.In every case, the Delegates need to be identical in terms of permissions, keys, connectivity, etc.With two or more Delegates running in the same target environment, HA is provided by default. One Delegate can go down without impacting Harness' ability to perform deployments. If you want more availability, you can set up three Delegates to handle the loss of two Delegates, and so on.

### Limitations

* Two Delegates in different locations with different connectivity do not support HA. For example, if you have a Delegate in a Dev environment and another in a Prod environment, the Dev Delegate will not communicate with the Prod Delegate or vice versa. If either Delegate went down, Harness would not operate in their environment.

### Step 1: Duplicate the Delegate Config File

These steps assume you have already installed and registered a Delegate. If you haven't, see the [Delegate installation topics](/category/9i5thr0ot2).Duplicate the config file for a Delegate you have installed and registered with your Harness account.

Ensure that the Delegate environment variables are set correctly.

The Delegate config file contains environment variables for account, Organization, and Project. The account variable is always set with your Harness account Id.

If your Delegate is registered at the account level, then the Organization and Project variables will be empty. If your Delegate is registered at the Organization level, then the Project variable will be empty. 

If your Delegate config file uses other environment variables, review them to make certain that you want them duplicated. 

The Delegate Environment Variables are described in the relevant Delegate installation topics.### Step 2: Rename the New Delegate

How you rename the Delegate depends on the type of Delegate. For Docker Delegates, you simply rename one environment variable in the Docker compose file.

For the Kubernetes Delegate, you need to multiple instances of the name.

#### Kubernetes Delegate Renaming

In the Kubernetes Delegate config file, several labels must be updated:

* `Secret.metadata.name`
* `StatefulSet.metadata.labels.harness.io/name`
* `StatefulSet.metadata.name`
* `StatefulSet.metadata.spec.selector.matchLabels.harness.io/name`
* `StatefulSet.metadata.spec.template.metadata.labels.harness.io/name`
* `StatefulSet.metadata.spec.template.spec.env.name: DELEGATE_NAME`

The `DELEGATE_NAME` environment variable looks like this:


```
...  
        - name: DELEGATE_NAME  
          value: foo  
...
```
#### Docker Delegate Renaming

To rename the Docker Delegate, simply rename the value for the `DELEGATE_NAME` environment variable.


```
...  
    - DELEGATE_NAME=my-new-delegate  
...
```
### Step 3: Install the New Delegate

Once the name(s) in the Delegate are updated, you can apply the Delegate and it will install and register with Harness.

### See Also

* [Run Scripts on Delegates](/article/yte6x6cyhn-run-scripts-on-delegates)

