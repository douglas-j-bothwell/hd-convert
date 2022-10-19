---
title: Node.js SDK Reference
description: This topic describes how to use the Harness Feature Flags Java SDK for your Java application. For getting started quickly, you can use our sample code from the Node.js SDK README. You can also clone…
tags: 
   - helpDocs
helpdocs_topic_id: 3v7fclfg59
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes how to use the Harness Feature Flags Java SDK for
your Java application.

For getting started quickly, you can use our [sample code from the
Node.js SDK
README](https://github.com/harness/ff-nodejs-server-sdk/blob/main/README.md){target="_blank"}.
You can
also [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"} and
run a sample application from the [Node.js SDK GitHub
Repository.](https://github.com/harness/ff-nodejs-server-sdk){target="_blank"}

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
The current version of this SDK is **1.2.7**.
:::

### Requirements

To use this SDK, make sure you:  

-   Install Node.js version 12 or newer
-   [Download the SDK from our GitHub
    repository](https://github.com/harness/ff-nodejs-server-sdk){target="_blank"}
-   Create a Java application,
    or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){target="_blank"} our [sample
    application](https://github.com/harness/ff-python-server-sdk){target="_blank"}.
-   [Create a Feature Flag on the Harness
    Platform](https://docs.harness.io/article/1j7pdkqh7j-create-a-feature-flag){target="_blank"}.
    If you are following along with the SDK README sample code, make
    sure your flag is called `harnessappdemodarkmode`
-   [Create an SDK key and make a copy of
    it](https://docs.harness.io/article/1j7pdkqh7j-create-a-feature-flag#step_3_create_an_sdk_key){target="_blank"}

### Install the SDK

#### Install using npm

``` {.hljs .coffeescript}
npm install @harnessio/ff-nodejs-server-sdk
```

#### Install using yarn

    yarn add @harnessio/ff-nodejs-server-sdk

### Initialize the SDK

To initialize the Node.js SDK, you need to:

1.  Import the package.
2.  Add your Server SDK Key to connect to your Harness Environment.
3.  Add a Target that you want to Evaluate against a Feature Flag.
4.  (Optional) Configure the SDK options. For more details on what
    features you can configure for this SDK, go to [Configure the
    SDK](/article/3v7fclfg59-node-js-sdk-reference#configure_the_sdk).

#### Import the package

##### CommonJS

To import with CommonJS, use:

    const { Client } = require('@harnessio/ff-nodejs-server-sdk');

##### ES modules

To import with ES modules use:

    import { Client } from '@harnessio/ff-nodejs-server-sdk';

#### Add the Server SDK Key

To connect to the correct Environment that you set up on the Harness
Platform, you need to add the Server SDK Key from that Environment.
Input the Client SDK Key into the `API_KEY` parameter, for example:

    const client = new Client('sdkKey');

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
Flags](https://docs.harness.io/article/xf3hmxbaji-targeting-users-with-flags){target="_blank"}.
:::

To add a Target, build it and pass in arguments for the following:

+-----------------+-----------------+-----------------+-----------------+
| **Parameter**   | **Description** | **Required?**   | **Example**     |
+-----------------+-----------------+-----------------+-----------------+
| `identifier`    | Unique ID for   | Required        | `iden           |
|                 | the Target.     |                 | tifier: 'HT_1'` |
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
| `name`          | Name for this   | Optional        | `name: 'Har     |
|                 | Target. This    |                 | ness_Target_1'` |
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
| `attributes`    | Additional data | Optional        | `               |
|                 | you can store   |                 | attributes: {`\ |
|                 | for a Target,   |                 |                 |
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

``` {.hljs .java}
const target = {
    identifier: 'HT_1',
    name: 'Harness_Target_1',
    attributes: {
       'email': 'demo@harness.io'
    }
  };
```

#### Configure the SDK

You can configure the following features of the SDK:

+-----------------------+-----------------------+-----------------------+
| **Name**              | **Description**       | **Default Value**     |
+-----------------------+-----------------------+-----------------------+
| baseUrl               | The URL used to fetch | `https://config.f     |
|                       | Feature Flag          | f.harness.io/api/1.0` |
|                       | Evaluations. When     |                       |
|                       | using the Relay       |                       |
|                       | Proxy, change this    |                       |
|                       | to: `h                |                       |
|                       | ttp://localhost:7000` |                       |
+-----------------------+-----------------------+-----------------------+
| eventUrl              | The URL for posting   | `https://events.f     |
|                       | metrics data to the   | f.harness.io/api/1.0` |
|                       | Feature Flag service. |                       |
|                       | When using the Relay  |                       |
|                       | Proxy, change this    |                       |
|                       | to: `h                |                       |
|                       | ttp://localhost:7000` |                       |
+-----------------------+-----------------------+-----------------------+
| pollInterval          | The interval **in     | `60` (seconds)        |
|                       | seconds** that we     |                       |
|                       | poll for changes when |                       |
|                       | you are using stream  |                       |
|                       | mode.                 |                       |
+-----------------------+-----------------------+-----------------------+
| streamEnabled         | Set to `true` to      | `true`                |
|                       | enable streaming      |                       |
|                       | mode.                 |                       |
|                       |                       |                       |
|                       | Set to `false` to     |                       |
|                       | disable streaming     |                       |
|                       | mode.                 |                       |
+-----------------------+-----------------------+-----------------------+
| analyticsEnabled      | Set to `true` to      | `true`                |
|                       | enable analytics.     |                       |
|                       |                       |                       |
|                       | Set to `false` to     |                       |
|                       | disable analytics.    |                       |
|                       |                       |                       |
|                       | **Note**: When        |                       |
|                       | enabled, analytics    |                       |
|                       | data is posted every  |                       |
|                       | 60 seconds.           |                       |
+-----------------------+-----------------------+-----------------------+

For example:

    // Create Options
    const options = {
      baseUrl: "http://localhost:7000",
      eventsUrl: "http://localhost:7000"
    }

#### Complete the initialization

Complete  the initialization by creating an instance of the Feature Flag
client and passing in the Server SDK Key and configuration options.

    // Create client with options
    const client = new Client(apiKey, options);

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

For example:

#### Evaluate a boolean Variation {#undefined}

    function boolVariation(
      identifier: string,
      target: Target,
      defaultValue: boolean = true,
    ): Promise<boolean>;

#### Evaluate a string Variation {#undefined}

    function stringVariation(
      identifier: string,
      target: Target,
      defaultValue: boolean = '',
    ): Promise<string>;

#### Evaluate a number Variation {#undefined}

    function numberVariation(
      identifier: string,
      target: Target,
      defaultValue: boolean = 1.0,
    ): Promise<number>;

#### Evaluate a JSON Variation {#undefined}

    function jsonVariation(
      identifier: string,
      target: Target,
      defaultValue: boolean = {},
    ): Promise<Record<string, unknown>>;

### Listen for events {#undefined}

#### Register the event listener

You can listen for the following events:

-   Event.READY - Indicates the SDK was successfully initialized.
-   Event.FAILED - Indicates the SDK had thrown an error.
-   Event.CHANGED - Indicates a Flag or Segment has been updated.

For example:

    on(Event.READY, () => {
      console.log('READY');
    });

    on(Event.FAILED, () => {
      console.log('FAILED');
    });

    on(Event.CHANGED, (identifier) => {
      console.log('Changed', identifier);
    });

#### Close the event listener

To avoid unexpected behavior, when the listener isn\'t needed, turn it
off.

To remove the `functionReference` listener for `Event.READY,` use:

    off(Event.READY, functionReference);

To remove all listeners, use:

    off(Event.READY);

::: note-callout
If you call `off()` without parameters it will close the client.
:::

### Test your app is connected to Harness {#undefined}

When you receive a response showing the current status of your Feature
Flag, go to the Harness Platform and toggle the Flag on and off. Then,
check your app to verify if the Flag Variation displayed is updated with
the Variation you toggled.

### Close the SDK {#undefined}

To help prevent memory leaks, we recommend closing the SDK when it's not
in use. To do this, us the following function: 

    function close(): void;

### Additional options  {#undefined}

#### Configure your logger

You can provide your own logger to the SDK by passing it in as a config
option. The following example creates an instance of the winston logger,
sets the level to DEBUG, and passes it to the client.

    const winston = require('winston')

    // Create client with logger
    const client = new Client(apiKey, {
      logger: new winston.createLogger({
        level: 'debug',
        transports: [new winston.transports.Console()]
      })
    });

### Sample code for a Node.js application

Here is a sample code for using the SDK with a Node.js application:

      const pkg = require('ff-nodejs-server-sdk');
    const { Client } = pkg;

    const client = new Client('1c100d25-4c3f-487b-b198-3b3d01df5794', {
      enableStream: true,
      pollInterval: 2 * 60 * 1000 // two min pollInterval
    });

    setInterval(() => {
      const target = {
        identifier: 'harness',
      };
      const value = client.boolVariation('test', target, false);
      console.log('Evaluation for flag test and target: ', value, target);
    }, 10000);
