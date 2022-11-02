---
title: Apex SDK Reference
description: This topic describes how to use the Harness Feature Flags Apex SDK for your Apex application. For getting started quickly, you can use our sample code from the Apex SDK README. You can also clone and…
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: aoe0y33mut
helpdocs_category_id: kkiqy1f6d7
helpdocs_is_private: false
helpdocs_is_published: true
---

This SDK is currently in beta. This topic describes how to use the Harness Feature Flags Apex SDK for your Apex application.

For getting started quickly, you can use our [sample code from the Apex SDK README](https://github.com/harness/ff-apex-server-sdk/blob/main/README.md). You can also [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and run a [sample application](https://github.com/harness/ff-apex-server-sample) from the [Apex SDK GitHub Repository.](https://github.com/harness/ff-apex-server-sdk)

### Before you begin

Make sure you read and understand:

* [Feature Flags Overview](/article/7n9433hkc0-cf-feature-flag-overview)
* [Getting Started with Feature Flags](/article/0a2u2ppp8s-getting-started-with-continuous-features)
* [Client-Side and Server-Side SDKs](/article/rvqprvbq8f-client-side-and-server-side-sdks)
* [Communication Strategy Between SDKs and Harness Feature Flags](/article/7ikyqtmjce-communication-sdks-harness-feature-flags)

### Version

This SDK is currently in beta. 

### Requirements

To use this SDK, make sure you:  

* Install [SalesForce SFDX cli](https://developer.salesforce.com/tools/sfdxcli).
* [Download the SDK from our GitHub repository](https://github.com/harness/ff-apex-server-sdk)
* Create an Apex application, or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) our [sample application](https://github.com/harness/ff-apex-server-sample).
* [Create a Feature Flag on the Harness Platform](/article/1j7pdkqh7j-create-a-feature-flag). If you are following along with the SDK README sample code, make sure your flag is called harnessappdemodarkmode.
* [Create an SDK key and make a copy of it](/article/1j7pdkqh7j-create-a-feature-flag#step_3_create_an_sdk_key)

### Install the SDK

Install the SDK by running the following command:

`$> sfdx force:source:deploy --targetusername='YOUR TARGET ORG' --sourcepath='force-app'`

### Initialize the SDK

To initialize the Apex SDK, you need to:

1. Add your Server SDK key to connect to your Harness Environment.
2. Add a Target that you want to Evaluate against a Feature Flag.
3. (Optional) Configure the SDK.
4. Complete the initialization with the SDK using the Server SDK Key, Target, and Configuration parameters you set.

#### Add the Server SDK Key

To connect to the correct Environment that you set up on the Harness Platform, you need to add the Server SDK Key from that Environment. Input the Server SDK Key, for example:

`FFClient client = new FFClient('Your SDK Key', target, config);`

#### Add a Target

**What is a Target?**  
  
Targets are used to control which users see which Variation of a Feature Flag, for example, if you want to do internal testing, you can enable the Flag for some users and not others. When creating a Target, you give it a name and a unique identifier. Often Targets are users but you can create a Target from anything that can be uniquely identified, such as an app or a machine.  
  
For more information about Targets, see [Targeting Users With Flags](/article/xf3hmxbaji-targeting-users-with-flags).To create a Target, pass in arguments for the following:



|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter** | **Description** | **Required?** | **Example** |
| Identifier | Unique ID for the Target | Required | `.identifier('Harness')` |
| Name | Name for this Target. This does not have to be unique. Note: If you don’t provide a value, Harness uses the ID as the name.  | Optional | `.name('Harness')` |

 

For example:

`FFTarget target = FFTarget.builder().identifier('Harness').name('Harness').build();`

#### Configure the SDK

When initializing the SDK, you also have the option of providing alternative configurations by using FFConfig.Builder(). 

You can configure the following base features of the SDK:



|  |  |  |
| --- | --- | --- |
| Name | Description | Default value |
| baseURL | The URL used to fetch Feature Flag Evaluations. When using the Relay Proxy, change this to: http://localhost:7000 | `https://config.ff.harness.io/api/1.0` |
| evalExpireAfter | The time (in seconds) that evaluations expire. The minimum allowed is 300 seconds.  | `300` |
| evalExpireAuth | The time (in seconds) that re-authentication occurs. The minimum allowed is 300 seconds.  | `300`  |
| cache | The details of your cache. You must set the namespace and partition. | No default - you must set the namespace and partition. |

 

For example: 


```
// set cache Namespace and Partition  
FFOrgCache cache = new FFOrgCache('local', 'basic');  
FFConfig config = new FFConfig.builder().cache(cache).build();
```
#### Complete the initialization

To complete the initialization, create an instance of the FFClient and pass in the sdkKey, target data, and any configuration options you want to include, for example: 

`FFClient client = new FFClient('Your SDK Key', target, config);`

#### Sample of initializing the SDK


```
// Set flagKey to the feature flag key you want to evaluate.  
String flag = 'harnessappdemodarkmode';  
  
// set cache Namespace and Partition  
FFOrgCache cache = new FFOrgCache('local', 'basic');  
FFConfig config = new FFConfig.builder().cache(cache).build();   
  
// Set up the target properties.  
FFTarget target = FFTarget.builder().identifier('Harness').name('Harness').build();  
FFClient client = new FFClient('Your SDK Key', target, config);
```
 

### Evaluating a Flag

Evaluating a Flag is when the SDK processes all Flag rules and returns the correct Variation of that Flag for the Target you provide. 

If a matching Flag can’t be found, or the SDK can’t remotely fetch flags, the default value is returned. 

There are different methods for the different Variation types and for each method you need to pass in:

* Identifier of the Flag you want to evaluate
* The Target object you want to evaluate against
* The default Variation

For example:


```
// Bool evaluation  
Boolean value = client.evaluate(flag, false);  
System.debug('Feature flag ' + flag + ' is '+ value + ' for this user');
```
 

### Test your app is connected to Harness

When you receive a response showing the current status of your Feature Flag, go to the Harness Platform and toggle the Flag on and off. Then, check your app to verify if the Flag Variation displayed is updated with the Variation you toggled.

### Sample code for an Apex application


```
// Set flagKey to the feature flag key you want to evaluate.  
String flag = 'harnessappdemodarkmode';  
   
// set cache Namespace and Partition  
FFOrgCache cache = new FFOrgCache('local', 'basic');  
FFConfig config = new FFConfig.builder().baseUrl(“harness url”).evalExpireAfter(300).authExpireAfter(60*60*24).cache(cache).build();  
   
// Set up the target properties.  
FFTarget target = FFTarget.builder().identifier('HT_1').name('Harness_Target_1').build();  
   
FFClient client = new FFClient('Your SDK Key', target, config);  
   
// Bool evaluation  
Boolean value = client.evaluate(flag, false);  
System.debug('Feature flag ' + flag + ' is '+ value + ' for this user');
```
 

