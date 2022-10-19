---
title: Android SDK Reference
description: This topic explains how to use the Harness Feature Flags SDK in your Android application.
tags: 
   - helpDocs
   - SDK
   - android SDK
   - Continuous features
   - feature flag
helpdocs_topic_id: 74t18egxbi
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags Android SDK
for your Android application. 

For getting started quickly, you can use our [sample code from the SDK
README](https://github.com/harness/ff-android-client-sdk/blob/main/README.md){target="_blank"}.
You can also
[clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
and run a sample application from the [Android SDK GitHub
Repository.](https://github.com/harness/ff-android-client-sdk){target="_blank"}

::: note-callout
The SDK caches your Feature Flags. If the cache can\'t be accessed,
the `defaultValue` is used.
:::

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
The current version of this SDK is **1.0.10.** To use this version of
the SDK, you also need to use Android API level 19 or higher.
:::

### Requirements

To use this SDK, make sure you:

-   Installed [Android
    Studio](https://developer.android.com/studio?gclid=CjwKCAjwp7eUBhBeEiwAZbHwkRqdhQkk6wroJeWGu0uGWjW9Ue3hFXc4SuB6lwYU4LOZiZ-MQ4p57BoCvF0QAvD_BwE&gclsrc=aw.ds) or
    the [Android
    SDK](https://github.com/harness/ff-android-client-sdk/blob/main/docs/dev_environment.md) for
    CLI only
-   Installed [Java
    11](https://www.oracle.com/java/technologies/downloads/#java11) or
    newer
-   Installed [Gradle 7.4.1](https://gradle.org/releases/) or newer
-   Use Android API level 19 or higher.

Then ensure you:

-   Create an Android application to use with the SDK, or [clone our
    sample
    application](https://github.com/harness/ff-android-client-sdk){target="_blank"} to
    use.
-   Download the SDK from our [GitHub
    Repository](https://github.com/harness/ff-android-client-sdk){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`.
-   [Create a Client SDK key and make a copy of
    it](../ff-creating-flag/create-a-feature-flag.md){target="_blank"}.

### Install the SDK

To add the Android SDK to your application, add the following snippet to
the root project\'s `build.gradle` file:

    buildscript {
        repositories {
            mavenCentral()
        }

Then, in your app module\'s `build.gradle` file, add the following
dependency for the SDK:

    implementation 'io.harness:ff-android-client-sdk:1.0.10'

### Initialize the SDK

To initialize the Android SDK, you need to:

1.  Add your Client SDK key to connect to your Harness Environment.
2.  Add a Target that you want to Evaluate against a Feature Flag.
3.  Configure the SDK options, if needed. For more details on what
    features you can configure for this SDK, go to [Configure the
    SDK](android-sdk-reference.md).
4.  Complete the initialization with the SDK using your Client SDK Key,
    Target, and Configuration parameters that you set.

#### Add a Target

::: tip-callout
**What is a Target?**\
Targets are used to control which users see which Variation of a Feature
Flag, for example, if you want to do internal testing, you can enable
the Flag for some users and not others. When creating a Target, you give
it a name and a unique identifier. Often Targets are users but you can
create a Target from anything that can be uniquely identified, such as
an app or a machine.\
\
For more information about Targets, go to [Targeting Users With
Flags](../ff-target-management/targeting-users-with-flags.md){target="_blank"}.
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| identifier      | ID of the       | Required        | `.iden          |
|                 | Target.         |                 | tifier("HT_1")` |
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
| name            | Name for this   | Optional        | `.name("Harn    |
|                 | Target. This    |                 | ess_Target_1")` |
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
|                 | Read **Regex    |                 |                 |
|                 | requirements    |                 |                 |
|                 | for Target      |                 |                 |
|                 | names and       |                 |                 |
|                 | iden            |                 |                 |
|                 | tifiers** below |                 |                 |
|                 | for accepted    |                 |                 |
|                 | characters.     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| attributes      | Additional data | Optional        | `ta             |
|                 | you can store   |                 | rget.attributes |
|                 | for a Target,   |                 | ["email"] = "de |
|                 | such as email   |                 | mo@harness.io"` |
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
letters, for example `Cafe_789`.

</div>

For example:

    val target = Target().identifier("HT_1").name("Harness_Target_1")
            target.attributes["email"] = "demo@harness.io"

#### Configure the SDK

You can configure the following features of the SDK:

+-----------------+-----------------+-----------------+-----------------+
| **Name**        | **Configuration | **Description** | **Default**     |
|                 | Option**        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| baseUrl         | `bas            | The URL used to | `https:/        |
|                 | eUrl("https://c | fetch Feature   | /config.ff.harn |
|                 | onfig.ff.harnes | Flag            | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Evaluations.    |                 |
|                 |                 | When using the  |                 |
|                 |                 | Relay Proxy,    |                 |
|                 |                 | change this     |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| eventsUrl       | `even           | The URL for     | `https:/        |
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
| pollInterval    | `polli          | The interval    | `60` (seconds)  |
|                 | ngInterval(60)` | **in seconds**  |                 |
|                 |                 | that we poll    |                 |
|                 |                 | for changes     |                 |
|                 |                 | when you are    |                 |
|                 |                 | using stream    |                 |
|                 |                 | mode.           |                 |
+-----------------+-----------------+-----------------+-----------------+
| enableStream    | `enab           | Set to `true`   | `true`          |
|                 | leStream(true)` | to enable       |                 |
|                 |                 | streaming mode. |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | streaming mode. |                 |
+-----------------+-----------------+-----------------+-----------------+
| enableAnalytics | `enableA        | Set to `true`   | `true`          |
|                 | nalytics(true)` | to enable       |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | analytics.      |                 |
+-----------------+-----------------+-----------------+-----------------+

For example:

      val sdkConfiguration = CfConfiguration.builder()
                .baseUrl("https://config.ff.harness.io/api/1.0")
                .eventUrl("https://events.ff.harness.io/api/1.0")
                .pollingInterval(60)
                .enableStream(true)
                .enableAnalytics(false)
                .build()

#### Complete the initialization

`CfClient`  is a base class that provides all the features of the SDK,
which can be accessed with `CfClient.getInstance()`.

To initialize the SDK, you must pass in the following:

-   `YOUR_API_KEY` - The client SDK key you created when [creating the
    Feature
    Flag](../ff-creating-flag/create-a-feature-flag.md).
-   Any configuration options you want to use.
-   The Target you want to evaluate.

#### Sample of initializing the SDK

``` {.hljs .kotlin}
val sdkConfiguration = CfConfiguration.builder()
    .pollingInterval(60) //time in seconds
    .build()

val target = Target().identifier("target")

CfClient.getInstance().initialize(context, "YOUR_API_KEY", sdkConfiguration, target)
```

### Evaluate a Flag

Evaluating a Flag is when the SDK processes all Flag rules and returns
the correct Variation of that Flag for the Target you provide. 

If a matching Flag can't be found, or the SDK can't remotely fetch
flags, the default value is returned. 

There are different methods for the different Variation types and for
each method you need to pass in:

-   Identifier of the Flag you want to evaluate
-   The default Variation

::: note-callout
The Flag is evaluated against the Target you pass in when initializing
the SDK.
:::

#### Evaluate a boolean Variation

`boolVariation(String evaluationId, boolean defaultValue)`

    // Get boolean evaluation:
    val evaluation: Boolean = CfClient.getInstance().boolVariation("demo_evaluation", false)  

#### Evaluate a number Variation

`numberVariation(String evaluationId, double defaultValue)`

    // Get number evaluation:
    val numberEvaluation: Double = CfClient.getInstance().numberVariation("demo_number_evaluation", 0.0)  

#### Evaluate a string Variation

`stringVariation(String evaluationId, String defaultValue)`

    // Get String evaluation:
    val stringEvaluation: String = CfClient.getInstance().stringVariation("demo_string_evaluation", "demo_value")  

#### Evaluate a JSON Variation

`jsonVariation(String evaluationId, JSONObject defaultValue)`

    // Get JSON evaluation:
    val jsonEvaluation: String = CfClient.getInstance().jsonVariation("demo_string_evaluation", JSONObject("{}"))  

::: note-callout
These methods must **not** be executed on the application\'s main thread
as they could trigger network operations.
:::

### Listen for events {#undefined}

#### Register the event listener

The `eventsListener` method provides a way to register a listener for
different events that might be triggered by SDK.

The possible events and their responses are outlined in the following
table:

  ------------------- --------------------
  **EVENT_TYPE**      **Response**
  SSE_START           \-
  SSE_END             \-
  EVALUATION_CHANGE   `Evaluation`
  EVALUATION_RELOAD   `List<Evaluation>`
  ------------------- --------------------

For example:

    private var eventsListener = EventsListener { event ->

        CfLog.OUT.v(tag, "Event: ${event.eventType}")
    }

    val registerEventsOk = CfClient.getInstance().registerEventsListener(eventsListener)
    val unregisterEventsOk = CfClient.getInstance().unregisterEventsListener(eventsListener)

#### Close the event listener

To avoid unexpected behavior, when the listener isn\'t needed, turn it
off by
calling `CfClient.getInstance().unregisterEventsListener(eventsListener),` for
example:

    val success = CfClient.getInstance().unregisterEventsListener(eventsListener)

### Test your app is connected to Harness

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

![](https://files.helpdocs.io/i5nl071jo5/articles/74t18egxbi/1656425256313/android-sdk.gif)

### Close the SDK

To avoid potential memory leaks, when you no longer need the SDK, you
should close it. For example, when the app is closed, also close the
SDK.

To close the SDK, call this method:

    CfClient.getInstance().destroy()

### Additional options

#### Configure your logger

We use Android Log for this SDK.

::: note-callout
For details on how to use Android Log, go to the [official
guide](https://source.android.com/devices/tech/debug/understanding-logging#log-standards). 
:::

The SDK uses the simple class names as tags. You can enable log levels
for each of them using the following tags:

-   `CfClient` - Main client logs
-   `AnalyticsManager` - Analytics logs
-   `SSEListener` - SEE stream logs
-   `DefaultApi` - HTTP request logs

You can enable these tags using the following command:

    adb shell setprop log.tag.<tag_name> VERBOSE

#### Use the SDK for unit tests

To be able to use the SDK in unit tests, you must set the SDKs logging
to `testModeOn`, which turns on the system output logging strategy.

    CfLog.testModeOn()

Alternatively, to use the Android [log
class](https://developer.android.com/reference/android/util/Log) use:

    CfLog.runtimeModeOn()

::: note-callout
Standard Android logging is the default logging strategy, so turning on
runtime mode is not required.
:::

#### Use our public API methods

Our public API exposes the following methods that you can use:

    public void initialize(

                final Context context,
                final String apiKey,
                final CfConfiguration configuration,
                final Target target,
                final AuthCallback authCallback

    ) throws IllegalStateException

    public void initialize(

            final Context context,
            final String apiKey,
            final CfConfiguration configuration,
            final Target target,
            final CloudCache cloudCache

    ) throws IllegalStateException

    public void initialize(

            final Context context,
            final String apiKey,
            final CfConfiguration configuration,
            final Target target

    ) throws IllegalStateException

-   `public boolean boolVariation(String evaluationId, boolean defaultValue)`
-   `public String stringVariation(String evaluationId, String defaultValue)`
-   `public double numberVariation(String evaluationId, double defaultValue)`
-   `public JSONObject jsonVariation(String evaluationId, JSONObject defaultValue)`
-   `public void registerEventsListener(EventsListener listener)`
-   `public void unregisterEventsListener(EventsListener observer)`
-   `public void destroy()`

### Sample code for an Android application

Here is a sample code for using Harness Feature Flag SDKs with the
Android application. To learn more about using the sample Android
application, go to the [Android GitHub
repository](https://github.com/drone/ff-android-client-sample/tree/main/app).

    package com.example.ffsdktryout
    import androidx.appcompat.app.AppCompatActivity
    import android.os.Bundle
    import io.harness.cfsdk.*
    import io.harness.cfsdk.cloud.model.Target
    import io.harness.cfsdk.logging.CfLog
    import io.harness.cfsdk.CfClient
    import io.harness.cfsdk.cloud.oksse.model.StatusEvent
    import io.harness.cfsdk.cloud.core.model.Evaluation
    import io.harness.cfsdk.cloud.events.EvaluationListener
    import io.harness.cfsdk.cloud.oksse.EventsListener
    class MainActivity : AppCompatActivity() {
        private val logTag = MainActivity::class.simpleName
        private var eventsListener = EventsListener { event ->
            if (event.eventType == StatusEvent.EVENT_TYPE.EVALUATION_CHANGE) {
                // Do something
            } else if (event.eventType == StatusEvent.EVENT_TYPE.EVALUATION_RELOAD) {
                // Do something else
            }
        }
        private val evaluationListener: EvaluationListener = EvaluationListener {
            // Do something
        }
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
            val target = Target().identifier("YOUT_TARGET_IDENTIFIER").name("YOUR_TARGET_NAME")
            val remoteConfiguration = CfConfiguration.builder()
                .enableStream(true)
                .build()
            io.harness.cfsdk.CfClient.getInstance()
                .initialize(
                    this,
                    "YOUR_API_KEY",
                    remoteConfiguration,
                    target
                ) { _, result ->
                    if (result.isSuccess) {
                        val registerEventsOk = CfClient.getInstance().registerEventsListener(eventsListener)
                        var registerEvaluationsOk = CfClient.getInstance().registerEvaluationListener(
                            "YOUR_EVALUATION_IDENTIFIER",
                            evaluationListener
                        )
                    } else {
                        CfLog.OUT.e(logTag, "Init. error")
                    }
                }
        }
    }
