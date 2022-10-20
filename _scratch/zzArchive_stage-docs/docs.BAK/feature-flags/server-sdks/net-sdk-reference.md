---
title: .NET SDK Reference
description: This topic explains how to use the Harness Feature Flags (FF) SDK in your .NET application.
tags: 
   - helpDocs
   - feature flag
   - SDK
   - .NET
helpdocs_topic_id: c86rasy39v
helpdocs_is_private: false
helpdocs_is_published: true
---

::: warning-callout
In Version 1.1.3 of the .NET SDK, the package name for installing the
SDK changed from **ff-netF48-server-sdk** to f**f-dotnet-server-sdk**.
To use this version, make sure you remove the old package name and use
the new one.\
\
You can do this by using the following commands:\
**Remove the old package**\
`dotnet remove package ff-netF48-server-sdk`\
**Add the new package\
**`dotnet add package ff-dotnet-server-sdk`
:::

This topic describes how to use the Harness Feature Flags .NET SDK for
your .Net application.

For getting started quickly, you can use our [sample code from the .NET
SDK
README](https://github.com/harness/ff-dotnet-server-sdk){target="_blank"}.
You can also
[clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
and run a sample application from the[.NET SDK GitHub
Repository.](https://github.com/harness/ff-dotnet-server-sdk){target="_blank"}

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
The current version of this SDK is **1.1.4.**
:::

### Requirements

To use this SDK, make sure you:  

-   Install [.NET Framework
    4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)
    or newer, or [.Net
    5.0.104](https://docs.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-using-the-dotnet-cli)
    or newer.

::: note-callout
The library is packaged as multi-target and supports the netstandard 2.0
set of API\'s as well as  net461 for older frameworks.
:::

-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-dotnet-server-sdk){target="_blank"}
-   Create a .NET application, or
    [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    our [sample
    application](https://github.com/harness/ff-dotnet-server-sdk){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](../ff-creating-flag/create-a-feature-flag.md).
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`.
-   [Create a server SDK key and make a copy of
    it](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}

### Install the SDK

Install the SDK by using the `dotnet add package` command, for example: 

    dotnet add package ff-dotnet-server-sdk --version 1.1.4

::: warning-callout
In Version 1.1.3 of the .NET SDK, the package name for installing the
SDK changed from **ff-netF48-server-sdk** to f**f-dotnet-server-sdk**.
To use this version, make sure you remove the old package name and use
the new one.\
\
You can do this by using the following commands:\
**Remove the old package**\
`dotnet remove package ff-netF48-server-sdk`\
**Add the new package\
**`dotnet add package ff-dotnet-server-sdk`
:::

### Initialize the SDK

To initialize the .NET SDK, you need to:

1.  Add your Server SDK key to connect to your Harness Environment.
2.  Add a Target that you want to Evaluate against a Feature Flag.
3.  (Optional) Configure the SDK.
4.  Complete the initialization with the SDK using the Server SDK Key,
    Target, and Configuration parameters you set.

#### Add the Server SDK Key

To connect to the correct Environment that you set up on the Harness
Platform, you need to add the Server SDK Key from that Environment.
Input the Client SDK Key into the `sdkKey` parameter, for example:

    public static String sdkKey = "YOUR_API_KEY";

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
| `Identifier`    | Unique ID for   | Required        | `.Iden          |
|                 | the Target.     |                 | tifier("HT_1")` |
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
| `Name`          | Name for this   | Optional        | `.Name("Harne   |
|                 | Target. This    |                 | ss_Target_1") ` |
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
| `Attributes`    | Additional data | Optional        | `.              |
|                 | you can store   |                 | Attributes(new  |
|                 | for a Target,   |                 | Dictionary<stri |
|                 | such as email   |                 | ng, string>(){{ |
|                 | addresses or    |                 | "email", "demo@ |
|                 | location.       |                 | harness.io"}})` |
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

    Target target = Target.builder()
                                .Name("Harness_Target_1") 
                                .Identifier("HT_1")
                                .Attributes(new Dictionary<string, string>(){{"email", "demo@harness.io"}})
                                .build();

 

#### Configure the SDK

When initializing the SDK, you also have the option of providing
alternative configuration by using `Config.Builder()`. 

You can configure the following base features of the SDK:

+-----------------+-----------------+-----------------+-----------------+
| **Name**        | **Example**     | **Description** | **Default       |
|                 |                 |                 | Value**         |
+-----------------+-----------------+-----------------+-----------------+
| configUrl       | `Confi          | The URL used to | `https:/        |
|                 | gUrl("https://c | fetch Feature   | /config.ff.harn |
|                 | onfig.ff.harnes | Flag            | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Evaluations.    |                 |
|                 |                 | When using the  |                 |
|                 |                 | Relay Proxy,    |                 |
|                 |                 | change this     |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| eventUrl        | `Even           | The URL for     | `https:/        |
|                 | tUrl("https://e | posting metrics | /events.ff.harn |
|                 | vents.ff.harnes | data to the     | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Feature Flag    |                 |
|                 |                 | service. When   |                 |
|                 |                 | using the Relay |                 |
|                 |                 | Proxy, change   |                 |
|                 |                 | this            |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| pollInterval    | `SetPolli       | The interval    | `20` (seconds)  |
|                 | ngInterval(20)` | **in seconds**  |                 |
|                 |                 | that we poll    |                 |
|                 |                 | for changes     |                 |
|                 |                 | when you are    |                 |
|                 |                 | using stream    |                 |
|                 |                 | mode.           |                 |
+-----------------+-----------------+-----------------+-----------------+
| streamEnabled   | `SetStrea       | Set to `true`   | `true`          |
|                 | mEnabled(true)` | to enable       |                 |
|                 |                 | streaming mode. |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | streaming mode. |                 |
+-----------------+-----------------+-----------------+-----------------+
| a               | `SetAnalytic    | Set             | `true`          |
| nalyticsEnabled | sEnabled(true)` | to `true` to    |                 |
|                 |                 | enable          |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | Set             |                 |
|                 |                 | to `false` to   |                 |
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

    CfClient.Instance.Initialize(apiKey, Config.Builder()
        .ConfigUrl("https://config.ff.harness.io/api/1.0")
        .EventUrl("https://events.ff.harness.io/api/1.0")
        .SetPollingInterval(60)
        .SetStreamEnabled(true)
        .SetAnalyticsEnabled(false)
        .Build());

#### Complete the initialization

To complete the initialization, create an instance of the `cfClient` and
pass in the `sdkKey` and `Config.Builder`, for example: 

    CfClient.Instance.Initialize(apiKey, Config.Builder().Build());

#### Sample of initializing the SDK

    public static String apiKey = Environment.GetEnvironmentVariable("FF_API_KEY");
            public static String flagName = Environment.GetEnvironmentVariable("FF_FLAG_NAME") is string v && v.Length > 0 ? v : "harnessappdemodarkmode";

                    static void Main(string[] args)
            {

                // Create a feature flag client
                CfClient.Instance.Initialize(apiKey, Config.Builder().Build());

                
                // Create a target (different targets can get different results based on rules)
                Target target = Target.builder()
                                .Name("DotNetSDK") 
                                .Identifier("dotnetsdk")
                                .Attributes(new Dictionary<string, string>(){{"location", "emea"}})
                                .build();

### Evaluate a Flag

Evaluating a Flag is when the SDK processes all Flag rules and returns
the correct Variation of that Flag for the Target you provide. 

If a matching Flag can't be found, or the SDK can't remotely fetch
Flags, the default value is returned. 

There are different methods for the different Variation types and for
each method you need to pass in:

-   Identifier of the Flag you want to evaluate
-   The Target object you want to evaluate against
-   The default Variation

For example:

#### Evaluate a boolean Variation

    public bool boolVariation(string key, dto.Target target, bool defaultValue)

#### Evaluate a number Variation 

    public double numberVariation(string key, dto.Target target, int defaultValue)

#### Evaluate a string Variation

    public string stringVariation(string key, dto.Target target, string defaultValue)

#### Evaluate a JSON Variation

    public JObject jsonVariation(string key, dto.Target target, JObject defaultValue)

### Listen for events

This method provides a way to listen to the different events that might
be triggered by the SDK, indicating a specific change in the SDK.

``` {.hljs .coffeescript}
client.InitializationCompleted += (sender, e) =>
{
    // fired when authentication is completed and recent configuration is fetched from server
    Console.WriteLine("Notification Initialization Completed");
};
client.EvaluationChanged += (sender, identifier) =>
{
    // Fired when flag value changes.
    Console.WriteLine($"Flag changed for {identifier}");
};
```

### Test your app is connected to Harness

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

### Additional options

#### Develop on your local environment

By default, you are connected to the Harness environment but you can use
a local connector to develop in your local environment, for example:

    LocalConnector connector = new LocalConnector("local");
    client = new CfClient(connector);

#### Store flags offline 

You can store your last Flag configuration for the SDK to use if your
application is offline or you have an asynchronous startup. For
example: 

    FileMapStore fileStore = new FileMapStore("Non-Freemium");
    LocalConnector connector = new LocalConnector("local");
    client = new CfClient(connector, Config.builder().store(fileStore).build()); 

If you don't store your Flag configuration and your application is
offline, the Flags will be evaluated based on the `defaultValue`. 

#### Configure your logger

You can use Serilog as your logger for this SDK. To do this, add the
Serilog package, for example: 

`dotnet add package Serilog`

You can then configure the logger to write to the console with debug,
for example: 

    // Logger
    Log.Logger = new LoggerConfiguration()
        .MinimumLevel.Debug()
        .WriteTo.Console()
        .CreateLogger();

#### Use the Relay Proxy

When using your Feature Flag SDKs with a [Harness Relay
Proxy](../relay-proxy/relay-proxy.md){target="_blank"} you need to
change the default ConfigURL and EventURL that we use. You can pass the
URLs in when initializing the SDK, for example: 

    CfClient.Instance.Initialize(apikey, Config.Builder()
                .ConfigUrl("http://localhost:7000")
                .EventUrl("http://localhost:7000")
                .Build());

### Sample code for a .NET application

Here is a sample code for integrating with the .NET SDK:

    using System;
    using System.Collections.Generic;
    using io.harness.cfsdk.client.dto;
    using io.harness.cfsdk.client.api;
    using System.Threading;

     namespace getting_started
    {
        class Program
        {

            public static String apiKey = Environment.GetEnvironmentVariable("FF_API_KEY");
            public static String flagName = Environment.GetEnvironmentVariable("FF_FLAG_NAME") is string v && v.Length > 0 ? v : "harnessappdemodarkmode";

                    static void Main(string[] args)
            {

                // Create a feature flag client
                CfClient.Instance.Initialize(apiKey, Config.Builder().Build());
                
                // Create a target (different targets can get different results based on rules)

                Target target = Target.builder()
                                .Name("Harness_Target_1") 
                                .Identifier("HT_1")
                                .Attributes(new Dictionary<string, string>(){{"email", "demo@harness.io"}})
                                .build();

                // Loop forever reporting the state of the flag
                while (true)
                {
                    bool resultBool = CfClient.Instance.boolVariation(flagName, target, false);
                    Console.WriteLine("Flag variation " + resultBool);
                    Thread.Sleep(10 * 1000);
                }
            }
        }
    }