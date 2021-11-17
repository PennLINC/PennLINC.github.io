---
layout: default
title: Using Containers
nav_order: 12
has_children: true
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


# Singularity on PMACS

PMACS requires a couple extra steps to run singularity. First, only one host
can run `singularity` *and* connect to the internet. You have to ssh into this
host from `sciget` like so:

```
$ ssh singularity01
$ module load singularity
```

Now you can build a singularity image from any image on DockerHub. Be sure
to save your `.sif` file in your project directory (ideally in a subdirectory named
`images`), as the home directories on `singularity01` do not sync with the rest of PMACS.

```console
$ cd /project/my_project/images
$ singularity build fmriprep-20.0.5.sif dockerhub://poldracklab/fmriprep:20.0.5
```

In the event that you do not have access to your project directory on singularity01,
you can pull the image in your home directory. After the image is in your home directory,
move the image over to your project directory while you are on sciget, but have
exited from singularity01.

```console
$ ssh singularity01
$ cd
$ singularity pull docker://antsx/ants
$ exit
$ mv ~/ants_latest.sif /project/my_project/images
```

### Note for images that use `templateflow`

Some of the `nipreps`-based pipelines use the `templateflow` library to
download templates. This is a problem on PMACS because the compute hosts
do not connect to the internet. This means you'll have to manually download
the templateflow data and link this directory into the container at run time.

Here is fmriprep's documentation on [this problem](https://fmriprep.org/en/stable/singularity.html#templateflow-and-singularity) with [more details here](https://neurostars.org/t/problems-using-pediatric-template-from-templateflow/4566/15).

Ultimately, you'll need to do something like this (templates listed are the ones that are typically needed to run fMRIPrep):

```console
$ export TEMPLATEFLOW_HOME=/path/to/keep/templateflow
$ python -m pip install -U templateflow  # Install the client
$ python
>>> from templateflow import api as tfapi
>>> tfapi.TF_S3_ROOT = 'http://templateflow.s3.amazonaws.com'
>>> tfapi.get('MNI152NLin6Asym', atlas=None, resolution=[1, 2], desc=None, extension=['.nii', '.nii.gz'])
>>> tfapi.get('MNI152NLin6Asym', atlas=None, resolution=[1, 2], desc='brain', extension=['.nii', '.nii.gz'])
>>> tfapi.get('MNI152NLin2009cAsym', atlas=None, extension=['.nii', '.nii.gz'])
>>> tfapi.get('OASIS30ANTs', extension=['.nii', '.nii.gz'])
>>> tfapi.get('fsaverage', density='164k', desc='std', suffix='sphere')
>>> tfapi.get('fsaverage', density='164k', desc='vaavg', suffix='midthickness')
>>> tfapi.get('fsLR', density='32k')
>>> tfapi.get('MNI152NLin6Asym', resolution=2, atlas='HCP', suffix='dseg')
```

And run the singularity image binding the appropriate folder:

```console
$ singularity run -B ${TEMPLATEFLOW_HOME}:/templateflow \
      --cleanenv fmriprep.sif <fmriprep arguments>
```

Here is an example of a call to singularity on PMACS:

```console
$ singularity run --writable-tmpfs --cleanenv -B /project/ExtraLong/data/templateflow:/templateflow -B /project/ExtraLong/data/license.txt:/opt/freesurfer/license.txt -B /project/ExtraLong/data/ /project/ExtraLong/images/fmriprep_20.0.5.sif /project/ExtraLong/data/bids_directory/sub-X/ses-PNC1 /project/ExtraLong/data/freesurferCrossSectional/fmriprep/sub-X/ses-PNC1 participant --skip_bids_validation --anat-only --fs-license-file /opt/freesurfer/license.txt --output-spaces MNI152NLin2009cAsym --skull-strip-template OASIS30ANTs --nthreads 7
```
