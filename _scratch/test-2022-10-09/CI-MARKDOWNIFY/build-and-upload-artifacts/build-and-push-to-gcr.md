---
title: Build and Push to GCR
description: This topic provides settings to Build and Push an image to Google Container Registry (GCR).
tags: 
   - helpDocs
helpdocs_topic_id: gstwrwjwgu
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic provides settings to Build and Push an image to [Google Container Registry](https://cloud.google.com/container-registry) (GCR).

The following steps build an image and push it to GCR.

In this topic:

* [Before You Begin](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#undefined)
* [Step 1: Create the CI Stage](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#step_1_create_the_ci_stage)
* [Step 2: Define the Build Farm Infrastructure](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#step_2_define_the_build_farm_infrastructure)
* [Step 3: Add the Build and Push Step](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#step_3_add_the_build_and_push_step)
* [Step 4: Specify Codebase Branch or Tag at Pipeline Execution](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#step_4_specify_codebase_branch_or_tag_at_pipeline_execution)
* [Step 5: View the Results](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#step_5_view_the_results)
* [See Also](https://ngdocs.harness.io/article/gstwrwjwgu-build-and-push-to-gcr#see_also)

### Before You Begin

* [CI Pipeline Quickstart](https://ngdocs.harness.io/article/x0d77ktjw8-ci-pipeline-quickstart)
* [Delegates Overview](https://ngdocs.harness.io/article/2k7lnc7lvl-delegates-overview)
* [CI Stage Settings](https://ngdocs.harness.io/article/yn4x8vzw3q-ci-stage-settings)
* [Learn Harness' Key Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)

### Step 1: Create the CI Stage

In your Harness Pipeline, click **Add Stage**, and then click CI.

### Step 2: Define the Build Farm Infrastructure

In the CI stage Infrastructure, define the build infrastructure for the Codebase.

The following steps use a Kubernetes cluster build farm.

See [Define Kubernetes Cluster Build Infrastructure](https://ngdocs.harness.io/article/x7aedul8qs-kubernetes-cluster-build-infrastructure-setup).

### Step 3: Add the Build and Push Step

In the stage's Execution, select **Build and Push to GCR**.

#### Step Parameters

##### Name

The unique name for this Step.

##### ID

See [Entity Identifier Reference](https://ngdocs.harness.io/article/li0my8tcz3-entity-identifier-reference).

##### GCP Connector

The Harness GCP Connector to use to connect to GCR. GCP account associated with the GCP Connector needs specific roles.

See [Google Cloud Platform (GCP) Connector Settings Reference](https://ngdocs.harness.io/article/yykfduond6-gcs-connector-settings-reference).

##### Host

The GCR registry hostname. For example, us.gcr.io hosts images in data centers in the United States in a separate storage bucket from images hosted by gcr.io.

##### Project ID

The GCP [Resource Manager project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

##### Image Name

The name of the image you want to build.

##### Tags

[Docker build tag](https://docs.docker.com/engine/reference/commandline/build/#tag-an-image--t) (-t).

Each tag should be added separately.

##### Option: Add a Tag using Harness Expression

You can tag the image in any way, but a Harness expression can be very useful.

The `<+pipeline.sequenceId>` is a built-in Harness variable. It represents the Build ID number, such as Build ID: 9. You can then use the same tag in another stage to reference the same build with its tag.

##### Dockerfile

Enter the path of the Dockerfile. If you don't provide a name, Harness assumes the Dockerfile is in the root folder of the codebase.

##### Context

Enter a path to a directory containing a Dockerfile.

##### Labels

[Docker object labels](https://docs.docker.com/config/labels-custom-metadata/) to add metadata to the Docker image.

##### Build Arguments

The [Docker build-time variables](https://docs.docker.com/engine/reference/commandline/build/#set-build-time-variables---build-arg) (--build-arg).

##### Target

The [Docker target build stage](https://docs.docker.com/engine/reference/commandline/build/#specifying-target-build-stage---target) (--target).

For example, build-env.

##### Remote Cache Image

The remote cache repository and build image need to be created on the same host and project. The Build creates the repository automatically if it doesn’t exist.

##### Set container resources

Maximum resources limit values for the resources used by the container at runtime.

##### Limit Memory

Maximum memory that the container can use.

You can express memory as a plain integer or as a fixed-point number using suffixes G or M. You can also use the power-of-two equivalents Gi or Mi.

##### Limit CPU

See [Resource units in Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes).

Limit the number of cores that the container can use.

Limits for CPU resources are measured in CPU units.

Fractional requests are allowed. The expression 0.1 is equivalent to the expression 100m, which can be read as one hundred millicpu.

##### Timeout

Timeout for the step. Once the timeout is reached, the step fails, and the Pipeline execution continues.

#### Advanced Options

##### Conditional Execution

Set conditions to determine when the step should be executed. See [Conditional Execution](https://ngdocs.harness.io/article/i36ibenkq2-step-skip-condition-settings).

##### Failure Strategy

Define one or more failure strategies to control the behavior of your pipeline when your step execution encounters an error. See [Failure Strategy](https://ngdocs.harness.io/article/htrur23poj-step-failure-strategy-settings). 

### Step 4: Specify Codebase Branch or Tag at Pipeline Execution

Select the Codebase Git Branch or Git Tag to use for the execution.

Enter the branch or tag and click **Run Pipeline**.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218110739/mzt-tjleo-46-qzwrs-wgasgnarhzvqc-arrc-fmfre-nytc-fb-zaefn-6-q-ztnmgo-q-9-pdg-ogbfc-zjmyb-1-m-8-l-c-9-bc-8-cax-3-twr-1-v-gy-rg-1-w-ltiq-i-4-m-6-txwjyiu-ykge-mwd-1-hj-7-yh-gk-ei-ju)###  Step 5: View the Results

You can see the logs for the Build and Push step in the Pipeline as it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218117572/f-fasi-omyjgn-gqw-1-mj-ng-kjrhzx-gxsahkms-4-cp-44-tkgss-fm-8-kmiue-g-0-e-wwb-0-c-mtmlx-swl-ex-eglsgo-ehbl-xkjcz-pxkvr-ler-z-7-u-zsux-amx-42-z-yby-i-4-def-xt-sx-5-t-0-llg-9-z-uok)In your Harness project's Builds, you can see the build listed.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218126856/ahth-iqde-si-wv-5-mvxu-r-9-n-v-81-tnpq-xzeh-e-3-p-7-h-tl-y-8-btw-ojdwv-0-ez-owzasbt-tq-e-9-hph-jjf-exqy-uen-v-30-nvs-czwia-72-u-xu-g-hipc-1-e-6-sm-jezlknje-p-72-e-3-kv-h-7-h-f-6-r-o-1-ckj-i)On GCR, you can see the image that you pushed.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218219885/86-mqci-xeqcvu-pj-sf-oiyi-ianh-jeq-e-41-h-9-u-d-3-p-1-u-iao-lq-2-xf-2-s-dupmi-zg-hmn-oi-qs-9-pt-vlq-t-66-m-cquj-6-efi-x-4-otztu-ybj-9-lhm-87-x-eyt-ct-fse-tdqqah-3-v-xsymn-wa-8-sfn-6-rzf-tc-e)### See Also

* [Run Step Settings](https://ngdocs.harness.io/article/1i1ttvftm4-run-step-settings)

