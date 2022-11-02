---
title: Choose a Client-Side or Server-Side SDK
description: This topic will help you understand the difference between Harness Feature Flag's client-side and server-side SDKs.
tags: 
   - helpDocs
   - feature flag
   - SDK
# sidebar_position: 2
helpdocs_topic_id: rvqprvbq8f
helpdocs_category_id: eyzngtupao
helpdocs_is_private: false
helpdocs_is_published: true
---

Harness Feature Flag provides several SDKs in different languages to help you access feature flags from your applications. The SDKs are divided into two main categories, regardless of the programming language:

* Client-side SDKs
* Server-side SDKs

The client and server-side SDKs have different security considerations as well as some behavioral and architectural differences. This topic will help you understand the difference between Harness Feature Flag's client-side and server-side SDKs.

### SDK architecture

Diagram of the SDK architecture![](https://files.helpdocs.io/i5nl071jo5/articles/rvqprvbq8f/1638442275737/image.png)The above diagram defines the behavior of a SDK. It covers various aspects like what happens at the beginning (initialization and authentication) followed by behavior of an SDK during normal operation.

* **SDK Initialization:** SDK initialization requires only one argument- SDK key and the optional configuration argument. There is a default configuration in the SDK and based on that configuration, an API client, a repository and an evaluator are set up.
* **SDK Authentication:** Authentication is the first step in the development of the SDK. Without authentication, the evaluation function will return only the default values. To successfully log in to the system, use the SDK key. The key for client-side SDK cannot be used in the server-side SDK and vice versa. In order to log in successfully, a request is sent with SDK key. In case of client-side SDK key, add a target.

After successful login to the Feature Flag server using one of the two types of keys, the other processors like **Poll Processor, Analytics Processor and Stream Processor** start.

* **Poll Processor:** Poll Processor fetches initial data from the Feature Flag server. Data such as details on feature flags and target groups is required during implementation. Poll Processor waits for both threads to complete. It ends one cycle in data retrieval and sets a delay in the duration of the value defined in the configuration. Each thread (one for flags and one for target groups) after a successful data retrieval from the Feature Flag server are saved to the repository.
* **Stream Processor:** Stream Processor runs real time updates. This processor runs after successful fetching of data. It is a unidirectional approach where data is sent from the server to the client. When the processor completes its task, it immediately runs a thread that fetches new data in the background and stores it in a repository.
* **Analytics/Update Processor:** Update Processor returns the data after evaluations. Once the data is fetched, this processor analyses the data with certain metrics; like flag evaluations, target events, and sends the data back.

### SDK Types

The following table lists the differences between the client-side and server-side SDKs with respect to type of users, security, storage, connection state, and operation.



|  |  |  |
| --- | --- | --- |
| **Parameter** | **Client Side SDK** | **Server Side SDK** |
| **Users** | Designed to be used in applications, your users run directly on their own devices, such as mobile, desktop, and web applications.Optimized to be used by a single user and low bandwidth consumption.Examples: JavaScript, iOS, Android, React Native SDKs.  | Designed to be used in server-side applications such as web servers and backend services.Optimized to be used in multi-user and secure environments.Examples, Java, Go, and Python SDKs. |
| **Security** | The SDKs are embedded in your applications and run on the browser or on mobile devices. Because of which these SDKs can be compromised by users when unpacking a mobile app or using the browser's developer tools to inspect the page. You should not use a server-side SDK key in client-side applications.Client-side SDKs only perform an evaluation of a flag and receive the result.  They don't store all data about a flag. | The SDKs are embedded in applications that run on your servers such as web servers or backend servers. These environments are comparatively safe.Server-side SDKs download all the feature flags that you have defined in a project and store them in memory. |
| **Storage** | Client-side SDK has a local cache. It communicates with Harness more often | Server-side SDKs downloads and caches all flag rules and states and avoids most Harness communication |
| **Connection state** | Client-side SDKs require a consistent connection to establish an evaluation decision. | Server-side SDKs can make an evaluation decision based on locally stored rules once instantiated. It requires a connection to pull or receive updates |
| **Operation** | Feature evaluation happens on the server-side, and SDK only gets the evaluated results of the Flags. | Server SDKs sync Flag rulesets in the background and keep in-memory cache. When an application makes the call for Flag value, the evaluation happens locally, and no network call is made. Hence it is very fast and efficient. |

### Supported application types



|  |  |
| --- | --- |
| **Client-Side SDKs** | **Server-Side SDKs** |
| [JavaScript](/article/bmlvsxhp13-java-script-sdk-references) | [Java](/article/i7et9ebkst-integrate-feature-flag-with-java-sdk) |
| [iOS](/article/6qt2v8g92m-ios-sdk-reference) | [Go](/article/4c8wljx60w-feature-flag-sdks-go-application) |
| [Android](/article/74t18egxbi-android-sdk-reference) | [.NET](/article/c86rasy39v-net-sdk-reference) |
| [Flutter](/article/mmf7cu2owg-flutter-sdk-reference) | [Python](/article/hwoxb6x2oe-python-sdk-reference) |
| [React Native](/article/z2w6uj9mzb-react-native-sdk-reference) | [Node.js](/article/3v7fclfg59-node-js-sdk-reference) |
| [Xamarin SDK Reference](/article/x9mh0o785u-xamarin-sdk-reference) | [Ruby SDK Reference](/article/uora4f0f22-ruby-sdk-reference) |
|  | [PHP](/article/3qrik15pkz-php-sdk-reference) |

