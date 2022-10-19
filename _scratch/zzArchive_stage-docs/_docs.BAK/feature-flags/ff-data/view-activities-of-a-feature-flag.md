---
title: View the Activities of Your Flags
description: This topic describes how to view the activity of a selected feature flag.
tags: 
   - helpDocs
   - feature flag
   - activity
   - YAML
helpdocs_topic_id: 51gbk0d2zh
helpdocs_is_private: false
helpdocs_is_published: true
---

The **Activity** tab allows you to view the actions performed on the
selected Feature Flag. The following details are available on the
Activity page:

-   **Time**: The time at which the Flag was turned `on` or `off`
-   **User**: Email ID of the user who performed the action on the
    selected Flag
-   **Action**: The action that was performed on the Flag. For example,
    turned `on` or `off`
-   **Event Summary**: The summary of all the events of the Flag. For
    example, the Project name, Environment details, etc. The event
    summary also displays the YAML difference with the flag details and
    the state of the events

### View activities

To view the actions performed on a Feature Flag:

1.  In **Feature Flags** select the Feature Flag for which you want to
    view the activity.
2.  Select the date range for the Feature Flag you want to view.\
    The **Time**, **User**, and **Action** details are displayed.

### View an event summary

To view a summary of an event:

1.  In **Feature Flags** select the Feature Flag for which you want to
    view the event summary.

2.  Select the date range for the Feature Flag you want to view.

3.  Click **View Event Summary**.

    ![](./static/view-activities-of-a-feature-flag-00.png){style="display:block;margin-left:0;margin-right:auto"
    hd-align="left"}

    *Figure 1: Viewing the event summary*

4.  The **Event Summary** is displayed.

5.  Click **YAML DIFFERENCE** to view the details of the Flag. The YAML
    file also highlights the different states of the events.

    ![](./static/view-activities-of-a-feature-flag-01.png){style="max-height:50%;max-width:50%;display:block;margin-left:0;margin-right:auto"
    hd-height="50%" hd-width="50%" hd-align="left"}

*Figure 2: An example YAML file*
