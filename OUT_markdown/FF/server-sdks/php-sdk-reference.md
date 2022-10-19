---
title: PHP SDK Reference
description: This topic describes how to use the Harness Feature Flags PHP SDK for your PHP application. For getting started quickly, you can use our sample code from the PHP SDK README. You can also clone and ru…
tags: 
   - helpDocs
helpdocs_topic_id: 3qrik15pkz
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags PHP SDK for
your PHP application.

For getting started quickly, you can use our [sample code from the PHP
SDK
README](https://github.com/harness/ff-php-server-sdk/blob/main/README.md){target="_blank"}.
You can also
[clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"}
and run a sample application from the [PHP SDK GitHub
Repository.](https://github.com/harness/ff-php-server-sdk){target="_blank"}

Important: Although the PHP SDK is a Server SDK, you must use a Client
SDK Key to connect to it. You also need to install the Feature Flag
Relay Proxy to handle Flag evaluations. 

### Before You Begin

Make sure you\'ve read and understood:

-   [Feature Flags
    Overview](/article/7n9433hkc0-cf-feature-flag-overview){target="_blank"}
-   [Getting Started with Feature
    Flags](/article/0a2u2ppp8s-getting-started-with-continuous-features){target="_blank"}
-   [Client-Side and Server-Side
    SDKs](/article/rvqprvbq8f-client-side-and-server-side-sdks){target="_blank"}
-   [Communication Strategy Between SDKs and Harness Feature
    Flags](/article/7ikyqtmjce-communication-sdks-harness-feature-flags){target="_blank"}

### Version

The current version of this SDK is **0.1.0.**

### Requirements

To use this SDK, make sure you:  

-   Install [PHP](https://www.php.net/){target="_blank"} version 7.4 or
    newer
-   Install [Composer](https://getcomposer.org/){target="_blank"}
-   Install the [Relay
    Proxy](https://github.com/harness/ff-proxy){target="_blank"} and
    pass in the URLs you want to use.

    ::: warning-callout
    You cannot use the default Harness URLs when using the Relay Proxy
    with this SDK.
    :::
-   Install [Redis](https://redis.io/){target="_blank"}
-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-php-server-sdk){target="_blank"}
-   Create a PHP application, or
    [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"}
    our [sample
    application](https://github.com/harness/ff-php-server-sample){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](/article/1j7pdkqh7j-create-a-feature-flag){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`.
-   [Create an SDK key and make a copy of
    it](/article/8ja1j98xgp-create-an-sdk-key){target="_blank"}

### Install the SDK

Use Composer to install the SDK as a dependency in your application, for
example: 

    composer require harness/ff-server-sdk

###  Initialize the SDK

To initialize the PHP SDK, you need to:

1.  Add your Client SDK key to connect to your Harness Environment.
2.  Add a Target that you want to Evaluate against a Feature Flag.
3.  (Optional) Configure the SDK.
4.  Complete the initialization using the Client SDK Key, Target, and
    any Configuration parameters you set.

#### Add the Client SDK Key

To connect to the correct Environment that you set up on the Harness
Platform, you need to add the Client SDK Key from that Environment. 

Input the Client SDK Key into the `SDK_KEY` parameter, for example:

    $SDK_KEY = getenv("SDK_KEY") ?: "";

#### Add a Target

::: note-callout
**What is a Target?**\
\
Targets are used to control which users see which Variation of a Feature
Flag, for example, if you want to do internal testing, you can enable
the Flag for some users and not others. When creating a Target, you give
it a name and a unique identifier. Often Targets are users but you can
create a Target from anything that can be uniquely identified, such as
an app or a machine.\
\
For more information about Targets, see [Target Users With
Flags](https://docs.harness.io/article/xf3hmxbaji-targeting-users-with-flags).
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| `Identifier`    | Unique ID for   | Required        | `"identif       |
|                 | the Target.     |                 | ier" => "HT_1"` |
|                 |                 |                 |                 |
|                 | Read Regex      |                 |                 |
|                 | requirements    |                 |                 |
|                 | for Target      |                 |                 |
|                 | names and       |                 |                 |
|                 | identifiers     |                 |                 |
|                 | below for       |                 |                 |
|                 | accepted        |                 |                 |
|                 | characters.     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Name`          | Name for this   | Optional        | `               |
|                 | Target. This    |                 | “name" => "Harn |
|                 | does not have   | **Note**: If    | ess_Target_1",` |
|                 | to be unique.   | you don\'t want |                 |
|                 |                 | to send a name, |                 |
|                 | Note: If you    | don\'t send the |                 |
|                 | don't provide a | parameter.      |                 |
|                 | value, the name | Sending an      |                 |
|                 | will be the     | empty argument  |                 |
|                 | same as the     | will cause an   |                 |
|                 | identifier.     | error.          |                 |
|                 |                 |                 |                 |
|                 | Read Regex      |                 |                 |
|                 | requirements    |                 |                 |
|                 | for Target      |                 |                 |
|                 | names and       |                 |                 |
|                 | identifiers     |                 |                 |
|                 | below for       |                 |                 |
|                 | accepted        |                 |                 |
|                 | characters.     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `Attributes`    | Additional data | Optional        | `“attrib        |
|                 | you can store   |                 | utes" =>    [“e |
|                 | for a Target,   |                 | mail” => “sampl |
|                 | such as email   |                 | e@sample.com”]` |
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

#### Configure the SDK

When initializing the SDK, you also have the option of providing
alternative configuration by passing in the configuration options to the
`cfClient`. 

You can configure the following base features of the SDK:

+-----------------------+-----------------------+-----------------------+
| **Name**              | **Description**       | **Default Value**     |
+-----------------------+-----------------------+-----------------------+
| configUrl             | The URL used to fetch | No default, provide   |
|                       | Feature Flag          | your own value.       |
|                       | Evaluations. When     |                       |
|                       | using the Relay       |                       |
|                       | Proxy, change this    |                       |
|                       | to:                   |                       |
|                       | `h                    |                       |
|                       | ttp://localhost:7000` |                       |
+-----------------------+-----------------------+-----------------------+
| eventUrl              | The URL for posting   | No default, provide   |
|                       | metrics data to the   | your own value.       |
|                       | Feature Flag service. |                       |
|                       | When using the Relay  |                       |
|                       | Proxy, change this    |                       |
|                       | to:                   |                       |
|                       | `h                    |                       |
|                       | ttp://localhost:7000` |                       |
+-----------------------+-----------------------+-----------------------+
| expireAfter           | The amount of time in | `60` (seconds)        |
|                       | seconds that data is  |                       |
|                       | removed from the      |                       |
|                       | cache.                |                       |
+-----------------------+-----------------------+-----------------------+
| streamEnabled         | Set to `true` to      | `true`                |
|                       | enable streaming      |                       |
|                       | mode.                 |                       |
|                       |                       |                       |
|                       | Set to `false` to     |                       |
|                       | disable streaming     |                       |
|                       | mode.                 |                       |
+-----------------------+-----------------------+-----------------------+
| analyticsEnabled      | Set to `true` to      | `true`                |
|                       | enable analytics.     |                       |
|                       |                       |                       |
|                       | Set to `false` to     |                       |
|                       | disable analytics.    |                       |
|                       |                       |                       |
|                       | **Note**: When        |                       |
|                       | enabled, analytics    |                       |
|                       | data is posted every  |                       |
|                       | 60 seconds.           |                       |
+-----------------------+-----------------------+-----------------------+

 

For example:

    $cfClient = new Client($SDK_KEY, new Target(["name" => "harness", "identifier" => "harness"]), [
        "base_url" => "http://ff-proxy:7000",
        "events_url" => "http://ff-proxy:7000",
        “analyticsEnabled” => “false”,
    ]); 

#### Complete the Initialization

To complete the initialization, create an instance of the `Client` and
pass in the `SDK_Key` and `Target`, for example: 

    $client = new Client($SDK_KEY, new Target(["name" => "harness", "identifier" => "harness"]));

#### Sample of Initializing the SDK

    $SDK_KEY = getenv("SDK_KEY") ?: "";  // you can put your SDK key inside the env variable, or you can provide in the code
    $FLAG_NAME = "harnessappdemodarkmode";
    $client = new Client($SDK_KEY, new Target(["name" => "harness", "identifier" => "harness"]));

### Evaluate a Flag

Evaluating a Flag is when the SDK processes all Flag rules and returns
the correct Variation of that Flag for the Target you provide. 

If a matching Flag can't be found, or the SDK can't remotely fetch
flags, the default value is returned. 

There are different methods for the different Variation types and for
each method you need to pass in:

-   Identifier of the Flag you want to evaluate
-   The default Variation

For example:

    $result = $client->evaluate($FLAG_NAME, false);

### Test Your App is Connected to Harness

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

### Sample Code for a PHP Application

Here is a sample code for integrating with the PHP SDK: 

    <?php 

    require_once realpath("vendor/autoload.php"); 

    use Harness\Client;
    use OpenAPI\Client\Model\Target;

    $SDK_KEY = getenv("SDK_KEY") ?: "";  // you can put your key in env variable or you can provide in the code
    $FLAG_NAME = "harnessappdemodarkmode";

    $client = new Client($SDK_KEY, new Target(["name" => "Harness_Target_1", "identifier" => "HT_1"]));
    $result = $client->evaluate($FLAG_NAME, false);

    echo "Evaluation value for flag '".$FLAG_NAME."' with target 'harness': ".json_encode($result);
