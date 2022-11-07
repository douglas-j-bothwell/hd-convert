---
title: Import an Input Set From Git
description: This topic explains the steps to import an Inputset from Git.
tags: 
   - helpDocs
   - Git sync
   - git experience
# sidebar_position: 2
helpdocs_topic_id: j7kdfi3640
helpdocs_category_id: rv2jo2hoiy
helpdocs_is_private: false
helpdocs_is_published: true
---



# The issue

I'm trying to create a regex that captures image URLs in the Harness docs in a "non-greedy" manner, up to the FIRST closing paren. The regex I've tried and tried to come up with a regex that works but haven't had any luck. The regex I'm using captures image URLs that include .jpg or png extension AND have a space or newline after the closing paren. These capture ~90% of the URLs, the ones that are correctly formatted. But there are still a lot of URLs that it's missing, and I believe it's all due to the regex used in the accompanying Python file:

_imgURLpattern = re.compile('https?:\/\/files.helpdocs.io\/.*\.(?:png|jpg)')

# Steps to Reproduce

1. Go to the parent folder: `cd $GIT_REPO_HOME/hd-convert/_test-files/images-regex-test`
2. Run the script and pipe to a log: `python3 get-images.TEST.py > test.log`
3. The log shows errors for the images that it can't download. If an image is downloaded successfully, it goes into `docs/static`.

(You'll need to view this README in a raw text editor to see what I'm talking about, GitHub is rendering the images but they're pointing to files on https://files.helpdocs.io, not local copies, which is what I'm looking to do...) 

# TEST 1 -- No space or newline after image link

** Intended behavior:** Regex captures each individual link up to closing paren (2 matches) and downloads/saves the image
** current behavior:**  Regex captures in a greedy mannager, up to the closing paren in the paragraph (one match) and cannot download/save the image

 
1. In Harness, click **Deployments**.
2. Select your Project and click on **Pipelines** and click on **Input Sets**.
3. Click **New Input Set** and select **Import From Git**.![](https://files.helpdocs.io/kw8ldg1itf/articles/j7kdfi3640/1658829738986/screenshot-2022-07-26-at-3-30-31-pm.png)The **Import Input Set From Git** settings appear.![](https://files.helpdocs.io/kw8ldg1itf/articles/j7kdfi3640/1658830029315/screenshot-2022-07-26-at-11-18-41-am.png)

# TEST 2 -- Image Link does not have Filename Extension

** Intended behavior:** Regex captures the image up to the closing paren. 
** current behavior:**  Regex misses this reference b/c it doesn't include an extension (.jpg or .png)
 
Enter the branch or tag and click **Run Pipeline**.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218110739/mzt-tjleo-46-qzwrs-wgasgnarhzvqc-arrc-fmfre-nytc-fb-zaefn-6-q-ztnmgo-q-9-pdg-ogbfc-zjmyb-1-m-8-l-c-9-bc-8-cax-3-twr-1-v-gy-rg-1-w-ltiq-i-4-m-6-txwjyiu-ykge-mwd-1-hj-7-yh-gk-ei-ju)###  Step 5: View the Results

You can see the logs for the Build and Push step in the Pipeline as it runs.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218117572/f-fasi-omyjgn-gqw-1-mj-ng-kjrhzx-gxsahkms-4-cp-44-tkgss-fm-8-kmiue-g-0-e-wwb-0-c-mtmlx-swl-ex-eglsgo-ehbl-xkjcz-pxkvr-ler-z-7-u-zsux-amx-42-z-yby-i-4-def-xt-sx-5-t-0-llg-9-z-uok)In your Harness project's Builds, you can see the build listed.

![](https://files.helpdocs.io/i5nl071jo5/articles/gstwrwjwgu/1625218126856/ahth-iqde-si-wv-5-mvxu-r-9-n-v-81-tnpq-xzeh-e-3-p-7-h-tl-y-8-btw-ojdwv-0-ez-owzasbt-tq-e-9-hph-jjf-exqy-uen-v-30-nvs-czwia-72-u-xu-g-hipc-1-e-6-sm-jezlknje-p-72-e-3-kv-h-7-h-f-6-r-o-1-ckj-i)On GCR, you can see the image that you pushed.

# TEST 3 -- Successful downloads


## Intended behavior

If the image link is followed by a space or newline, the regex works as intended

## Note

When you run the script and a file downloads successfully, it will update the following links. To revert to the originals, copy/paste this section from backup.txt file. 


Here's a quick visual summary:

![](https://files.helpdocs.io/i5nl071jo5/articles/f0aqiv3td7/1636407720427/clean-shot-2021-11-08-at-13-37-44.gif)#### Create API Key


Click each stage's steps to see the logs in real time.



![](https://files.helpdocs.io/i5nl071jo5/articles/x0d77ktjw8/1625180234470/clean-shot-2021-07-01-at-15-57-04.png)

* Click **Set Up Stage**. The new stage is added to the Pipeline.

 Click **Console View** to see more details.

 * Under Select a Kubernetes Cluster, click **Select**.

 ![](https://files.helpdocs.io/i5nl071jo5/articles/x0d77ktjw8/1625180326375/clean-shot-2021-07-01-at-15-58-38.png)

 * Click **New Connector** and set up the new Connector as follows:
 	+ **Name:** ci-delegate
 	+ **Details:** Select **Use the credentials of a specific Harness Delegate**. You'll add this Delegate next.
 	+ **Delegates Setup:** Select the Kubernetes Delegate you added earlier using its Tags.
 	+ **Connection Test:** Wait for the test to finish and then click **Finish**. The new Connector is added to the Kubernetes Cluster field.
 * In **Namespace**, enter the namespace `harness-delegate-ng`. Click **Next** to proceed to the Execution tab.




