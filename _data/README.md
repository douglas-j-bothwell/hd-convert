This folder is intended for data files used in the production process.

## article-mappings.LATEST.json

Useful for redirects -- if a URL contains the HelpDocs article ID (key value), use the equivalent value to redirect to the equivalent URL in Harness Developer Hub.

For example, the following URL:

https://docs.harness.io/article/***z56wmnris8***-set-up-an-aws-vm-build-infrastructure

Would get redirected to:

https://developer.harness.io/***docs/continuous-integration/use-ci/set-up-build-infrastructure/set-up-an-aws-vm-build-infrastructure***

## category-mappings.LATEST.json

Useful for redirects -- if a URL contains the HelpDocs category ID (key), use the equivalent value to redirect to the equivalent URL in Harness Developer Hub.

For example, the following URL:

https://docs.harness.io/category/***rg8mrhqm95***-set-up-build-infrastructure

Would get redirected to:

https://developer.harness.io/***category/set-up-build-infrastructure***

## image-mappings.LATEST.yml 

Primarily of interest to writers. `02-get-images.sh` downloads and saves an image file for each URL found in the markdown. If the same URL is referenced multiple times, there will be multiple local copies of the same image. You can parse this YAML to find duplicate files and the markdown files that reference them. This file has the following format:

`helpdocs-image-url`:
     `local-copy-1` : `markdown-file-that-references-local-copy-1`,
     `local-copy-2` : `markdown-file-that-references-local-copy-2`,
     ....