---
title: Sample: Kubernetes Manifest - NFS Volume
description: This Kubernetes manifest creates an NFS volume. For a sample manifest for an NFS server, see Sample --  Create a Permanent Volume - NFS Server. apiVersion --  v1 kind --  PersistentVolumeClaim metadata --  name -- …
tags: 
   - helpDocs
# sidebar_position: 2
helpdocs_topic_id: 6929n499sf
helpdocs_category_id: vm60533pvt
helpdocs_is_private: false
helpdocs_is_published: true
---

This Kubernetes manifest creates an NFS volume. For a sample manifest for an NFS server, see [Sample: Create a Permanent Volume - NFS Server](https://docs.harness.io/article/3onmos2n3v).


```
apiVersion: v1  
kind: PersistentVolumeClaim  
metadata:  
  name: nfs-ng  
spec:  
  accessModes:  
    - ReadWriteMany  
  storageClassName: ""  
  resources:  
    requests:  
      storage: 1Gi  
  volumeName: nfs-ng  
  
---  
  
apiVersion: v1  
kind: PersistentVolume  
metadata:  
  name: nfs-ng  
spec:  
  capacity:  
    storage: 1Gi  
  accessModes:  
    - ReadWriteMany  
  nfs:  
    server: nfs-server.default.svc.cluster.local  
    path: "/"  
  mountOptions:  
    - nfsvers=4.2  

```
