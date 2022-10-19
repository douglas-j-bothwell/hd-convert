---
title: Export Perspective Data
description: export your Perspectives reports as CSV files
tags: 
   - helpDocs
helpdocs_topic_id: t07cnubtp1
helpdocs_is_private: false
helpdocs_is_published: true
---

You can export your Perspectives reports as comma-separated values (CSV) files. Exporting allows you to use the data in other software.

### Before You Begin

* [Set Up Cloud Cost Management for AWS](../set-up-cloud-cost-management/set-up-cost-visibility-for-aws.md)
* [Set Up Cloud Cost Management for GCP](../set-up-cloud-cost-management/set-up-cost-visibility-for-gcp.md)
* [Set Up Cloud Cost Management for Azure](../set-up-cloud-cost-management/set-up-cost-visibility-for-azure.md)
* [Set Up Cloud Cost Management for Kubernetes](../set-up-cloud-cost-management/set-up-cost-visibility-for-kubernetes.md)
* [Create Cost Perspectives](create-cost-perspectives.md)

### Limitations

* Only comma-separated values files (CSV) are supported.
* The maximum number of rows allowed in one export is 10,000 rows. If you have more rows, you can export separate CSV files using the **Export rows up to** option.
* The more rows you export, the slower the export will be.

### Step 1: Create a Perspective Export

Open a Perspective.

Below the **Group By** graph, you can see the **Export CSV** option.

![](https://files.helpdocs.io/i5nl071jo5/articles/t07cnubtp1/1656364542019/clean-shot-2022-06-27-at-14-14-40.png)Click **Export CSV**.

Enter a name for the CSV file.

In **Export rows up to**, enter the number of rows you want exported. The number of rows should be greater than or equal to 1.

### Option: Exclude rows with cost below

Use **Exclude rows with cost below** to set a cost ceiling on the cost data exported.

The amount must be a number. You cannot use symbols or punctuation.

### Step 2: Export the CSV

Click **Download**. 

Depending on your browser, you might be prompted to allow downloads.

 

![](https://files.helpdocs.io/i5nl071jo5/articles/t07cnubtp1/1656367252910/clean-shot-2022-06-27-at-14-53-37.png)The file is downloaded to your local computer.

