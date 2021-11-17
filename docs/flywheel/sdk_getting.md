---
layout: default
title: "Getting Data from Flywheel"
parent: Flywheel
nav_order: 4
---

## Requirements

These tutorials require

  * A local installation or [Python](/docs/Basics/basics/#installing-python)
  * [Logging in](/docs/flywheel/#connecting-with-the-sdk) to Flywheel using the CLI


# Getting data from Flywheel

Flywheel stores data and its accompanying metadata in a proprietary system in the cloud. This data can be downloaded manually using the web interface or through the SDK. The process of getting data from Flywheel involves two steps

  1. Finding the data's [container](/docs/flywheel/sdk_theory/#data-containers)
  2. Finding the file object and downloading it or a part of it

## Accessing data in Python

Suppose we ran FMRIPREP and would like to download some of its outputs. In this example FMRIPREP was run and attached to a session container (it could also be attached to a subject or project). The first step is to find the session container:

```python
>>> import flywheel
>>> fw = flywheel.Client()
>>> session_id = "5cd31cbc08a9960041650843"
>>> analysis = fw.get_container_analyses(
...     session_id, filter='label="fmriprep 06/03/2019 10:58:53"')[0]
>>> print(analysis.label)
fmriprep 06/03/2019 10:58:53
```
In this case we know that there is only one analysis with this name so we access it from the list that is returned by indexing at `[0]`. The `analysis` variable represents the analysis container.

### Listing file attachments

Now we can see which files are attached to this analysis data container:

```python
>>> print("\n".join([file_obj.name for file_obj in analysis.files]))
sub-01_5cf535cb36da2300443b2fb9.html.zip
fmriprep_work_sub-01_5cf535cb36da2300443b2fb9.zip
fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip
```

These are the names of each file object attached to the container. These names should be meaningful to us.

### Downloading file attachments

The most straightforward approach to getting data from Flywheel is to directly download the zip file. Then you can unzip it and access its contents on your local machine. To do that,

```python
>>> analysis.download_file("fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip",
...                        "fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip")
```

and the file `fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip` will exist in your current working directory.

### Extracting files from zip archive attachments

It is very common for these attachments to be zip files. Often we don't need all the data in a zip file. Instead we just want to get one or more files from the zip directly. First, we can get information about the contents of the zip

```python
>>> zip_info = analysis.get_file_zip_info(
...     'fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip')
>>> print('\n'.join([member.path for member in zip_info.members]))
5cf535cb36da2300443b2fb9/
5cf535cb36da2300443b2fb9/fmriprep/
5cf535cb36da2300443b2fb9/fmriprep/logs/
5cf535cb36da2300443b2fb9/fmriprep/logs/CITATION.tex
5cf535cb36da2300443b2fb9/fmriprep/logs/CITATION.html
5cf535cb36da2300443b2fb9/fmriprep/logs/CITATION.md
5cf535cb36da2300443b2fb9/fmriprep/sub-01/
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_task-mixedgamblestask_run-02_carpetplot.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_task-mixedgamblestask_run-01_carpetplot.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_task-mixedgamblestask_run-01_rois.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_task-mixedgamblestask_run-01_flirtbbr.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_t1_2_mni.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_task-mixedgamblestask_run-02_flirtbbr.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_task-mixedgamblestask_run-02_rois.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/figures/sub-01_seg_brainmask.svg
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-01_desc-confounds_regressors.tsv
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/func/sub-01_task-mixedgamblestask_run-02_desc-confounds_regressors.tsv
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_from-MNI152NLin2009cAsym_to-T1w_mode-image_xfm.h5
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_space-MNI152NLin2009cAsym_desc-preproc_T1w.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_desc-brain_mask.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_desc-preproc_T1w.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_label-GM_probseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_space-MNI152NLin2009cAsym_dseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_space-MNI152NLin2009cAsym_label-WM_probseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_label-CSF_probseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_label-WM_probseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_from-orig_to-T1w_mode-image_xfm.txt
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_dseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_from-T1w_to-MNI152NLin2009cAsym_mode-image_xfm.h5
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_space-MNI152NLin2009cAsym_label-GM_probseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/sub-01/anat/sub-01_space-MNI152NLin2009cAsym_label-CSF_probseg.nii.gz
5cf535cb36da2300443b2fb9/fmriprep/dataset_description.json
5cf535cb36da2300443b2fb9/fmriprep/sub-01.html
```

That's all the fmriprep output! Suppose we only want to get the confound regressors out of this zip. we can easily do this with a few lines:

```python
>>> from os import listdir, path as op
>>> confounds_file = [member for member in zip_info.members if
...                   member.path.endswith('confounds_regressors.tsv')][0]
>>> confounds_file_name = op.split(confounds_file.path)[1]
>>> print(confounds_file_name)
>>> analysis.download_file_zip_member('fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip',
...                                   confounds_file.path,
...                                   confounds_file_name)
>>> listdir(".")  # Verify that it was downloaded
[ 'sub-01_task-mixedgamblestask_run-01_desc-confounds_regressors.tsv' ]
```

Since BIDS requires that subject and session are in each filename, we can iterate over all the analyses and download these files to the current working directory. Alternatively, we can read the data directly into memory:

```python
>>> mem_tsv = analysis.read_file_zip_member('fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip',
...                                         confounds_file.path)
>>> import pandas as pd
>>> from io import BytesIO
>>> confounds_df = pd.read_csv(BytesIO(mem_tsv), delimiter='\t')
>>> confounds_df.head()
         csf  white_matter  global_signal  std_dvars      dvars  framewise_displacement  ...   trans_x   trans_y   trans_z     rot_x     rot_y     rot_z
0  583.33704           0.0      485.55243        NaN        NaN                     NaN  ...  0.000000  0.000000  0.000000 -0.000170 -0.000000  0.000000
1  579.08600           0.0      483.35240   1.179028  18.223396                0.072119  ...  0.000000  0.020775  0.046312 -0.000271 -0.000000  0.000000
2  579.21936           0.0      481.93520   1.102987  17.048092                0.034897  ...  0.000000  0.000000  0.045737  0.000000 -0.000000  0.000000
3  574.88620           0.0      481.27450   1.024027  15.827655                0.033394  ...  0.010164 -0.010357  0.042451  0.000000 -0.000000  0.000192
4  575.22850           0.0      481.20953   0.997114  15.411689                0.032764  ...  0.016909 -0.008537  0.034754  0.000000 -0.000223  0.000085

[5 rows x 25 columns]
```

## A full example

Suppose we want to extract the QC tsv from all of the QSIPREP gears attached to the PNC project. First we get a reference to the project container.

```python
>>> pnc = fw.projects.find_first('label=PNC_CS_810336')
>>> analyses = fw.get_analyses('projects', pnc.id, 'sessions')
>>> qsiprep_results = [ana for ana in analyses if
...                    ana.label.startswith("qsiprep_0.3.16_0.8.0RC3")]
```

We can write a temporary function that gets the non-html zip file and extracts the qc file.

```python
>>> import os.path as op
>>> def download_qc_files(analysis, output_dir):
...     # Safely get a list of files
...     analysis_files = analysis.files or []
...     # Search for a non-html zip file
...     zip_files = [f_obj for f_obj in analysis_files if
...                  f_obj.name.endswith('.zip') and
...                  not f_obj.name.endswith('.html.zip')]
...  
...     # if it succeeded, there will be exactly one results zip
...     if not len(zip_files) == 1:
...         return False
...     zip_obj = zip_files[0]
...
...     # List the contents of the zip archive
...     zip_members = analysis.get_file_zip_info(zip_obj.name)['members']
...     # find the confounds file and the qc file
...     confounds_files = [f_obj for f_obj in zip_members if 'confounds.tsv' in f_obj.path]
...     qc_files = [f_obj for f_obj in zip_members if 'ImageQC' in f_obj.path]
...
...     # We need both files
...     if not confounds_files and qc_files:
...         return False
...     confounds_files = [f_obj for f_obj in zip_members if 'confounds.tsv' in f_obj.path]
...     qc_files = [f_obj for f_obj in zip_members if 'ImageQC' in f_obj.path]
...     # We need both files
...     if not confounds_files and qc_files:
...         return False
...     # Download the confounds file
...     confounds_file = confounds_files[0].path
...     downloaded_confounds_file = output_dir + "/" + op.split(confounds_file)[1]
...     if not op.exists(downloaded_confounds_file):
...         analysis.download_file_zip_member(zip_obj.name,
...                                           confounds_file,
...                                           downloaded_confounds_file)
...     # Download the qc file
...     qc_file = qc_files[0].path
...     downloaded_qc_file = output_dir + "/" + op.split(qc_file)[1]
...     if not op.exists(downloaded_qc_file):
...         analysis.download_file_zip_member(zip_obj.name,
...                                           qc_file,
...                                           downloaded_qc_file)
...     return True
...
```

Then we can loop over the analysis objects and download the files we want:

```python
>>> import os
>>> failed_analyses = []
>>> out_dir = "qsiprep_tsvs"
>>> os.makedirs(out_dir, exist_ok=True)
>>> for result in tqdm(qsiprep_results):
...     if not load_qc_txt(result, out_dir):
...         failed_analyses.append(result)
```

And all the files we wanted will be in `qsiprep_tsvs/`!


## Downloading BIDS

### Using the CLI

We don't recommend using this approach, but it is possible to use the Flywheel CLI
to download BIDS directly without using Python. See their documentation for
[usage](https://docs.flywheel.io/hc/en-us/articles/360008224093-Command-Line-Interface-Overview).

### Using `fw-heudiconv-export`

## Downloading analysis results

### Accessing zip members
