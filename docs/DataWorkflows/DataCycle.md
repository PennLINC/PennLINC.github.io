---
layout: default
title: Data Cycle
parent: Data Workflows
nav_order: 1
has_toc: true
---
# The Data Cycle

The data cycle includes the following steps: 
1. Fetching raw data
3. Dataset curation
2. Fetching the data onto the right cluster
3. Unzipping the data (as needed)
4. Processing the data!
5. Sharing the data

Steven Meisler's [BIDS workshop](https://www.stevenmeisler.com/bids_workshop/0_intro.html) provides a great tutorial covering the steps in the data cycle from BIDS curation to data processing. Each of these steps is detailed below: 

# Fetching Your Data
{: .no_toc}

There are a number of places you may have to fetch data from to get them onto a cluster filesystem. We will briefly cover best practices for the methods we've used before. Additions will be made as we gain more experience.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Between Clusters Or Local Disks

The best option for moving a large amount of data between clusters is to use the `scp` command. Remember that this process must remain open and running in your terminal, so it might be useful to do this in a fresh terminal window or use `&` at the end of your command. You could also use [`screen`](https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/) to set up a non-terminating terminal.

## Flywheel

On Flywheel, your data may already be in BIDS. In this case we recommend using Flywheel's export function `fw export bids`, or the export function provided by [`fw-heudiconv`](https://fw-heudiconv.readthedocs.io/en/latest/). We built the export function into `fw-heudiconv` because we wanted to have more flexibility in what BIDS data we could grab, including data that's not yet supported in the official BIDS spec. Admittedly though, downloading all of `fw-heudiconv` a lot of overhead for just the export function.

```
# with fw export bids
fw export bids <DESTINATION_DIRECTORY> --project <PROJECT_NAME> --subject <SUBJECT_FILTER>

# with fw-heudiconv
fw-heudiconv-export --project <PROJECT_NAME> --subject <SUBJECTS_FILTER> --session <SESSION_FILTER> --folders <LIST_OF_BIDS_FOLDERS>
```

Try `fw-heudiconv-export -h` for more info.

## Via datalad
You can `datalad clone` many relevant datasets, particularly via OpenNeuro. More information on this is available [here](https://handbook.datalad.org/en/latest/usecases/openneuro.html).


# Curating BIDS Datasets


BIDS curation can be a frustrating process. 
Please refer to our [CuBIDS documentation](https://cubids.readthedocs.io/en/latest/index.html), especially the [example walkthrough](https://cubids.readthedocs.io/en/latest/example.html).


## Preparing your environment

If you are curating data on a Penn cluster, you will need to set up a
[conda environment](https://pennlinc.github.io/docs/cubic#installing-miniforge-in-your-project) for your project.

You'll also need to install `deno` for the BIDS Validator:

```shell
conda install deno
```

After setting up your conda environment, please follow the CuBIDS installation instruction [here](https://cubids.readthedocs.io/en/latest/installation.html).

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

And remember, if you explicitly want to ignore something from tracking (with either `git` or `datalad`), add that path to a `.gitignore` file ([see here](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) and [here](https://handbook.datalad.org/en/latest/beyond_basics/101-179-gitignore.html)).

### Add NIfTI information to the sidecars

See [here](https://cubids.readthedocs.io/en/latest/example.html#adding-nifti-information-to-json-sidecars)

### Removing sensitive metadata

{: .warning-title }
> ⚠️ Important Note ⚠️
>
> This step must occur **BEFORE** any imaging data is checked in to datalad.

See [here](https://cubids.readthedocs.io/en/latest/example.html#identifying-and-removing-phi)

### Copying your Imaging Data

Now you can begin a datalad tracked dataset for your working BIDS data.

```bash
$ datalad create -c text2git BIDS
```

Finally, copy your data from `original_data` to the working BIDS dataset 
**only once you are certain `original_data/` is anonymized**:

```bash
cp -r original_data/* curation/BIDS
datalad save -m "add initial data" curation
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
can be found on the [CuBIDS documentation](https://cubids.readthedocs.io/en/latest/usage.html#more-definitions).


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

To detect acquisition groups in your data set, see [here](https://cubids.readthedocs.io/en/latest/example.html#visualizing-metadata-heterogeneity)

### Rename, merge or delete parameter groups

Relevant parties will then edit the summary csv
requesting new names for parameter groups as well as merging or deleting them
where appropriate. A description of how this process works can be found on
the [CuBIDS documentation](https://cubids.readthedocs.io/en/latest/example.html#visualizing-metadata-heterogeneity)

See below for examples of cross sections of a cubids-group csv:

[Pre-apply](https://github.com/PennLINC/RBC/tree/master/PennLINC/HRC_BIDS_Fix/HRC_pre_apply)
[Post-apply](https://github.com/PennLINC/RBC/tree/master/PennLINC/HRC_BIDS_Fix/HRC_post_apply)

Once the edited CSV is ready, the merges, renamings and deletions can be
applied to your BIDS data. See [here](https://cubids.readthedocs.io/en/latest/example.html#applying-changes).

Once you are satisfied with your key/parameter groups, be sure to re-run
`cubids validate` to make sure you haven't introduced any BIDS-incompatible
names.

Congratulations! You have created a fully-curated BIDS dataset.

This data is typically stored on PMACS as BIDS datasets, transferred from CUBIC after curation via `rsync`. 



# Getting your data from PMACS to CUBIC
Data can be fetched back from PMACS, if needed, using the documentation specified [here](/docs/DataWorkflows/FetchingYourPMACSData.md). At the moment, all the data we have is already on PMACS and you will not need to curate any legacy data/ data that has already been collected a while back. These datasets and the links to fetch them are listed [here](./AvailableStaticData.md).

# Unzipping your data

Occasionally, data may be zipped. More information about this can be found [here](/PennLINC.github.io/docs/DataWorkflows/FetchingYourPMACSData.md)!

# Processing your data
[BABS](https://pennlinc-babs.readthedocs.io/en/latest/) is a quick and easy tool for processing pipelines via [Datalad](./Datalad.md). The documentation is thorough, with information on setting up, installing, and running BABS on data. An example walkthrough is also available via the documentation.

If you run a pipeline that cannot be implemented via BABS, but still want to use `datalad` please review [this link](https://pennlinc.github.io/docs/Archive/TheWay/RunningDataLadPipelines/).

# Sharing your data
{: .no_toc}

Collaboration is an important part of our work. Sharing the input data and outputs/derivatives of a project is a critical step in the scientific process, and so doing it both accurately and efficiently is a high priority. Overall, remember that this step can be a strain, especially when dealing with external collaborators or systems that are foreign to you. Be patient, and remember that we have to balance accuracy/reproducibility with efficiency/speed.

Below are a few example scenarios and what best recommendations we have for sharing data, particularly outputs from BABS

## Datalad to Datalad
Generally, if you have outputs from BABS in a `datalad` dataset, you should try to have collaborators ingest that as `datalad` datasets too! This is best accomplished if the user can `clone` the dataset:

```shell
#cloning a dataset from a git repo

datalad clone https://github.com/datalad-datasets/longnow-podcasts.git
```

For most of our use, you want to clone the _output_ of a specific pipeline -- these outputs are stored in the _output RIA store_, so you have to clone them like so:

```shell
#cloning from an output ria of an fmriprep run
datalad clone ria+file:///PATH_TO_DATASET/output_ria#~data outputs
```

If the person is happy with this format and working with `datalad`, they can use this command to get the cloned data. 

## Datalad to Non-Datalad

If they want regular files with no `datalad` tracking involved, they can then use `rsync` to copy the physical data by following the symbolic links. That looks like this:

```shell
# YOU clone from an output ria of an fmriprep run
datalad clone ria+file:///PATH_TO_DATASET/output_ria#~data outputs
datalad get .

# THEY extract the data from this output RIA as regular files
rsync -avzh --progress outputs FINAL_DESTINATION
```

## Datalad to OpenNeuro

Data can be transferred via Datalad to OpenNeuro, following [these](https://docs.openneuro.org/packages/openneuro-cli.html) steps. 
