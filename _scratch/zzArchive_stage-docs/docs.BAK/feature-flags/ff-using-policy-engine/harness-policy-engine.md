---
title: Policies Overview for Feature Flags
description: This topic gives an overview of how Harness Policy Engine works with Feature Flags and OPA.
tags: 
   - helpDocs
   - harness policy engine
   - OPA
   - feature flag
helpdocs_topic_id: 4vx27jqwv2
helpdocs_is_private: false
helpdocs_is_published: true
---

::: note-callout
Currently, this feature is behind the Feature Flags
`OPA_PIPELINE_GOVERNANCE`, `CUSTOM_POLICY_STEP`, and
`OPA_FF_GOVERNANCE`. Contact [Harness
Support](mailto:support@harness.io){target="_blank"} to enable the
feature.
:::

Harness Policy Engine uses [Open Policy Agency
(OPA)](https://www.openpolicyagent.org/docs/latest/){target="_blank"} to
store policies that you can then enforce on your Feature Flags. You can
use Harness Policy Engine with the following [Harness
entities](https://docs.harness.io/article/tygjin99y9-harness-entity-reference){target="_blank"}
on the Harness Platform:

-   Flag
-   Target
-   Target group
-   Environment
-   SDK keys

For example, you can use policies to ensure your Feature Flags: 

-   Match the naming convention you set.
-   Are created using a specific flag type, for example, only allowing
    Boolean flags to be created.
-   Have the correct default on and off values set. 
-   Have been turned on in a test environment before being enabled in a
    production environment.

This topic provides an overview of how Harness Policy Engine works with
Feature Flags.

::: note-callout
For steps to set up your policies on the Harness Platform, go to [Use
Harness Policy Engine for Feature
Flags.](https://docs.harness.io/article/vb6ilyz194-using-harness-policy-engine-for-feature-flags){target="_blank"}
:::

#### Before you begin

Before using Harness Policy Engine, you should understand the following:

-   [Harness\' Key
    Concepts](https://docs.harness.io/article/hv2758ro4e-learn-harness-key-concepts){target="_blank"}
-   [How to
    Write](https://www.openpolicyagent.org/docs/latest/policy-language/)
    [Rego for
    OPA ](https://www.openpolicyagent.org/docs/latest/policy-language/)

New to Rego? Use the following resources to learn it:

-   Free online course on Rego from Styra founder and OPA co-creator Tim
    Hendricks: [OPA Policy
    Authoring](https://academy.styra.com/courses/opa-rego).
-   See [Policy
    Language](https://www.openpolicyagent.org/docs/latest/policy-language/)
    from OPA. The [Rego Cheat
    Sheet](https://dboles-opa-docs.netlify.app/docs/v0.10.7/rego-cheatsheet/)
    is also helpful to have on hand.

#### How does the Harness Policy Engine use OPA?

The Harness Policy Engine uses [OPA](https://www.openpolicyagent.org/)
as the central service to store and enforce policies for the different
entities and processes across the Harness Platform. You can define and
store policies directly in the Harness Platform. 

In the Harness Platform, you add policies written in Rego to a Policy
Set and select the Harness entities (for example, Feature Flags) for
evaluation.

![](https://files.helpdocs.io/i5nl071jo5/articles/4vx27jqwv2/1651152284589/opa-p-1-1.png){style="max-height:70%;max-width:70%;display:block;margin-left:0;margin-right:auto"
hd-height="70%" hd-width="70%" hd-align="left"}

*Figure 1: Adding a Policy*

Then, when a Feature Flag is saved, Harness reaches out to the Harness
OPA server to evaluate the action using the Policy Set. The Feature Flag
is saved successfully, saved with a warning, or not saved and an error
is received.

##### Example of adding a policy for a Feature Flag

1.  Set your policy: The names of all Feature Flags created must match
    the regex you set. You set the regex as having to be in the format
    ABC, dash, and three numbers, for example, ABC-123.
2.  Insert the Rego code into the Policy Engine on the Harness Platform,
    for example, the Rego code for the policy above is:

```{=html}
<!-- -->
```
    package feature_flags

    # Deny flags whose names aren't a valid Jira ticket format for our projects
    # e.g. "ABC-123" is allowed. "My cool flag" is not allowed

    deny[sprintf("feature flag name '%s' doesn't match regex", [input.flag.name])] {
       not regex.match("[ABC]+[-][1-9][0-9]?", input.flag.name)
    }

1.  Run the policy against your Feature Flags.

::: note-callout
When you create the policy you can choose whether a Feature Flag
receives only a warning message, or receives an error and can't be saved
when the policy isn't met. For more information about how to do this, go
to [Creating a
Policy](https://docs.harness.io/article/vb6ilyz194-using-harness-policy-engine-for-feature-flags#step_1_creating_a_policy).
:::

-   **Success**: You create a Feature Flag and name it `ABC-567`, which
    matches the naming regex you set. When you save the flag, the policy
    rule is evaluated, returns `Flag created`, and the flag is saved.
-   **Warning**: You create a Feature Flag and name it `Flag2`, which
    doesn't match the naming regex you set. The flag is saved but you
    receive the following warning message:

![](https://files.helpdocs.io/i5nl071jo5/articles/4vx27jqwv2/1651155268645/opa-p-1-2.png){style="max-height:60%;max-width:60%;display:block;margin-left:0;margin-right:auto"
hd-height="60%" hd-width="60%" hd-align="left"}

*Figure 2: A Flag with policy warnings*

-   **Failure**: You create a Feature Flag and name it `Flag2`, which
    doesn't match the naming regex you set. The flag doesn't save and
    you receive the following error message:

![](https://files.helpdocs.io/i5nl071jo5/articles/4vx27jqwv2/1651155323841/opa-p-1-3.png){style="max-height:60%;max-width:60%;display:block;margin-left:0;margin-right:auto"
hd-height="60%" hd-width="60%" hd-align="left"}

*Figure 3: A Flag with policy failures*

#### Next step

To understand how to add policies for Feature Flags, go to [Use Harness
Policy Engine for Feature
Flags](https://docs.harness.io/article/vb6ilyz194-using-harness-policy-engine-for-feature-flags){target="_blank"}.