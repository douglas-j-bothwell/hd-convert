---
title: Save and Restore Cache from S3
description: To solve [problem], [general description of How-to solution]. In this topic&#58; Before You Begin. Visual Summary. Step 1&#58; Title. Step 2&#58; Title. Next Steps. Before You Begin. Your target environment must…
tags: 
   - helpDocs
helpdocs_topic_id: qibyllcmza
helpdocs_is_private: false
helpdocs_is_published: true
---

Caching has two primary benefits:

-   It can make your jobs run faster by reusing the expensive fetch
    operation data from previous jobs. 
-   It enables you to share data across Stages.

In a Harness CI Pipeline, you can save the cache to an AWS S3 bucket in
one Stage using the **Save Cache to S3** step, and restore it in the
same or another Stage using **Restore Cache from S3 step**. 

The topic explains how to configure the **Save Cache to S3** and
**Restore Cache from S3** steps in CI using a two-stage Pipeline.

::: note-callout
You cannot share access credentials or other [Text
Secrets](https://ngdocs.harness.io/article/osfw70e59c-add-use-text-secrets)
across Stages.
:::

### Before You Begin

-   [CI Pipeline
    Quickstart](https://newdocs.helpdocs.io/article/x0d77ktjw8-ci-pipeline-quickstart)
-   [CI Stage
    Settings](https://newdocs.helpdocs.io/article/yn4x8vzw3q-ci-stage-settings)
-   [Set Up Build
    Infrastructure](https://newdocs.helpdocs.io/category/rg8mrhqm95-set-up-build-infrastructure)
-   [Learn Harness\' Key
    Concepts](https://newdocs.helpdocs.io/article/hv2758ro4e-learn-harness-key-concepts)

### Limitations

-   You cannot share access credentials or other [Text
    Secrets](https://ngdocs.harness.io/article/osfw70e59c-add-use-text-secrets)
    across Stages.
-   Use a dedicated bucket for your Harness cache operations. Do not
    save files to the bucket manually. The Retrieve Cache operation will
    fail if the bucket includes any files that do not have a Harness
    cache key.

### Review: YAML Example

If you want to configure your Pipeline in YAML, in **Pipeline Studio,**
click **YAML**. 

The following YAML file creates a Pipeline with two Stages: Save Cache
and Restore Cache. Copy the following YAML, paste it in the Harness YAML
editor, and modify its based on your Pipeline requirements.

``` {.hljs .yaml}
pipeline:
    name: Save and Restore AWS
    identifier: Save_and_Restore_AWS
    projectIdentifier: Example
    orgIdentifier: default
    tags: {}
    stages:
        - stage:
              identifier: s3_save_cache
              name: s3_save_cache
              type: CI
              variables:
                  - name: AWS_ACCESS_KEY
                    type: String
                    value: <+input>
                  - name: AWS_SECRET_KEY
                    type: Secret
                    value: <+input>
              spec:
                  sharedPaths:
                      - /shared
                  execution:
                      steps:
                          - step:
                                identifier: createBucket
                                name: create bucket
                                type: Run
                                spec:
                                    command: |
                                        aws configure set aws_access_key_id $AWS_ACCESS_KEY
                                        aws configure set aws_secret_access_key $AWS_SECRET_KEY
                                        aws configure set default.region us-west-2
                                        aws s3 rb s3://harnesscie-cache-tar --force || true
                                        aws s3 mb s3://harnesscie-cache-tar
                                    envVariables:
                                        HOME: /shared
                                    connectorRef: <+input>
                                    image: amazon/aws-cli:2.0.6
                          - step:
                                identifier: rootFile
                                name: create file at slash
                                type: Run
                                spec:
                                    command: |
                                        echo hello world > /shared/cache
                                    connectorRef: <+input>
                                    image: alpine
                          - step:
                                identifier: saveCacheTar
                                name: save cache
                                type: SaveCacheS3
                                spec:
                                    region: us-west-2
                                    connectorRef: <+input>
                                    bucket: harnesscie-cache-tar
                                    sourcePaths:
                                        - src/main/resources
                                        - /shared/cache
                                    key: cache-tar
                                    archiveFormat: Tar
                  infrastructure:
                      type: KubernetesDirect
                      spec:
                          connectorRef: <+input>
                          namespace: default
                  cloneCodebase: true
        - stage:
              identifier: s3_restore_cache
              name: s3 restore cache
              type: CI
              variables:
                  - name: AWS_ACCESS_KEY
                    type: String
                    value: <+input>
                  - name: AWS_SECRET_KEY
                    type: Secret
                    value: <+input>
              spec:
                  sharedPaths:
                      - /shared
                  execution:
                      steps:
                          - step:
                                identifier: restoreCacheTar
                                name: restore
                                type: RestoreCacheS3
                                spec:
                                    region: us-west-2
                                    connectorRef: <+input>
                                    bucket: harnesscie-cache-tar
                                    key: cache-tar
                                    failIfKeyNotFound: true
                                    archiveFormat: Tar
                  infrastructure:
                      useFromStage: s3_save_cache
                  cloneCodebase: false
```

If you want to configure your Pipeline in the Harness UI, go to
**Pipeline Studio** and click the **VISUAL** tab at the top of the
screen.

### Step 1: Open the Build Stage

In your Harness Pipeline, open the Stage where you want to save the
cache.

### Step 2: Define the Build Farm Infrastructure

In the Infrastructure tab, define the build farm for the codebase.

The following step uses a Kubernetes cluster build farm.

See [Define Kubernetes Cluster Build
Infrastructure](https://ngdocs.harness.io/article/x7aedul8qs-kubernetes-cluster-build-infrastructure-setup).

### Step 3: Save Cache to S3

In Execution, click **Add Step**, and select **Save Cache to S3**. Here
you configure S3 bucket, keys, and source paths to enable Harness to
save the cache to S3.

For step settings, see [Save Cache to S3
Settings.](https://ngdocs.harness.io/article/qtvjvrp9sn-save-cache-to-s-3-step-settings)

![](https://files.helpdocs.io/i5nl071jo5/articles/qibyllcmza/1625206915954/rb-8-xz-xoq-t-9-p-7-ph-9-fnls-w-4-g-pms-urw-v-5-j-ura-ar-ip-t-h-3-f-7-yn-lyoz-yhve-6-o-z-9-sefk-f-2-kul-pen-rki-fmo-hq-8-yj-c-2-le-i-4-yy-a-0-ra-25-hb-qoi-uruc-tyr-domj-gl-moiec-vi-jzpk-y-542-imk-u){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

### Step 4: Restore Cache from S3 Stage

In your Pipeline, click **Add Stage** where you want to restore the
saved cache from S3. 

In **Execution**, click **Add Step**, and select **Restore Cache from
S3**. Here you configure the keys for the S3 bucket where you saved your
cache.

For step settings, see [Restore Cache Step
Settings](/article/zlpx6lli6d-restore-cache-from-s-3-step-settings).

![](https://files.helpdocs.io/i5nl071jo5/articles/qibyllcmza/1636688998165/z-z-463-f-n-851-z-qgiskzdy-eof-xmd-cg-ebx-ny-r-ltcom-nh-1-ymgbs-xu-nfhpd-48-hvb-yj-6-nu-pe-uj-0-iav-g-2-efhx-sxi-ol-pmg-gwzx-ggw-0-m-6-r-29-g-bj-la-ql-ebq-4-w-5-lq-4-obf-6-w-1-tli-q-06-u-dnhhbzw){style="max-height:50%;max-width:50%"
hd-height="50%" hd-width="50%"}

When you are done, click **Apply Changes**.

### Step 5: Run Pipeline

Click **Save** to save the changes, then click **Run Pipeline**. 

### Step 6: View the Results

You can see the logs for the Pipeline as it runs.

#### Save Cache Stage Output

In the Save Cache stage, you can see the logs for Save Cache to S3 step
in the Pipeline as it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/qibyllcmza/1636688942744/5-q-su-6-x-4-lor-32-aq-vhehh-7-hv-fl-q-0-ib-wmj-x-7-wt-6-hid-9-b-rpf-sjaqi-8-z-5-o-rw-o-af-2-d-byln-o-3-t-dfcsa-e-34-rn-xw-jggn-i-e-ci-8-g-8-n-bs-htvk-vgpvnt-go-epn-wf-d-9-zoqa-jlqul-o-0-ys-54){style="max-height:50%;max-width:50%"
hd-height="50%" hd-width="50%"}

    level=info name=drone-cache ts=2021-11-11T07:08:02.169728067Z caller=rebuilder.go:93 component=plugin component=rebuilder msg="cache built" took=217.977195ms

#### Restore Cache Stage Output

In the Restore Cache stage, you can see the logs for Restore Saved Cache
from the S3 step in the Pipeline as it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/qibyllcmza/1636688932988/r-pelu-1-vp-uyknq-citu-4-m-ox-0-w-orpby-1-n-ra-eo-aiwp-ev-hh-fiyvz-dyzjjba-1-j-uc-h-9-qhop-sheyuhvsvn-swf-ilqtt-yn-v-22-kw-k-9-qa-3-o-gvew-5-ffg-3-n-9-jmfi-1-jjrzg-7-fy-xyk-ddkas-aqw-ry){style="max-height:50%;max-width:50%"
hd-height="50%" hd-width="50%"}

    level=info name=drone-cache ts=2021-11-11T07:08:15.915788644Z caller=restorer.go:94 component=plugin component=restorer msg="cache restored" took=439.384074ms

### See Also

-   [Save and Restore Cache from
    GCS](/article/v0agy0hlyj-save-cache-in-gcs)
