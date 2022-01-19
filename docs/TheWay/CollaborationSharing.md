---
layout: default
title: Collaboration & Sharing
parent: The Way
nav_order: 4
has_toc: true
---

# Collaboration & How to Share Data
{: .no_toc}

Collaboration is an important part of our work. Sharing the input data and outputs/derivatives of a project is a critical step in the scientific process, and so doing it both accurately and efficiently is a high priority. Overall, remember that this step can be a strain, especially when dealing with external collaborators or systems that are foreign to you. Be patient, and remember that we have to balance accuracy/reproducibility with efficiency/speed.

Below are a few example scenarios and what best recommendations we have for sharing data.

# BIDS Data

Sharing BIDS data typically happens at the beginning of a project. We recommend looking into the options on [this page about fetching your data](/docs/TheWay/FetchingYourData#FetchingYourData).

# Outputs from TheWay

## Datalad to Datalad
Generally, if you have outputs from TheWay in a `datalad` dataset, you should try to have collaborators ingest that as `datalad` datasets too! This is best accomplished if the user can `clone` the dataset:

```shell
#cloning a dataset from a git repo

datalad clone https://github.com/datalad-datasets/longnow-podcasts.git
```

For most of our use, you want to clone the _output_ of a specific pipeline -- these outputs are stored in the _output RIA store_, so you have to clone them like so:

```shell
#cloning from an output ria of an fmriprep run
datalad clone --reckless ephemeral ria+file:///PATH_TO_FMRIPREP_DATASET/output_ria#~data fmriprep_outputs
```

If the person is happy with this format and working with `datalad`, they can use this command to get the cloned data. 

## Datalad to Non-Datalad

If they want regular files with no `datalad` tracking involved, they can then use `rsync` to copy the physical data by following the symbolic links. That looks like this:

```shell
# YOU clone from an output ria of an fmriprep run
datalad clone --reckless ephemeral ria+file:///PATH_TO_FMRIPREP_DATASET/output_ria#~data fmriprep_outputs

# THEY extract the data from this output RIA as regular files
rsync -avzhL --progress fmriprep_outputs FINAL_DESTINATION
```

---
NOTE FOR EXPERTS: This is part of the `datalad` workflow on _aliasing_; visit [http://handbook.datalad.org/en/latest/beyond_basics/101-147-riastores.html](this resource) to learn more about how you can use aliasing to share data flexibly.

---

## Zipped or Unzipped?

A lot of outputs from our pipelines can be very large. We typically keep these zipped after running, but for collaboration you can choose to unzip all or part of the outputs into an _unzipped outputs_ `datalad` dataset. We have an example script [here](https://github.com/PennLINC/TheWay/blob/main/scripts/cubic/bootstrap-unzip-fmriprep.sh) that unzips fMRIPrep outputs -- you could, for example, modify the `datalad` runscript section in lines 150-160 to include/exclude what you need:

```shell
# continued from the unzip script
# Line 150

# unzip outputs
unzip -n $ZIP_FILE 'fmriprep/*' -d .

# remove files we don't need at your discretion
rm fmriprep/func/*from-scanner_to-T1w_mode-image_xfm.txt
rm fmriprep/func/*from-T1w_to-scanner_mode-image_xfm.txt
rm fmriprep/func/*space-MNI152NLin6Asym_res-2_boldref.nii.gz
rm fmriprep/func/*space-MNI152NLin6Asym_res-2_desc-aparcaseg_dseg.nii.gz
rm fmriprep/func/*space-MNI152NLin6Asym_res-2_desc-aseg_dseg.nii.gz
# copy outputs out of fmriprep
cp -r fmriprep/func/* .
```

This can help save space on disk or make it easy for collaborators to transfer smaller outputs.

# PennLINC-Kit

PennLINC-Kit is a toolkit for common analysis functions used by the PennLINC scientists. It comes with prepackaged datasets and accessible functions for fetching some of our most used data on-the-fly in your Python session. For many data sharing applications, this alone may suffice, so always check with PennLINC-Kit before you engineer your own solution.

Documentation (in progress) is available [here](https://pennlinc-kit.readthedocs.io/en/latest/#).

# Permissions, VPNs, and Picking a Medium

There are always barriers to sharing data. Someone needs access to something and that often entails a lot of bureaucracy; maybe there is data that can't be shared with PHI; maybe there is not enough disk space to move data. Here are some thoughts to help you guide what decisions to make:

- Is this a one-time transaction, or will there be data moving back-and-forth repeatedly? VPNs + permissions are an investment that can take a week or sometimes more to be approved
- How big is the data? Does this _have to_ be shared on a cluster? Maybe it's more appropriate to download it locally and upload it to [Box](https://www.isc.upenn.edu/pennbox) or [SecureShare](https://www.isc.upenn.edu/security/secure-share)
- What clusters are involved? CUBIC has a complicated permissions system; PMACS is more lenient but how will you move data from CUBIC to PMACS?
- Do you need `datalad` tracking? How much do collaborators care about that (weighed against how much _you_ care about that)? `datalad` can be fun, but it is definitely a commitment that you can't easily back out of