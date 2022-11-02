---
title: Tutorial 2: Integrated STO Pipelines with CI/CD
description: This tutorial builds on Tutorial 1&#58; Standalone STO Workflows. You need to complete Tutorial 1 first. The Pipeline you created in Tutorial 1 is an example of a stand-alone STO workflow. It scans a tes…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: zy4h4ch6dh
helpdocs_category_id: 8nywcs2sa7
helpdocs_is_private: false
helpdocs_is_published: true
---

This tutorial builds on [Tutorial 1: Standalone STO Workflows](https://docs.harness.io/article/yvy4pmt8bw). You need to complete Tutorial 1 first.

The Pipeline you created in Tutorial 1 is an example of a stand-alone STO workflow. It scans a test target and reports on the vulnerabilities, but doesn't do anything else.

In this section, you'll learn how to integrate STO functionality into CI and CD Pipelines. The core benefit of STO in an integrated Pipeline is to fail the Pipeline if a scanner finds any "show-stopper" vulnerabilities. The following sections describe the different failure strategies you can implement.

For the list of supported scanners, see [Security Step Settings Reference](https://docs.harness.io/article/0k0iubnzql).

### Review: Ingestion Workflows

STO supports three different workflows to ingest scan results into a pipeline:

* [Orchestrated workflows](#orchestrated_workflows) — A Security step runs a scan with predefined settings and ingests the results.
* [Ingestion-Only workflows](#ingestion-only-workflows) — Run a scan in a Run step, or outside the pipeline, and save in a shared folder. A Security step then ingests the results.
* [Data-Load workflows](#data-load-workflows) — A Security step downloads and ingests results from an external scanner.

### Fail Pipelines on Severity

**Key Concept: Fail on Severity**  
Every Security Step supports a `fail_on_severity` setting. If any vulnerability with the specified severity or higher is found, the Pipeline fails. It is good practice to include this setting in every Security Step in an integrated Pipeline.1. In the Pipeline Studio, open the **STO Quickstart** pipeline > **STOLAB** stage > **bandit** step.
2. Under **Settings**, add the following: `fail_on_severity` = `CRITICAL`
3. Click **Apply Changes**, save the updated pipeline, and run a new build with the **DEMO-001** branch.  
The pipeline now fails because the bandit step is now configured to fail on any vulnerability with a severity of low or higher. The last log message in the bandit step log is:
```
Exited with message: fail_on_severity is set to CRITICAL and that threshold was reached.
```
![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659137645262/02-tests-demo-001-failed-severity-low.png)

### Exemptions for Specific Issues

**Key Concept: Issue Exemptions**  
In some cases, developers might want to create "ignore rules" that override the `fail_on_severity` setting. If an issue is marked as Ignored, it will not fail the Pipeline.  
Developer users cannot create Ignore Rules; only SecOps users have this permission.You're now acting as a Security Officer. A developer has sent a request to add two Ignore Rules to unblock their Pipeline temporarily. Do the following:

1. Go to the Security Tests page for the build you ran previously: Click **Security Tests** and then **Test Targets**. Then click the previous build you ran before the failed build.![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659138631300/02-a-tests-demo-001-goto-previous-branch.png)
2. In the **Security Tests** tab, go to the list of detected issues (bottom left). For each of the two critical issues, do the following:
	1. Click in the row to open the Issue Details pane.
	2. Click the **Ignore Issue** button.![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659108419315/01-c-tests-demo-001-branch-ignore-issue.png)![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659108396757/01-d-tests-demo-001-branch-ignore-issue.png)
3. Run another build with the DEMO-001 branch. When the build finishes, go to the **Security Tests** page.  
The Pipeline now finishes successfully, but the ignored issues still appear in the issues list with Status = Ignored.![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659204960237/exemption-dev-001-results-with-critical-ignored.png)
4. Go to **Security Tests** > **Security Review**. This page includes the Ignore Rules you just created. Click **Cancel Ignore** for both issues.

### Next Steps

You've now learned the core STO features and workflows. Here are the next steps you can take.

#### Add More Scanner Steps

STO supports an extensive set of external scanners for repos, images, and artifacts. See [Security Steps Reference](https://docs.harness.io/article/0k0iubnzql).

#### Add Steps or Stages for CI/CD Workflows

You know how to implement Pipelines when scanners detect security issues, and how to create Ignore Rules for specific issues. Once you set up your Security Steps, Baselines, and Ignore Rules, you can add more Stages and Steps to implement your CI/CD workflows.

#### Add Governance Policies

You can use the [Harness Policy Engine](https://docs.harness.io/article/1d3lmhv4jl) to create policies based on the [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) standard. For example, you could create a rule like the following to ensure that all Pipelines include a Security Stage.


```
package pipeline_required  
  
# Deny pipelines that are missing required steps  
deny[sprintf("CI stage '%s' is missing required step '%s'", [stage.name, existing_steps])] {   
     stage = input.pipeline.stages[i].stage                                # Find all stages ...   
     stage.type == "CI"                                                    # ... that are CI Stages  
     existing_steps := [ s | s = stage.spec.execution.steps[_].step.type ] # ... and create a list of all step types in use   
     required_step := required_steps[_]                                    # For each required step ...   
     not contains(existing_steps, required_step)                           # ... check if it's present in the existing steps  
}  
  
# Steps that must be present in every CI Stage - try to create a CI Stage without a Security Step to see the policy fail  
required_steps = ["Security"]  
  
contains(arr, elem) {   
    arr[_] = elem  
}
```
#### Add Failure Strategies to a CI/CD Stage

You can implement [Failure Strategies](https://docs.harness.io/article/0zvnn5s1ph) to bypass the failure policies in previous Security steps. One use case for this would be to enable manual interventions when a Security Step generates a failure. You could set up a workflow like this:

1. A Build Step is downstream from the Security Step. It has a Failure Strategy that's set to run on [All Errors](https://docs.harness.io/article/htrur23poj#error_types).
2. The scanner detects issues and the Security Step generates an error.
3. The Failure Strategy in the Build Step initiates a 30-minute pause before proceeding.
4. The developer and security team evaluate the issues and then abort the Pipeline or allow it to proceed.

### Integrated STO/CI Workflow Example

The following Pipeline provides a simple example of how you can implement STO into a CI workflow. This is an expanded version of the standalone STO Stage we have been working with. The [YAML](https://docs.harness.io/article/qhgshfw3mg#integrated_workflow_yaml) of this pipeline is provided below.

![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659290775295/integrated-workflow-pipeline.png)This Pipeline works as follows:

1. The **owasp scan** step has `fail_on_severity` set to `HIGH`. It scans the **master** branch of the [dvpwa](https://github.com/anxolerd/dvpwa) repo and detects one Critical issue, which results in an error.
2. The **Build Image** step is set up to build (but not push) an image from the dvpwa repo. It has a Failure Strategy that responds to the error from owasp as follows:
	1. Pauses the pipeline and waits for you to choose what to do. You examine the detected issues and decide if you want to proceed.
	2. If you don't choose to proceed after 20 minutes, the pipeline aborts.
3. If you click Proceed, the **Build Image** step builds an image from the repo.
4. The **aqua-trivy** step also has `fail_on_severity` set to `HIGH`. It scans the resulting image, detects issues with high and critical severities and generates an error, which causes the pipeline to fail.

You can view all issues from all scanners in the **Security Tests** tab, and also filter the issue list by scanner.

![](https://files.helpdocs.io/kw8ldg1itf/articles/qhgshfw3mg/1659295566043/integrated-workflow-scan-results.png)### Congratulations!

In this tutorial, you learned how to:

1. Add a STO Security stage to your Harness Pipelines.
2. Configure Security steps for different security scanners: one for code scanning and one for container scanning.
3. Run a Pipeline and scan its codebase and the container image.
4. View the normalized and deduplicated security results in the Security dashboard.

### Integrated Workflow YAML

Here's the YAML of the [integrated workflow example](https://docs.harness.io/article/yvy4pmt8bw) we examined previously.


```
pipeline:  
    name: quickstart-integrated-pipeline  
    identifier: quickstartintegratedpipeline  
    projectIdentifier: STO  
    orgIdentifier: default  
    tags: {}  
    properties:  
        ci:  
            codebase:  
                connectorRef: $CODEBASE_CONNECTOR  
                build: <+input>  
    stages:  
        - stage:  
              name: Docker Build and Scan  
              identifier: Docker_Build_and_Scan  
              type: CI  
              spec:  
                  cloneCodebase: true  
                  infrastructure:  
                      type: KubernetesDirect  
                      spec:  
                          connectorRef: $K8S_CONNECTOR  
                          namespace: harness-delegate-ng  
                          automountServiceAccountToken: true  
                          nodeSelector: {}  
                          os: Linux  
                  sharedPaths:  
                      - /var/run  
                  serviceDependencies:  
                      - identifier: dind  
                        name: dind  
                        type: Service  
                        spec:  
                            connectorRef: $DOCKER_CONNECTOR  
                            image: docker:dind  
                            privileged: true  
                            entrypoint:  
                                - dockerd-entrypoint.sh  
                  execution:  
                      steps:  
                          - step:  
                                type: Security  
                                name: owasp scan  
                                identifier: owasp_scan  
                                spec:  
                                    privileged: true  
                                    settings:  
                                        policy_type: orchestratedScan  
                                        scan_type: repository  
                                        repository_project: nodegoat  
                                        repository_branch: <+codebase.branch>  
                                        product_name: owasp  
                                        product_config_name: default  
                                        fail_on_severity: HIGH  
                                    imagePullPolicy: Always  
                                failureStrategies:  
                                    - onFailure:  
                                          errors:  
                                              - AllErrors  
                                          action:  
                                              type: Ignore  
                          - step:  
                                type: Run  
                                name: Build Image  
                                identifier: Build_Docker_Image  
                                spec:  
                                    connectorRef: $DOCKER_CONNECTOR  
                                    image: docker:latest  
                                    shell: Sh  
                                    command: |-  
                                        docker build .  -f Dockerfile.app -t nodegoat:local  
                                    privileged: true  
                                when:  
                                    stageStatus: All  
                                failureStrategies:  
                                    - onFailure:  
                                          errors:  
                                              - AllErrors  
                                          action:  
                                              type: ManualIntervention  
                                              spec:  
                                                  timeout: 20m  
                                                  onTimeout:  
                                                      action:  
                                                          type: Abort  
                          - step:  
                                type: Security  
                                name: aqua-trivy scan  
                                identifier: aqua_trivy_scan  
                                spec:  
                                    privileged: true  
                                    settings:  
                                        product_name: aqua-trivy  
                                        product_config_name: aqua-trivy  
                                        policy_type: orchestratedScan  
                                        scan_type: container  
                                        container_type: local_image  
                                        container_domain: docker.io  
                                        container_project: nodegoat  
                                        container_tag: local  
                                        fail_on_severity: HIGH  
                                    imagePullPolicy: Always  
                                failureStrategies: []  
              variables:  
                  - name: sto_api_key  
                    type: Secret  
                    value: <+input>  

```
### Congratulations!

In this tutorial you've learned how to use STO to protect repos, images, and artifacts from vulnerabilities automatically.

### See Also

* [STO Ingestion Workflows](https://docs.harness.io/article/cjqnd71y07)
* [Run an Orchestrated Scan in an STO Pipeline](https://docs.harness.io/article/wk018r6x3g)
* [Ingest Scan Results into an STO Pipeline](https://docs.harness.io/article/wk018r6x3g)
* [Security Step Settings Reference](https://docs.harness.io/article/0k0iubnzql)

