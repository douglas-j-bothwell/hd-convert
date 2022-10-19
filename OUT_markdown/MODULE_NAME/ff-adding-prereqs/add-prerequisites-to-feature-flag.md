---
title: Add a Prerequisite to Your Flags
description: This topic describes how to use feature flag prerequisites to enable or disable features based on different flag states.
tags: 
   - helpDocs
   - feature flag
   - prerequisites
helpdocs_topic_id: iijdahygdm
helpdocs_is_private: false
helpdocs_is_published: true
---

A Prerequisite is a Flag you add as a dependency that needs to be met before another Flag can be toggled `ON` or `OFF`. For example, if you have a Flag that allows users to write Java, the user must be able to read the Java first. Therefore, you add a Prerequisite that the `Read_Java` Flag must be enabled before the `Write_Java` Flag can be toggled on. 

### Add a Prerequisite

1. Go to the Feature Flag you want to add the Prerequisite to.
2. Click **+ New Prerequisite**.

![A screenshot of the Write Java Flag with the Prerequisites button highlighted.](https://files.helpdocs.io/kw8ldg1itf/articles/iijdahygdm/1657796522532/screenshot-2022-07-14-at-12-01-19.png)*Figure 1: Adding a Prerequisite*

1. In **Add Prerequisites**, click **+ Prerequisites**.
2. In the first drop-down menu, select the Flag you want to use as a Prerequisite.
3. In the second drop-down, select which Variation of the Prerequisite Flag must be served before the Feature Flag can be turned on. For the example below, the Read\_Java Flag must be set to `True` before this Flag can be enabled.
4. Click **Save**. The Prerequisite Flag is listed on the Feature Flag page and must be met before you can turn on the Feature Flag.

![A screenshot of the Prerequisite Flag added to the Write_Java Flag.](https://files.helpdocs.io/kw8ldg1itf/articles/iijdahygdm/1657796709480/screenshot-2022-07-14-at-12-04-25.png)*Figure 2: The Read\_Java Flag as a Prerequisite to the Write\_Java Flag*

