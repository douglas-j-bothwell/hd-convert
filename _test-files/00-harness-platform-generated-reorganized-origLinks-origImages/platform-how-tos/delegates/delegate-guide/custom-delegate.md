---
title: Create a custom delegate that Includes custom tools
description: Create your own custom Delegate and include the tools needed for your builds and deployments.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: nbi9uj9wm4
helpdocs_category_id: m9iau0y3hv
helpdocs_is_private: false
helpdocs_is_published: true
---

[Harness Delegates](/article/2k7lnc7lvl-delegates-overview) are installed from the Harness Manager and typically contain the binaries you need for your CI/CD Pipelines.

In some cases, you might want to add more tools or even create your own custom Delegate and include the tools needed for your builds and deployments.

This topic explains the different ways to create a custom Delegate.

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/nbi9uj9wm4-custom-delegate#before_you_begin)
* [Option: Use INIT\_SCRIPT Environment Variable](https://ngdocs.harness.io/article/nbi9uj9wm4-custom-delegate#option_use_init_script_environment_variable)
* [Option: Add a Delegate Image](https://ngdocs.harness.io/article/nbi9uj9wm4-custom-delegate#option_add_a_delegate_image)
* [See Also](https://ngdocs.harness.io/article/nbi9uj9wm4-custom-delegate#see_also)

### Before you begin

* [Delegates Overview](/article/2k7lnc7lvl-delegates-overview)
* [Supported Platforms and Technologies](/article/1e536z41av-supported-platforms-and-technologies)
* [Delegate Installation Overview](/article/re8kk0ex4k-delegate-installation-overview)

### Option: Use the INIT\_SCRIPT environment variable

In the Delegate config file, locate the `INIT_SCRIPT` environment variable.

For example, here it is in the Kubernetes Delegate harness-delegate.yaml file:


```
...  
apiVersion: apps/v1  
kind: StatefulSet  
...  
spec:  
...  
    spec:  
    ...  
        env:  
        ...  
        - name: INIT_SCRIPT  
          value: |-  
            echo install wget  
            apt-get install wget  
            echo wget installed  
...
```
In `value`, enter your script. For a list of common scripts, see [Common Delegate Initialization Scripts](https://newdocs.helpdocs.io/article/auveebqv37-common-delegate-profile-scripts).

For steps on using the `INIT_SCRIPT` environment variable, see [Run Scripts on Delegates](/article/yte6x6cyhn-run-scripts-on-delegates).

You can see all of the environment variables for the Delegates in the following topics:

* [Install a Kubernetes Delegate](/article/f9bd10b3nj-install-a-kubernetes-delegate)
* [Install a Docker Delegate](/article/cya29w2b99-install-a-docker-delegate)

### Option: Add a delegate image

Harness Delegate Docker images are public and you can use them to compose your own Delegate image.

The Harness Delegate Docker images are located on [Docker Hub](https://hub.docker.com/r/harness/delegate/tags).

For example, you can curl and install all the tool libraries you want and then curl `delegate:latest` to add the latest Delegate image.

Or you can create your own image and simply include the Delegate image.

Here's and example that installs Node.JS on top of a Delegate image and sets an environment variable key:value pair.


```
...  
FROM harness/delegate:latest  
  
RUN apt-get update && apt-get -y install nodejs  
  
ENV key=value  
...
```
You can see all of the environment variables for the Delegates in the following topics:

* [Install a Kubernetes Delegate](/article/f9bd10b3nj-install-a-kubernetes-delegate)
* [Install a Docker Delegate](/article/cya29w2b99-install-a-docker-delegate)

### See also

* [Delegate How-tos](/category/9i5thr0ot2-delegates).

