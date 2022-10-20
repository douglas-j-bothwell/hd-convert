---
title: Go SDK Reference
description: This topic explains how to integrate your feature flags with Go SDK.
tags: 
   - helpDocs
   - feature flag
   - Go SDK
   - SDK
helpdocs_topic_id: 4c8wljx60w
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags Go SDK for
your Go application. 

For getting started quickly, you can use our [sample code from the SDK
README](https://github.com/harness/ff-golang-server-sdk). You can also
[clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
and run a sample application from the [Go SDK GitHub
Repository.](https://github.com/harness/ff-golang-server-sdk)

### Before you begin

Make sure you read and understand:

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
The current version of this SDK is **0.1.2.**
:::

### Requirements

To use this SDK, make sure you:

-   Install Go version 1.6 or newer.
-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-golang-server-sdk){target="_blank"}
-   Create a Go application, or
    [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    our [sample
    application](https://github.com/harness/ff-golang-server-sdk/blob/main/examples/getting_started.go){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`.
-   [Create an SDK key and make a copy of
    it](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}.

### Install the SDK

Install the SDK using the following Go command:

    go get github.com/harness/ff-golang-server-sdk

### Import the SDK 

Import the SDK using the following Go command: 

    import harness "github.com/harness/ff-golang-server-sdk/client"

### Initialize the SDK

To initialize the Go SDK, you need to:

1.  Add your Server SDK Key to connect to your Harness Environment.
2.  (Optional) Configure the SDK options. For more details on what
    features you can configure for this SDK, go to [Configure the
    SDK](feature-flag-sdks-go-application.md).
3.  Complete the initialization by creating an instance of the Feature
    Flag client and  passing in the Server SDK Key and Configuration.
4.  Add a Target that you want to Evaluate against a Feature Flag.

#### Add the Server SDK Key

To connect to the correct Environment that you set up on the Harness
Platform, you need to add the Server SDK Key from that Environment.
Input the Server SDK Key into the `sdkKey` parameter. For example:

    client, err := harness.NewCfClient(sdkKey)

#### Configure the SDK

You can configure the following features of the SDK:

+-----------------+-----------------+-----------------+-----------------+
| **Name**        | **Example**     | **Description** | **Default       |
|                 |                 |                 | Value**         |
+-----------------+-----------------+-----------------+-----------------+
| baseUrl         | `harness.Wit    | The URL used to | `https:/        |
|                 | hURL("https://c | fetch Feature   | /config.ff.harn |
|                 | onfig.ff.harnes | Flag            | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Evaluations.    |                 |
|                 |                 | When using the  |                 |
|                 |                 | Relay Proxy,    |                 |
|                 |                 | change this     |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| eventUrl        | `ha             | The URL for     | `https:/        |
|                 | rness.WithEvent | posting metrics | /events.ff.harn |
|                 | sURL("https://e | data to the     | ess.io/api/1.0` |
|                 | vents.ff.harnes | Feature Flag    |                 |
|                 | s.io/api/1.0")` | service. When   |                 |
|                 |                 | using the Relay |                 |
|                 |                 | Proxy, change   |                 |
|                 |                 | this            |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| pollInterval    | `               | The interval    | `60 (seconds)`  |
|                 | harness.WithPul | **in seconds**  |                 |
|                 | lInterval(60))` | that we poll    |                 |
|                 |                 | for changes     |                 |
|                 |                 | when you are    |                 |
|                 |                 | using stream    |                 |
|                 |                 | mode.           |                 |
+-----------------+-----------------+-----------------+-----------------+
| streamEnabled   | `har            | Set to `true`   | `true`          |
|                 | ness.WithStream | to enable       |                 |
|                 | Enabled(false)` | streaming mode. |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | streaming mode. |                 |
+-----------------+-----------------+-----------------+-----------------+
| a               | `harnes         | Set to `true`   | `true`          |
| nalyticsEnabled | s.WithAnalytics | to enable       |                 |
|                 | Enabled(false)` | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | **Note**:       |                 |
|                 |                 | Analytics are   |                 |
|                 |                 | not cached.     |                 |
+-----------------+-----------------+-----------------+-----------------+

::: note-callout
Enabling analytics is currently not available using the Go SDK.
:::

For further configuration options and samples, such as configuring your
logger or using the SDK with the Relay Proxy, go to [Additional
Options](feature-flag-sdks-go-application.md).

#### Complete the initialization

Complete  the initialization by creating an instance of the Feature Flag
client and passing in the `sdkKey`, and any configuration options. For
example:

    // Create Options
    client, err := harness.NewCfClient(myApiKey, 
     harness.WithURL("https://config.ff.harness.io/api/1.0"), 
     harness.WithEventsURL("https://events.ff.harness.io/api/1.0"), 
     harness.WithPullInterval(1),
     harness.WithStreamEnabled(false))

#### Add a Target

::: note-callout
**What is a Target?**\
Targets are used to control which users see which Variation of a Feature
Flag, for example, if you want to do internal testing, you can enable
the Flag for some users and not others. When creating a Target, you give
it a name and a unique identifier. Often Targets are users but you can
create a Target from anything that can be uniquely identified, such as
an app or a machine.\
For more information about Targets, go to [Targeting Users With
Flags](../ff-target-management/targeting-users-with-flags.md){target="_blank"}. 
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| `Identifier`    | Unique ID for   | Required        | `Iden           |
|                 | the Target.     |                 | tifier: "HT_1"` |
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
| `Name`          | Name for this   | Optional        | `Name: "Har     |
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
| `Attributes`    | Additional data | Optional        | `Attri          |
|                 | you can store   |                 | butes: &map[str |
|                 | for a Target,   |                 | ing]interface{} |
|                 | such as email   |                 | {"email":"demo@ |
|                 | addresses or    |                 | harness.io"},`\ |
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

##### Create a Target

    target2 := evaluation.Target{
     Identifier: "HT_1",
     Name: "Harness_Target_1",
     Attributes: &map[string]interface{}{"email":"demo@harness.io"},
    }

##### Create a Target with the builder

If you create a Target with the builder, use `Custom` instead of
`Attributes`.

    target := dto.NewTargetBuilder("HT_1").
     Name("Harness_Target_1").
     Custom("email", "demo@harness.io").
     Build()

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

#### Evaluate a string Variation

    client.StringVariation(flagName, &target, "default_string")

#### Evaluate a boolean Variation

    showFeature, err := client.BoolVariation(featureFlagKey, &target, false)

#### Evaluate a number Variation

    client.NumberVariation(flagName, &target, -1)

#### Evaluate a JSON Variation

    client.JSONVariation(flagName, &target, types.JSON{"darkmode": false})

### Test Your App is Connected to Harness

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

### Close the SDK

To help prevent memory leaks, we recommend closing the SDK when it's not
in use. To do this, run the following command: 

    client.Close()

### Additional options 

#### Configure your logger

The SDK has a default logger, however, you can provide your own logger
to the SDK by passing it in as a configuration option. 

For example, the following creates an instance of the logrus logger and
passes it in as a configuration option:

    logger := logrus.New()
    logger.SetLevel(logrus.ErrorLevel)

     // Create a feature flag client
    client, err := harness.NewCfClient(sdkKey, harness.WithLogger(logger))

#### Use the Relay Proxy

When using your Feature Flag SDKs with a [Harness Relay
Proxy](../relay-proxy/relay-proxy.md){target="_blank"} you need to
change the default URL and events URL to `http://localhost:7000` when
initializing the SDK. For example:

    client, err := harness.NewCfClient(apiKey,
    harness.WithURL("http://localhost:7000"),
    harness.WithEventsURL("http://localhost:7000"))

### Sample code for a Go application

Here is a sample code for integrating with the Go SDK:

    package main

     import (
             "context"
             "fmt"
             "log"
             "time"
     
             harness "github.com/harness/ff-golang-server-sdk/client"
             "github.com/harness/ff-golang-server-sdk/dto"
             "github.com/sirupsen/logrus"
    )

     const sdkKey = "your SDK key"

     const featureFlag = "harnessappdemodarkmode"

     func main() {

            logger := logrus.New()
            logger.SetLevel(logrus.ErrorLevel)
        
            client, err := harness.NewCfClient(myApiKey, 
                     harness.WithURL("https://config.ff.harness.io/api/1.0"), 
                     harness.WithEventsURL("https://events.ff.harness.io/api/1.0”), 
                     harness.WithPullInterval(1),
                     harness.WithLogger(logger),
                     harness.WithStreamEnabled(false)
    )

            defer func() {
                   if err := client.Close(); err != nil {
                         log.Printf("error while closing client err: %v", err)
                   }
             }()

            if err != nil {
                     log.Printf("could not connect to CF servers %v", err)
             }

            target := dto.NewTargetBuilder("HT_1").
                     Name("Harness_Target_1").
                     Custom("email", "demo@harness.io").
                     Build()
        
            ctx, cancel := context.WithCancel(context.Background())

             go func() {
                     for {
                            select {
                             case <-ctx.Done():
                                     return
                             default:
                                     showFeature, err :=     client.BoolVariation(featureFlag, &target, false)

                                      if err != nil {
                                            fmt.Printf("Error getting value: %v", err)
                                      }

                                      fmt.Printf("KeyFeature flag '%s' is %t for this user\n", featureFlag, showFeature)
                          time.Sleep(10 * time.Second)
                     }
                 }
            }()

            time.Sleep(5 * time.Minute)
            cancel()
    }
