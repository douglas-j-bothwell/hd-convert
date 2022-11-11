---
title: Bandit Scanner Reference
description: You can set up a Security step with Bandit to find common security issues in your Python code.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: n3dcx6wzb3
helpdocs_category_id: m01pu2ubai
helpdocs_is_private: false
helpdocs_is_published: true
---

You can set up a Security step with [Bandit](https://bandit.readthedocs.io/en/latest/) to find common security issues in your Python code.

### Scan policy types

STO supports the following policy\_type settings for Bandit:

* `orchestratedScan`  — A Security step in the pipeline runs the scan and ingests the results. This is the easiest to set up and supports scans with default or predefined settings.
* `ingestionOnly` — Run the scan in a Run step, or outside the pipeline, and then ingest the results. This is useful for advanced workflows that address specific security needs. See [Ingest scan results into an STO pipeline](https://docs.harness.io/article/ijkyokxrot).

### Required Settings

* `product_name` = `bandit`
* `scan_type` = `repository`
* `product_config_name` = `default` — Run a Bandit scan with the default settings.
* `repository_project` — The repository name. If you want to scan https://github.com/my-github-account/codebaseAlpha, for example, you would set this to `codebaseAlpha`.
* `repository_branch` — This tells Bandit the Git branch to scan. You can specify a hardcoded string or use the runtime variable [`<+codebase.branch>`](https://docs.harness.io/article/576gjpak61-built-in-cie-codebase-variables-reference). This sets the branch based on the user input or trigger payload at runtime.

