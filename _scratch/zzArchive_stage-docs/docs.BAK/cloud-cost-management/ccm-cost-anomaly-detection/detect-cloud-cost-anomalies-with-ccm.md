---
title: Detect Cloud Cost Anomalies with CCM
description: Currently, this feature is in Beta. Harness Cloud Cost Management (CCM) detects cost anomalies for your Kubernetes clusters and cloud accounts. Cloud cost anomaly detection can be used as a tool to k…
tags: 
   - helpDocs
helpdocs_topic_id: x0z3r0bv99
helpdocs_is_private: false
helpdocs_is_published: true
---

Currently, this feature is in Beta.Harness Cloud Cost Management (CCM) detects cost anomalies for your Kubernetes clusters and cloud accounts. Cloud cost anomaly detection can be used as a tool to keep cloud costs under control. It also provides alerting capability (email and Slack) so that the stakeholders are notified of each anomaly that is detected.

Currently, CCM detects anomalies for the following:

* **Clusters**: Kubernetes Clusters, Namespaces, and Workloads
* **AWS**: Service and Account
* **GCP**: Products, Projects, and SKUs
* **Azure**: Subscription ID, Service Name, and Resources

### Before You Begin

* [Cloud Cost Management Overview](../ccm-concepts/cloud-cost-management-overview.md)
* [Create Cost Perspectives](../ccm-perspectives/create-cost-perspectives.md)

### Review: What is Cost Anomaly Detection?

Cost anomaly detection points you to what you should be paying attention to to keep your cloud costs under control. Whenever there is a significant increase in your cloud cost, an alert is triggered. This helps to keep track of potential waste and unexpected charges. It also keeps an account of the recurring events (seasonalities) that happen on a daily, weekly, or monthly basis.

CCM cost anomaly compares the previous cloud cost spends with the current spending to detect the cost anomalies. If the actual cost incurred deviates substantially from the expected cost then it can be a potential cost anomaly.

### Review: How Does Cost Anomaly Detection Work?

CCM uses [statistical anomaly detection techniques](https://docs.harness.io/article/akdd3mxobc-detect-cost-anomalies-with-ce#anomaly_detection_techniques) and [Forecasting at scale](https://peerj.com/preprints/3190/) to determine the cost anomalies. These methods can detect various types of anomalies, such as a one-time cost spike, gradual, or consistent cost increases.

CCM analyzes 15 to 60 days of data to predict the cost. If the predicted cost and the actual cost incurred deviate beyond the fixed parameters (as described in the anomaly detection techniques), it is marked as the cost anomaly.

For example, you run a compute-intensive job that gets kicked off every Monday morning. The algorithm picks up the pattern and updates its model. Based on these learnings predictions are made for what might happen in the future. Anything that does not align with these predictions is a potential anomaly.

The anomaly detection techniques are run every 24 hours and the alert is triggered for any anomaly that is detected.#### Anomaly Detection Techniques

One of the challenges of anomaly detection is reducing the number of false positives and noisy alerts. To avoid this, CE uses the following prediction techniques to detect the cost anomalies:

##### Absolute Difference Method

This method takes the absolute difference between the two variables in the dataset. CCM considers the actual and predicted cost as two variables. If the difference between the actual and predicted costs exceeds $75, then the cost is considered as a potential anomaly.

`Actual cost - Predicted Cost > $75`

For example, the actual cost of your cloud resource is $120 and the predicted cost was $25.

The difference between the actual and predicted is $120 - $21 = $99 which is greater than the $75 fixed amount.

Hence, it is a potential cost anomaly.

##### Relative Method

In this method, if the actual cost is a minimum of 1.25 times higher than the predicted cost, then it is a potential cost anomaly.

`Actual Cost / Predicted Cost >= 1.25X`

For example, the difference between the actual and predicted is 120 / 21 = 5.71 which is higher than the fixed 1.25x value.

Hence, it is a potential cost anomaly.

##### Probability Method

In this method, the algorithm uses a probability of 99% within a range to predict the cost.

For example, the actual cost is predicted to be in the range of 10-14$ with a 99% probability. Anything that deviates from this range is a potential cost anomaly.

### Step: View Cost Anomalies

You can view cost anomalies for the following:

* **Clusters**: Kubernetes Clusters, Namespaces, and Workloads
* **AWS**: Service and Account
* **GCP**: Products, Projects, and SKUs
* **Azure**: Subscription ID, Service Name, and Resources

Perform the following steps to view cost anomalies:

1. In **Cloud Costs**, click **Anomalies**.  
  
The Anomalies page display the following information:  
![](https://files.helpdocs.io/i5nl071jo5/articles/x0z3r0bv99/1650907857712/screenshot-2022-04-25-at-10-59-16-pm.png)  


|  |  |
| --- | --- |
| Anomalies Detected | The total number of anomalies detected across all of your cloud providers during the specified time period. |
| Total Cost Impact | The total cost impact because of the anomalous spend across all the resources in your cloud infrastructure. |
| Top 3 Anomalies | Top 3 anomalies across all the resources. Hover on the resource to view the detail of the resource. |
| Anomalies by Cloud Providers | The number of anomalies by the cloud providers. For example, GCP, AWS. |
| Anomalies by Status | The total number of anomalies according to their status across all the resources. Currently, only the **Open** state is available. |
| Date | The date on which anomaly was detected. |
| Anomalous Spend | The total amount of anomalous spend per resource. |
| Resource | Detail of the resource on which the anomalous cost was detected. |
| Status | The current status of an anomaly. |

 

1. From the **Resource**, click the anomaly for which you want to view the details.![](https://files.helpdocs.io/i5nl071jo5/articles/x0z3r0bv99/1650908711574/screenshot-2022-04-25-at-11-14-54-pm.png)
2. Click the three-dot and then click **This is false anomaly** to determine if this is a false anomalous event. This helps CCM [cost anomaly detection models](detect-cloud-cost-anomalies-with-ccm.md) to learn and improve the algorithm to be more tailored to your assessments.![](https://files.helpdocs.io/i5nl071jo5/articles/x0z3r0bv99/1650909831935/screenshot-2022-04-25-at-11-33-37-pm.png)

