---
title: Relay Proxy Overview
description: This topic describes what is Relay Proxy and how to use it with Harness Feature Flags (FF).
tags: 
   - helpDocs
   - Relay Proxy
   - Proxy
   - feature flag
helpdocs_topic_id: q0kvq8nd2o
helpdocs_is_private: false
helpdocs_is_published: true
---

This topic describes what is Relay Proxy and how to use it with Harness
Feature Flags (FF).

The Relay Proxy enables your apps to connect directly to Feature Flag
services without having to make a significant number of outbound
connections to FF services. The Relay Proxy establishes a connection to
the Feature Flags configuration data and relays that connection to
clients in an organization\'s network.

### Why use the Relay Proxy?

In the following cases, you might want to set up Relay Proxy:

-   **Air-gap Deployments**: You can deploy the proxy in your network if
    you don\'t have or can\'t allow external access to your apps. Local
    apps connect directly to the proxy, and the proxy has external
    access to the remote feature flag service to synchronize
    configuration.
-   **Offline Mode**: This is identical to air-gaped, except that the
    proxy does not have a connection to the internet. In that scenario,
    the configuration must be loaded from the outside using
    configuration files. Configuration files are used to link your
    programmes to the proxy.
-   **High Availability / Reliability**: The feature flag service is
    extremely reliable. We will fail over to the failover cluster in the
    event of a major failure. However, in the event of a full network
    loss, the Relay Proxy ensures that your apps continue to run even
    after restarts.

If you decide to use the Relay Proxy, make sure it has a good place in
your network design. For your app to run, it needs to be able to contact
the Relay Proxy, and the architecture differs depending on the type of
app. For example, if you want to link the Relay Proxy to any client-side
apps, don\'t put it inside a firewall.

### Relay Proxy architecture

Diagram of the Relay Proxy architecure

<div>

![](https://files.helpdocs.io/i5nl071jo5/articles/q0kvq8nd2o/1641815845703/screenshot-2022-01-10-at-5-26-46-pm.png){style="max-height:60%;max-width:60%;display:block;margin-left:0;margin-right:auto"
hd-height="60%" hd-width="60%" hd-align="left"}

</div>

The FF Relay Proxy resides between the SDKs and the hosted Harness
Feature Flag services. On startup, proxy loads the necessary data from
the FF services to ensure that it is completely functional even if the
network connection drops temporarily.

The Proxy creates an instance of the Go SDK for each API key that's
passed to it as a part of the [Proxy
Configuration](/article/q0kvq8nd2o-configure-relay-proxy#configuration_variables){target="_blank"},
and each instance of the SDK uses the Cache implementation. The Go SDK
then takes care of populating this cache on startup and keeping it up to
current whenever the remote service changes. When the Go SDK starts up,
it retrieves all of the Features and Segments and then sends a request
to the remote server to listen for any updates. Whenever there is an
update in the remote service, it sends out an event, and when the
embedded SDK sees one of these events, it sends a request to the remote
service to get the most recent flag values and save them to the cache.

The Proxy can also use streaming functionality if it is configured with
Redis. To view the variables that you need to configure for Redis, go to
[Proxy
Configuration](/article/q0kvq8nd2o-configure-relay-proxy#configuration_variables){target="_blank"}
.

#### Configuration variables

The configuration variables used in the proxy are listed in the
following table:

+-------------+-------------+-------------+-------------+-------------+
| **          | **Type**    | **Flag**    | **Example** | **Usage**   |
| Environment |             |             |             |             |
| Variable**  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| ACCOUNT     | string      | -account    | zAbbD-FLS42 | The Account |
| _IDENTIFIER |             | -identifier | 5IEO7OLzXYz | that you    |
|             |             |             |             | want the    |
|             |             |             |             | Proxy to    |
|             |             |             |             | pull down   |
|             |             |             |             | and load    |
|             |             |             |             | config for  |
+-------------+-------------+-------------+-------------+-------------+
| ORG         | string      | -org        | fea         | The         |
| _IDENTIFIER |             | -identifier | tureflagsqa | O           |
|             |             |             |             | rganization |
|             |             |             |             | that you    |
|             |             |             |             | want the    |
|             |             |             |             | Proxy to    |
|             |             |             |             | pull down   |
|             |             |             |             | and load    |
|             |             |             |             | config for  |
+-------------+-------------+-------------+-------------+-------------+
| AD          | string      | -ad         | https://qa  | Used for    |
| MIN_SERVICE |             | min-service | /harness.io | creating    |
|             |             |             | /gateway/cf | the Client  |
|             |             |             |             | that        |
|             |             |             |             | interacts   |
|             |             |             |             | with the    |
|             |             |             |             | F           |
|             |             |             |             | eatureFlags |
|             |             |             |             | Admin       |
|             |             |             |             | Service to  |
|             |             |             |             | retrieve    |
|             |             |             |             | Target and  |
|             |             |             |             | AuthConfig  |
+-------------+-------------+-------------+-------------+-------------+
| SE          | string      | -se         | ZHN         | Token that  |
| RVICE_TOKEN |             | rvice-token | vdWZoNjczMj | the Proxy   |
|             |             |             | R0aGZiLWk1N | can use to  |
|             |             |             | C0tMGRzZg== | a           |
|             |             |             |             | uthenticate |
|             |             |             |             | with the    |
|             |             |             |             | Admin       |
|             |             |             |             | service     |
+-------------+-------------+-------------+-------------+-------------+
| AUTH_SECRET | string      | -           | some        | To          |
|             |             | auth-secret | thingSecret | a           |
|             |             |             |             | uthenticate |
|             |             |             |             | the         |
|             |             |             |             | connection  |
|             |             |             |             | between     |
|             |             |             |             | your SDK    |
|             |             |             |             | and the     |
|             |             |             |             | Proxy, the  |
|             |             |             |             | Proxy       |
|             |             |             |             | generates   |
|             |             |             |             | an          |
|             |             |             |             | aut         |
|             |             |             |             | hentication |
|             |             |             |             | token (JWT) |
|             |             |             |             | that is     |
|             |             |             |             | signed with |
|             |             |             |             | the         |
|             |             |             |             | AUTH_SECRET |
|             |             |             |             | you set in  |
|             |             |             |             | your        |
|             |             |             |             | con         |
|             |             |             |             | figuration. |
|             |             |             |             |             |
|             |             |             |             | When the    |
|             |             |             |             | Proxy       |
|             |             |             |             | receives    |
|             |             |             |             | the         |
|             |             |             |             | aut         |
|             |             |             |             | hentication |
|             |             |             |             | token, it   |
|             |             |             |             | verifies    |
|             |             |             |             | that it is  |
|             |             |             |             | signed      |
|             |             |             |             | using the   |
|             |             |             |             | A           |
|             |             |             |             | UTH_SECRET. |
|             |             |             |             | If it       |
|             |             |             |             | isn't, the  |
|             |             |             |             | token is    |
|             |             |             |             | rejected as |
|             |             |             |             | invalid.    |
+-------------+-------------+-------------+-------------+-------------+
| S           | string      | -sdkBaseUrl | https:      | The Base    |
| DK_BASE_URL |             |             | //config.fe | URL that    |
|             |             |             | ature-flags | the         |
|             |             |             | -qa.harness | internal Go |
|             |             |             | .io/api/1.0 | SDK         |
|             |             |             |             | connects to |
+-------------+-------------+-------------+-------------+-------------+
| SDK         | string      | -s          | https       | The Event   |
| _EVENTS_URL |             | dkEventsUrl | ://event.fe | URL that    |
|             |             |             | ature-flags | the         |
|             |             |             | .qa.harness | internal Go |
|             |             |             | .io/api/1.0 | SDK         |
|             |             |             |             | connects to |
+-------------+-------------+-------------+-------------+-------------+
| API_KEYS    | string      | -apiKey     | 5ecb        | The API     |
|             |             |             | 5049-e071-4 | Keys of the |
|             |             |             | beb-ae43-38 | e           |
|             |             |             | 1aa8f0d3a2, | nvironments |
|             |             |             | a7c         | you want to |
|             |             |             | b7fc6-c4fa- | configure   |
|             |             |             | 4ecb-b01f-0 | the Proxy   |
|             |             |             | 68456f3e500 | to work     |
|             |             |             |             | with.       |
|             |             |             |             |             |
|             |             |             |             | For         |
|             |             |             |             | example,    |
|             |             |             |             | create an   |
|             |             |             |             | SDK key     |
|             |             |             |             | called      |
|             |             |             |             | Proxy Key   |
|             |             |             |             | in your     |
|             |             |             |             | Environment |
|             |             |             |             | and pass it |
|             |             |             |             | in via the  |
|             |             |             |             | `API_KEYS`  |
|             |             |             |             | env. Then   |
|             |             |             |             | all the     |
|             |             |             |             | other       |
|             |             |             |             | a           |
|             |             |             |             | pplications |
|             |             |             |             | in that     |
|             |             |             |             | Environment |
|             |             |             |             | would be    |
|             |             |             |             | able to use |
|             |             |             |             | the Proxy.  |
+-------------+-------------+-------------+-------------+-------------+
| TARGET_PO   | int         | target-po   | 30          | Time in     |
| LL_DURATION |             | ll-duration |             | seconds     |
|             |             |             |             | that        |
|             |             |             |             | determines  |
|             |             |             |             | how         |
|             |             |             |             | frequently  |
|             |             |             |             | the Proxy   |
|             |             |             |             | polls       |
|             |             |             |             | Feature     |
|             |             |             |             | Flags to    |
|             |             |             |             | get the     |
|             |             |             |             | latest      |
|             |             |             |             | Targets     |
+-------------+-------------+-------------+-------------+-------------+
| RE          | string      | re          | loc         | Configures  |
| DIS_ADDRESS |             | dis-address | alhost:6379 | the Proxy   |
|             |             |             |             | to use      |
|             |             |             |             | Redis       |
|             |             |             |             | rather than |
|             |             |             |             | an          |
|             |             |             |             | in-memory   |
|             |             |             |             | cache.      |
|             |             |             |             |             |
|             |             |             |             | Configuring |
|             |             |             |             | the Proxy   |
|             |             |             |             | with Redis  |
|             |             |             |             | also        |
|             |             |             |             | enables     |
|             |             |             |             | streaming   |
+-------------+-------------+-------------+-------------+-------------+
| RED         | string      | red         | a-secret    | (Optional)  |
| IS_PASSWORD |             | is-password |             | This is     |
|             |             |             |             | required    |
|             |             |             |             | only if the |
|             |             |             |             | Redis       |
|             |             |             |             | server is   |
|             |             |             |             | password    |
|             |             |             |             | protected   |
+-------------+-------------+-------------+-------------+-------------+
| REDIS_DB    | int         | redis-db    | 1           | (Optional)  |
|             |             |             |             | After       |
|             |             |             |             | connecting  |
|             |             |             |             | to the      |
|             |             |             |             | Redis       |
|             |             |             |             | server, it  |
|             |             |             |             | allows you  |
|             |             |             |             | to select   |
|             |             |             |             | which       |
|             |             |             |             | database to |
|             |             |             |             | use. In     |
|             |             |             |             | most cases  |
|             |             |             |             | using the   |
|             |             |             |             | default     |
|             |             |             |             | database is |
|             |             |             |             | desired     |
+-------------+-------------+-------------+-------------+-------------+
| FLAG_STR    | boolean     | flag-str    | true        | Allows the  |
| EAM_ENABLED |             | eam-enabled |             | proxy to    |
|             |             |             |             | get flag    |
|             |             |             |             | updates by  |
|             |             |             |             | connecting  |
|             |             |             |             | to Harness  |
|             |             |             |             | in          |
|             |             |             |             | streaming   |
|             |             |             |             | mode.       |
|             |             |             |             |             |
|             |             |             |             | This        |
|             |             |             |             | variable    |
|             |             |             |             | defaults to |
|             |             |             |             | `true`.     |
|             |             |             |             | While       |
|             |             |             |             | updating    |
|             |             |             |             | Harness     |
|             |             |             |             | flags, if   |
|             |             |             |             | you have    |
|             |             |             |             | networking  |
|             |             |             |             | issues when |
|             |             |             |             | receiving   |
|             |             |             |             | streaming   |
|             |             |             |             | events, set |
|             |             |             |             | this to     |
|             |             |             |             | `false`.    |
+-------------+-------------+-------------+-------------+-------------+
| FLAG_PO     | int         | flag-po     | 5           | How often   |
| LL_INTERVAL |             | ll-interval |             | (in         |
|             |             |             |             | minutes)    |
|             |             |             |             | the proxy   |
|             |             |             |             | polls for   |
|             |             |             |             | flag        |
|             |             |             |             | updates.    |
|             |             |             |             | This        |
|             |             |             |             | variable    |
|             |             |             |             | applies     |
|             |             |             |             | only if     |
|             |             |             |             | FLAG_STR    |
|             |             |             |             | EAM_ENABLED |
|             |             |             |             | is set to   |
|             |             |             |             | `false`.    |
+-------------+-------------+-------------+-------------+-------------+
| G           | boolean     | g           | false       | Generates a |
| ENERATE_OFF |             | enerate-off |             | directory   |
| LINE_CONFIG |             | line-config |             | for storing |
|             |             |             |             | co          |
|             |             |             |             | nfiguration |
|             |             |             |             | data to use |
|             |             |             |             | in offline  |
|             |             |             |             | mode.       |
|             |             |             |             |             |
|             |             |             |             | If set to   |
|             |             |             |             | `true` the  |
|             |             |             |             | proxy       |
|             |             |             |             | generates   |
|             |             |             |             | the offline |
|             |             |             |             | co          |
|             |             |             |             | nfiguration |
|             |             |             |             | directory,  |
|             |             |             |             | then        |
|             |             |             |             | terminates. |
|             |             |             |             |             |
|             |             |             |             | Set to      |
|             |             |             |             | `false` as  |
|             |             |             |             | default.    |
+-------------+-------------+-------------+-------------+-------------+

### What data does the Relay Proxy store?

The Proxy stores authentication, feature, Target, and Target Group
configurations in a cache.

-   Keys are stored against a map of fields and values in the feature,
    Target, and Target Group settings.
-   The authentication configuration is stored as a key-value pair, with
    the key being a hashed API key and the value being an environment
    ID.

When the proxy starts, an embedded Go server SDK retrieves the Feature
and Segment config and populates the cache.

### How does the Relay Proxy fetch client and server SDK configuration details?

Client and Server SDKs fetch the evaluation details in the same way as
they would if they were interacting with the FF Services on ff-server.

### Blog post

For more information about the Relay Proxy, go to our blog post
[In-Depth: Harness Feature Flags Relay
Proxy](https://harness.io/blog/in-depth-feature-flags-relay-proxy/){target="_blank"}.

### Next step

After you understand the basics of the Relay Proxy, you can then [deploy
it](/article/rae6uk12hk-deploy-relay-proxy).
