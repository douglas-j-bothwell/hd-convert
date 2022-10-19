---
title: Manage Access Control
description: This topic describes how to add and manage access control for Feature Flags.
tags: 
   - helpDocs
   - Access Control
   - feature flag
helpdocs_topic_id: g8ajhy6msi
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness provides Role-Based Access Control (RBAC) that enables you to
control user and group access to Harness resources according to the
user\'s role. By using RBAC, you can increase security and improve
efficiency.

This topic describes the roles available for Feature Flags. For more
information about RBAC works with Harness, go to [Access Management
(RBAC) Overview](/article/vz5cq0nfg2-rbac-in-harness){target="_blank"}
and for steps to implement Access Control, go to [Add and Manage
Users](/article/hyoe7qcaz6-add-users){target="_blank"}.

### Feature Flags roles and permissions

The following default Role is available specifically for Feature Flags:

-   **Feature Flag Manage Role**: Can create new Feature Flags and also
    edit and view existing Flags

+-----------------+-----------------+-----------------+-----------------+
| **Roles**       | **Scope**       | **Permissions** |                 |
+-----------------+-----------------+-----------------+-----------------+
| Feature Flag    | Project or      | -   Create      | ![](h           |
| Manage Role     | Environment     |     Flags       | ttps://files.he |
|                 |                 | -   View Flags  | lpdocs.io/i5nl0 |
|                 |                 | -   Edit Flags  | 71jo5/articles/ |
|                 |                 | -   View Target | g8ajhy6msi/1625 |
|                 |                 |     Groups      | 510324546/scree |
|                 |                 | -   Edit Target | nshot-2021-07-0 |
|                 |                 |     Groups      | 6-at-12-08-09-a |
|                 |                 | -   View        | m.png){style="d |
|                 |                 |                 | isplay:block;ma |
|                 |                 |    Environments | rgin-left:0;mar |
|                 |                 |     and         | gin-right:auto" |
|                 |                 |     redacted    | h               |
|                 |                 |     SDK keys    | d-align="left"} |
|                 |                 |                 |                 |
|                 |                 |                 | *Figure 1: The  |
|                 |                 |                 | Feature Flag    |
|                 |                 |                 | Manage role*    |
+-----------------+-----------------+-----------------+-----------------+

::: note-callout
If you have permissions at the Project level, you can edit Flags within
that Project or its Environments. If you have permissions for the
Environment, then the role is limited to that Environment only.\
:::

### See also

The following topics can help you understand how to implement Access
Control:

-   [Add and Manage
    Users](/article/hyoe7qcaz6-add-users){target="_blank"}
-   [Add and Manage User
    Groups](/article/dfwuvmy33m-add-user-groups){target="_blank"}
-   [Add and Manage Resource
    Groups](/article/yp4xj36xro-add-resource-groups){target="_blank"}
-   [Add and Manage
    Roles](/article/tsons9mu0v-add-manage-roles){target="_blank"}
