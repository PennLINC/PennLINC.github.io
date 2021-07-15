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

If curating data on a Penn cluster, you will need to set up a conda
environment for your project. For information on how to set up conda
on each clustess [instructions for CUBIC]() and
[instructions for PMACS](). You will need to install datalad and CuBIDS
for the rest of the steps in this workflow. To do so, create a conda
environment.

The easiest way to get your CUBIC project user started is to download
the project initialization script. Immediately upon getting access to
your project, log in as the project user and run:

```shell
$ wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/cubic-setup-project-user.sh
$ bash cubic-setup-project-user.sh ${HOME}
```

Finally, [download and install CuBIDS](linktocubids.html). Note that
this environment must be activated for the rest of the steps.


## Stage 0: Organization

The process begins when data arrives on one of our servers. While it may not
be possible to document everything that has happened to the data prior to its
arrival to our server, the goal of the organization step is to document as
much as we can about the process of receiving the data and any initial
changes we might make to it. The person in charge of organizing a data set
should document any changes they make in a *Data Narrative* along with any
relevant scripts used to a git-tracked repository.

Create a project root directory. Initially we suggest keeping one copy of your
initial data that will remain untouched as a backup during early stages of
the workflow. This is not necessary if your data is archived elsewhere online.
In the project root consider something like

```
project
├── original_data
│   ├── sub-1
│   ├── sub-2
│   ├── ...
│   └── sub-N
└── curation
    ├── code
    │   ├── DataNarrative.md
    │   ├── Fix1.sh
    │   └── Fix2.sh
    └── BIDS
        ├── dataset_description.json
        ├── README.txt
        ├── sub-1
        ├── sub-2
        ├── ...
        └── sub-N
```

The `original_data` directory should be an unchanged copy of the original data.

Next, create a curation dataset that will track the changes made to your original
data. From the same directory as your `original_data/` directory, you can setup a
datalad bids curation dataset like so

```bash
$ datalad create -c yoda curation
```

If there is potentially sensitive metadata in your `original_data
is impossible, you can [remove sensitive metadata](#removing-sensitive-metadata)
before copying the contents of your `original_data/` directory into your
`curation/BIDS/` directory. **Once you are certain `original_data/` is anonymized**
you can copy it into `curation/BIDS/` and save it as a datalad dataset.

```bash
$ cp -r original_data/* curation/BIDS
$ datalad save -m "add initial data" curation
```

This could take some time depending on how big your input data is.

### OPTIONAL: set up a remote backup

At this point you may want to back up this data on a separate server for
safe-keeping. One great option is to use the `sciget.pmacs.upenn.edu` server
as a RIA store. You can push a copy of your original data to this store, then
push again when curation is complete. To create a RIA store on pmacs, be sure
you can log in using ssh key pairs from CUBIC.

```bash
(base) [yourname@cubic-login2 testing]$ ssh sciget.pmacs.upenn.edu
Last login: Wed Mar 24 14:27:30 2021 from 170.212.0.164
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
$ bids_remote=ria+ssh://sciget.pmacs.upenn.edu:/project/myproject/datalad_ria
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

The *Data Narrative* should begin with a section describing where the data
came from.

```markdown
# Transfer Process

The data were acquired at [SITE] as part of [STUDY] study. Access was given
to PennLINC as part of the [COLLABORATION/GRANT] project. The data was
transferred from [SITE] to [PennLINC CLUSTER] using [TOOLS & SOFTWARE +
VERSIONS]. The approximate date of transfer was [DATE RANGE]. In sum,
PennLINC received [APPROX VOLUME OF DATA] comprising of [N] subjects with a
range of [N] sessions. The imaging data consisted of [MODALITIES].
Additionally, [ANY ADDITIONAL CLINICAL OR COHORT DATA]. The imaging data was
organised [IN BIDS/NOT IN BIDS] and [ANONYMIZED/NOT ANONYMIZED] at the time
of transfer, and the raw data was stored in [DIRECTORY ON THE CLUSTER] and
tracked on [GITHUB].
```

Where the fields in brackets are replaced by your specific information.

### Documenting initial steps taken

Files with clearly non-BIDS-compliant names, unnecessary data and any sensitive
information should be removed as soon as possible. Each of these steps should be
documented in the *Data Narrative* like so:

```markdown
# Initial Steps

The initial data contained localizer scans that will not be used. These files
were removed using [curation_code/delete_localizers.sh](link_to_script_on_github).
```

Any other scripts applied at this stage should be noted here, including both
their path in the git repository and a description of the action they
implement.

### Removing sensitive metadata

> ⚠️ NOTE: This step must occur **BEFORE** data is checked in to datalad.

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

You can check your data into datalad any time after you've removed all
sensitive metadata fields.


## Stage 1: BIDS Validation

At the end of Step 0 you should have a BIDS-like data set containing NIfTI
and JSON files. The goal of this stage is to get your data passing the
BIDS Validator without any errors. This is an iterative process - fixing
one error may introduce new errors. Expect this step to take a number of
iterations and be sure to describe each step in your *Data Narrative*.

Suppose you ran `cubids-validate` on your BIDS data. This will create
a file containing all the errors present in your data. Add this file
to your git repository and describe it in the *Data Narrative*:

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

After re-running the validator you may find new errors. In this case, write more scripts
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

CuBIDS provides a utility that finds variations in important imaging
parameters within each BIDS *name group*. In our example there might
be two unique *parameter groups* that map to the same *name group* of
`sub-X_task-1_bold`: one with `MultibandAccelerationFactor` 1 and
the other 4. A complete description of name and parameter groups
can be found on the [CuBIDS documentation](https://bids-bond.readthedocs.io/en/latest/usage.html#definitions).

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
$ cubids-add-nifti-info dataset_path
```

Once run, you will find volume information in the JSON sidecars.

### Find unique acquisition groups

CuBIDS reads and writes CSV files during the grouping process. You should create an
`iterations/` directory in `working/code` to store these CSVs and so they can be
tracked in git. Your project should look like

```
project
├── original_data
└── working
    ├── code
    │   ├── DataNarrative.md
    │   ├── iterations
    │   ├── Fix1.sh
    │   └── Fix2.sh
    └── BIDS
```

To detect acquisition groups in your data set, change into `working/` and run

```shell
$ cubids-group BIDS code/iterations/iter0
```

This command will write four CuBIDS files delineating name/param groups and
acquisition groups.

### Rename, merge or delete parameter groups

Relevant parties will then edit the summary csv
requesting new names for parameter groups as well as merging or deleting them
where appropriate. A description of how this process works can be found on
the [CuBIDS documentation](https://bids-bond.readthedocs.io/en/latest/usage.html#modifying-key-and-parameter-group-assignments)
[//]: # (Sydney, could you add the actual csv names in a tree printout?)

Once the edited CSV is ready, the merges, renamings and deletions can be
applied to your BIDS data. Again from `working/`, if you're not using
datalad at this point, run

```shell
$ cubids-apply \
    BIDS \
    code/iterations/iter0_summary.csv \
    code/iterations/iter0_files.csv \
    code/iterations/iter1
```

If using datalad, be sure to include `--use-datalad` as the first argument to
`cubids-apply`. If not using Datalad, be sure to add to your *Data Narrative*
so you know that CuBIDS was used to change your data. Describe any major
renaming, deleting or merging of parameter groups.

New parameter groups will be described in `code/iterations/iter1*.csv` and you
should make sure your data was changed as intended.

Once you are satisfied with your name/parameter groups, be sure to re-run
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

To create a testing directory of only exemplar subjects into its BIDS
subdataset, use the CuBIDS program `cubids-copy-exemplars`

```bash
$ cubids-copy-exemplars \
    BIDS \
    exemplars_dir \
    code/iterations/iter1_AcqGrouping.csv
```

this will create `exemplars_dir`, which is a new BIDS-valid dataset containing one
subject per acquisition group. You will want to test each of these subjects with
each pipeline to ensure that they are processed correctly.

Before using the `exemplars_dir` as input to the pipelines, initialize it
as a Datalad dataset.

```bash
$ cd exemplars_dir
$ datalad create -d . --force -D "Exemplars BIDS dataset"
$ datalad save -m "add input data"
$ datalad run-procedure cfg_text2git
$ cd ..
```
**Note:** If you have created the exemplars_dir inside an existing datalad dataset, don't f
orget to also `datalad save` the superdataset that exemplars_dir belongs to. 

Now you can bootstrap a pipeline run with these as your inputs. You want to create this 
exemplar_test directory somewhere outside of your superdataset (i.e. not inside a folder 
that is already indexed by Datalad). Supposing fmriprep is the pipeline we want to test:

```bash
$ cd </desired/location/of/exemplar_test/directory/>
$ mkdir exemplar_test && cd exemplar_test
$ wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/bootstrap-fmriprep.sh
$ bash bootstrap-fmriprep.sh <path/to/exemplars_dir>
$ cd fmriprep/anaysis/
$ bash code/qsub_calls.sh
```

This will link the exemplars BIDS dataset into an fmriprep analysis dataset and
launch jobs for each exemplar subject. 

**Note:** If your dataset happens to include multiple sessions per subject, you would
instead use a different script:

```bash
$ cd </desired/location/of/exemplar_test/directory/>
$ mkdir exemplar_test && cd exemplar_test
$ wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/bootstrap-fmriprep-multises.sh
$ bash bootstrap-fmriprep-multises.sh <path/to/exemplars_dir>
$ cd fmriprep/anaysis/
$ bash code/qsub_calls.sh
```

You can check how your jobs are doing by looking at individual log files, which are
stored in `fmriprep/anaysis/logs/`

**Note:** If for some reason you need to edit the `qsub_calls.sh` script, you must
be sure to register the changes with datalad and push to siblings before rerunning the 
script. From within `fmriprep/anaysis/`:

```bash
datalad save
datalad push --to input
datalad push --to output
```

Follow the instructions in
[here](/docs/TheWay/RunningDataLadPipelines#preparing-the-analysis-dataset)
for aggregating and checking the results. Note that a nearly identical
workflow will be used for running the entire BIDS dataset through pipelines.



### Checking outputs from your exemplar subjects

The `fmriprep` or `qsiprep` directory in your `working/testing` directory
will have branches for each of your test subjects. To see if pipelines worked
as you anticipated, run a completeness check on the derivatives from
`working/`:

```shell
$ cubids-derivatives-check testing code/iterations
```

If you found that some Acquisition groups need to have their BIDS data
changed to work properly in the pipelines, return to [Stage 2](#stage-2-bids-optimization)
