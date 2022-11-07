---
title: Harness Role-Based Access Control Quickstart
description: This document explains how to set up RBAC for Pipelines.
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: lrz2e4t1ko
helpdocs_category_id: w4rzhnf27d
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Role-Based Access Control (RBAC) helps you manage who has access to your Harness resources, what they can do with those resources, and in what scope they have access.

[Role Assignments](/article/vz5cq0nfg2-rbac-in-harness#role_assignment) to Users, User Groups, and Service Accounts at a specific scope, determine their permissions.

This quickstart shows how to configure Role-Based Access Control (RBAC) for Pipeline Creation, Execution, and Connector Admin.

### Objectives

You will learn how to:

* Create custom Roles.
* Create custom Resource Groups.
* Set up role-based access control for Pipeline Owner.
* Set up role-based access control for Connector Admin.

### Before You Begin

* [Learn Harness' Key Concepts](https://ngdocs.harness.io/article/hv2758ro4e-learn-harness-key-concepts)
* [Create Organizations and Projects](https://ngdocs.harness.io/article/36fw2u92i4-create-an-organization)
* [Role-Based Access Management (RBAC) Overview](/article/vz5cq0nfg2-rbac-in-harness)
* [Add and Manage Users](/article/hyoe7qcaz6-add-users)
* [Add and Manage User Groups](https://docs.harness.io/article/dfwuvmy33m-add-user-groups)
* [Add and Manage Resource Groups](https://docs.harness.io/article/yp4xj36xro-add-resource-groups)
* [Add and Manage Roles](https://ngdocs.harness.io/article/tsons9mu0v-add-roles)
* For information on creating a Pipeline and adding a Stage, see [Add a Stage](/article/2chyf1acil-add-a-stage#step_1_start_a_pipeline).
* Make sure you have **Admin** rights for the Account/Org/Project where you want to configure Access Management.

### Prerequisites

* You must have **View**, **Manage**, and **Invite** permissions for **Users**.
* You must have **View** and **Manage** permissions for **User Groups**.
* You must have **View**, **Create/Edit**, and **Delete** permissions for **Resource Groups**.
* You must have **View**, **Create/Edit**, and **Delete** permissions for **Roles**.
* You must have created your Organizations and Projects. See [Create Organizations and Projects](/article/36fw2u92i4-create-an-organization).

### RBAC Components

To manage access control in Harness, you must have the following components in place:

* **Principal**: can be a [User](/article/hyoe7qcaz6-add-users), [User Group](/article/dfwuvmy33m-add-user-groups), or [Service Account](/article/e5p4hdq6bd-add-and-manage-service-account).
* **Resource Group**: is a list of resources within a specific scope on which a Principal can perform actions. See [Add and Manage Resource Groups](/article/yp4xj36xro-add-resource-groups).
* **Roles**: is a set of permissions that is assigned to a Principal for specific Resource Groups. See [Add and Manage Roles](https://ngdocs.harness.io/article/tsons9mu0v-add-roles).

Harness provides a set of built-in Resource Groups and Roles for you to easily manage access control. For more information, see [Role Assignments](/article/vz5cq0nfg2-rbac-in-harness#role_assignment).

However, you can always create your own custom Resource Groups and Roles to manage access control as per your needs.

For example, you can give access to **Create** Pipelines within all the Projects under Org O1, but not **Delete** or **Execute** them.

Let us look at a few examples to create a few custom Resource Groups and Roles and set up RBAC accordingly.

### Set Up RBAC for Pipeline Owner

Let us set up access control for a custom Role called Pipeline Owner.

Following are the components required for this RBAC setup:

* **Principal**: a User Group named `Pipeline Owners`.
* **Resource Group**: a custom Resource Group named `All Pipeline Resources`.
* **Role**: a custom Role named `Pipeline Admin`.

The following table shows the Role Assignment for a Pipeline Owner:



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Custom Role Name** | **Custom Resource Group Name** | **Resource Scope** | **Resources** | **Permissions** |
| **Pipeline Admin** | **All Pipeline Resources** | **All (including all Organizations and Projects)** | * Pipelines
* Secrets
* Connectors
* Delegates
* Environments
* Templates
* Variables
 | * View, Create/Edit, Delete, Execute Pipelines
* View, Create/Edit, Access Secrets
* View, Create/Edit, Delete, Access Connectors
* View, Create/Edit Delegates
* View, Create/Edit, Access Environments
* View, Create/Edit, Access Templates
* View, Create/Edit Variables
 |

#### Step 1: Create a User Group

1. In your Harness Account, click **Account Settings**.
2. Click **Access Control**.
3. In **User Groups,** click **New User** **Group****.** The New User Group settings appear.
4. Enter a **Name** for your **User Group**. In this case, enter Pipeline Owners.
5. Enter **Description** and [**Tags**](https://docs.harness.io/article/i8t053o0sq) for your **User Group**.
6. Select Users under **Add Users**.
7. Click **Save.**

Your User Group is now listed under User Groups.

#### Step 2: Create a Custom Resource Group

1. In your Harness Account, click **Account Settings**.
2. Click **Access Control**.
3. In **Resource Groups**, click **New Resource** **Group****.** The New Resource Group settings appear.
4. Enter a **Name** for your **Resource Group**. In this case, enter **All Pipeline Resources**.
5. Enter **Description** and **Tags** for your **Resource Group**.
6. Click **Save**.
7. In **Resource Scope**, select **All (including all Organizations and Projects)**. This would mean the Principal can access the specified resources within the Account as well as those within the Organizations and their Projects.![](https://files.helpdocs.io/kw8ldg1itf/articles/lrz2e4t1ko/1657257327365/screenshot-2022-07-08-at-10-43-37-am.png)
8. In Resources, select **Specified**.![](https://files.helpdocs.io/kw8ldg1itf/articles/lrz2e4t1ko/1657257421564/screenshot-2022-07-08-at-10-45-49-am.png)
9. Select the following resources:
	1. Environments
	2. Variables
	3. Templates
	4. Secrets
	5. Delegates
	6. Connectors
	7. Pipelines
10. Click **Save**.

#### Step 3: Create a Custom Role

1. In your Harness Account, click **Account Settings**.
2. Click **Access Control**.
3. In **Roles**, click **New Role**. The New Role settings appear.
4. Enter a **Name** for your **Role**. In this case, enter **Pipeline Admin.**
5. Enter optional **Description** and **Tags** for your **Role**.
6. Click **Save**.
7. Select the following permissions for the resources:
	1. View, Create/Edit, Delete, Execute Pipelines
	2. View, Create/Edit, Access Secrets
	3. View, Create/Edit, Delete, Access Connectors
	4. View, Create/Edit Delegates
	5. View, Create/Edit, Access Environments
	6. View, Create/Edit, Access Templates

#### Step 4: Assign Role Permission to the User Group

Let us now complete the [Role Assignment](/article/vz5cq0nfg2-rbac-in-harness#role_assignment) for the User Group to complete the RBAC set up for Pipeline Owner.

1. In your Harness Account, click **Account Settings**.
2. Click **Access Control**.
3. In **User Groups,** locate the User Group you just created and click on **Role**.![](https://files.helpdocs.io/kw8ldg1itf/articles/lrz2e4t1ko/1657256417402/screenshot-2022-07-08-at-10-24-02-am.png)The **Add Role** settings appear.
4. In **Assign Role Bindings**, click **Add**.
5. In **Role**, select the custom Role that you created.
6. In **Resource** **Group**, select the custom Resource Group you just created.![](https://files.helpdocs.io/kw8ldg1itf/articles/lrz2e4t1ko/1657257127722/screenshot-2022-07-08-at-10-41-21-am.png)
7. Click **Apply**.

### Next Steps

* [Permissions Reference](/article/yaornnqh0z-permissions-reference)

