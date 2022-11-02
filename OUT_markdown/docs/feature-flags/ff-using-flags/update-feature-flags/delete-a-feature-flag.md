---
title: Delete a Feature Flag
description: When you are finished with a Feature Flag, it's best practice to remove it to keep your Flags and application organised and tidy. This topic describes how to delete a Feature Flag on the Harness Plat…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: h4qn3szedc
helpdocs_category_id: skrwlcueml
helpdocs_is_private: false
helpdocs_is_published: true
---

When you are finished with a Feature Flag, it's best practice to remove it to keep your Flags and application organised and tidy. This topic describes how to delete a Feature Flag on the Harness Platform and using [Git](/article/6f5eylg819-manage-featureflags-in-git-repos).


Make sure you are ready to delete the Flag from all of your Environments. When you delete a Flag on the Harness Platform or on Git, it is removed from all Environments.
### Delete a Flag using the Harness Platform


1. In Harness, go to **Feature Flags**, then to the Flag you want to delete.
2. Click **more options (****︙****)**next to the flag that you want to delete, then click **Delete**.


![A screenshot showing the Delete button for deleting a Flag on the Harness Platform.](https://files.helpdocs.io/kw8ldg1itf/articles/h4qn3szedc/1660563628196/2022-08-15-12-38-23.png)
*Figure 1: Delete a Flag*


1. In **Delete Flag**, click **Delete**.


### Delete a Flag using Git


If you [have set up Git Experience to manage your Flags](/article/6f5eylg819-manage-featureflags-in-git-repos) via a `.yaml` file on Git, you can delete Flags from there. To do this:


1. Go to the `.yaml` file where you manage your Feature Flags.
2. Find the Flag you want to delete.
3. Delete the `- flag` object. For example, the following highlighted section would be deleted for the Flag called `New_Flag:`


![The .yaml file on Github. The flag object is highlighed for deletion. ](https://files.helpdocs.io/kw8ldg1itf/articles/h4qn3szedc/1660569642238/2022-08-15-14-20-26.png)
*Figure 2: Sample YAML file with the Flag object highlighted*

