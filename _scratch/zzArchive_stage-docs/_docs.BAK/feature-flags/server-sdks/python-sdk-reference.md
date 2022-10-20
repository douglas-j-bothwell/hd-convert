---
title: Python SDK Reference
description: This topic explains how to use the Harness Feature Flags SDK in your Python application.
tags: 
   - helpDocs
   - SDK
   - feature flag
   - Python
helpdocs_topic_id: hwoxb6x2oe
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags Java SDK for
your Java application.

For getting started quickly, you can use our [sample code from the
Python SDK
README](https://github.com/harness/ff-python-server-sdk/blob/main/README.md){target="_blank"}.
You can
also [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"} and
run a sample application from the [Python SDK GitHub
Repository.](https://github.com/harness/ff-python-server-sdk){target="_blank"}

### Before You Begin

You should read and understand the following:

-   [Feature Flags
    Overview](../ff-overview/cf-feature-flag-overview.md){target="_blank"}
-   [Getting Started with Feature
    Flags](../ff-getting-started/getting-started-with-feature-flags.md){target="_blank"}
-   [Client-Side and Server-Side
    SDKs](../sdk-overview/client-side-and-server-side-sdks.md){target="_blank"}
-   [Communication Strategy Between SDKs and Harness Feature
    Flags](../sdk-overview/communication-sdks-harness-feature-flags.md){target="_blank"}

### Version

::: note-callout
The current version of this SDK is **1.1.2.**
:::

### Requirements

To use this SDK, make sure you:  

-   Install [Python 3.7](https://www.python.org/downloads/) or newer
-   Install
    [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#id12) 
-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-python-server-sdk){target="_blank"}
-   Create a Java application,
    or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"} our [sample
    application](https://github.com/harness/ff-python-server-sdk){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`
-   [Create an SDK key and make a copy of
    it](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}

### Install the SDK

Install the python SDK using pip

    python -m pip install harness-featureflags

### Initialize the SDK

To initialize the Python SDK, you need to:

1.  Add your Server SDK Key to connect to your Harness Environment.
2.  Add a Target that you want to Evaluate against a Feature Flag.
3.  (Optional) Configure the SDK options. For more details on what
    features you can configure for this SDK, go to [Configure the
    SDK](python-sdk-reference.md).

#### Add the Server SDK Key

To connect to the correct Environment that you set up on the Harness
Platform, you need to add the Server SDK Key from that Environment.
Input the Server SDK Key into the `api_key` parameter. For example:

    """
    Put the API Key here from your environment
    """
    api_key = "YOUR_API_KEY";

    cf = CfClient(api_key);

#### Add a Target

::: note-callout
**What is a Target?\
**Targets are used to control which users see which Variation of a
Feature Flag, for example, if you want to do internal testing, you can
enable the Flag for some users and not others. When creating a Target,
you give it a name and a unique identifier. Often Targets are users but
you can create a Target from anything that can be uniquely identified,
such as an app or a machine.\
For more information about Targets, go to [Targeting Users With
Flags](../ff-target-management/targeting-users-with-flags.md){target="_blank"}. 
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| `identifier`    | Unique ID for   | Required        | `ide            |
|                 | the Target.     |                 | ntifier='HT_1'` |
|                 |                 |                 |                 |
|                 | Read **Regex    |                 |                 |
|                 | requirements    |                 |                 |
|                 | for Target      |                 |                 |
|                 | names and       |                 |                 |
|                 | identifiers**   |                 |                 |
|                 | below for       |                 |                 |
|                 | accepted        |                 |                 |
|                 | characters.     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `name`          | Name for this   | Optional        | `name="Har      |
|                 | Target. This    |                 | ness_Target_1"` |
|                 | does not have   | **Note**: If    |                 |
|                 | to be unique.   | you don\'t want |                 |
|                 |                 | to send a name, |                 |
|                 | **Note**: If    | don\'t send the |                 |
|                 | you don't       | parameter.      |                 |
|                 | provide a       | Sending an      |                 |
|                 | value, the name | empty argument  |                 |
|                 | will be the     | will cause an   |                 |
|                 | same as the     | error.          |                 |
|                 | identifier.     |                 |                 |
|                 |                 |                 |                 |
|                 | Read **Regex    |                 |                 |
|                 | requirements    |                 |                 |
|                 | for Target      |                 |                 |
|                 | names and       |                 |                 |
|                 | identifiers**   |                 |                 |
|                 | below for       |                 |                 |
|                 | accepted        |                 |                 |
|                 | characters.     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `attributes`    | Additional data | Optional        | `attributes     |
|                 | you can store   |                 | ={"email": "dem |
|                 | for a Target,   |                 | o@harness.io"}` |
|                 | such as email   |                 |                 |
|                 | addresses or    |                 |                 |
|                 | location.       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

Regex requirements for Target names and identifiers

<div>

**Identifier\
**Regex: `^[A-Za-z0-9.@_-]*$`\
\
Must consist of only alphabetical characters, numbers, and the following
symbols:\
. (period)\
@ (at sign)\
- (dash)\
\_ (underscore)\
\
The characters can be lowercase or uppercase but cannot include accented
letters, for example `Cafe_789`.\
\
**Name\
**Regex: `^[\\p{L}\\d .@_-]*$`\
\
Must consist of only alphabetical characters, numbers, and the following
symbols:\
. (period)\
@ (at sign)\
- (dash)\
\_ (underscore)\
(space)\
\
The characters can be lowercase or uppercase and can include accented
letters, for example `Café_123`.

</div>

For example:

     target = Target(identifier='HT_1', name="Harness_Target_1", attributes={"email": "demo@harness.io"})

#### Configure the SDK

You can configure the following features of the SDK:

+-----------------+-----------------+-----------------+-----------------+
| **Name**        | **Example**     | **Description** | **Default       |
|                 |                 |                 | Value**         |
+-----------------+-----------------+-----------------+-----------------+
| baseUrl         | `with_base      | The URL used to | `https:/        |
|                 | _url("https://c | fetch Feature   | /config.ff.harn |
|                 | onfig.ff.harnes | Flag            | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Evaluations.    |                 |
|                 |                 | When using the  |                 |
|                 |                 | Relay Proxy,    |                 |
|                 |                 | change this     |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| eventUrl        | `with_events    | The URL for     | `https:/        |
|                 | _url("https://e | posting metrics | /events.ff.harn |
|                 | vents.ff.harnes | data to the     | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Feature Flag    |                 |
|                 |                 | service. When   |                 |
|                 |                 | using the Relay |                 |
|                 |                 | Proxy, change   |                 |
|                 |                 | this            |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| pollInterval    | `Config(pul     | The interval    | `60` (seconds)  |
|                 | l_interval=60)` | **in seconds**  |                 |
|                 |                 | that we poll    |                 |
|                 |                 | for changes     |                 |
|                 |                 | when you are    |                 |
|                 |                 | using stream    |                 |
|                 |                 | mode.           |                 |
+-----------------+-----------------+-----------------+-----------------+
| streamEnabled   | `with_stream    | Set to `True`   | `True`          |
|                 | _enabled(True)` | to enable       |                 |
|                 |                 | streaming mode. |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `False`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | streaming mode. |                 |
+-----------------+-----------------+-----------------+-----------------+
| a               | `with_analytics | Set             | `True`          |
| nalyticsEnabled | _enabled(True)` | to `True` to    |                 |
|                 |                 | enable          |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | Set             |                 |
|                 |                 | to `False` to   |                 |
|                 |                 | disable         |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | **Note**: When  |                 |
|                 |                 | enabled,        |                 |
|                 |                 | analytics data  |                 |
|                 |                 | is posted every |                 |
|                 |                 | 60 seconds.     |                 |
+-----------------+-----------------+-----------------+-----------------+

For example:

    # Create a Feature Flag Client
        client = CfClient(apiKey,
                          with_base_url("https://config.ff.harness.io/api/1.0"),
                          with_events_url("https://events.ff.harness.io/api/1.0"),
                          with_stream_enabled(True),
                          with_analytics_enabled(True),
                          Config(pull_interval=60))

### Evaluate a Flag

Evaluating a Flag is when the SDK processes all Flag rules and returns
the correct Variation of that Flag for the Target you provide. 

If a matching Flag can't be found, or the SDK can't remotely fetch
flags, the default value is returned. 

There are different methods for the different Variation types and for
each method you need to pass in:

-   Identifier of the Flag you want to evaluate
-   The Target object you want to evaluate against
-   The default Variation

For example:

#### Evaluate a boolean Variation

``` {.hljs .sql}
result = cf.bool_variation("identifier_of_your_bool_flag", target, False);  
```

#### Evaluate a string Variation

    result = client.string_variation('identifier_of_your_string_flag', target, "")

#### Evaluate a number Variation

    result = client.number_variation('identifier_of_your_number_flag', target, -1)

#### Evaluate a JSON Variation

    client.json_variation('identifier_of_your_json_flag', target, {})

### Test your app is connected to Harness {#undefined}

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

### Close the SDK {#undefined}

To help prevent memory leaks, we recommend closing the SDK when it's not
in use. To do this, run the following command: 

    client.close()

### Additional options {#undefined}

#### Configure your logger {#undefined}

The SDK provides a logger that wraps the standard Python logging
package. You can import and use it with the following:

    from featureflags.util import log
    log.info("Hello, World!")

To change the default log level, you can use the standard logging levels

    from featureflags.util import log
    import logging

    log.setLevel(logging.WARN)

#### Use the Relay Proxy {#undefined}

When using your Feature Flag SDKs with a [Harness Relay
Proxy](../relay-proxy/relay-proxy.md){target="_blank"} you need to
change the default URL and events URL to `http://localhost:7000` when
initializing the SDK. To do this:

1.  Import the URL helper functions, for example:

        from featureflags.config import with_base_url
        from featureflags.config import with_events_url

2.  Pass the new URLs in when initializing the SDK, for example:

            client = CfClient(api_key,
                              with_base_url("https://config.feature-flags.uat.harness.io/api/1.0"),
                              with_events_url("https://event.feature-flags.uat.harness.io/api/1.0"))

### Sample code for a Python application

Here is a sample code for integrating with the Python SDK:

    import time

    from featureflags.evaluations.auth_target import Target
    from featureflags.client import CfClient
    from featureflags.util import log
    from featureflags.config import with_base_url
    from featureflags.config import with_events_url


    def main():
        log.debug("Starting example")
        api_key = "Your API key"
        client = CfClient(api_key,
                          with_base_url("https://config.ff.harness.io/api/1.0"),
                          with_events_url("https://events.ff.harness.io/api/1.0"))

        target = Target(identifier='harness')

        while True:
            result = client.bool_variation('your_flag_identifier', target, False)
            log.debug("Result %s", result)
            time.sleep(10)

    if __name__ == "__main__":
        main()
