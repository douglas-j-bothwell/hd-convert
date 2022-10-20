---
title: Save and Restore Cache from GCS
description: Caching has two primary benefits&#58; It can make your jobs run faster by reusing the expensive fetch operation data from previous jobs. . It enables you to share data across Stages. In a Harness CI Pipe…
tags: 
   - helpDocs
helpdocs_topic_id: v0agy0hlyj
helpdocs_is_private: false
helpdocs_is_published: true
---

Caching has two primary benefits:

-   It can make your jobs run faster by reusing the expensive fetch
    operation data from previous jobs. 
-   It enables you to share data across Stages.

In a Harness CI Pipeline, you can save the cache to Google Cloud Storage
(GCS) bucket in one stage using the Save Cache to GCS step and then
restore it in the same or another stage using Restore Cache from GCS
step. 

The topic explains how to configure the Save Cache to GCS and Restore
Cache from GCS steps in CIE using a two-Stage Pipeline.

::: note-callout
You cannot share access credentials or other [Text
Secrets](https://ngdocs.harness.io/article/osfw70e59c-add-use-text-secrets)
across Stages.
:::

### Before You Begin {#undefined}

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

### Review: YAML Example {#undefined}

If you want to configure your Pipeline in YAML, in **Pipeline
Studio,** click **YAML**. 

The following YAML file defines a Pipeline with two Stages: Save Cache
and Restore Cache. Copy the following YAML, paste it in the Harness YAML
editor, and modify its attributes based on your Pipeline requirements.

``` {.hljs .yaml}
pipeline:
    identifier: GCS_Save_and_Restore_Cache
    name: GCS Save and Restore Cache
    stages:
        - stage:
              identifier: GCS_Save_Cache
              name: GCS Save Cache
              type: CI
              variables:
                  - name: GCP_Access_Key
                    type: String
                    value: <+input>
                  - name: GCP_Secret_Key
                    type: Secret
                    value: <+input>
              spec:
                  sharedPaths:
                      - /.config
                      - /.gsutil
                  execution:
                      steps:
                          - step:
                                identifier: createBucket
                                name: create bucket
                                type: Run
                                spec:
                                    connectorRef: <+input>
                                    image: google/cloud-sdk:alpine
                                    command: |+
                                        echo $GCP_SECRET_KEY > secret.json
                                        cat secret.json
                                        gcloud auth -q activate-service-account --key-file=secret.json
                                        gsutil rm -r gs://harness-gcs-cache-tar || true

                                        gsutil mb -p ci-play gs://harness-gcs-cache-tar

                                    privileged: false
                          - step:
                                identifier: saveCacheTar
                                name: Save Cache
                                type: SaveCacheGCS
                                spec:
                                    connectorRef: <+input>
                                    bucket: harness-gcs-cache-tar
                                    key: cache-tar
                                    sourcePaths:
                                        - <+input>
                                    archiveFormat: Tar
                  infrastructure:
                      type: KubernetesDirect
                      spec:
                          connectorRef: <+input>
                          namespace: default
                  cloneCodebase: true
        - stage:
              identifier: gcs_restore_cache
              name: GCS Restore Cache
              type: CI
              variables:
                  - name: GCP_Access_Key
                    type: String
                    value: <+input>
                  - name: GCP_Secret_Key
                    type: Secret
                    value: <+input>
              spec:
                  sharedPaths:
                      - /.config
                      - /.gsutil
                  execution:
                      steps:
                          - step:
                                identifier: restoreCacheTar
                                name: Restore Cache
                                type: RestoreCacheGCS
                                spec:
                                    connectorRef: <+input>
                                    bucket: harness-gcs-cache-tar
                                    key: cache-tar
                                    archiveFormat: Tar
                                    failIfKeyNotFound: true
                  infrastructure:
                      useFromStage: gcs_save_cache
                  cloneCodebase: false
 
```

### Step 1: Open the Build Stage {#undefined}

In your Harness Pipeline, open the Stage where you want to save the
cache.

### Step 2: Define the Build Farm Infrastructure {#undefined}

In the Infrastructure tab, define the build farm for the codebase.

The following step uses a Kubernetes cluster build farm.

See [Define Kubernetes Cluster Build
Infrastructure](https://ngdocs.harness.io/article/x7aedul8qs-kubernetes-cluster-build-infrastructure-setup).

### Step 3: Save Cache to GCS {#undefined}

In the Execution tab, click **Add Step** and then select **Save Cache to
GCS**. Here you configure the GCS bucket, keys, and source paths to
enable Harness to save the cache to GCS.

For step settings, see [Save Cache to GCS Step
Settings](/article/11nzeuntrz-save-cache-to-gcs-step-settings).

![](./static/save-cache-in-gcs-00.png){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

### Step 4: Restore Cache from GCS Stage

In your Pipeline, click **Add Stage** where you want to restore the
saved cache from GCS. 

In the Execution tab, click **Add Step** and then select **Restore Cache
from GCS**. Here you configure the GCS bucket keys on which you have
your saved cache.

For step settings, see [Restore Cache Step
Settings](/article/zlpx6lli6d-restore-cache-from-s-3-step-settings).

![](https://files.helpdocs.io/i5nl071jo5/articles/v0agy0hlyj/1636692026066/zyucv-ui-f-4-al-29-rh-ld-89-y-kqe-gvwwpu-dh-xfw-kd-i-0-ek-jl-q-70-p-ztu-bzc-xxekr-4-uqn-p-6-p-2-t-y-57-a-6-cy-0-dvk-ouxr-56-qvikega-mlh-o-8-xqeczz-xmke-eoe-qm-7-js-m-ysa-z-k-2-s-wcdo-tidu){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

When you are done, click **Apply Changes**.

### Step 5: Run Pipeline

Click **Save** to save the changes, then click **Run Pipeline**. 

### Step 6: View the Results

You can see the logs for the Pipeline as it runs.

#### Save Cache Stage Output

In the Save Cache stage, you can see the logs for **Save Cache to GCS**
step in the Pipeline as it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/v0agy0hlyj/1636692038272/7-l-71-d-i-299-k-gmdcsez-xi-0-d-sktn-ahjm-r-1-kfpjow-vntx-y-4-zxai-io-7-w-2-unw-l-4-d-1-mc-nma-av-m-5-m-3-he-47-thjv-bccgj-in-rk-nmrcn-syin-4-od-3-uvbr-3-yf-ql-m-3-q-tkx-sd-1-wvqat-hiul-e-5-rnq){style="max-height:50%;max-width:50%"
hd-height="50%" hd-width="50%"}

    level=info name=drone-cache ts=2021-11-11T09:06:48.834761074Z caller=rebuilder.go:93 component=plugin component=rebuilder msg="cache built" took=253.210746ms

#### Restore Cache Stage Output

In the Restore Cache stage, you can see the logs for **Restore Cache
from GCS** step in the Pipeline as it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/v0agy0hlyj/1636692067156/nni-uc-1-0-j-wlovaf-l-49-ufvwgyg-w-6-j-6-kyjqd-wwc-5-ilic-srxvn-93-a-ovy-s-82-yqnfwwe-dfj-txwe-um-1-e-6-x-h-2-i-3-h-9-oynudvqrc-qd-0-tv-crkv-7-prrqarfm-x-8-anm-n-9-bp-vwi-fqqa-rseh-z-0){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
hd-height="50%" hd-width="50%" hd-align="left"}

    level=info name=drone-cache ts=2021-11-11T09:07:00.803158076Z caller=restorer.go:94 component=plugin component=restorer msg="cache restored" took=239.769663ms

### See Also {#undefined}

-   [Save and Restore Cache from S3](/article/qibyllcmza-saving-cache)