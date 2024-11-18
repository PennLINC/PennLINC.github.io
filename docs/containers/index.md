---
layout: default
title: Using Containers
parent: Computation Basics
nav_order: 6
has_children: false
permalink: docs/containers
has_toc: false
---


# Using Containers for Research
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

# Containers on high performance computing clusters

Many useful software tools have difficult-to-compile dependencies. A great way to solve this problem is to bundle the software and its dependencies into a **container**, which can be run directly. This is typically done using ``docker``.  Since we are using a computing cluster and don't have the privileges necessary to run ``docker``, we can download an image and convert it into a singularity image.

## Creating a singularity image

Docker images are available on dockerhub. You can choose any of these images and convert them to a singularity image by specifying their location on dockerhub. For example, there is a docker image of DSI Studio that we might want to run on the cluster. This program is very difficult to compile, so we can point singularity at this docker url and build a singularity image.

```console
$  singularity \
>  build \
>  dsistudio_latest.sif \
>  docker://dsistudio/dsistudio:latest
```

## Running a singularity container

The previous section produces a file called ``dsistudio_latest.sif``. We can do lots of things with this image. We can enter the image and access a shell:

```console
$ /share/apps/singularity/2.5.1/bin/singularity shell dsistudio_latest.sif
Singularity dsistudio_latest.sif:~> cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
NAME="Debian GNU/Linux"
VERSION_ID="8"
VERSION="8 (jessie)"
ID=debian
HOME_URL="http://www.debian.org/"
SUPPORT_URL="http://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

```
The line starting with ``Singularity`` is a bash shell inside the image. We can prove this by printing the contents of ``/etc/os-release``, which shows that this shell thinks it's in Debian. If we run a similar command outside of the container's shell, we can see we're back on Centos:

```console
$ cat /etc/redhat-release
CentOS release 6.9 (Final)
```

By specifying ``shell`` as the first argument to singularity, we drop into the interactive shell. In order to do anything useful, we need to access data on the host machine's file system.

## Linking file systems

Since we want to run the containerized software on data on our filesystem, we need a way to point the singularity image to this filesystem. This can be somewhat tricky because certain directories are automatically mounted in the image and the image has trouble following symlinks to destinations outside its filesystem. Here we use the antsCT BIDS app as the singularity image and tell it to execute "ls" inside of itself. We see it's placed us in our home directory and has access to all these files.

```console
$ APPS_DIR=/data/joy/BBL/applications/bids_apps
$ ANTSCT=${APPS_DIR}/antsct_bids.sif
$ singularity exec $ANTSCT ls
Desktop				   conv			 dicoms		  matlab
Miniconda3-latest-Linux-x86_64.sh  data			 label_names.csv  projects
bio				   dicominfo_ses-01.tsv  link_bids.py	  tmp
$ singularity exec $ANTSCT pwd
/home/<username>
```

This is cool, but we don't keep any data in our home directories. Unfortunately, ``/data`` does not get mounted by default:

```console
$ singularity exec $ANTSCT ls /data
ls: cannot access '/data': No such file or directory
```
So we have to make a directory in our home directories where ``/data`` will be mounted.

```console
$ mkdir /home/<username>/data
$ # This won't work
$ singularity exec -B /data $ANTSCT ls /data
WARNING: Skipping user bind, non existent bind point (directory) in container: '/data'
ls: cannot access '/data': No such file or directory
$ # This will work
$ singularity exec -B /data:/home/<username>/data $ANTSCT ls data
ADNI_longitudinal  XNAT     grossman  jet  jux	  picsl-build  tesla-home
HCP_data	   archive  jag       joy  picsl  tesla-data
```

### Very important note

Remember that containerized software can't see outside of its container. As a result, all i/o within the container needs to be relative to its bound directories. If your software requires a text file listing paths to files as input, the path to this file needs to be the container version of the path and all the paths in the file need to point to the files *as they would be seen by the container*.

One very nice thing is that /tmp is automatically mounted in the container. This means that if you are running the container using SGE, the $TMPDIR directory is directly accessible from a container.

## Running a BIDS app

BIDS apps are containerized versions of pipelines that run on data that have been named using the BIDS convention. By containerizing an entire pipeline, you can guarantee that the exact same software and computing environment are used every time the pipeline is run. There are also lots of publicly available BIDS apps that implement popular pipelines. Here we'll run the ANTs cortical thickness BIDS app on one of the grmpy subjects. First, we need to have everything in BIDS format. These files exist in ``/data/jux/BBL/studies/grmpy/BIDS``.

Running the actual pipeline is then as simple as

```console
$ SNGL_BIDS=/home/<username>/data/jux/BBL/studies/grmpy/BIDS
$ singularity run -B /data:/home/<username>/data $ANTSCT \
>   singularity_BIDS singularity_BIDS/derivatives/ANTsCT participant \
>   --participant_label 080557
```


```
