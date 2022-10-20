---
title: Run a Script in a CI Stage
description: The Build stage Run step can be used to run scripts in your CI stages. The Run step pulls in a Docker image such as the Docker image for Maven. Then you run a script such as mvn package with the tool…
tags: 
   - helpDocs
helpdocs_topic_id: ota4xj59le
helpdocs_is_private: false
helpdocs_is_published: true
---

The Build stage **Run** step can be used to run scripts in your CI
stages.

The **Run** step pulls in a Docker image such as the Docker image for
Maven. Then you run a script such as`mvn package` with the tool. You can
use any Docker image from any public or private Docker registry.

This topic describes how to run a simple script in a CI stage.

### Before You Begin

-   [CI Pipeline
    Quickstart](https://ngdocs.harness.io/article/x0d77ktjw8-ci-pipeline-quickstart)
-   [Delegates
    Overview](https://ngdocs.harness.io/article/2k7lnc7lvl-delegates-overview)
-   [CI Stage
    Settings](https://ngdocs.harness.io/article/yn4x8vzw3q-ci-stage-settings)
-   [Learn Harness\' Key
    Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)

### Step 1: Create the CI Stage

In your Harness Pipeline, click **Add Stage** and then click CI.

### Step 2: Add the Codebase

Do one of the following:

-   If this is the first CI stage in the Pipeline, in the CI stage
    settings enable **Clone Codebase**.
-   If you have an existing Pipeline with a CI stage, click
    **Codebase**. See [Edit Codebase Configuration]().

### Step 3: Define the Build Farm Infrastructure

In the CI stage Infrastructure, define the build farm for the codebase.
See [Set Up Build
Infrastructure](/category/rg8mrhqm95-set-up-build-infrastructure){target="_blank"}.

### Step 4: Configure the Run Step

In the Execution tab, click **Add** **step** and then click **Run**.

![](https://files.helpdocs.io/i5nl071jo5/articles/ota4xj59le/1625209864101/m-j-1-lr-06-ym-d-9-zml-tr-6-q-bh-mopb-7-axr-wzgz-z-2-ps-wp-ywfk-eb-4-g-f-2-y-y-7-wmaj-bb-j-uum-jtadr-0-d-mdq-kgm-3-cx-jbqk-kk-2-srm-9-aalmht-xkumes-jl-nag-b-63-ki-ni-tby-7-jgd-5-s-sosn-rivzj-y){style="display:block;margin-left:0;margin-right:auto"
hd-align="left"}

The Run step executes one or more commands on the image you added from
any public or private Docker registry.

In **Container Registry**, select a Connector to a container registry
for the image needed to run your script. For example, if you are running
a cURL script in this step, you might add or select a Connector to
DockerHub so Harness can pull the image for cURL.

In **Image**, enter the name of the image to pull and run for this step.
For example, if you are running a cURL script, you might use
`curlimages/curl:7.73.0`.

In **Commands**, you enter the script you want to run on the container.

See [Run Step
Settings](https://ngdocs.harness.io/article/1i1ttvftm4-run-step-settings).

### Step 5: Run the Pipeline

Now you can run your Pipeline. You simply need to select the codebase.

1.  Click **Save and Publish**.

2.  Click **Run**. The Pipeline Inputs settings appear.

3.  In **CI Codebase**, click **Git branch**.

4.  In Git Branch, enter the name of the branch where the codebase is,
    such as a master.

    ![](https://files.helpdocs.io/i5nl071jo5/articles/ota4xj59le/1625209923841/e-11-g-x-0-l-5-w-c-eg-ei-2-n-ul-6-ldu-8-b-mi-ji-jb-k-apxu-r-g-kw-yupq-87-awar-il-3-o-49-mfknq-gikb-dkeyk-5-sw-1-a-c-9-k-njc-lc-3-e-x-3-y-9-wwkm-hj-q-mf-htrkw-sk-djm-8-sce-qrx-gro-mu-7-o-nh-dq){style="display:block;margin-left:0;margin-right:auto"
    hd-align="left"}

5.  Click **Run Pipeline**.

### Example: View a Test Report

Once the Pipeline is executed in CI, Click **Tests**. The Tests show the
test report of the unit test that you configured and ran. 

![](https://files.helpdocs.io/i5nl071jo5/articles/ota4xj59le/1625209945023/ahgq-6-x-8-f-3-ym-lu-fttatcc-ubya-wk-z-4-b-gg-8-j-tr-ufsg-jucz-t-8-p-3-xrsx-n-71-i-xq-gwk-zykz-e-rw-k-5-ma-jhal-4-b-rrugm-k-ncja-8-av-dys-93-nagn-m-1-sf-c-4-i-i-7-a-rn-bviy-b-8-abfw-52-hkm-4)

### See Also

-   [View Test
    Report](https://ngdocs.harness.io/article/sof7n3qjap-viewing-tests)
