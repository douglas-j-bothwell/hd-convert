---
title: Configure Service Dependency Step Settings
description: A Service Dependency is a detached service that's accessible to all Steps in a Stage. Service dependencies support workflows such as Integration testing&#58; You can set up a service and then run tests a…
tags: 
   - helpDocs
helpdocs_topic_id: vo4sjbd09g
helpdocs_is_private: false
helpdocs_is_published: true
---

A *Service Dependency* is a detached service that\'s accessible to all
Steps in a Stage. Service dependencies support workflows such as

-   Integration testing: You can set up a service and then run tests
    against this service.
-   Running Docker-in-Docker: You can [set up a dind
    service](https://ngdocs.harness.io/article/ajehk588p4) to process
    Docker commands in Run Steps.

This topic provides settings and permissions for the Configure Service
Dependency step.

### Before You Begin

#### Good Practice: Add a Health Check to Verify that the Service is Up

After a container starts, the software running inside the container
takes time to initialize and begin accepting requests. Before you send
the first request, add a health check to verify that the service is
running. You can add a `sleep` command to a Run Step, or implement a
simple `while` loop to make the Step wait until the service is up. For
example, if your Stage uses a dind step, you can run the following:

``` {.hljs .bash}
while ! docker ps ;do 
     echo "Docker not available yet"
done
```

#### Service and Step Networking

Service and Step containers within the same Stage all share the same
network. To communicate with a Service, use the local-host address and
the port number defined in the Docker image. For example, you can use
`127.0.0.1:6379` to communicate with a Redis server or `localhost:27017`
to communicate with a Mongo database (assuming the default ports aren\'t
overridden).

In a Kubernetes build infrastructure, all Steps run in Containers. In an
AWS build infrastructure, some Steps might run directly on the VM. See
[Port Bindings](#port_bindings) below.

### Name

The unique name for this step.

### ID

See [Entity Identifier
Reference](/article/li0my8tcz3-entity-identifier-reference){target="_blank"}.

### Description

Text string.

### Container Registry

Harness Connector for the container registry containing the Service
Dependency image, such as DockerHub.

### Image

The name of the Docker image.

The image name should include the tag and will default to the latest tag
if unspecified.

You can use any Docker image from any Docker registry, including Docker
images from private registries.

Example: `mysql:5`

### Optional Configurations {#undefined}

#### Privileged

Enable this option to run the container with escalated privileges. This
is the equivalent of running a container with the
Docker `--privileged` flag.

#### Environment Variables

Add any environment variables you want to inject into the container.

#### Entry Point

ENTRYPOINT instructions allow you to configure a container that will run
as an executable.

You can add commands in Entry Point to override the image
[ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint){target="_blank"}.
See ENTRYPOINT best practices from Docker.

![](./static/configure-service-dependency-step-settings-08.png)

Commands should be in exec form.

Each command and parameter should be added separately. For example:

![](./static/configure-service-dependency-step-settings-09.png)

For a useful summary of ENTRYPOINT and CMD see [Demystifying ENTRYPOINT
and CMD in
Docker](https://aws.amazon.com/blogs/opensource/demystifying-entrypoint-cmd-docker/){target="_blank"}
from AWS.

#### Arguments

Overrides the image
[CMD](https://docs.docker.com/engine/reference/builder/#cmd){target="_blank"}.
Each argument should be in exec format. For example:

![](./static/configure-service-dependency-step-settings-10.png){style="display:block;margin-left:0;margin-right:auto"
hd-align="left"}

For a useful summary of ENTRYPOINT and CMD, see [Demystifying ENTRYPOINT
and CMD in
Docker](https://aws.amazon.com/blogs/opensource/demystifying-entrypoint-cmd-docker/){target="_blank"}
in the AWS docs.

#### Port Bindings {#port_bindings}

When a Pipeline runs in an AWS build infrastructure, some Steps might
run on a bare metal VM and others run in a container. The port used to
communicate with the Service Dependency depends on where the Step is
running: bare-metal Steps use the Host Port and containerized Steps use
the Container Port.

Suppose you create a Service Dependency with the Name and Id
**myloginservice**.

\- A containerized Step talks to the service using
**myloginservice:*****container_port***.

\- A Run or Run Test Step that runs directly on the VM talks to the
service using **localhost:*****host_port***.

The binding of Host and Container Ports is similar to [port mapping in
Docker](https://docs.docker.com/config/containers/container-networking/){target="_blank"}.
Usually the ports are the same unless the default Host Port for the
service dependency is already in use by another local service.

#### Image Pull Policy

Select an option to set the pull policy for the image.

-   **Always**: The kubelet queries the container image registry to
    resolve the name to an image digest every time the kubelet launches
    a container. If the kubelet encounters an exact digest cached
    locally, it uses its cached image; otherwise, the kubelet downloads
    (pulls) the image with the resolved digest, and uses that image to
    launch the container.
-   **If Not Present**: The image is pulled only if it isn\'t already
    present locally.
-   **Never**: The image is assumed to exist locally. The kubelet
    doesn\'t try to pull the image.

#### Run as User

Set the value to specify the user id for all processes in the pod,
running in containers. See [Set the security context for a
pod](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod).

#### Set container resources

These settings specify the maximum resources used by the container at
runtime.

##### Limit Memory

Maximum memory that the container can use. You can express memory as a
plain integer or as a fixed-point number using the suffixes `G` or `M`.
You can also use the power-of-two equivalents `Gi` and `Mi`.

##### Limit CPU

The maximum number of cores that the container can use. CPU limits are
measured in cpu units. Fractional requests are allowed: you can specify
one hundred millicpu as `0.1` or `100m`. See [Resource units in
Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes){target="_blank"}.

##### Timeout

Timeout for the step. Once the timeout is reached, the Step fails and
the Pipeline execution continues.

### See Also

-   [Share CI Data across Steps and
    Stages](https://ngdocs.harness.io/article/fbrgw2ixjr)

-   ## [Run Docker-in-Docker in a CI Stage](https://ngdocs.harness.io/article/ajehk588p4)
