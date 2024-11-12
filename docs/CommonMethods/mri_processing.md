---
layout: default
title: Neuroimaging Data Processing Tools
parent: Common Methods
---

There are many tools out there for processing and analyzing neuroimaging data.
In the PennLINC team, we typically acquire magnetic resonance imaging (MRI)
data with a handful of modalities, such as functional MRI (fMRI),
diffusion-weighted imaging (DWI),
structural MRI (sMRI) (especially T1- and/or T2-weighted imaging),
and arterial spin labeling (ASL).
This page summarizes the acquisitions we tend to use,
as well as the processing tools we use for each.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Structural Magnetic Resonance Imaging (sMRI)

The two main types of structural images we tend to acquire are
high-resolution T1-weighted and T2-weighted images.

A high-resolution T1-weighted image is required for most of the processing workflows
for other modalities, such as fMRI, DWI, and ASL.

We generally try to acquire a high-resolution T2-weighted image as well,
in order to (1) improve Freesurfer segmentation and (2) to calculate a myelin-weighted map.

### sMRIPrep

We recommend using sMRIPrep to process T1w and T2w images.
sMRIPrep is a BIDS App that minimally preprocesses structural MRI data,
runs Freesurfer to segment the data and project it to the surface,
and warps the data to requested template spaces.

{: .note-title }
> Tip
>
> A number of processing pipelines for other MRI modalities,
> including fMRIPrep and ASLPrep, will automatically run sMRIPrep.
> We generally rely on the structural processing from these pipelines
> instead of running sMRIPrep directly.


## Functional Magnetic Resonance Imaging

### PennLINC-preferred fMRI Protocols

Starting in 2023, we began using a specific fMRI protocol in our studies.
This is a multi-echo fMRI protocol with complex reconstruction and
no-excitation noise volumes acquired at the end of each run.

{: .highlight-title }
> Fun fact
>
> This is the same basic protocol used in
> [Siegel et al. (2024)](https://www.nature.com/articles/s41586-024-07624-5) and
> [Moser et al. (preprint)](http://biorxiv.org/lookup/doi/10.1101/2023.10.27.564416).
>
> We have some openly-available data with this protocol on
> [OpenNeuro](https://openneuro.org/datasets/ds005250).

#### Multi-echo fMRI

We use multi-echo fMRI instead of the more common single-echo approach.
While acquiring multiple echoes means that we end up with a longer TR than common
highly-accelerated protocols, such as the HCP protocol,
multi-echo data have improved SNR over single-echo data,
and the echoes can be leveraged to distinguish BOLD and non-BOLD noise with ``tedana``.

For more information on the costs and benefits of multi-echo fMRI please see
the ME-ICA team's
[multi-echo data analysis book](https://me-ica.github.io/multi-echo-data-analysis/content/intro.html)
or the [tedana documentation](https://tedana.readthedocs.io/en/stable/).

#### Complex-valued fMRI

We enable complex reconstruction for our fMRI sequences,
which produces both magnitude and phase data rather than the more common magnitude-only
reconstruction.
While there are many methods to leverage phase information in fMRI data out there
in the literature,
in practice we mostly use the phase data for thermal noise removal with NORDIC.

In the future, we will be able to use the phase data for the following:

- Dynamic distortion correction with the MEDIC algorithm.
- Phase regression (see [`nipreps/fMRIPost-phase`](https://github.com/nipreps/fmripost-phase))
- Complex-valued ICA (see [`nipreps/fMRIPost-phase`](https://github.com/nipreps/fmripost-phase))
- Phase jolt and phase jump time series calculation (see [`nipreps/fMRIPost-phase`](https://github.com/nipreps/fmripost-phase))

#### No-excitation noise volumes

At the end of the protocol, we acquire 3 volumes without a radiofrequency pulse.
These no-excitation volumes are then used to characterize the thermal noise levels in the data,
which improves thermal noise removal by NORDIC.


### Processing fMRI Data

In order to process these unique data, we use the following basic workflow:

1. [complex-valued data only] Thermal noise removal with NORDIC.
2. Minimal preprocessing with fMRIPrep.
3. [multi-echo data only] Multi-echo denoising with tedana.
4. Post-processing and connectivity extraction with XCP-D.
5. Statistical analysis with (usually) custom R code.


## Diffusion-Weighted Imaging

### PennLINC-preferred DWI Protocols

We generally use compressed-sensing diffusion spectrum imaging (CS-DSI)
as our preferred DWI protocol.

{: .highlight-title }
> Fun fact
>
> We have some openly-available data with our preferred CS-DSI protocol on
> [OpenNeuro](https://openneuro.org/datasets/ds004737).
> One important modification is that we enable complex reconstruction,
> which will allow for improved thermal noise removal with MP-PCA.

### Processing DWI Data

We use the following workflow for DWI data:

1. Minimal preprocessing with QSIPrep.
2. Reconstruction with QSIRecon.
3. Statistical analysis with (usually) custom R code.


## Arterial Spin Labeling

### PennLINC-preferred ASL Protocols

Generally, for developmental samples (PennLINC's bread and butter),
we use a single-delay PCASL protocol developed by Manuel Taso.

For aging populations, we might use a multi-delay PCASL protocol,
but that hasn't come up in our internal studies yet.

### Processing ASL Data

We use the following workflow for ASL data:

1. Preprocessing, CBF estimation, and connectivity extraction with ASLPrep.
2. Statistical analysis with (usually) custom R code.
