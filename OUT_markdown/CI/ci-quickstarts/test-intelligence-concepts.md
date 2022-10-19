---
title: Test Intelligence
description: Harness Test Intelligence dramatically improves test time by running only those tests required to confirm the quality of the code changes which triggered the build
tags: 
   - helpDocs
helpdocs_topic_id: vtu9k1dsfa
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes Harness Test Intelligence (TI). TI dramatically
improves test times by running only the tests required to confirm the
quality of the code changes that triggered the CI Pipeline.

Test Intelligence is supported for Java and .NET Core codebases only at
this time.

### Before You Begin

Before learning about Test Intelligence, you should understand the
following:

-   [Harness Key
    Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)
-   [Run a script in CI
    Stage](https://ngdocs.harness.io/article/ota4xj59le-run-a-script-in-a-ci-stage)

### Visual Summary

The following video walks you through setting up Test Intelligence in
the Harness CIE stage. The TI section starts after 11 min. mark in the
video.

::: {.hd--embed provider="YouTube" thumbnail="https://i.ytimg.com/vi/kZmOCLCpvmk/hqdefault.jpg"}
::: iframe
::: {#player}
:::

::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on
www.youtube.com](https://www.youtube.com/watch?v=eAtIO4bJ3No){target="_blank"},
or enable JavaScript if it is disabled in your browser.
:::
:::
:::
:::

### Overview

Testing is an important part of Continuous Integration (CI). Testing
safeguards the quality of your product before shipping. But testing can
also take a lot of time because a test cycle involves multiple tests.
Often, the tests run are irrelevant to the code changes that triggered
the build.

Harness TI helps your test cycle move faster without compromising on
quality. 

At runtime, TI selects only those tests you need to run. Instead of
running all your tests, TI selects a subset of tests and skips the
rest. 

You\'ll have full visibility on which tests were selected and why. TI
doesn't require you to update your source code or build and test
process.

### How Does Test Intelligence Work?

Test Intelligence (TI) does the following:

-   Prioritizes and runs only important tests. Running all unit tests
    every time the code changes is expensive and time-consuming.
-   Identifies negative trends and provides actionable insights to
    improve quality. 

### What Does Test Intelligence Do?

Test Intelligence builds software faster than a full build-and-test run
by doing the following:

Test Selection: TI runs only the tests required to confirm the quality
of the code changes that triggered the build. TI also includes any newly
added or modified tests.

To ensure full accuracy, TI uses the call graph of the instrumented
source code. 

### What are the Test Intelligence Components?

#### Test Intelligence Service

Test Intelligence (TI) runs as a service, agnostic to the CI solution. 

A TI service manages the data about repositories, git-commit graphs,
test results, and call graphs. 

During the selection phase, a TI service uses the list of added/modified
files with the call graph to identify which tests to run.

The TI service can also receive real-time webhook notifications from Git
for any commit or merge. The TI service pulls the git commit-graph and
other metadata from Git for test selection and ordering. When the TI
test runner agent sends a call graph generated from a PR, the TI service
keeps that data in a staging area in case the PR doesn't get merged to
the master. Once the TI receives the merge notification from Git, it
updates and inserts the partial call graph with the master call graph.

#### Test Runner Agent

The Test Runner Agent runs on the build infrastructure. It\'s
responsible for communicating with the TI service. Whenever a test step
is about to execute, the Test Runner Agent communicates with the TI
service providing the build number, commit-id, and other details. The TI
service returns the ordered selected tests to run. The Test Runner Agent
runs the tests with the instrumentation ON. After all the test
completion, the agent parses the test results and uploads the results
along with the newly generated call graph.

#### TI and the Test Step Packaging

The Test Step is similar to the Run Step, but it accepts additional
information such as the programming language of the source code being
tested, build tools, and other parameters. 

TI identifies the programming language and uses the Test step to run the
selected tests in the Test step container. The Test step parses test
results and returns the results to the TI service.

### How Does TI Sync with Tests?

TI is always up to date and syncs when you merge the code to the main
branch.

When you perform a pull request, TI determines which tests should be run
based on the following metrics:

-   Changed Code: TI queries Git to learn exactly which code has changed
    in a specific build. TI uses this data to select all the tests that
    are associated directly, or indirectly, with the source code
    changes. TI selects these tests as part of the subset of the tests
    run in the Pipeline. Lastly, TI skips tests that aren\'t needed
    because there was no relevant code change.
-   Changed Tests: When a specific test change is identified, TI chooses
    it even if the code it covers hasn\'t changed.
-   New Tests: As soon as Harness identifies a new test,
    it\'s automatically selected. This ensures that the test is running
    successfully and also finds correlations between the test and
    new/existing code.

After each test cycle, you have full visibility into which tests were
selected by TI and why. You can also see the visualization graph on your
Pipeline Tests page.

### Viewing Tests Selected by TI

Here\'s an example of a specific PR. You can see the number of Selected
Tests and Time Saved.  On the right, you can see a breakdown of the
selection. 

![](https://files.helpdocs.io/i5nl071jo5/articles/vtu9k1dsfa/1630596895878/ti-desc.png){style="max-height:80%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="80%" hd-width="70%" hd-align="left"}

We also provide full visualization of the test graph. It shows the
reason behind every test selection. Click on any test (the purple node),
and you can see all the classes and methods covered by this test. These
are the changed classes and methods (denoted by the blue nodes), which
led to the selection of that test.

![](https://files.helpdocs.io/i5nl071jo5/articles/vtu9k1dsfa/1630477676163/98-xp-7-u-6-ocyq-688-smq-znjtui-ib-20-u-7-b-2-t-w-pox-ibyt-yvyjo-2-p-sbacz-m-4-uqz-avguz-bervc-1-ukpfhgqd-qbhhd-slh-dl-lx-7-cjqzdz-i-met-kp-66-q-y-j-2-hnkb-s-131-f-8-vyhk-uxq-c-8-mmfw-8-c-s-0){style="max-height:80%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="80%" hd-width="70%" hd-align="left"}

### What Can You Achieve With Test Intelligence?

Here's a summary of what we achieved running Test Intelligence on our
biggest repository, Harness-Core.

![](https://files.helpdocs.io/i5nl071jo5/articles/vtu9k1dsfa/1630477664781/cb-ot-pg-04-ovrt-ie-1-ok-jdu-olse-jc-4-q-ti-7-iqn-rf-2-s-oazst-hsvv-d-1-z-7-q-fdbpv-3-rz-25-i-9-jfzs-c-8-dha-rye-xc-mo-ipzz-vv-zv-a-8-q-c-ysv-r-y-1-m-ulr-4-y-ync-45-i-1-o-89-u-8-dv-n-6-w-29-nhwg-6-y-s-0){style="max-height:80%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="80%" hd-width="70%" hd-align="left"}

Here's how Harness Test Intelligence performed with some popular
open-source repositories:

+-----------------------+-----------------------+-----------------------+
| **Project Name**      | **Avg Test Execution  | **Avg Test Execution  |
|                       | Time without TI**     | time **               |
|                       |                       |                       |
|                       |                       | **with TI**           |
+-----------------------+-----------------------+-----------------------+
| Harness-Core          | 43 mins               | 32 mins               |
+-----------------------+-----------------------+-----------------------+
| Incubator Pinot       | 338 mins              | 228 mins              |
+-----------------------+-----------------------+-----------------------+
| Hudi                  | 58 mins               | 43 mins               |
+-----------------------+-----------------------+-----------------------+
| RocketMQ              | 4.6 mins              | 3.1 mins              |
+-----------------------+-----------------------+-----------------------+
| Spring Cloud Alibaba  | 0.744 mins            | 0.59 mins             |
+-----------------------+-----------------------+-----------------------+
| Incubator Shenyu      | 1.16 min              | 0.4 min               |
+-----------------------+-----------------------+-----------------------+
| Sentinel              | 1.90 min              | 1 min                 |
+-----------------------+-----------------------+-----------------------+

### Try It Yourself

Interested in trying Test Intelligence yourself? Wait no more! It\'s
available as part of the Harness CI free trial --- [Sign
up](https://harness.io/pricing/){target="_blank"} and give it a spin! 

### See Also

[Set up Test Intelligence](https://ngdocs.harness.io/article/428cs02e6u)
