---
layout: default
title: Curating BIDS Datasets
parent: The Way
nav_order: 2
has_toc: true
---

# Curating BIDS Datasets
{: .no_toc }

BIDS curation can be a frustrating process. This guide describes best practices for
the curation process using a local filesystem. We divide this process into multiple
stages.



* TOC
{:toc}

## Preparing your environment

If you are curating data on a Penn cluster, you will need to set up a conda
environment for your project. For information on how to set up conda
on each clustess [instructions for CUBIC]() and
[instructions for PMACS](). You will need to install datalad and CuBIDS
for the rest of the steps in this workflow. To do so, create a conda
environment.

If you've already got `conda` setup for environment management, please skip this
step and instead directly download `CuBIDS` [here](https://bids-bond.readthedocs.io/en/latest/). After that, you can head over to _Stage 0_.

Otherwise, the easiest way to get your CUBIC project user started is to download
the project initialization script.  Immediately upon getting access to
your project, log in as the project user and run:

```shell
$ wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/cubic-setup-project-user.sh
$ bash cubic-setup-project-user.sh ${HOME}
```

[Download and install CuBIDS](https://bids-bond.readthedocs.io/en/latest/index.html). Note that
this environment must be activated for the rest of the steps.

You'll also need to install BIDS Validator:

```shell
$ conda install nodejs
$ npm install -g bids-validator
$ which bids-validator #to make sure it installed
```

## Stage 0: Organization

The process begins when data arrives on one of our servers. While it may not
be possible to document everything that has happened to the data prior to its
arrival to our server, the goal of the organization step is to document as
much as we can about the process of receiving the data, and any initial
changes we might make to it. The person in charge of organizing a data set
should document any changes they make in a *Data Narrative* along with any
relevant scripts used to a git-tracked repository.

Create a project root directory. Initially we suggest keeping one copy of your
initial data that will remain untouched as a backup during early stages of
the workflow. This is not necessary if your data is archived elsewhere online.
In the project root create a directory structure similar to this:

```
# the actual directory structure can
# vary depending on the needs of your project

project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
└── curation
    ├── code
    |   ├── sandbox                # a place for untracked files
    │   └── ProjectGithub          # the home for all your scripts, tracked by github
    |       └── DataNarrative.md   # the data narrative file
    └── BIDS
```

The `original_data` directory should be an unchanged copy of the original data. You can
get a template Data Narrative file with:

```shell
$ wget https://raw.githubusercontent.com/PennLINC/RBC/master/Data_Narrative_Template.md
```

Next, add tracking to your project for scripts to be shared and tracked. 
data:

```
project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
└── curation
    ├── code
    |   ├── sandbox
    │   └── ProjectGithub         # add git here
    |       └── DataNarrative.md
    └── BIDS
```

You can add git like so:

```bash
$ git init
```

And remember, if you explicitly want to ignore something from tracking (with either `git` or `datalad`), add that path to a `.gitnignore` file ([see here](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) and [here](https://handbook.datalad.org/en/latest/beyond_basics/101-179-gitignore.html)).

### Add NIfTI information to the sidecars

Image files (NIfTI) are large binary files that contain information about
the spatial coverage of MRI images. We want to be able to detect variability
in this, but don't necessarily want to always be reading it from NIfTI files.
For example, the nifti files may be checked in to git annex or stored on
a remote server. These are somewhat common use cases, so we recommend
adding the information you would normally get from NIfTI files directly
to the JSON files. CuBIDS comes with a NIfTI metadata extractor, which
can be run with

```bash
$ cubids-add-nifti-info ~/project/original_data
```

Once run, you will find volume, dimension, and obliquity information in the JSON sidecars.

### Removing sensitive metadata

> ⚠️ NOTE: This step must occur **BEFORE** any imaging data is checked in to datalad.

Sometimes the DICOM-to-NIfTI conversion process results in unwanted information
in the JSON sidecars. You can use `cubids-remove-metadata-fields` to purge these
from all .json files in your data. All unique metadata fields can be listed
using `cubids-print-metadata-fields`.Be sure to note the fields you removed in
your *Data Narrative*.

```markdown
Sensitive fields, included in: AccessionNumber, PatientBirthDate, PatientID,
PatientName, PatientSex, AcquisitionDateTime, SeriesInstanceUID,
DeviceSerialNumber, InstitutionAddress, AcquisitionTime, StationName,
ReferringPhysicianName, InstitutionName, InstitutionalDepartmentName,
AccessionNumber were removed from all metadata files using
`cubids-remove-metadata-fields`.
```
### Copying your Imaging Data

Now you can begin a datalad tracked dataset for your working BIDS data.

```bash
$ datalad create -c text2git BIDS
```

Finally, copy your data from `original_data` to the working BIDS dataset 
**only once you are certain `original_data/` is anonymized**:

```bash
$ cp -r original_data/* curation/BIDS
$ datalad save -m "add initial data" curation
```

This could take some time depending on how big your input data is. The result will look like this:

```
project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
└── curation
    ├── code
    |   ├── sandbox
    │   └── ProjectGithub
    |       └── DataNarrative.md
    └── BIDS                      # BIDS data added
        ├── dataset_description.json
        ├── README.txt
        ├── sub-1
        ├── sub-2
        ├── ...
        └── sub-N
```

Admittedly, `cp` can be a time consuming process for very large BIDS datasets — we have a solution (currently available on PMACS) for a much quicker copy using bootstrapped `datalad` [here](https://github.com/PennLINC/TheWay/blob/main/scripts/pmacs/bootstrap-bids-dataladdening.sh).

### OPTIONAL: set up a remote backup

At this point you may want to back up this data on a separate server for
safe-keeping. One great option is to use the `sciget` server
as a RIA store. You can push a copy of your original data to this store, then
push again when curation is complete. To create a RIA store on pmacs, be sure
you can log in using ssh key pairs from CUBIC.

```bash
(base) [yourname@cubic-login2 testing]$ ssh sciget
Last login: Wed Mar 24 14:27:30 2021 from 
[yourname@sciget ~]$
```

If the above does not work, set up SSH keys and edit `~/.ssh/config` until it does.
Once working, create a directory on `sciget` that will hold your RIA store.

```bash
[yourname@sciget ~]$ mkdir /project/myproject/datalad_ria
[yourname@sciget ~]$ logout
```

and back on `CUBIC` add the store to your dataset

```bash
$ cd curation/
$ bids_remote=ria+ssh://sciget:/project/myproject/datalad_ria
$ ds_id=$(datalad -f '{infos[dataset][id]}' wtf -S dataset)
$ bids_ria_url="${bids_remote}#${dsi_id}"
$ datalad create-sibling-ria -s pmacs-ria ${bids_ria_url}
$ datalad push --to pmacs-ria

```

If these succeed, you will have a completely backed-up copy of your original
data and scripts that you can push to and pull from as you work. If you want
to work on a temporary copy of the data, you can clone it anywhere:

```bash
$ cd /tmp
$ datalad clone ${bids_ria_url} curation
$ cd curation
$ git annex dead here
```

And `/tmp/curation` will have all files on demand from the original repository.

### Documenting data provenance

As mentioned, we document the process of curating and preprocessing a dataset with a Data Narrative.

Here's a template data narrative; you'll fill out the fields as necessary for your project:

```markdown
# Data Narrative for [INSERT DATASET NAME HERE]

## Important Links (should all be on GitHub):
* Data Processing Flow Diagram:
   * Flow diagram that describes the lifecycle of this dataset 
* DSR GitHub Project Page(Curation/Validation and Processing Queue Status):
   * Cards for tracking the curation and validation portion of the dataset. This page should be updated every time you perform an action on the data. 
   * Cards for tracking the progress of containerized pipeline runs on the data. 
   
## Plan for the Data 

* Why does PennLINC need this data?
* For which project(s) is it intended? Please link to project pages below:
* What is our goal data format?
   * i.e. in what form do we want the data by the end of the "Curation" step? BIDS? Something else? 

## Data Acquisition

* Who is responsible for acquiring this data?
* Do you have a DUA? Who is allowed to access the data?
* Where was the data acquired? 
* Describe the data. What type of information do we have? Things to specify include:
   * number of subjects
   * types of images
   * demographic data
   * clinical/cognitive data
   * any canned QC data
   * any preprocessed or derived data

## Download and Storage 

* Who is responsible for downloading this data?
* From where was the data downloaded?
* Where is it currently being stored?
* What form is the data in upon intial download (DICOMS, NIFTIS, something else?)
* Are you using Datalad? 
* Is the data backed up in a second location? If so, please provide the path to the backup location:

## Curation Process

* Who is responsible for curating this data?
* GitHub Link to curation scripts/heurstics: 
* GitHub Link to final CuBIDS csvs: 
* Describe the Validation Process. Include a list of the initial and final errors and warnings.
* Describe additions, deletions, and metadata changes (if any).

## Preprocessing Pipelines 
* For each pipeline (e.g. QSIPrep, fMRIPrep, XCP, C-PAC), please fill out the following information:
   * Pipeline Name: 
   * Who is responsible for running preprocessing pipelines/audits on this data?
   * Where are you running these pipelines? CUBIC? PMACS? Somewhere else?
   * Did you implement exemplar testing? If so, please fill out the information below:
      * Path to exemplar dataset:
      * Path to exemplar outputs:
      * GitHub Link to exemplar audit:
    * For production testing, please fill out the information below:
      * Path to production inputs:
      * GitHub Link to production outputs:
      * GitHub Link to production audit: 

## Post Processing 

* Who is using the data/for which projects are people in the lab using this data?
   * Link to project page(s) here  
* For each post-processing analysis that has been run on this data, fill out the following
   * Who performed the analysis?
   * Where it was performed (CUBIC, PMACS, somewhere else)?
   * GitHub Link(s) to result(s)
   * Did you use pennlinckit?  
      * https://github.com/PennLINC/PennLINC-Kit/tree/main/pennlinckit  
```

## Stage 1: BIDS Validation

At the end of Step 0 you should have a BIDS-like data set containing NIfTI
and JSON files, tracked by datalad, and a regular git repository tracking the
scripts you create to curate it. 
The goal of this stage is to get your data passing the
BIDS Validator without any errors and to ensure all scans in your dataset
appear as expected and are usable. This is an iterative process - fixing
one error may introduce new errors. Expect this step to take a number of
iterations and be sure to describe each step in your Data Narrative. In
order to do this, we recommend running `cubids-group` and `cubids-validate`
simultaneously, via a `qsub` (if the dataset is large) after every change.
Suppose you ran `cubids-validate` on your BIDS data. This will create
a file containing all the errors present in your data. Add this file
to your git repository and describe it in the Data Narrative (you can simply add the content below to the bottom of DataNarrative.md):

```markdown
# BIDS Validation

Upon first run of the validator, we found [N] errors:

[ERROR CODE1 + SHORTHAND DESCRIPTION1]: [NUMBER OF SUBJECTS WITH ERROR1]
[ERROR CODE2 + SHORTHAND DESCRIPTION2]: [NUMBER OF SUBJECTS WITH ERROR2]
[ERROR CODEn + SHORTHAND DESCRIPTIONn]: [NUMBER OF SUBJECTS WITH ERRORn]
[GITHUB URL TO VALIDATOR OUTPUT AT DATE OF COMMIT]
```

For example, this might look like:

```markdown
Code 39 (Inconsistent Parameters): 15 subjects
Code 86 (Suspiciously Short Event Design): 136 subjects
Commit:
https://github.com/PennLINC/RBC/blob/3dd4e931cc96f7f74512c57b86ede30735ef9252/PennLINC/Validation/Merging.ipynb

We attempted to iteratively remove each of these errors in [GITHUB URL TO
NOTEBOOK/SCRIPT]. Specifically, [SCRIPT URL] was used to solve code [ERROR
CODEn].

```

If there is no restriction on sharing subject/session IDs with Github, the validator
outputs and scripts for changes can be stored in the Github tracked directory;
otherwise they can be placed in a `.gitignore` file or in the `sandbox`:

```
project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
└── curation
    ├── code
    |   ├── sandbox
    │   └── ProjectGithub
    |       ├── validator_outputs  # Put validator outputs here
    |       ├── notebooks          # e.g. ipython notebooks that investigate BIDS data
    |       ├── Fix1.sh            # e.g. a script that renamed some BIDS data
    |       └── DataNarrative.md
    └── BIDS                      
        ├── dataset_description.json
        ├── README.txt
        ├── sub-1
        ├── sub-2
        ├── ...
        └── sub-N
```

After re-running `cubids-group` and `cubids-validate`, you may find new errors. In this case, write more scripts
that fix the errors and describe them in the *Data Narrative*

```markdown
After re-running the validator on [APPROX DATE], we found a further [N] errors:

[ERROR CODEn + SHORTHAND DESCRIPTIONn]: [NUMBER OF SUBJECTS WITH ERRORn]
[GITHUB URL TO VALIDATOR OUTPUT AT DATE OF COMMIT]

We solved this error with  [GITHUB URL TO NOTEBOOK/SCRIPT].

```

Eventually you will have fixed all the problems and achieved BIDS compliance.
Note this victory in your *Data Narrative*:

```markdown
We were satisfied with curation in/on [APPROX LAST DATE OF CURATION]. The
last BIDS validator output is available [GITHUB URL TO VALIDATOR OUTPUT AT
DATE OF COMMIT], after which data was checked into datalad and backed up to
[CLUSTER/DIRECTORY]. The datalad commit was [SHASUM of datalad commit].

```

## Stage 2: BIDS Optimization

> BIDS is a file naming and metadata specification - what's there to optimize?

We found that it's difficult to come up with BIDS file names that accurately
represent both what a file contains and how its acquisition is different
from similar images.

Consider the case where someone created a BIDS data set using heudiconv.
It's common for a heudiconv heuristic to rely on a simple field like
`ProtocolName`, which is defined by the scanner technician. The technician
can use the same protocol name (eg "task1BOLD") because a scan was a
BOLD acquisition during which the subject performed "task1". Suppose
a scanner upgrade occurred or a fancy new sequence became available
that changed the `MultibandAccelerationFactor` from 1 to 4. The
`ProtocolName` may still be "task1BOLD" since the image will still
contain BOLD collected as the participant performed task1, but the
signal will be very different. Without changes to the heuristic,
both acquisitions would result in `sub-X_task-1_bold` as the
BIDS name.

`CuBIDS` provides a utility that finds variations in important imaging
parameters within each BIDS *key group*. In our example there might
be two unique *parameter groups* that map to the same *key group* of
`sub-X_task-1_bold`: one with `MultibandAccelerationFactor` 1 and
the other 4. A complete description of key and parameter groups
can be found on the [CuBIDS documentation](https://bids-bond.readthedocs.io/en/latest/usage.html#definitions).


### Find unique acquisition groups

`CuBIDS` reads and writes CSV files during the grouping process. You should create an
`iterations/` directory in `working/code` to store these CSVs and so they can be
tracked in git. Your project should look like:

```
project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
└── curation
    ├── code
    |   ├── sandbox
    │   └── ProjectGithub
    |       ├── validator_outputs  # Put validator outputs here
    |       ├── notebooks          # e.g. ipython notebooks that investigate BIDS data
    |       ├── Fix1.sh            # e.g. a script that renamed some BIDS data
    |       └── DataNarrative.md
    └── BIDS                      
        ├── dataset_description.json
        ├── README.txt
        ├── sub-1
        ├── sub-2
        ├── ...
        └── sub-N
```

To detect acquisition groups in your data set, change into `working/` and run

```shell
$ cubids-group BIDS code/iterations/iter0
```

This command will write four CuBIDS files delineating key/param groups and
acquisition groups.

### Rename, merge or delete parameter groups

Relevant parties will then edit the summary csv
requesting new names for parameter groups as well as merging or deleting them
where appropriate. A description of how this process works can be found on
the [CuBIDS documentation](https://bids-bond.readthedocs.io/en/latest/usage.html#modifying-key-and-parameter-group-assignments)
[//]: #

See below for examples of cross sections of a cubids-group csv:

[Pre-apply](https://github.com/PennLINC/RBC/tree/master/PennLINC/HRC_BIDS_Fix/HRC_pre_apply)
[Post-apply](https://github.com/PennLINC/RBC/tree/master/PennLINC/HRC_BIDS_Fix/HRC_post_apply)

Once the edited CSV is ready, the merges, renamings and deletions can be
applied to your BIDS data. Again from `working/`, if you're not using
datalad at this point, run

```shell
$ cubids-apply \
    BIDS \
    code/iterations/iter0_summary.csv \
    code/iterations/iter0_files.csv \
    code/iterations/apply1
```

If using datalad, be sure to include `--use-datalad` as the first argument to
`cubids-apply`. If not using Datalad, be sure to add to your *Data Narrative*
so you know that CuBIDS was used to change your data. Describe any major
renaming, deleting or merging of parameter groups.

New parameter groups will be described in `code/iterations/apply1*.csv` and you
should make sure your data was changed as intended.

Once you are satisfied with your key/parameter groups, be sure to re-run
`cubids-validate` to make sure you haven't introduced any BIDS-incompatible
names.


## Stage 3: Preprocessing Pipelines with Datalad

This stage includes two distinct parts. The first is a final check that your
BIDS curation is sufficient for correctly running BIDS Apps on your data. The
second stage is running those BIDS Apps for real. The exemplar subject test
and the full cohort run follow the exact same steps, just using different
data as inputs.

### Testing pipelines on example subjects

Each subject belongs to one Acquisition group. Since all subjects in an
acquisition group will be processed the same way in the \*preps, you only
need to test one subject per acquisition group. We will need to add some
directories to our project for the outputs of each test.

The process of testing exemplar subjects is identical to the process of
running pipelines on entire BIDS datasets. Instead of passing the entire
BIDS dataset, we extract a single subject from each acquisition group
into a smaller, representative BIDS dataset. This directory then serves as input to
[the pipeline](/docs/TheWay/RunningDataLadPipelines#preparing-the-analysis-dataset).

Create a testing directory from the root of your project, and within that directory, create a BIDS directory of only exemplar subjects into its BIDS
subdataset. Use the CuBIDS program `cubids-copy-exemplars`:

```bash
$ cubids-copy-exemplars \
    BIDS \
    exemplars_dir \
    code/iterations/iter1_AcqGrouping.csv
```

This will create `exemplars_dir`, which is a new BIDS-valid dataset containing one
subject per acquisition group. You will want to test each of these subjects with
each pipeline to ensure that they are processed correctly.

Before using the `exemplars_dir` as input to the pipelines, initialize it
as a Datalad dataset.

```bash
$ cd exemplars_dir
$ datalad create -d . --force -D "Exemplars BIDS dataset"
$ datalad save -m "add input data"
$ cd ..
```

At this point, your project should look like this:

```
project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
├── curation
│   ├── code
│   |   ├── sandbox
│   │   └── ProjectGithub
│   |       ├── validator_outputs
│   |       ├── notebooks
│   |       ├── Fix1.sh
│   |       └── DataNarrative.md
│   └── BIDS                      
│       ├── dataset_description.json
│       ├── README.txt
│       ├── sub-1
│       ├── sub-2
│       ├── ...
│       └── sub-N
└── testing                     # new testing directory
    ├── exemplars_dir           # BIDS directory of exemplars you'll be testing
    |   ├── dataset_description.json
    │   ├── README.txt
    │   ├── sub-1
    │   ├── sub-2
    │   ├── ...
    │   └── sub-N
    └── exemplar_test           # directory for testing scripts
```

Now you can bootstrap a pipeline run with these as your inputs. Go to the next section [here](/docs/TheWay/RunningDataLadPipelines/) to learn more.

If you have any trouble with your exemplar testing, such as needing to adjust your exemplars, simply remove the testing `exemplars_dir` and begin again from there.
