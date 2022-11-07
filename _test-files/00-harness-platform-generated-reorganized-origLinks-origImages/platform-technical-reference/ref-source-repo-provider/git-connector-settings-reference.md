---
title: Git Connector Settings Reference
description: This topic provides settings and permissions for the Git Connector.
tags: 
   - helpDocs
   - Connectors
# sidebar_position: 2
helpdocs_topic_id: tbm2hw6pr6
helpdocs_category_id: xyexvcc206
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic provides settings and permissions for the platform-agnostic Git Connector. For Connectors to popular Git platforms like GitHub, see [Code Repo Connectors](/category/xyexvcc206).

### Limitations

* Before Harness syncs with your Git repo, it'll confirm that all Harness' settings are in a valid state. If a connection isn't working, Harness won't sync with your Git repo.

### Name

The unique name for this Connector.

### ID

See [Entity Identifier Reference](https://ngdocs.harness.io/article/li0my8tcz3-entity-identifier-reference).

### Description

A description of this Connector.

### Tags

See [Tags Reference](https://ngdocs.harness.io/article/i8t053o0sq-tags-reference).

### URL Type

You can select **Account** or **Repository**.

You can add a connection to your entire Git account or just a repo in the account. Selecting a Git account enables you to use one Connector for all of your subordinate repositories.

Later when you test this connection, you will use a repo in the account.

In either case, when you use the Connector later in Harness, you will specify which repo to use.

### Connection Type

You can select **HTTPS** or **SSH** for the connection.

You will need to provide the protocol-relevant URL.

If you use Two-Factor Authentication for your Git repo, you connect over **HTTPS** or **SSH**. **HTTS** requires a personal access token.

For SSH, ensure that the key is not OpenSSH, but rather PEM format. To generate an SSHv2 key, use: `ssh-keygen -t rsa -m PEM` The `rsa` and `-m PEM` ensure the algorithm and that the key is PEM. Next, follow the prompts to create the PEM key. For more information, see the [ssh-keygen man page](https://linux.die.net/man/1/ssh-keygen).### Git Account or Repository URL

The URL for your Git repo. Ensure that it matches the Connection Type option you selected.

If you selected **Git Repository** in **URL** **Type**, enter the full URL for the repo.

If you selected **Git Account** in **URL** **Type**, enter the URL without the repo name. When you use this Connector in a Harness setting you will be prompted to provide a repo name.

### Username

The username for the account.

### Password

A [Harness Encrypted Text](/article/osfw70e59c-add-text-secrets) secret for the credentials of your Git user account.

### SSH Key

If you selected **SSH** as the connection protocol, you must add the **Username** as `git` and an **SSH Key** for use with the connection as a [Harness Encrypted Text secret](https://ngdocs.harness.io/article/osfw70e59c-add-text-secrets).

### Setup Delegates

You can select **Connect via any available delegate** or **Connect only via delegates which has all of the following tags**.

You need to enter **Selectors** to connect via specific delegates. For more information see [Select Delegates with Tags](/article/nnuf8yv13o-select-delegates-with-selectors).

