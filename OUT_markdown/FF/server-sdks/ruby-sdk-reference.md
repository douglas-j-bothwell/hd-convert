---
title: Ruby SDK Reference
description: This topic explains how to use the Harness Feature Flags (FF) SDK in your Ruby application.
tags: 
   - helpDocs
   - server SDK
   - ruby
helpdocs_topic_id: uora4f0f22
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags Ruby SDK for
your Java application.

For getting started quickly, you can use our [sample code from the Ruby
SDK
README](https://github.com/harness/ff-ruby-server-sdk/blob/main/README.md){target="_blank"}.
You can
also [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"} and
run a sample application from the [Ruby SDK GitHub
Repository.](https://github.com/harness/ff-ruby-server-sdk){target="_blank"}

### Before you begin

You should read and understand the following:

-   [Feature Flags
    Overview](/article/7n9433hkc0-cf-feature-flag-overview){target="_blank"}
-   [Getting Started with Feature
    Flags](/article/0a2u2ppp8s-getting-started-with-continuous-features){target="_blank"}
-   [Client-Side and Server-Side
    SDKs](/article/rvqprvbq8f-client-side-and-server-side-sdks){target="_blank"}
-   [Communication Strategy Between SDKs and Harness Feature
    Flags](/article/7ikyqtmjce-communication-sdks-harness-feature-flags){target="_blank"}

### Version

::: note-callout
The current version of this SDK is **1.0.2**.
:::

### Requirements

To use this SDK, make sure you:  

-   Install [Ruby
    2.7](https://www.ruby-lang.org/en/documentation/installation/) or
    newer
-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-ruby-server-sdk){target="_blank"}
-   Create a Java application,
    or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"} our [sample
    application](https://github.com/harness/ff-ruby-server-sdk){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](/article/1j7pdkqh7j-create-a-feature-flag){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`
-   [Create an SDK key and make a copy of
    it](/article/1j7pdkqh7j-create-a-feature-flag#step_3_create_an_sdk_key){target="_blank"}

### Install the SDK

Install the Ruby SDK using gem, for example:

    gem install harness-featureflags

Or by adding the following snippet to your project\'s `Gemfile` file:

    gem "ff-ruby-server-sdk"

### Clone the SDK Repository

Run the following command to clone the Feature Flag SDK repository:

    git clone --recurse-submodules git@github.com:harness/ff-ruby-server-sdk.git

### Initialize the SDK

To initialize the Go SDK, you need to:

1.  Add your Server SDK Key to connect to your Harness Environment.
2.  (Optional) Configure the SDK options.
3.  Pass in the Server SDK Key and configuration options.
4.  Add a Target that you want to Evaluate against a Feature Flag.

#### Add the Server SDK Key {#undefined}

To connect to the correct Environment that you set up on the Harness
Platform, you need to add the Server SDK Key from that Environment. For
example:

``` {.hljs .lua}
key = "YOUR_API_KEY_GOES_HERE"
```

#### Configure the SDK {#undefined}

You can configure the following features of the SDK:

+-----------------+-----------------+-----------------+-----------------+
| **Name**        | **Example**     | **Description** | **Default       |
|                 |                 |                 | Value**         |
+-----------------+-----------------+-----------------+-----------------+
| baseUrl         | `config         | The URL used to | `https:/        |
|                 | _url("https://c | fetch Feature   | /config.ff.harn |
|                 | onfig.ff.harnes | Flag            | ess.io/api/1.0` |
|                 | s.io/api/1.0")` | Evaluations.    |                 |
|                 |                 | When using the  |                 |
|                 |                 | Relay Proxy,    |                 |
|                 |                 | change this     |                 |
|                 |                 | to: `http://    |                 |
|                 |                 | localhost:7000` |                 |
+-----------------+-----------------+-----------------+-----------------+
| eventUrl        | `event          | The URL for     | `https:/        |
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
| pollInterval    | `poll_interval_ | The             | `60` (seconds)  |
|                 | in_seconds(60)` | interval **in   |                 |
|                 |                 | seconds** that  |                 |
|                 |                 | we poll for     |                 |
|                 |                 | changes when    |                 |
|                 |                 | you are using   |                 |
|                 |                 | stream mode.    |                 |
+-----------------+-----------------+-----------------+-----------------+
| streamEnabled   | `stream         | Set             | `true`          |
|                 | _enabled(true)` | to `true` to    |                 |
|                 |                 | enable          |                 |
|                 |                 | streaming mode. |                 |
|                 |                 |                 |                 |
|                 |                 | Set             |                 |
|                 |                 | to `false` to   |                 |
|                 |                 | disable         |                 |
|                 |                 | streaming mode. |                 |
+-----------------+-----------------+-----------------+-----------------+
| a               | `analytics      | Set             | `true`          |
| nalyticsEnabled | _enabled(true)` | to `true` to    |                 |
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

For further configuration options and samples, such as configuring your
logger or using the SDK with the Relay Proxy, go to [Additional
Options](https://docs.harness.io/article/4c8wljx60w-feature-flag-sdks-go-application#additional-options).

#### Complete the initialization {#undefined}

Complete  the initialization by creating an instance of the Feature Flag
client and passing in the Server SDK Key and any configuration options.
For example:

``` {.hljs .lua}
client.init(key, config)
```

#### Add a Target {#undefined}

::: note-callout
**What is a Target?\
**Targets are used to control which users see which Variation of a
Feature Flag, for example, if you want to do internal testing, you can
enable the Flag for some users and not others. When creating a Target,
you give it a name and a unique identifier. Often Targets are users but
you can create a Target from anything that can be uniquely identified,
such as an app or a machine.\
For more information about Targets, go to [Targeting Users With
Flags](https://docs.harness.io/article/xf3hmxbaji-targeting-users-with-flags){target="_blank"}. 
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| `identifier`    | Unique ID for   | Required        | `ide            |
|                 | the Target.     |                 | ntifier="HT_1"` |
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
| `name`          | Name for this   | Optional        | `("Harne        |
|                 | Target. This    |                 | ss_Target_1") ` |
|                 | does not have   | **Note**: If    |                 |
|                 | to be unique.   | you don\'t want |                 |
|                 |                 | to send a name, |                 |
|                 | **Note**: If    | don\'t send the |                 |
|                 | you don't       | parameter.      |                 |
|                 | provide a       | Sending an      |                 |
|                 | value, Harness  | empty argument  |                 |
|                 | generates the   | will cause an   |                 |
|                 | name based on   | error.          |                 |
|                 | the ID.         |                 |                 |
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
| `attributes`    | Additional data | Optional        | `attributes=    |
|                 | you can store   |                 | {"email": "demo |
|                 | for a Target,   |                 | @harness.io"})` |
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

    target = Target.new("Harness_Target_1", identifier="HT_1", attributes={"email": "demo@harness.io"})

### Evaluate a Flag {#undefined}

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

#### Evaluate a string Variation {#undefined}

    def string_variation(identifier, target, default_value)

#### Evaluate a boolean Variation {#undefined}

    def bool_variation(identifier, target, default_value)

#### Evaluate a number Variation {#undefined}

    def number_variation(identifier, target, default_value)

#### Evaluate a JSON Variation {#undefined}

    def json_variation(identifier, target, default_value)

### Test your app is connected to Harness {#undefined}

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

### Close the SDK

To help prevent memory leaks, we recommend closing the SDK when it's not
in use. To do this, run the following command: 

    client.close

### Additional options

#### Use the Relay Proxy

When using your Feature Flag SDKs with a [Harness Relay
Proxy](https://docs.harness.io/article/q0kvq8nd2o-relay-proxy){target="_blank"} you
need to change the default URL and events URL
to `http://localhost:7000` when initializing the SDK. For example:

    config = ConfigBuilder.new
                          .config_url("https://config.feature-flags.uat.harness.io/api/1.0")
                          .event_url("https://event.feature-flags.uat.harness.io/api/1.0")
                          .build

### Use our public API methods

Our Public API exposes the following methods that you can use for
instantiating, initializing, and closing the SDK:

    def initialize(api_key = nil, config = nil, connector = nil)

    def init(api_key = nil, config = nil, connector = nil)

    def wait_for_initialization

    def close

### Sample code for a Ruby application

Here is a sample code for using the Feature Flag Ruby SDK:

    require "logger"
    require "securerandom"

    require_relative '../lib/ff/ruby/server/sdk/dto/target'
    require_relative '../lib/ff/ruby/server/sdk/api/config'
    require_relative '../lib/ff/ruby/server/sdk/api/cf_client'
    require_relative '../lib/ff/ruby/server/sdk/api/config_builder'

    flag_b = "flag1"
    flag_n = "flag2"
    flag_s = "flag3"
    flag_j = "flag4"

    clients = {}
    targets = {}

    logger = Logger.new(STDOUT)

    executor = Concurrent::FixedThreadPool.new(100)

    keys = {

      "Freemium" => "1f3339b4-e004-457a-91f7-9b5ce173eaaf",
      "Non-Freemium" => "a30cf6aa-67f2-4545-8ac7-f86709f4f3a0"
    }

    keys.each do |name, key|

      targets[name] = Target.new("ruby_target_" + name)

      config = ConfigBuilder.new
                            .logger(logger)
                            .build

      client = CfClient.new(key, config)

      # .config_url("https://config.feature-flags.uat.harness.io/api/1.0")
      # .event_url("https://event.feature-flags.uat.harness.io/api/1.0")

      client.init

      config.logger.debug "We will wait for the initialization"

      client.wait_for_initialization

      config.logger.debug "Initialization is complete"

      clients[name] = client
    end

    iterations = 10

    counted = 0
    count_to = keys.size * iterations

    logger.debug "To count: " + count_to.to_s

    keys.each do |name, key|

      client = clients[name]
      target = targets[name]

      executor.post do

        (1..iterations).each do |iteration|

          logger.debug name + " :: iteration no: " + iteration.to_s

          bool_result = client.bool_variation(flag_b, target, false)
          number_result = client.number_variation(flag_n, target, -1)
          string_result = client.string_variation(flag_s, target, "unavailable !!!")
          json_result = client.json_variation(flag_j, target, JSON.parse("{}"))

          logger.debug name + " :: '" + flag_b.to_s + "' has the value of: " + bool_result.to_s
          logger.debug name + " :: '" + flag_n.to_s + "' has the value of: " + number_result.to_s
          logger.debug name + " :: '" + flag_s.to_s + "' has the value of: " + string_result.to_s
          logger.debug name + " :: '" + flag_j.to_s + "' has the value of: " + json_result.to_s
          logger.debug "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

          counted = counted + 1

          logger.debug "Counted: " + counted.to_s

          sleep 10
        end
      end
    end

    while counted != count_to

      sleep(1)
    end

    clients.each do |name, client|

      logger.debug name + " :: closing"

      client.close
    end
