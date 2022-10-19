---
title: STO Basics
description: Enable DevOps and DevSecOps teams to left shift security testing.
tags: 
   - helpDocs
helpdocs_topic_id: ap7y94ap7h
helpdocs_is_private: false
helpdocs_is_published: true
---

Companies perform security testing to avoid introducing vulnerabilities
into the products their customers depend on. If a customer catches the
security issue instead of the company, trust is lost.

Harness Security Testing Orchestration (STO) enables DevOps and
DevSecOps teams to left shift security testing. STO orchestrates
scanning, intelligently deduplicating scanner output, prioritizing
remediations, and enforcing governance into your Pipeline. STO puts
scanning directly into your Pipelines to ensure that vulnerabilities are
caught and fixed before your products are ever released.

This topic describes the security scanning problems facing developers
and how STO provides the solutions they need.

### Common Scanning Problems

Some of the many of the problems with current security testing:

-   **Mostly manual and standalone:** scanners are run individually on
    parts of a release manually, instead of integrated into the Pipeline
    and run automatically.
-   **Too slow or delayed:** identifying vulnerabilities is often done
    after the vulnerabilities are released.
-   **Siloed visibility:** multiple tools for different types of scans
    reduces the overall visibility into your product\'s vulnerabilities.
-   **Inconsistent Governance:** developers don\'t have guidance and
    governance to help them decide where scans should be in their
    release process.
-   **Not integrated with CI/CD:** scans happen outside of the Pipeline
    instead of acting as gate checks.

#### Delayed Feedback Loop

Current security testing is challenging for DevOps teams because most
security testing is done right before code has reached production. This
is a delayed feedback loop.

![](https://files.helpdocs.io/i5nl071jo5/articles/ap7y94ap7h/1647988169396/clean-shot-2022-03-22-at-15-29-09.png)

All of the release stages where security testing could have been applied
are past, and fixing the issue requires reworking each stage.

Developers need to move forward but by the time the security testing
feedback arrives it could be days or weeks later and they have to stop
current work and fix it.

#### DevSecOps Complexity Problem

DevSecOps is too complicated because there are many tools for so many
types of scanning and the outputs from all these tools are disparate.
There is no uniform data format or language.

![](https://files.helpdocs.io/i5nl071jo5/articles/ap7y94ap7h/1647988618571/clean-shot-2022-03-22-at-15-36-03.png)

Consequently, developers don\'t have a deduplicated and prioritized list
of vulnerabilities to remedy.

So DevSecOps must normalize all the output, track exemptions, and
verifying fixes. This all requires DevSecOps synchronization with
developers, and it takes DevSecOps away from other work.

In addition, developers, PMs, DevSecOps, and others have to act on the
information provided from security testing, but ensuring that these are
the only vulnerabilities is challenging.

### Harness Security Testing Orchestration (STO) Solution

Harness STO enables DevOps and DevSecOps teams to left shift security
testing:

-   **Test:** test code, OSS libraries, containers, and live apps with
    popular security scanners as part of the CI/CD Pipeline. Harness
    orchestrates the scanners to ensure that scanning is timely and easy
    to apply.
-   **Remediate:** repair security vulnerabilities by empowering
    developers with a prioritized list that is intelligently
    deduplicated across all scanners. Harness provides dashboards with
    clear security vulnerabilities identified.
-   **Govern:** use governance policies and real-time security
    dashboards for ensuring critical security issues never make it to
    production. You can apply [Harness existing OPA policy
    governance](/article/1d3lmhv4jl-harness-governance-overview) to
    enforce your security testing practices.

With Harness STO, you are scanning at any stage in the CI/CD Pipeline,
and providing developers with deduplicated and prioritized
vulnerabilities:

![](https://files.helpdocs.io/i5nl071jo5/articles/ap7y94ap7h/1647974851933/image.png)

### Quick Summary

The following 1min video provides a quick summary of STO:

::: {.hd--embed provider="Wistia" thumbnail=""}
:::

### STO Features

Harness STO automatically aggregates, normalizes, and deduplicates data
to identify vulnerabilities across all your scanners. You can use STO
with no other Harness modules. See [STO Tutorial 1: Standalone STO
Workflows](https://docs.harness.io/article/t57yct5guh){target="_blank"}.

You can also include STO features in CI and CD workflows. You can set up
your Pipelines to scan repos, images, and artifacts, and then fail the
Pipeline automatically if any \"show-stopper\" vulnerabilities are
detected. See [STO Quickstart 2: Integrated STO/CI/CD
Workflows](https://docs.harness.io/article/zy4h4ch6dh){target="_blank"}.

![](https://files.helpdocs.io/kw8ldg1itf/articles/ap7y94ap7h/1660650807410/sto-overview-update.png)

Now let\'s apply these features to common use cases:

+-----------------+-----------------+-----------------+-----------------+
| **Use Cases**   | **Shift Left    | **              | **Governance,   |
|                 | Security        | Developer-first | Dashboards &    |
|                 | Testing To      | Remediation**   | Reports**       |
|                 | CI/CD           |                 |                 |
|                 | Pipeline**      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Features**    | -   STO built   | -               | -   Pipeline    |
|                 |     into        |   Deduplication |     design and  |
|                 |     Harness     |     and         |     deployment  |
|                 |     CI/CD       |                 |     governance. |
|                 |     Pipelines.  |  prioritization | -   Audit       |
|                 | -   STO         |     across all  |     trails for  |
|                 |     standalone  |     scanners.   |     scan        |
|                 |     stage added | -               |     execution,  |
|                 |     to Harness  |  Categorization |     approvals,  |
|                 |     CD.         |     of new vs.  |     and policy  |
|                 | -   STO         |     existing    |                 |
|                 |     standalone  |                 |    enforcement. |
|                 |     stage       | vulnerabilities | -   Enterprise  |
|                 |     initiated   |                 |     dashboards  |
|                 |     from any    |   (with/without |     and         |
|                 |     CI/CD       |                 |     reports.    |
|                 |     stage.      |    exemptions). |                 |
+-----------------+-----------------+-----------------+-----------------+

### Scanner Coverage

For a list of supported scanners, see [Scanners, Target Types, and Scan
Approach](https://docs.harness.io/article/0k0iubnzql#scanners_target_types_and_scan_approach){target="_blank"}.

### Next Steps

-   [Security Testing Orchestration
    Quickstart](/article/b5jv0vlrvf-security-testing-orchestration-quickstart)
