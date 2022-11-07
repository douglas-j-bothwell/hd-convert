---
title: Add SMTP Configuration
description: Explains how to configure SMTP for email-based deployment notifications, approvals, and tracking.
tags: 
   - helpDocs
   - Platform
# sidebar_position: 2
helpdocs_topic_id: d43r71g20s
helpdocs_category_id: y9pmm3ig37
helpdocs_is_private: false
helpdocs_is_published: true
---

You can send email notifications to Harness User Groups using your SMTP accounts.

Emails can be sent automatically in response to Pipeline and stage events like Pipeline Failed and Stage Succeeded.

Your Harness SaaS account includes an SMTP server, so you don't need to add one of your own.

If you are using the Harness On-Prem offering, then you will need to add an SMTP server to your Harness account.This topic explains how to configure an SMTP server with your Harness account and send email notifications according to different Pipeline events.

In this topic:

* [Before You Begin](#before_you_begin)
* [Limitations](#limitations)
* [Step 1: Add SMTP Configuration](#step_1_add_smtp_configuration)
* [Step 2: Details](#step_2_details)
* [Step 3: Credentials](#step_3_credentials)
* [Step 4: Test Connection](#step_4_test_connection)
* [Option: Send Notifications for a User Group using Email](/article/d43r71g20s-add-smtp-configuration#option_send_notifications_for_a_user_group_using_email)
* [Option: Send Notification for a Pipeline](/article/d43r71g20s-add-smtp-configuration#option_send_notification_for_a_pipeline)
* [See Also](/article/d43r71g20s-add-smtp-configuration#see_also)

### Before You Begin

* [User Group Notification Preferences](https://ngdocs.harness.io/article/dfwuvmy33m-add-user-groups#option_notification_preferences)

### Limitations

Configuring your SMTP server is required only if you are using [Harness On-Prem](/article/tb4e039h8x-harness-on-premise-overview), or if you wish to use your own SMTP server instead of the Harness SaaS default SMTP option.

### Step 1: Add SMTP Configuration

In your Harness account, go to **Account Settings**.

Click **Account Resources.**

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641565895369/screenshot-2022-01-07-at-8-00-09-pm.png)Click **SMTP Configuration** and then click **Setup**.

The SMTP Configuration settings appear.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641566012391/screenshot-2022-01-07-at-8-03-04-pm.png)### Step 2: Details

Enter **Name** for your SMTP Configuration.

In **Host,** enter your SMTP server's URL.

Enter the port number on which the SMTP server is listening (typically, `25`).

Select **Enable SSL** for secure connections (SSL/TLS).

Select **Start TSL** to enable SMTP over TLS, or when the connection is upgraded to SSL/TLS using `STARTTLS`.

In **From Address**, enter the email address from which Harness will send notification emails.

Click **Continue**.

### Step 3: Credentials

Enter the username and password for the email account.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641790061990/screenshot-2022-01-10-at-10-13-38-am.png)Click **Save and Continue**.

### Step 4: Test Connection

In **To,** enter the email address to which you want to send notifications.

Enter **Subject** and **Body** for the email.

Click **Test**.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641791867080/screenshot-2022-01-10-at-10-45-37-am.png)Click **Continue** after the test is successful.

SMTP is configured for your account.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641791965795/screenshot-2022-01-10-at-10-48-37-am.png)### Option: Send Notifications for a User Group using Email

In your **Account**/**Organization**/**Project** click Access Control.

Click **User Groups**.

Select the User Group to which you want to add notification preferences.

In **Notification Preferences**, select **Email/Alias**.

Enter the email address from which you want to send email notifications and click **Save**.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641813881193/screenshot-2022-01-10-at-4-51-39-pm.png)### Option: Send Notification for a Pipeline

You can send Pipeline event notifications using email. Event notifications are set up using **Notify** option in your Pipeline.

In Harness, go to your Pipeline and click **Notify**.

Click **Notifications**. The **New Notification** settings appear.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641977579613/screenshot-2022-01-12-at-2-22-33-pm.png)Enter a name for your notification rule and click **Continue**.

Select the Pipeline Events for which you want to send notifications. Click **Continue**.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641977771418/screenshot-2022-01-12-at-2-25-42-pm.png)In **Notification Method**, select **Email**.

Enter the email addresses to which you want to send the notifications.

Select the User groups which you want to notify.

Click **Test**.

Once the test is successful, click **Finish**.

![](https://files.helpdocs.io/i5nl071jo5/articles/d43r71g20s/1641979385777/screenshot-2022-01-12-at-2-49-31-pm.png)Your Notification Rule is now listed in Notifications. Post this users will get email notifications when the events listed in the Notification Rule occur.

### See Also

* [Send Notifications using Slack](/article/h5n2oj8y5y-send-notifications-using-slack)
* [Send Notifications to Microsoft Teams](/article/xcb28vgn82-send-notifications-to-microsoft-teams)

