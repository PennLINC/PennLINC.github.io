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

Each of these steps is detailed here: 

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

As mentioned in our general [PMACS documentation](/docs/pmacs), you should scp *into* a node called `transfer`, for PMACS projects. That would look like this:

```
## my username is <username>
scp -r path/to/your/data <username>@transfer:/path/on/pmacs
```

An alternative to `scp` is `rsync`, but that tends to have [more happening under the hood](https://stackoverflow.com/questions/20244585/how-does-scp-differ-from-rsync).

## Flywheel

On Flywheel, your data may already be in BIDS. In this case we recommend using Flywheel's export function `fw export bids`, or the export function provided by [`fw-heudiconv`](https://fw-heudiconv.readthedocs.io/en/latest/). We built the export function into `fw-heudiconv` because we wanted to have more flexibility in what BIDS data we could grab, including data that's not yet supported in the official BIDS spec. Admittedly though, downloading all of `fw-heudiconv` a lot of overhead for just the export function.

```
# with fw export bids
fw export bids <DESTINATION_DIRECTORY> --project <PROJECT_NAME> --subject <SUBJECT_FILTER>

# with fw-heudiconv
fw-heudiconv-export --project <PROJECT_NAME> --subject <SUBJECTS_FILTER> --session <SESSION_FILTER> --folders <LIST_OF_BIDS_FOLDERS>
```

Try `fw-heudiconv-export -h` for more info.

## Globus

{: .warning-title }
> Warning
>
> This section has not been tested in a long time.
[Globus](https://www.globus.org/) is a research data management platform whose best feature is data transfer and sharing. It's surprisingly easy to use and gets the job done with minimal setup. The data sharing concept revolves around setting virtual *endpoints* that data can be shared to and from. Endpoints can be thought of conceptually as mounts, where you can give outbound network access to a certain directory on your machine or cluster, and by sharing the URL of your endpoint, someone can access your directory through the internet or network cluster.

Currently, the best way to use Globus is either through your local disk or on PMACs (recommended). We're still awaiting CUBIC authorization. The general docs for globus are located [here](https://docs.globus.org/how-to/), but for posterity, here are the best instructions:

On a local disk:

1. Log in to Globus with your UPenn organization account -- [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/) -- and try out the tutorial for sharing between two test endpoints on Globus' system
2. Download and install [Globus Connect Personal](https://www.globus.org/globus-connect-personal); this service will manage the endpoint on your local machine
3. Download and install the [CLI](https://docs.globus.org/cli/) with pip -- remember to use conda environments! This service will allow you to manage the Globus session when it's running
4. [Login with the CLI](https://docs.globus.org/cli/quickstart/) and transfer your data either through the CLI commands or by visiting the file manager (which you saw in step 1). If someone has shared a Globus endpoint with your account, you'll have access to it in "Endpoints".

On PMACs:

0. Make sure you have access to the PULSE Secure VPN -- [remote.pmacs.upenn.edu](remote.pmacs.upenn.edu)

1. Log in to PMACs' dedicated node for Globus functionality:

```
# first ssh into bblsub for network access
ssh -y <username>@bblsub

# then from there, log onto the globus node
ssh -y <username>@sciglobus
```

2. Globus Connect Personal should be available. As above, use it to initialize an endpoint on a directory of your choice on PMACs. Specifically, you should run it as below so that it opens a GUI for logging in with an auto-generated token:

```
# this command will return a URL you can open in any browser and a token you can use to sign in
globusconnect -start &
```

3. Using a new or existing conda environment (see [here](https://pennlinc.github.io/docs/pmacs#logging-in-to-pmacs-lpc) for how to activate conda on PMACs), install the [CLI](https://docs.globus.org/cli/) using `pip` and login with `globus login`.

4. Visit [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/) to access the File Manager, as in the Local Disk instructions, to start transferring data.


# Curating BIDS Datasets


BIDS curation can be a frustrating process. This guide describes best practices for
the curation process using a local filesystem. We divide this process into multiple
stages.


## Preparing your environment

If you are curating data on a Penn cluster, you will need to set up a conda
[environment](https://pennlinc.github.io/docs/cubic#installing-miniconda-in-your-project-the-hard-way) for your project. You will need to install [datalad](Datalad.md) and CuBIDS
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

[Download and install CuBIDS](https://bids-bond.readthedocs.io/en/latest/index.html). Note that this environment must be activated for the rest of the steps.

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

And remember, if you explicitly want to ignore something from tracking (with either `git` or `datalad`), add that path to a `.gitignore` file ([see here](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) and [here](https://handbook.datalad.org/en/latest/beyond_basics/101-179-gitignore.html)).

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
safe-keeping. One great option is to use the `bblsub` server
as a RIA store. You can push a copy of your original data to this store, then
push again when curation is complete. To create a RIA store on pmacs, be sure
you can log in using ssh key pairs from CUBIC.

```bash
(base) [yourname@cubic-login2 testing]$ ssh bblsub
Last login: Wed Mar 24 14:27:30 2021 from 
[yourname@bblsub ~]$
```

If the above does not work, set up SSH keys and edit `~/.ssh/config` until it does.
Once working, create a directory on `bblsub` that will hold your RIA store.

```bash
[yourname@bblsub ~]$ mkdir /project/myproject/datalad_ria
[yourname@bblsub ~]$ logout
```

and back on `CUBIC` add the store to your dataset

```bash
$ cd curation/
$ bids_remote=ria+ssh://bblsub:/project/myproject/datalad_ria
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

Congratulations! You have created a fully-curated BIDS dataset.

This data is typically stored on PMACS as BIDS datasets, transferred from CUBIC after curation via `rsync`. 



# Getting your data from PMACS to CUBIC
Data can be fetched back from PMACS, if needed, using the documentation specified [here](/docs/DataWorkflows/FetchingYourData.md). At the moment, all the data we have is already on PMACS and you will not need to curate any legacy data/ data that has already been collected a while back. These datasets and the links to fetch them are listed [here](./AvailableStaticData.md).

# Unzipping your data

Occasionally, data may be zipped. More information about this can be found [here](/PennLINC.github.io/docs/DataWorkflows/FetchingYourData.md)!

# Processing your data
[BABS](https://pennlinc-babs.readthedocs.io/en/latest/) is a quick and easy tool for processing pipelines via [Datalad](./Datalad.md). The documentation is thorough, with information on setting up, installing, and running BABS on data. An example walkthrough is also available via the documentation. 

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
rsync -avzhL --progress outputs FINAL_DESTINATION
```

---
NOTE FOR EXPERTS: This is part of the `datalad` workflow on _aliasing_; visit [http://handbook.datalad.org/en/latest/beyond_basics/101-147-riastores.html](this resource) to learn more about how you can use aliasing to share data flexibly.

---


## Permissions, VPNs, and Picking a Medium

There are always barriers to sharing data. Someone needs access to something and that often entails a lot of bureaucracy; maybe there is data that can't be shared with PHI; maybe there is not enough disk space to move data. Here are some thoughts to help you guide what decisions to make:

- Is this a one-time transaction, or will there be data moving back-and-forth repeatedly? VPNs + permissions are an investment that can take a week or sometimes more to be approved
- How big is the data? Does this _have to_ be shared on a cluster? Maybe it's more appropriate to download it locally and upload it to [Box](https://www.isc.upenn.edu/pennbox) or [SecureShare](https://www.isc.upenn.edu/security/secure-share)
- What clusters are involved? CUBIC has a complicated permissions system; PMACS is more lenient but how will you move data from CUBIC to PMACS?
- Do you need `datalad` tracking? How much do collaborators care about that (weighed against how much _you_ care about that)? `datalad` can be fun, but it is definitely a commitment that you can't easily back out of
