---
title: Upload Artifacts to JFrog
description: This topic provides settings to upload artifacts to JFrog Artifactory.
tags: 
   - helpDocs
   - JFrog
helpdocs_topic_id: lh082yv36h
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic provides settings to upload artifacts to [JFrog Artifactory](https://www.jfrog.com/confluence/display/JFROG/JFrog+Artifactory).

The following steps run SSH commands and push the artifacts to JFrog Artifactory.

In this topic:

* [Before you Begin](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#before_you_begin)
* [Step 1: Create the CI Stage](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#undefined)
* [Step 2: Define the Build Farm Infrastructure](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#undefined)
* [Step 3: Configure the Run Step](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#undefined)
* [Step 4: Upload Artifacts to JFrog Artifactory](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#undefined)
* [Step 5: View the Results](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#undefined)
* [See Also](https://ngdocs.harness.io/article/lh082yv36h-upload-artifacts-to-jfrog#undefined)

### Before you Begin

* [CI Pipeline Quickstart](https://ngdocs.harness.io/article/x0d77ktjw8-ci-pipeline-quickstart)
* [CI Stage Settings](https://ngdocs.harness.io/article/yn4x8vzw3q-ci-stage-settings)
* [Set Up Build Infrastructure](https://ngdocs.harness.io/category/rg8mrhqm95-set-up-build-infrastructure)
* [Learn Harness' Key Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)

### Step 1: Create the CI Stage

In your Harness Pipeline, click **Add Stage**, and then click CI.

### Step 2: Define the Build Farm Infrastructure

In the CI stage Infrastructure, define the build farm for the codebase. See [Define Kubernetes Cluster Build Infrastructure](https://ngdocs.harness.io/article/x7aedul8qs-kubernetes-cluster-build-infrastructure-setup).

### Step 3: Configure the Run Step

In the stage's Execution step, select **Run**. The Run step executes one or more commands on a container image. See [Configure Run Step](https://ngdocs.harness.io/article/vo4sjbd09g-configure-service-dependency-step-settings). 

### Step 4: Upload Artifacts to JFrog Artifactory

In the CI Artifact, select **Upload Artifacts to JFrog Artifactory**.

In this step, configure the Harness Artifactory Connector, enter the source file/path, and the target path. 

The JFrog Account associated with the Connector must have read/write permission. See [C](https://ngdocs.harness.io/article/euueiiai4m-artifactory-connector-settings-reference)[onnector Settings Reference](https://ngdocs.harness.io/article/euueiiai4m-artifactory-connector-settings-reference).

For the step Settings, see [Upload Artifacts to JFrog Artifactory](https://ngdocs.harness.io/article/gjoggc66fy-upload-artifacts-to-jfrog-artifactory-step-settings).

[![](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218900031/j-0-gyt-06-tgq-0-rg-gg-9-dk-ejq-3-qx-niz-gi-n-04-m-1-uef-0-m-fxq-pfj-0-uuv-ve-w-llx-dw-ggci-2-zl-889-i-wnj-8-yoh-rmsher-ogz-a-8-bo-8-ik-0-r-60-dzn-0-k-nmks-3-cqo-68-n-9-hv-fslbm-dk-ejgxll-g-5-w-au)](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218900031/j-0-gyt-06-tgq-0-rg-gg-9-dk-ejq-3-qx-niz-gi-n-04-m-1-uef-0-m-fxq-pfj-0-uuv-ve-w-llx-dw-ggci-2-zl-889-i-wnj-8-yoh-rmsher-ogz-a-8-bo-8-ik-0-r-60-dzn-0-k-nmks-3-cqo-68-n-9-hv-fslbm-dk-ejgxll-g-5-w-au)### Step 5: View the Results

Save the Pipeline and click **Run**. 

You can see the logs for the Run and Upload step in the Pipeline as it runs.

[![](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218924096/d-axc-zlmfn-32-uc-9-pktyh-hse-d-1-uehom-ovy-1-ded-5-e-l-8-wld-3-ny-mpmosz-qw-s-0-k-4-x-5-evu-8-drj-6-y-zali-bxzt-5-o-s-4-vt-5-iqz-ssnp-tcf-2-d-31-t-3-pho-zsxlenvex-vn-ht-7-rz-50-yq-5-mvfn-nmgvc)](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218924096/d-axc-zlmfn-32-uc-9-pktyh-hse-d-1-uehom-ovy-1-ded-5-e-l-8-wld-3-ny-mpmosz-qw-s-0-k-4-x-5-evu-8-drj-6-y-zali-bxzt-5-o-s-4-vt-5-iqz-ssnp-tcf-2-d-31-t-3-pho-zsxlenvex-vn-ht-7-rz-50-yq-5-mvfn-nmgvc)In your Harness project's Builds, you can see the build listed.

[![](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218929695/7-lpav-2-cc-60-cv-16-tak-wxmk-tvp-vcts-al-425-i-td-nwl-n-3-c-tr-j-f-fwzz-rdq-zavg-und-ux-szthkyk-oishue-ksl-ixy-pntfloc-0-av-udl-0-o-ob-82-k-q-8-j-a-7-nevpcvm-5-lx-2-od-s-3-cf-ik-fo)](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218929695/7-lpav-2-cc-60-cv-16-tak-wxmk-tvp-vcts-al-425-i-td-nwl-n-3-c-tr-j-f-fwzz-rdq-zavg-und-ux-szthkyk-oishue-ksl-ixy-pntfloc-0-av-udl-0-o-ob-82-k-q-8-j-a-7-nevpcvm-5-lx-2-od-s-3-cf-ik-fo)On JFrog, you can see the file that you pushed.

[![](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218934313/r-yfrua-c-88-tr-8-wi-72-bf-fjw-tb-5-lq-vv-2-sv-0-6-v-vfl-g-8-c-lwkeft-as-mlik-5-ol-2-txld-cy-6-le-7-j-6-jy-nlab-sra-incsku-jwmxsi-p-59-u-rrzr-thb-n-4-lueuh-i-1-d-i-1-eyf-ho-ur-5-r-5-i-bbgpb-8)](https://files.helpdocs.io/i5nl071jo5/articles/ku0km8tpwf/1625218934313/r-yfrua-c-88-tr-8-wi-72-bf-fjw-tb-5-lq-vv-2-sv-0-6-v-vfl-g-8-c-lwkeft-as-mlik-5-ol-2-txld-cy-6-le-7-j-6-jy-nlab-sra-incsku-jwmxsi-p-59-u-rrzr-thb-n-4-lueuh-i-1-d-i-1-eyf-ho-ur-5-r-5-i-bbgpb-8)### See Also

* [Build and Push an Artifact](https://ngdocs.harness.io/article/8l31vtr4hi-build-and-upload-an-artifact)

