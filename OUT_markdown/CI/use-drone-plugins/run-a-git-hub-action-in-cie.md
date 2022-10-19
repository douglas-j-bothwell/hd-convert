---
title: Run a GitHub Action in CI
description: Github Actions is a GitHub feature that enables you to automate various event-driven activities in GitHub, such as cloning a repository, generating Docker images, and testing scripts. Harness CI supp…
tags: 
   - helpDocs
helpdocs_topic_id: 7kb90dkxw0
helpdocs_is_private: false
helpdocs_is_published: true
---

[Github
Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
is a GitHub feature that enables you to automate various event-driven
activities in GitHub, such as cloning a repository, generating Docker
images, and testing scripts.

Harness CI supports launching GitHub Actions as part of a Pipeline Stage
using the **Plugin** step.

You simply use the GitHub Actions Drone Plugin,
[plugins/github-actions](https://github.com/drone-plugins/github-actions),
in the **Plugin** step, and then replicate the GitHub Action settings.

The Github Actions Drone Plugin runs your GitHub Actions in the
background using [nektos/act](https://github.com/nektos/act).

In this topic, we cover using GitHub Actions in the Plugin step with one
of the several GitHub Actions listed in [GitHub
Marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=).

In this topic:

-   [Before You
    Begin](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#before_you_begin)
-   [Step 1: Create the CI
    Stage](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#step_1_create_the_ci_stage)
-   [Step 2: Add the
    Codebase](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#step_2_add_the_codebase)
-   [Step 3: Define the Build Farm
    Infrastructure](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#step_3_define_the_build_farm_infrastructure)
-   [Step 4: Add the Plugin
    step](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#step_4_add_the_plugin_step)
-   [Step 5: View the
    Results](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#step_5_view_the_results)
-   [Configure As Code:
    YAML](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#configure_as_code_yaml)
-   [See
    Also](https://ngdocs.harness.io/article/7kb90dkxw0-run-a-git-hub-action-in-cie#see_also)

### Before You Begin

-   [CI Pipeline
    Quickstart](https://ngdocs.harness.io/article/x0d77ktjw8-ci-pipeline-quickstart)
-   [CI Stage
    Settings](https://ngdocs.harness.io/article/yn4x8vzw3q-ci-stage-settings)
-   [Set Up Build
    Infrastructure](https://ngdocs.harness.io/category/rg8mrhqm95-set-up-build-infrastructure)
-   [Learn Harness\' Key
    Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)

### Step 1: Create the CI Stage

In your Harness Pipeline, click Add Stage, and then click CI.

### Step 2: Add the Codebase

In Connector, select an existing Connector to your codebase repo, or
create a new one. See [Code Repo
Connectors](https://ngdocs.harness.io/category/xyexvcc206-ref-source-repo-provider).

You can see the URL for the repo account below **Repository Name**.
Don\'t add the URL into Repository Name.

In Repository Name, enter the name of the repo containing the codebase.

For example, if the account URL is `https://github.com/mycompany` and
the repo in that account is `myapp`, enter `myapp` in the **Repository
Name**.

### Step 3: Define the Build Farm Infrastructure

In the CI stage Infrastructure, define the build farm for the codebase.

The following example uses a Kubernetes cluster build farm. You can use
AWS for your build infrastructure as well. See [Set Up an AWS VM Build
Infrastructure](https://ngdocs.harness.io/article/z56wmnris8).

In **Select a Kubernetes Cluster**, select, or create, a Kubernetes
Connector. See [Kubernetes Cluster Connector Settings
Reference](https://ngdocs.harness.io/article/sjjik49xww-kubernetes-cluster-connector-settings-reference).
This Connector connects Harness to the cluster to use as the build farm.

In **Namespace**, enter the Kubernetes namespace to use. You can use a
Runtime Input (`<+input>`) or expression also. See [Runtime
Inputs](https://ngdocs.harness.io/article/f6yobn7iq0-runtime-inputs).

See [Define a Kubernetes Cluster Build
Infrastructure](/article/ia5dwx5ya8-set-up-a-kubernetes-cluster-build-infrastructure)
for more information.

### Step 4: Add the Plugin step

In the stage\'s Execution, click **Add step**, select **Plugin**.

The Plugin settings appear.

Enter the following settings:

+-----------------------------------+-----------------------------------+
| **Name**                          | Enter a unique name for the step. |
+-----------------------------------+-----------------------------------+
| **Description**                   | Harness automatically generates a |
|                                   | unique ID for the step.           |
+-----------------------------------+-----------------------------------+
| **Container Registry**            | Select or create a Harness        |
|                                   | Connector for the container       |
|                                   | registry.                         |
+-----------------------------------+-----------------------------------+
| **Image**                         | Enter the name of the Drone       |
|                                   | Plugin: `plugins/github-actions`. |
|                                   | This Plugin allows running GitHub |
|                                   | Action in CI.                     |
+-----------------------------------+-----------------------------------+
| **Privileged**                    | The Drone Plugin uses             |
|                                   | [nektos/ac                        |
|                                   | t](https://github.com/nektos/act) |
|                                   | to run GitHub Actions in CI. It   |
|                                   | requires DIND (docker-in-docker)  |
|                                   | to run your images. Hence, the    |
|                                   | **Privileged** attribute needs to |
|                                   | be enabled to run with escalated  |
|                                   | permissions.                      |
+-----------------------------------+-----------------------------------+
| **Settings**                      | Replicate the GitHub Action       |
|                                   | attributes under                  |
|                                   | **Settings**.  For example:       |
|                                   |                                   |
|                                   | -   **name**: It refers to the    |
|                                   |     GitHub repo of action along   |
|                                   |     with branch or tag.           |
|                                   | -   **with**: It is a map with    |
|                                   |     key and value as strings.     |
|                                   |     These are inputs to the       |
|                                   |     GitHub Actions.               |
|                                   | -   **env**: Environment          |
|                                   |     variables passed to the       |
|                                   |     GitHub Actions.               |
|                                   |                                   |
|                                   | For example, for the [Upload      |
|                                   | Cloud Storage                     |
|                                   | Action](https://github            |
|                                   | .com/google-github-actions/upload |
|                                   | -cloud-storage){target="_blank"}, |
|                                   | the attributes are as follows:    |
|                                   |                                   |
|                                   | +--------------+--------------+   |
|                                   | | Key          | Value        |   |
|                                   | +--------------+--------------+   |
|                                   | | **uses:**    | `            |   |
|                                   | |              | google-githu |   |
|                                   | |              | b-actions/up |   |
|                                   | |              | load-cloud-s |   |
|                                   | |              | torage@main` |   |
|                                   | +--------------+--------------+   |
|                                   | | **  with:**  | `pa          |   |
|                                   | |              | th: pom.xml` |   |
|                                   | |              |              |   |
|                                   | |              | `destinati   |   |
|                                   | |              | on: cie-demo |   |
|                                   | |              | -pipeline/gi |   |
|                                   | |              | thub-action` |   |
|                                   | |              |              |   |
|                                   | |              | `creden      |   |
|                                   | |              | tials: <+sta |   |
|                                   | |              | ge.variables |   |
|                                   | |              | .GCP_SECRET_ |   |
|                                   | |              | KEY_BASE64>` |   |
|                                   | +--------------+--------------+   |
|                                   |                                   |
|                                   | The                               |
|                                   | `<+stage.                         |
|                                   | variables.GCP_SECRET_KEY_BASE64>` |
|                                   | setting uses a Stage variable and |
|                                   | a Harness Secret. See [Add a      |
|                                   | Stage](                           |
|                                   | /article/2chyf1acil-add-a-stage). |
|                                   |                                   |
|                                   | The above attributes of Upload    |
|                                   | Cloud Storage Action are          |
|                                   | replicated in CI Plugin Settings  |
|                                   | as follows:                       |
|                                   |                                   |
|                                   | !                                 |
|                                   | [](https://files.helpdocs.io/i5nl |
|                                   | 071jo5/articles/7kb90dkxw0/163820 |
|                                   | 5607190/ojjxttzb-j-6-j-qct-kaefr- |
|                                   | 21-fe-idx-26-g-mlw-byn-tm-bzaton- |
|                                   | 5-h-0-wg-dsri-wgho-2-bsrlvgpnk-pv |
|                                   | -ic-z-x-fjmjxhhh-4-aae-dpjf-5-e-4 |
|                                   | -x-9-ezjz-8-vxv-8-h-lhg-jv-7-p-rp |
|                                   | -ctlz-qjqu-v-2-st-5-i-z-5-cs){sty |
|                                   | le="max-height:50%;max-width:50%" |
|                                   | hd-height="50%" hd-width="50%"}   |
+-----------------------------------+-----------------------------------+

Here\'s an example:

![](https://files.helpdocs.io/i5nl071jo5/articles/7kb90dkxw0/1644533671813/image.png)

For the step settings on CI Plugins, see [Plugin Step
Settings](https://ngdocs.harness.io/article/8r5c3yvb8k-plugin-step-settings-reference).

### Step 5: View the Results

Save the Pipeline and click **Run**. 

You can see the logs for the GitHub GCP Upload Action in the Pipeline as
it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/7kb90dkxw0/1638205727555/2-kztp-livgq-6-g-7-q-ti-0-ljqj-63-mv-wm-6-pb-th-enjaddyp-lpp-2-ny-bzw-wn-n-7-tgskb-xw-7-bgw-v-8-z-yuue-6-g-1-y-7-a-sa-kt-0-xy-1-xc-gyp-9-gc-8-td-ai-nvg-j-5-do-qgh-jg-6-r-81-c-fmp-wmen-bgzyq-b-6-r-y){style="max-height:50%;max-width:50%"
hd-height="50%" hd-width="50%"}

### Configure As Code: YAML

To configure your pipeline as YAML in CI, go to Harness **Pipeline
Studio** and click **YAML**. Here's is a working example of GitHub
Action Cloud Storage Upload to GCP in CI. Modify the YAML attributes
such as name, identifiers, codebase, connector ref, environment
variables based on your Pipeline requirements.

``` {.hljs .yaml}
pipeline:
    name: gcp-upload-github-action # Configure your Pipeline name
    identifier: gcpuploadgithubaction # Configure your Pipeline identifier
    projectIdentifier: Demo_CI_pipelines # Configure your Project identifier
    orgIdentifier: default # Configure your Organization
    tags: {}
    stages:
        - stage:
              identifier: gcp_upload_success_gha # Configure your Stage identifier
              name: stage 1
              type: CI
              variables: 
                  - name: GCP_SECRET_KEY_BASE64 # Configure your Secret Key Name
                    type: Secret
                    value: gcpbase64secret # Configure your Secret Key Value
              spec:
                  execution:
                      steps:
                          - step:
                                identifier: gcsuploader # Configure your step identifier name
                                name: step one # Configure your step name
                                type: Plugin
                                spec:
                                    connectorRef: dockerhub
                                    image: plugins/github-actions
                                    privileged: true
                                    settings: # Configure your plugins Settings configuration
                                        uses: google-github-actions/upload-cloud-storage@main
                                        with:
                                            path: pom.xml
                                            destination: cie-demo-pipeline/github-action
                                            credentials: <+stage.variables.GCP_SECRET_KEY_BASE64>
                  infrastructure: # Configure your Infrastructure Settings
                      type: KubernetesDirect
                      spec:
                          connectorRef: buildfarm
                          namespace: cie-demo-pipeline
    properties:
        ci:
            codebase: # Configure your Codebase
                connectorRef: githubautouser
                repoName: springboot
                build:
                    type: branch
                    spec:
                        branch: ci-autouser
```

### See Also

-   [Plugin Step
    Settings](https://ngdocs.harness.io/article/8r5c3yvb8k-plugin-step-settings-reference)
-   [GitHub
    Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
