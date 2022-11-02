---
title: Hosted builds on virtual machines quickstart
description: Harness offers hosted virtual machines to run your builds. With hosted builds, your builds run on VMs that contain an environment of tools, packages, and settings so you can start building and testin…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: jkh1wsvajv
helpdocs_category_id: 
helpdocs_is_private: false
helpdocs_is_published: false
---

Harness offers hosted virtual machines to run your builds. With hosted builds, your builds run on VMs that contain an environment of tools, packages, and settings so you can start building and testing your applications in no time. 

Hosted builds provide the following advantages:

* Easy setup. Create your first pipeline in minutes.
* Low maintenance. Run CI pipelines without having to manage your own infrastructure for builds.
* Secure system. Each build stage runs on an isolated virtual machine.
* Multiple platforms. Use hosted runners to run your builds on Linux, Windows, or MacOS.

You can select where to run your stage by using "platform"

`platform:`

 `os: Linux`

If the platform isn't specified, Harness defaults to using the Linux operating system. 

When a pipeline is executed, Harness executes each of its CI stages in a new M. All steps in the stage execute on the VM, allowing the steps in that job to share information using the runner's filesystem. You can run workflows directly on the VM or in a Docker container. When the job is finished, the VM is automatically decommissioned. 

#### Supported runners and hardware resources



|  |  |
| --- | --- |
| Linux | 4-core CPU (ARM and AMD)16 GB RAM |
| Windows | 4-core CPU (x86\_64) |
| MacOS | 2-core CPU16 GB Ram |

#### Getting started with a hosted build on a VM

Follow these steps to create your first pipeline using a Harness-hosted VM.

1. On the app.harness.io **Sign in** page, select **Sign up**, and sign up for an account.
2. Select **Continuous Integration**, and then select **Continue**.
3. Select **Get Started**.
4. Select the code repository tool you use, and then select the authentication method you want to use to connect to your repository, either **OAuth** or **Access Token**.
5. Select **Next: Select Repository**.
6. Select the repository you want to clone, and then select **Create Pipeline**. A sample pipeline with an Echo Welcome message is set up for you.
7. Select **Run**, and then select **Run Pipeline**.

