---
title: Select Delegates with Delegate Selectors and Tags
description: Use Delegate Tags to select specific Delegates in Connectors, steps, and more.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: nnuf8yv13o
helpdocs_category_id: m9iau0y3hv
helpdocs_is_private: false
helpdocs_is_published: true
---

When Harness needs to run a task, it makes a connection to a resource via the Harness Delegates you have set up in your environment.

Harness selects the best Delegate according to its history or it round robins between Delegates. See [How Does Harness Manager Pick Delegates?](/article/2k7lnc7lvl-delegates-overview#how_does_harness_manager_pick_delegates).

In some cases, you might want Harness to select specific Delegates. In these cases, you can use the **Delegate Selector** settings in Pipelines, Connectors, etc and corresponding Delegate Tags.

### Before You Begin

* [Learn Harness' Key Concepts](/article/hv2758ro4e-learn-harness-key-concepts)
* [Delegates Overview](/article/2k7lnc7lvl-delegates-overview)
* [Delegate Installation Overview](/article/re8kk0ex4k-delegate-installation-overview)
* [Install a Kubernetes Delegate](/article/f9bd10b3nj-install-a-kubernetes-delegate)

### Review: Delegate Tags

A Delegate Tag is added to your Delegate automatically when you set it up in Harness. The Tag is added using the name you give your Delegate.

You can also add more Tags using the Tags setting:

![](https://files.helpdocs.io/i5nl071jo5/articles/nnuf8yv13o/1654274177068/clean-shot-2022-06-03-at-09-35-54.png)For detailed information on how Delegates are selected during execution, see [Delegates Overview](/article/2k7lnc7lvl-delegates-overview).

Once a Delegate has Tags, the Delegate can be selected in the **Delegate Selector** settings of Harness entities like Pipelines and Connectors.

### Review: Delegate Selector Priority

You can use Delegate Selectors at multiple places, such as the Pipeline, Stage, and Step levels.

It's important to know which Delegate Selectors are given priority so that you ensure the correct Delegate is used when you want it used.

The Delegate Selector Priority is:

1. Step
2. Step Group
3. Stage
4. Pipeline
5. Connector

![](https://files.helpdocs.io/kw8ldg1itf/articles/nnuf8yv13o/1657746136816/clean-shot-2022-07-13-at-14-02-04.png)The Step level has the highest priority. Any Delegate selected in a Step's **Delegate Selector** setting overrides any Delegates selected in 2-5 above.

A Connector can be used in multiple places in a Pipeline, such as a Stage Infrastructure's **Cloud Provider** setting or even in certain step settings.### Option: Step and Step Group Delegate Selector

Delegates can be selected for Steps and [Step Groups](/article/ihnuhrtxe3-run-steps-in-parallel-using-a-step-group) in their **Advanced** settings.

Here is a step example:

![](https://files.helpdocs.io/kw8ldg1itf/articles/nnuf8yv13o/1657742633092/clean-shot-2022-07-13-at-13-03-12.png)Here is a Step Group example:

![](https://files.helpdocs.io/kw8ldg1itf/articles/nnuf8yv13o/1657742697622/clean-shot-2022-07-13-at-13-04-15.png)### Option: Select a Delegate for a Connector using Tags

When you add a Connector you are given the option of connecting to your third part account using any available Delegate or specific Delegates.

![](https://files.helpdocs.io/i5nl071jo5/articles/nnuf8yv13o/1625693513715/clean-shot-2021-07-07-at-14-31-31.png)You select specific Delegates using their Tags.

You only need to select one of a Delegate's Tags to select it. All Delegates with the Tag are selected.

Here, the Tag is **test1**, and you can see multiple Delegates match it:

![](https://files.helpdocs.io/i5nl071jo5/articles/nnuf8yv13o/1625693674019/clean-shot-2021-07-07-at-14-34-13.png)### Option: Pipeline Delegate Selector

Delegates can be selected for an entire Pipeline in the Pipeline **Advanced Options** settings.

![](https://files.helpdocs.io/kw8ldg1itf/articles/nnuf8yv13o/1657742306209/clean-shot-2022-07-13-at-12-58-04.png)### Option: Stage Delegate Selector

Delegates can be selected for an entire Stage in the Stage **Advanced** settings.

![](https://files.helpdocs.io/kw8ldg1itf/articles/nnuf8yv13o/1657742384596/clean-shot-2022-07-13-at-12-59-30.png)### Option: Infrastructure Connector

Delegates can be selected for the Connector used in a Stage's Infrastructure settings, such as a CD Stage's **Cluster Details** > **Connector** setting.

![](https://files.helpdocs.io/kw8ldg1itf/articles/nnuf8yv13o/1657742439869/clean-shot-2022-07-13-at-13-00-20.png)### Option: Select a Delegate for a Step using Tags

You can select one or more Delegates for each Pipeline step.

In each step, in **Advanced**, there in the **Delegate Selector** option:

![](https://files.helpdocs.io/i5nl071jo5/articles/nnuf8yv13o/1625694858143/clean-shot-2021-07-07-at-14-54-08.png)You only need to select one of a Delegate's Tags to select it. All Delegates with the Tag are selected.

### Option: Modify Tags via API

See [Delegate Group Tags Resource](https://harness.io/docs/api/tag/Delegate-Group-Tags-Resource/).

### See Also

* [Delegates Overview](/article/2k7lnc7lvl-delegates-overview)

