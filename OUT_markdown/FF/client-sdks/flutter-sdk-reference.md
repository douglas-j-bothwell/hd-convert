---
title: Flutter SDK Reference
description: This topic explains how to use the Feature Flags (FF) SDK in your Flutter application.
tags: 
   - helpDocs
   - flutter
   - feature flag
   - SDK
   - Flutter SDK
helpdocs_topic_id: mmf7cu2owg
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags SDK for your
Flutter application. 

For getting started quickly, you can use our [sample code from the SDK
README](https://github.com/harness/ff-flutter-client-sdk/blob/main/README.md){target="_blank"}.
You can also
[clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
and run a sample application from the [Flutter SDK GitHub
Repository.](https://github.com/harness/ff-flutter-client-sdk){target="_blank"}

### Before you begin

You should read and understand the following:

-   [Feature Flags
    Overview](/article/7n9433hkc0-cf-feature-flag-overview)
-   [Getting Started with Feature
    Flags](/article/0a2u2ppp8s-getting-started-with-continuous-features)
-   [Client-Side and Server-Side
    SDKs](/article/rvqprvbq8f-client-side-and-server-side-sdks)
-   [Communication Strategy Between SDKs and Harness Feature
    Flags](/article/7ikyqtmjce-communication-sdks-harness-feature-flags)

### Version

::: note-callout
The current version of this SDK is **1.0.4.**
:::

### Requirements

To use this SDK, make sure you:

-   Install the [Flutter SDK, version 2.10.4 or
    higher](https://docs.flutter.dev/get-started/install){target="_blank"}.
-   (For iOS apps) Install
    [Xcode](https://docs.flutter.dev/get-started/install/macos#install-xcode){target="_blank"}.
-   (For Android apps) Install [Android
    Studio](https://developer.android.com/studio?gclid=CjwKCAjwp7eUBhBeEiwAZbHwkRqdhQkk6wroJeWGu0uGWjW9Ue3hFXc4SuB6lwYU4LOZiZ-MQ4p57BoCvF0QAvD_BwE&gclsrc=aw.ds){target="_blank"}, or
    install the Android SDK for Command-Line Interface (CLI) only.

::: note-callout
To check you have installed the prerequisites, run the `flutter doctor`
command.
:::

-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-flutter-client-sdk){target="_blank"}
-   Create a Flutter application, or
    [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"}
    our [sample
    application](https://github.com/harness/ff-flutter-client-sdk){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](/article/1j7pdkqh7j-create-a-feature-flag){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`.
-   [Create an SDK key and make a copy of
    it](/article/1j7pdkqh7j-create-a-feature-flag#step_3_create_an_sdk_key){target="_blank"}.

### Install the SDK

To install the SDK, add the Feature Flag Flutter SDK dependency into the
`pubspec.yaml` file, for example:

    ff_flutter_client_sdk: ^1.0.4

Then import the following packages into your project:

    import 'package:ff_flutter_client_sdk/CfClient.dart';
    import 'package:ff_flutter_client_sdk/CfConfiguration.dart';
    import 'package:ff_flutter_client_sdk/CfTarget.dart';

### Initialize the SDK

To initialize the Flutter SDK, you need to:

1.  Add a Target that you want to Evaluate against a Feature Flag.
2.  (Optional) Configure the SDK options.
3.  Add your Client SDK key to connect to your Harness Environment.
4.  Complete the initialization with the SDK using the Client SDK Key,
    Target, and Configuration parameters you set.

#### Add a Target to Evaluate

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
Flags](/article/xf3hmxbaji-targeting-users-with-flags){target="_blank"}.
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| identifier      | Unique ID for   | Required        | `.setIden       |
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
| name            | Name for this   | Optional        | `.setName("Harn |
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

    var target = CfTargetBuilder().setIdentifier("HT_1").setName("Harness_Target_1").build();

#### Configure the SDK

You can configure the following options for the SDK:

+-----------------+-----------------+-----------------+-----------------+
| **Name**        | **Configuration | **Description** | **Default       |
|                 | Option**        |                 | Value**         |
+-----------------+-----------------+-----------------+-----------------+
| baseUrl         | `setConfi       | The URL used to | `https:/        |
|                 | gUri("https://c | fetch Feature   | /config.ff.harn |
|                 | onfig.ff.harnes | Flag            | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Evaluations.    |                 |
|                 |                 | When using the  |                 |
|                 |                 | Relay Proxy,    |                 |
|                 |                 | change this     |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| eventsUrl       | `setEven        | The URL for     | `https:/        |
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
| pollInterval    | `setPolli       | The interval    | `60` (seconds)  |
|                 | ngInterval(60)` | **in seconds**  |                 |
|                 |                 | that we poll    |                 |
|                 |                 | for changes     |                 |
|                 |                 | when you are    |                 |
|                 |                 | using stream    |                 |
|                 |                 | mode.           |                 |
+-----------------+-----------------+-----------------+-----------------+
| enableStream    | `setStrea       | Set to `true`   | `true`          |
|                 | mEnabled(True)` | to enable       |                 |
|                 |                 | streaming mode. |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | streaming mode. |                 |
+-----------------+-----------------+-----------------+-----------------+
| enableAnalytics | `setAnalytic    | Set to `true`   | `true`          |
|                 | sEnabled(True)` | to enable       |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | Set to `false`  |                 |
|                 |                 | to disable      |                 |
|                 |                 | analytics.      |                 |
|                 |                 |                 |                 |
|                 |                 | **Note**: When  |                 |
|                 |                 | enabled,        |                 |
|                 |                 | analytics data  |                 |
|                 |                 | is posted every |                 |
|                 |                 | 60 seconds.     |                 |
+-----------------+-----------------+-----------------+-----------------+

For example:

    // Flutter SDK Config
    var conf = CfConfigurationBuilder()
            .setConfigUri("https://config.ff.harness.io/api/1.0")
            .setEventUrl("https://events.ff.harness.io/api/1.0")
            .setPollingInterval(60)
            .setStreamEnabled(true)
            .setAnalyticsEnabled(true)
            .build();

#### Complete the initialization

`CfClient`  is a base class that provides all the features of the SDK,
which can be accessed with `CfClient.initialize`.

To initialize the SDK, you must pass in the following:

-   `apiKey` - The Client SDK Key you created when [creating the Feature
    Flag](https://ngdocs.harness.io/article/1j7pdkqh7j-create-a-feature-flag#step_3_create_an_sdk_key).
-   Any configuration options you want to use.
-   The Target you want to evaluate.

#### Sample of initializing the SDK

    final conf = CfConfigurationBuilder()
        .setStreamEnabled(false)
        .setPollingInterval(60)
        .build();

    final target = CfTargetBuilder().setIdentifier(name).build();

    final res = await CfClient.initialize(apiKey, conf, target);

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

    //get boolean evaluation
    final evaluation = await CfClient.boolVariation("demo_bool_evaluation", false);

#### Evaluate a number Variation

    //get number evaluation
    final numberEvaluation = await CfClient.numberVariation("demo_number_evaluation", 0);

#### Evaluate a string Variation

    //get string evaluation
    final stringEvaluation = await CfClient.stringVariation("demo_string_evaluation", "default");

#### Evaluate a JSON Variation

    //get json evaluation
    final jsonEvaluation = await CfClient.jsonVariation("demo_json_evaluation", {});

### Listen for events

#### Register the events listener

The `eventsListener` method provides a way to register a listener for
different events that might be triggered by SDK.

The possible events and their responses are outlined in the following
table:

  -------------------- ----------------------------
  **EventType**        **Response**
  SSE_START            null
  SSE_END              null
  EVALUATION_POLLING   List\<EvaluationResponse\>
  EVALUATION_CHANGE    EvaluationResponse
  -------------------- ----------------------------

To listen for events, register the events listener, for example:

    CfClient.registerEventsListener((EvaluationResponse, EventType) {
         
        });

The triggered event will return one of the following types:

    enum EventType {
        SSE_START,
        SSE_END,
        EVALUATION_POLLING,
        EVALUATION_CHANGE
    }

#### Close the events listener

To avoid unexpected behavior, when the listener isn\'t needed, turn it
off by
calling `CfClient.getInstance().unregisterEventsListener(eventsListener),` for
example:

    CfClient.unregisterEventsListener(eventsListener)

### Test your app is connected to Harness

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

![](https://files.helpdocs.io/i5nl071jo5/articles/mmf7cu2owg/1656593738339/flutter.gif){style="display:block;margin-left:0;margin-right:auto"
hd-align="left"}

### Close the SDK

To avoid potential memory leaks, when you no longer need the SDK, you
should close it. For example, when the app is closed, also close the
SDK.

To close the SDK, call this method:

    CfClient.destroy()

### Additional options

#### Use our public API methods

The Public API exposes the following methods that you can use:

    static Future<InitializationResult> initialize(String apiKey, CfConfiguration configuration, CfTarget target)

    static Future<bool> boolVariation(String evaluationId, bool defaultValue)

    static Future<String> stringVariation(String evaluationId, String defaultValue)

    static Future<double> numberVariation(String evaluationId, double defaultValue)

    static Future<Map<dynamic, dynamic>> jsonVariation(String evaluationId, Map<dynamic, dynamic> defaultValue)

    static Future<void> registerEventsListener(CfEventsListener listener)

    static Future<void> unregisterEventsListener(CfEventsListener listener)

    static Future<void> destroy()

### Sample code for a Flutter application

Here is a sample code for using FF SDKs with the Flutter application.

    final conf = CfConfigurationBuilder()
        .setStreamEnabled(true)
        .setPollingInterval(60) //time in seconds (minimum value is 60)
        .build();
    final target = CfTargetBuilder().setIdentifier(name).build();

    final res = await CfClient.initialize(apiKey, conf, target);


    //get number evaluation
    final numberEvaluation = await CfClient.numberVariation("demo_number_evaluation", 0);

    //get string evaluaation
    final stringEvaluation = await CfClient.stringVariation("demo_string_evaluation", "default");

    //get json evaluation
    final jsonEvaluation = await CfClient.jsonVariation("demo_json_evaluation", {});

    CfClient.registerEventsListener((responseData, eventType) {
        _eventListener = (responseData, eventType){};
        switch (eventType) {
          case EventType.SSE_START:
            print("Started SSE");
            break;
          case EventType.SSE_END:
            print("SSE Completed");
            break;
          case EventType.EVALUATION_CHANGE:
            String flag = (responseData as EvaluationResponse).flag;
            dynamic value = (responseData as EvaluationResponse).value;

            break;
          case EventType.EVALUATION_POLLING:
            List pollingResult = responseData;

            pollingResult.forEach((element) {
              String flag = (element as EvaluationResponse).flag;
              dynamic value = (element as EvaluationResponse).value;

            });
            break;
        }
    });

    //Shutting down SDK
    CfClient.destroy()
