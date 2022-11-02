This folder includes the following scripts:

# get-images.DEV.py



## Known Issues
This script has the following known issues:

Only downloads/updates files with .jpg or .png extensions
The filename in the HelpDocs cloud must have a .jpg or .png extension. In some cases, a filename has no extension. This is especially true in the CI docs, where ~50 files have really weird filenames with no extension. An example:

```
<figure><img src="https://files.helpdocs.io/i5nl071jo5/articles/qr4h6kn6yd/1632730868502/uobh-xzoza-9-sbwf-1-dky-45-bqsnutdzxc-nk-akh-itd-zgp-rs-4-pgi-7-g-hxd-a-pziks-cm-4-wmr-ni-66-nxyb-xk-emd-m-u-0-zk-2-m-7-t-ugdk-p-1-w-pszdanb-gvfr-0-awhf-gj-90-uw-03-b-4-ru-844-q-ca-gvdl-u-s-0" style="max-height:50%;max-width:50%" data-hd-height="50%" data-hd-width="50%"/></figure>
```

Workaround: In this case, I needed to download the files and update the links manually, which took about 6 hours. I’ve attached a ZIP file that includes all the downloaded files and updated links, so I don’t need to do it again. 

The image link in the markdown file must be followed by a whitespace or a newline
In some cases, an image link will include the filename in the URL text section, so the image link is essentially repeated. For example: 

[![](https://files.helpdocs.io/i5nl071jo5/articles/q6fr5bj63w/1610059179870/image.png)](https://files.helpdocs.io/i5nl071jo5/articles/q6fr5bj63w/1610059179870/image.png
In this case, remove the filename in the text section so that the link appears like this:

![](https://files.helpdocs.io/i5nl071jo5/articles/q6fr5bj63w/1610059179870/imag
