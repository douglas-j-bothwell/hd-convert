---
title: Docker Connector Settings Reference
description: This topic provides settings and permissions for the Docker Connector. Docker Registries in Cloud Platforms. The Docker Connector is platform-agnostic and can be used to connect to any Docker contain…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: u9bsd77g5a
helpdocs_category_id: 1ehb4tcksy
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic provides settings and permissions for the Docker Connector.

### Docker Registries in Cloud Platforms

The Docker Connector is platform-agnostic and can be used to connect to any Docker container registry, but Harness provides first class support for registries in AWS and GCR.

See:

* [Add an AWS Connector](/article/98ezfwox9u-add-aws-connector)
* [Google Cloud Platform (GCP) Connector Settings Reference](/article/cii3t8ra3v-connect-to-google-cloud-platform-gcp)

### Docker Registry Permissions Required

Make sure the connected user account has the following permissions.

* Read permission for all repositories.

The user needs access and permissions to the following:

* List images and tags
* Pull images

See [Docker Permissions](https://docs.docker.com/datacenter/dtr/2.0/user-management/permission-levels/).

If you are using anonymous access to a Docker registry for a Kubernetes deployment, then `imagePullSecrets` should be removed from the container specification. This is standard Kubernetes behavior and not related to Harness specifically.### Name

The unique name for this Connector.

### ID

See [Entity Identifier Reference](/article/li0my8tcz3-entity-identifier-reference).

### Description

Text string.

### Tags

See [Tags Reference](/article/i8t053o0sq-tags-reference).

### Docker Registry URL

The URL of the Docker Registry. This is usually the URL used for your [docker login](https://docs.docker.com/engine/reference/commandline/login/) credentials.

To connect to a public Docker registry like Docker Hub, use `https://registry.hub.docker.com/v2/`.

To connect to a private Docker registry, use `https://index.docker.io/v2/`.

### Provider Type

The Docker registry platform that you want to connect. Some examples:

* DockerHub
* Harbor
* Quay

### Authentication

You can authenticate using username and password, or select anonymous.

### Credentials

The username and password for the Docker registry account.

The password uses a [Harness Encrypted Text secret](/article/osfw70e59c-add-text-secrets).

