---
title: Manage Access Control for CCM Dashboards
description: This topic describes how to add and manage access control for CCM Dashboards.
tags: 
   - helpDocs
   - Dashboards
   - Access Control
   - RBAC 
helpdocs_topic_id: ng6yaxqi2r
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness provides Role-Based Access Control (RBAC) that enables you to control user and group access to Harness Resources according to their Role assignment.

This topic describes how to add and manage access control for CCM Dashboards.

In this topic:

* [Before You Begin](manage-access-control-for-ccm-dashboards.md)
* [Review CCM Dashboards Roles and Permissions](manage-access-control-for-ccm-dashboards.md)
* [Step: Add and Manage Dashboard - Static Editor Role](manage-access-control-for-ccm-dashboards.md)
* [Step: Add and Manage Dashboard - All View Role](manage-access-control-for-ccm-dashboards.md)
* [Step: Add and Manage Access Control for Resource Groups](manage-access-control-for-ccm-dashboards.md)
* [Step: Add and Manage Access Control for Users](manage-access-control-for-ccm-dashboards.md)

### Before You Begin

* [Access Management (RBAC) Overview](https://ngdocs.harness.io/article/vz5cq0nfg2-rbac-in-harness)

### Review CCM Dashboards Roles and Permissions

The following roles are needed for CCM Dashboards: 

* **Dashboard - Static Editor**: To add, edit, and delete CCM Dashboards
* **Dashboard - All View**: To view all the **By Harness** and **Custom** dashboards



|  |  |  |
| --- | --- | --- |
| **Roles** | **Scope** | **Permissions** |
| Dashboard - Static Editor | Folder | * Add Dashboard
* Add Tile
* Edit Dashboard
* Delete Dashboard
 |
| Dashboard - All View | Folder | * View CCM Dashboards
 |

### Step: Add and Manage Dashboard - Static Editor Role

Perform the following steps to add and manage permissions **Dashboard - Static Editor** role.

1. In **Harness**, click **Account Settings**, and then click **Access Control**.
2. Click **Roles**.
3. Click **New Role**. The New Role settings appear.
4. In **Name**, enter **Dashboard - Static Editor** and click **Save**.  
![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1629906863193/screenshot-2021-08-25-at-9-24-07-pm.png)
5. Click **Shared Resources** for the role that you created.
6. Select the **View** and **Manage** checkbox. This will allow you to add dashboards, add tiles, edit dashboards, and delete dashboards.  
![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1629907311437/screenshot-2021-08-25-at-9-31-14-pm.png)
7. Click **Apply Changes**.

### Step: Add and Manage Dashboard - All View Role

Perform the following steps to add and manage permissions **Dashboard - All View** role.

1. In **Harness**, click **Account Settings**, and then click **Access Control**.
2. Click **Roles**.
3. Click **New Role**. The New Role settings appear.
4. In **Name**, enter **Dashboard - All View** and click **Save**.  
![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1629907446670/screenshot-2021-08-25-at-9-33-42-pm.png)
5. Click **Shared Resources** for the role that you created.
6. Select the **View** checkbox. This will allow you to view all the dashboards.  
![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1629907508930/screenshot-2021-08-25-at-9-34-54-pm.png)
7. Click **Apply Changes**.

### Step: Add and Manage Access Control for Resource Groups

Perform the following steps to limit access to specific Dashboards.

1. In **Harness**, click **Account Settings**, and then click **Access Control**.![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1626373534560/screenshot-2021-07-15-at-11-55-08-pm.png)
2. In **Resource Groups**, click your Resource Group. For more information on adding and managing resource groups, see [Add and Manage Resource Groups](https://ngdocs.harness.io/article/yp4xj36xro-add-resource-groups).  
  
This section uses **Dashboard - All** as an example.
3. In **Shared Resources**, select **Dashboards**.  
  
By default, **All Dashboards** is selected.![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1626759172270/screenshot-2021-07-20-at-10-53-46-am.png)
4. Click **Add Dashboards**.
5. In **Add Dashboards**, select the folders for which you want to limit the access.  
  
The selected folder may have more than one dashboard. All the dashboards in the selected folders will have the same access.![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1626759377508/screenshot-2021-07-20-at-11-04-02-am.png)
6. Click **Apply Changes**.

### Step: Add and Manage Access Control for Users

Perform the following steps to limit the access to specific Dashboards for different users.

1. In **Harness**, click **Access Control**.![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1626373534560/screenshot-2021-07-15-at-11-55-08-pm.png)
2. In **User**, in **New User**, select the User for which you want to add or modify the access control. For more information on adding and managing resource groups, see [Add and Manage Users](https://ngdocs.harness.io/article/hyoe7qcaz6-add-users).
3. In **Assign Roles**, select the **Role** from the drop-down list. You can select either **Dashboard - Static Editor** or **Dashboard - All View**.
4. In **Resource Groups**, select the resource group for which you want to add or modiy the access control.![](https://files.helpdocs.io/i5nl071jo5/articles/ng6yaxqi2r/1626771149381/screenshot-2021-07-20-at-2-22-02-pm.png)
5. Click **Save**.

