---
layout: default
title: Running Pipelines with DataLad
parent: The Way
nav_order: 3
has_toc: true
---

# Running Bids App pipelines
{: .no_toc }

In general, we will need to apply an image processing workflow to the raw
data we've
[curated in BIDS](/docs/TheWay/CuratingBIDSonDisk#curating-bids-datasets).
This workflow is essentially the same for any of the preps, including
fMRIPrep, QSIPrep, c-PAC and ASLPrep. In this section we show how to create an
*analysis dataset* that contains the prep containers, the provenance of the
prep runs, and the prep outputs. Then, we'll demonstrate how to run pipelines on
your exemplars (and eventually the full dataset) using the "bootstrap" method.


* TOC
{:toc}

## Preparing your containers

---
Note:
On CUBIC, the RBC user can't build singularity images. You should build the
container as your personal user and copy it to /cbica/projects/RBC/dropbox.

---


Here, for example, we build a qsiprep image:
```bash
singularity build qsiprep-0.14.2.sif docker://pennbbl/qsiprep:0.14.2
```

This image needs to be added to a datalad "containers dataset". Be sure you've installed
the datalad containers plugin via `pip install datalad_container`. Now create the
dataset:

```bash
$ datalad create -D "Note about the container" qsiprep-container
$ cd qsiprep-container
$ datalad containers-add --url /full/path/to/qsiprep-0.14.2.sif qsiprep-0-14-2
```

Note the last argument is the *image ID* in the datalad container dataset. This string
can only have characters and dashes in it. Remember what you assign as the *image ID* because
you will need to add it to your scripts later.

Lastly, you've copied the sif file into `qsiprep-container/` so you can delete the original
sif file:

```bash
$ rm /full/path/to/qsiprep-0.14.2.sif
```

## Preparing the analysis dataset

We assume your BIDS data is curated and available either on your local file system
or a remote datalad source. We're going to "bootstrap" the process of both
creating the analysis dataset, and running a pipeline on each subject. The 
word “bootstrap” can be thought of as a term for "set up a pipeline to
datalad-clone each participant to a temporary working space, process 
each participant with a reproducible/tracked datalad-run command,
and safely merge the outputs together in the user’s project”.


You can [download](https://github.com/PennLINC/TheWay/tree/main/scripts/cubic) and run one or more of our "bootstrap setup" scripts that sets up a
working directory for the running of your pipeline. Set the `BIDSAPP` variable
to the lowercase version of the pipeline you'd like to run.

Different bootstrap scripts require different argmuents. For BIDSApps, the arguments are

  1. The datalad-interpretable path to your BIDS dataset. Examples may be ria+ssh://, ria+file://,
     https:// or a path to a local datalad-enabled directory containing BIDS data. If a local path, `/full/path/to/BIDS` should be the directory that contains the `sub-` directories as children (one level of depth) and **must** be a datalad dataset.
  2. The path to the container dataset you created in the previous step.

---
**NOTE:** Both arguments must be *absolute paths* and *cannot contain a trailing /*.

---

Here we "bash the bootstrap" to create a `qsiprep` directory:

```bash
$ BIDSAPP=qsiprep
$ wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/bootstrap-${BIDSAPP}.sh
$ bash bootstrap-${BIDSAPP}.sh /full/path/to/BIDS /full/path/to/qsiprep-container
```

This will create a `qsiprep` directory that contains numerous other
directories needed to run the app at scale.

---
### ⚠️ ⚠️ WARNING ⚠️ ⚠️
Once you have run the command to create your `${BIDSAPP}` directory,
DO NOT rename or change the path to any of the directories that were inputs to your
bootstrap script!!

---

Inside the `${BIDSAPP}` directory, the subdirectory most relevant for you is the
`analysis` directory. This is a regular datalad dataset that
contains the code, input data, and remote configuration needed to run the
jobs on the cluster.

```bash
$ cd ${BIDSAPP}
$ ls
analysis	input_ria	output_ria	pennlinc-containers
$ cd analysis
$ datalad siblings
.: here(+) [git]
.: input(-) [/Users/<username>/projects/tmp/BIDSAPP/input_ria/9d1/e46ef-27a2-400c-84da-7ea466afd3e7 (git)]
.: output-storage(+) [ora]
.: output(-) [/Users/<username>/projects/tmp/BIDSAPP/output_ria/9d1/e46ef-27a2-400c-84da-7ea466afd3e7 (git)]
```

We can see that in addition to the `analysis` dataset there are two remotes
configured for pushing and pulling provenance and data from. These are
required for performance on large datasets, but it's not required for you to
know exactly how this all works as an end user.

## Editing the executable code

The bootstrapping script will also create some scripts in
`analysis/code` that will be used to run your job. You will want to
edit these to tailor the call to your prep in case there are any specific
options for this particular run. The files `analysis/code/participant_job.sh`
and `analysis/code/*zip.sh` are the key to running your job. You can edit these
however you like, but be sure you save your changes and push them to the
input and output ria stores. For example, if I just edited one of the scripts
and saved the file:

```bash
$ datalad save -m "edited participant_job.sh" code/participant_job.sh
$ datalad push --to input
$ datalad push --to output
```

### Keeping files from an example run

If you want to have your job persist somewhere accessible, you should edit
`participant_job.sh` and change the line

```bash
cd ${CBICA_TMPDIR}
```

to point somewhere on a network file system. On CUBIC you could use:

```bash
cd /cbica/comp_space/$(basename $HOME)
```

This will create a directory in your project user's `/cbica/comp_space` directory
that you can visit and investigate. This is particularly useful for debugging your
`*_zip.sh` script.

---
**NOTE:** Be sure to change the line back to `cd ${CBICA_TMPDIR}` *before* you
submit jobs for all your subjects. Otherwise they will all run in your
`comp_space` directory, which may fill up.

---


### Making sure you're using the correct singularity image

The bootstrap scripts are supposed to be templates for running a containerized
pipeline on datalad-tracked data. The environment they set up will be correct,
but it is likely that the content of the scripts in `analysis/code` will not
meet your needs.

The most likely change you'll need to make is in the name of the image in the
container dataset. Remember from above that you assign an *image ID* to the
sif file in your container dataset? You will need to make sure that container
ID is referenced in the `datalad run` command in `participant_job.sh` and
in `*zip.sh`. Be sure to make the zip file names match the version of
the image.



## Running a test subject

After editing the scripts in `analysis/code`, saving them and pushing them
to input and output ria stores, it's time to test.
You never know if your scripts will work until you do a test run. To
submit a single subject, you can execute the last line of `code/qsub_calls.sh`
and see how it goes. From the `analysis` directory run

```bash
$ $(tail -n 1 code/qsub_calls.sh)
```

This will submit the last subject. If this run succeeds you should delete the
last line of `code/qsub_calls.sh` so the test subject isn't run again.

Once your test subject finishes, launch the rest of the jobs with

```bash
$ bash code/qsub_calls.sh
```

This will submit one job per subject, which will generate a lot of text printed
in the terminal. Note: if you have other jobs running and want to cancel all
the jobs you launched, you might unintentionally kill non-pipeline jobs if
you delete all your jobs.


### When jobs are stuck in the "r" state

Sometimes, your qsub jobs will get stuck due to cluster/node issues. This will require you to rerun those stuck jobs. In order to do this, you can use our `qstat_to_qsub_calls_rerun.sh` script that can be found [here](https://github.com/PennLINC/RBC/blob/master/PennLINC/Generic/qstat_to_qsub_calls_rerun.py). This script takes in the path to the analysis directory of the pipeline you ran, runs `qstat` under the hood, cross references the job IDs with the logs directory to get the subject IDs of all stuck subjects, and writes out a `qsub_calls_rerun.sh` file to the `analysis/code directory`, and `qdel` the stuck jobIDs. This file contains a truncated version of `qsub_calls.sh` and includes the qsub calls to the pipeline for only the subjects who were stuck. Lastly, you will need to kill the stuck jobs and `bash code/qsub_calls_rerun.sh` from the analysis directory. Repeat this process if another rerun is required. See below for an example: 

`python qstat_to_qsub_calls_rerun.sh /cbica/projects/RBC/production/PNC/fmriprep/analysis`

The command above will write out a `qsub_calls_rerun.sh` file to the `/cbica/projects/RBC/production/PNC/fmriprep/analysis/code` directory.

# After the pipeline runs

At the end of your pipeline runs, each subject/job will exist as a datalad branch in
the `output` special remote set up by the bootstrap script. These branches will
need to be merged into a single branch to create a complete results dataset.

A script to do this was created during the bootstrapping. To run the merge:

```bash
$ bash code/merge_outputs.sh
```

---
### ⚠️ ⚠️ WARNING ⚠️ ⚠️
NEVER do production work in the `merge_ds` directory. It is meant only
as a place to merge branches, NOT to gather data for further analysis.
The appropriate method for accessing data created by a bootstrap run
is described in the next section.

---


## Accessing files created by a bootstrap script

Once the `code/merge_outputs.sh` script finishes, you will have all
the results from your bootstrap script stored in the `output_ria`.
As an RIA store, it's not intended for a human to work with its contents.
Instead, you should clone from the RIA store to create a normal datalad
dataset, where all your files will be accessible. For example

```bash
$ datalad clone ria+file:///path/to/qsiprep/output_ria#~data qsiprep_outputs
$ cd qsiprep_outputs
$ # Unlock one of the results zip files
$ datalad get sub-X_qsiprep-0.14.2.zip
$ datalad unlock sub-X_qsiprep-0.14.2.zip
$ unzip sub-X_qsiprep-0.14.2.zip
```

this will unzip sub-X's qsiprep results. You'll notice that it is inefficient
and cumbersome to `get` and `unlock` the files you created.

## Auditing Your Runs

It's impractical of course to check every single subject for successful
run output. Instead, we recommend taking this bootstrap approach and using it
to assess the data in what we call a _bootstrap audit_. This stage simply
uses bootstrapping to dive into the outputs of each subject's datalad branch
and collect some information from it. Note that audit scripts are in
development, and more will be added for other pipelines as we go
along — below is an example using an fMRIPrep exemplar test.

After you've run fMRIPrep exemplars, your `testing` directory may look like this:

```
testing
├── exemplars_dir
└── exemplar_test
    ├── bootstrap-fmriprep.sh
    ├── fmriprep                 # your analysis lives here           
    │   ├── analysis               # datalad tracked scripts and logs
    │   │   ├── CHANGELOG.md
    │   │   ├── code
    │   │   ├── inputs
    │   │   ├── logs
    │   │   ├── pennlinc-containers
    │   │   └── README.md
    │   ├── input_ria             # datalad dataset of input data (points to exemplars dir)
    │   │   ├── 553               # don't worry about this notation, it's expected
    │   │   ├── error_logs
    │   │   └── ria-layout-version
    │   ├── merge_ds              # a temp space for merging outputs; do not modify
    │   │   ├── CHANGELOG.md
    │   │   ├── code
    │   │   ├── inputs
    │   │   ├── pennlinc-containers
    │   │   └── README.md
    │   ├── output_ria            # datalad dataset of analysis outputs
    │   │   ├── 553
    │   │   ├── alias
    │   │   ├── error_logs
    │   │   └── ria-layout-version
    │   └── pennlinc-containers
    └── fmriprep-container

```

A quick way to assess if your jobs ran successfully is to see if an output branch was created for each subject. The output branches are located in the `output_ria`, which has a hashed string as a directory name. Simply descend into that directory like:

```shell
$ cd fmriprep/output_ria/553/6b78d-a143-45e9-9fc4-684fad48fd29
```

Then, check the branches with `git branch -a`:

```shell
$ git branch -a
  git-annex
  job-9650320-sub-X1
  job-9650321-sub-X2
  job-9650322-sub-X3
  job-9650323-sub-X4
  job-9650324-sub-X5
  job-9650325-sub-X6
  job-9650327-sub-X7
  job-9650328-sub-X8
  job-9650329-sub-X9
  job-9650330-sub-X10
  job-9650331-sub-X11
* master
```

That should be the only thing you should do in this directory -- it's a special git directory that is fragile and shouldn't be tampered with.

Instead of tampering with these branches, we have an fMRIPrep audit bootstrap available [here](https://github.com/PennLINC/TheWay/blob/main/scripts/cubic/bootstrap-freesurfer-audit.sh). Running it is very similar to running the pipeline.

First, download the script in the same place that you started your fMRIPrep pipeline:

```
wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/bootstrap-fmriprep-audit.sh
```

Then, bash the script, providing the full path to the `fmriprep` directory:

```shell
$ tree -L 2 .
.
├── bootstrap-fmriprep-audit.sh      # run this
├── bootstrap-fmriprep.sh
├── fmriprep                         # with this as input
│   ├── analysis
│   ├── input_ria
│   ├── merge_ds
│   ├── output_ria
│   └── pennlinc-containers
└── fmriprep-container
```

Like so:

```shell
$ bash bootstrap-fmriprep-audit.sh /path/to/exemplar_test/fmriprep
```

The contents of the resulting `fmriprep-audit` directory are analogous to the 
`fmriprep` directory. Hence, you should make sure to edit `analysis/code/participant_job.sh`
to suit your needs — particularly, you should set the correct conda environment:

```
#participant_job.sh

#!/bin/bash
#$ -S /bin/bash
#$ -l h_vmem=5G
#$ -l s_vmem=3.5G
# Set up the correct conda environment
source ${CONDA_PREFIX}/bin/activate reward         ## you will need to edit this
echo I\'m in $PWD using `which python`

# fail whenever something is fishy, use -x to get verbose logfiles
set -e -u -x
```

As always, don't forget to `datalad save`!

```
$ datalad save -m "edited participant_job.sh" code/participant_job.sh
$ datalad push --to input
$ datalad push --to output
```

Now, you're ready to run the audit (from the `analysis` directory):

```bash
$ bash code/qsub_calls.sh
```

This is a very quick program — once it's complete, you can check if a branch was 
created successfully as before:

```bash
$ cd ../output_ria/9c4/d63ba-c4d7-4066-a385-cbc895fb9dbe/
$ git branch -a
  git-annex
  job-9654895-sub-X1
  job-9654896-sub-X2
  job-9654897-sub-X3
  job-9654898-sub-X4
  job-9654899-sub-X5
  job-9654900-sub-X6
  job-9654901-sub-X7
  job-9654902-sub-X8
  job-9654903-sub-X9
  job-9654904-sub-X10
  job-9654905-sub-X11
  job-9654906-sub-X12
* master
```

Next, run `merge_outputs.sh` (again from the `analysis` directory):

```bash
$ bash code/merge_outputs.sh
```

The difference is that you'll have CSV files in the merge_ds/csvs directory:

```
fmriprep-audit/
├── analysis
├── fmriprep_logs
├── input_ria
├── merge_ds
│   ├── CHANGELOG.md
│   ├── code
│   ├── csvs
│   │   ├── sub-X1_fmriprep_audit.csv -> ../.git/annex/objects/Fq/KK/MD5E-s438--a54abe84d4358d32e9890f31159e1856.csv/MD5E-s438--a54abe84d4358d32e9890f31159e1856.csv
│   │   ├── sub-X2_fmriprep_audit.csv -> ../.git/annex/objects/M2/0M/MD5E-s438--8aedcadb5dca8000482b5d85285ab1ee.csv/MD5E-s438--8aedcadb5dca8000482b5d85285ab1ee.csv
│   │   ├── sub-X3_fmriprep_audit.csv -> ../.git/annex/objects/Xw/Wg/MD5E-s438--69ecb85a526ad82e5d576765f7122193.csv/MD5E-s438--69ecb85a526ad82e5d576765f7122193.csv
│   │   ├── sub-X4_fmriprep_audit.csv -> ../.git/annex/objects/34/p1/MD5E-s438--2405e9984f82eefe68bf1fbaa31c0a03.csv/MD5E-s438--2405e9984f82eefe68bf1fbaa31c0a03.csv
│   │   ├── sub-X5_fmriprep_audit.csv -> ../.git/annex/objects/W4/qq/MD5E-s438--d7fac36464daa5d4a058c8990f96588b.csv/MD5E-s438--d7fac36464daa5d4a058c8990f96588b.csv
│   │   ├── sub-X6_fmriprep_audit.csv -> ../.git/annex/objects/px/6x/MD5E-s687--31fb3d57f20d867bb69bba3d77cc93f1.csv/MD5E-s687--31fb3d57f20d867bb69bba3d77cc93f1.csv
│   │   ├── sub-X7_fmriprep_audit.csv -> ../.git/annex/objects/fp/xG/MD5E-s438--83300886d60d830d39d4b654f62599f8.csv/MD5E-s438--83300886d60d830d39d4b654f62599f8.csv
│   │   ├── sub-X8_fmriprep_audit.csv -> ../.git/annex/objects/kX/Fz/MD5E-s438--7cc964e74969fbfa94422bdc057ffb34.csv/MD5E-s438--7cc964e74969fbfa94422bdc057ffb34.csv
│   │   ├── sub-X9_fmriprep_audit.csv -> ../.git/annex/objects/6w/f4/MD5E-s438--0fdf942a1e56de372038162e2721922b.csv/MD5E-s438--0fdf942a1e56de372038162e2721922b.csv
│   │   ├── sub-X10_fmriprep_audit.csv -> ../.git/annex/objects/fF/K9/MD5E-s438--fb10874c8acd455fb2bc816950d4aae8.csv/MD5E-s438--fb10874c8acd455fb2bc816950d4aae8.csv
│   │   ├── sub-X11_fmriprep_audit.csv -> ../.git/annex/objects/f6/k2/MD5E-s438--3f606b7b6309c1ad88b0eb4a1678a5bc.csv/MD5E-s438--3f606b7b6309c1ad88b0eb4a1678a5bc.csv
│   │   └── sub-X12_fmriprep_audit.csv -> ../.git/annex/objects/xQ/K1/MD5E-s438--cc3ba3bf880ed13d29b9af868dbd6133.csv/MD5E-s438--cc3ba3bf880ed13d29b9af868dbd6133.csv
│   ├── inputs
│   └── README.md
└── output_ria
```

These are the audit results, tracked in datalad. Again, don't tamper with these.
Instead, concatenate these single row CSVs into a table, which will contain one row per subject, by running the following command, also from the analysis directory:

```shell
$ bash code/concat_outputs.sh
```

Once you see `SUCCESS`, the output will be available in the root of the audit directory:

```
fmriprep-audit
├── analysis
├── FMRIPREP_AUDIT.csv     #HERE IT IS!
├── fmriprep_logs
├── input_ria
├── merge_ds
└── output_ria
```

## Something Went Wrong in BIDS

Let's say you've audited your bootstrap and notice something went wrong — e.g. two or
three subjects have unusable BOLD data — and now you have to
adjust your BIDS data to fix it. You go back to your BIDS and make some adjustments, saving
them in datalad as before, but how does your bootstrap know to re-run the data with
the newly updated BIDS?

*The easiest way to solve this problem is to burn down your `testing` directory and start again from
the top of this page* — this is especially recommended if you're new to this process and only have
a handful of bootstraps to run. But if you're _not_ interested and want to keep
your work, there is a way to re-run
only the _adjusted_ BIDS participants that adheres to the bootstrap workflow:

1. Adjust your BIDS data and `datalad save` it; you should be familiar with this.

2. Now, head to the `analysis` directory of your bootstrap:

```shell
.
├── bootstrap-fmriprep.sh
├── fmriprep                         
│   ├── analysis                # go here
│   ├── input_ria
│   ├── merge_ds
│   ├── output_ria
│   └── pennlinc-containers
└── fmriprep-container
```

3. Now, tell datalad to uninstall the input directory (inputs being your BIDS)

```shell
datalad remove -d . inputs/data
```

This will make sure your data is cleanly removed.

4. Re-clone the data and push this update:

```shell
datalad clone -d . ${BIDSINPUT} inputs/data
datalad push --to input
```

Now, if you run the handful of subjects (by finding that subject's line in `analysis/code/qsub_calls.sh`
and simply copy-pasting it into the terminal), their BIDS inputs remote should be updated with your changes.

# Running a bootstrap on the outputs of another bootstrap

Suppose you want to extract a specific file from each subject's output
zips. One great way to get all this data is to create a new bootstrap
script that does this. You can find an example
[here](https://github.com/PennLINC/TheWay/blob/main/scripts/cubic/bootstrap-fmriprep-bugcheck.sh).

Other bootstrap scripts work on the outputs of other bootstraps by
design, such as [XCP](https://github.com/PennLINC/TheWay/blob/main/scripts/cubic/bootstrap-xcp.sh),
[QSIRecon](https://github.com/PennLINC/TheWay/blob/main/scripts/cubic/bootstrap-qsirecon.sh),
and the various Audit scripts.

# Generating QCs

First, download the script in the same place that you started your pipeline. We currently have QCscripts for ASLPrep and XCP. 
For fMRIPrep, QCs are analyzed from XCP. 
Note that for XCP, the unzip script is different https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/bootstrap-xcp-qc.sh due to the presence of different tasks. 

The example shown below uses ASLPrep outputs. 
```
wget https://raw.githubusercontent.com/PennLINC/TheWay/main/scripts/cubic/bootstrap-aslprep-qc.sh
```

Then, bash the script, providing the full path to the `aslprep` directory:

```shell
$ tree -L 2 .
.
├── bootstrap-aslprep-qc.sh      # run this
├── bootstrap-aslprep.sh
├── aslprep                         # with this as input
│   ├── analysis
│   ├── input_ria
│   ├── merge_ds
│   ├── output_ria
│   └── pennlinc-containers
└── aslprep-container
```

Like so:

```shell
$ bash bootstrap-aslprep-qc.sh /path/to/exemplar_test/aslprep
```

The contents of the resulting `ASLPREP_QC` directory are analogous to the 
`ASLPrep` directory. Hence, you should make sure to edit `analysis/code/participant_job.sh`
to suit your needs — particularly, you should set the correct conda environment:

```
#participant_job.sh

#!/bin/bash
#$ -S /bin/bash
#$ -l h_vmem=5G
#$ -l s_vmem=3.5G
# Set up the correct conda environment
source ${CONDA_PREFIX}/bin/activate base         ## you will need to edit this
echo I\'m in $PWD using `which python`

# fail whenever something is fishy, use -x to get verbose logfiles
set -e -u -x
```

As always, don't forget to `datalad save`!

```
$ datalad save -m "edited participant_job.sh" code/participant_job.sh
$ datalad push --to input
$ datalad push --to output
```

Now, you're ready to run the script (from the `analysis` directory):

```bash
$ bash code/qsub_calls.sh
```

This is a very quick program — once it's complete, you can check if a branch was 
created successfully as before:

```bash
$ cd ../output_ria/9c4/d63ba-c4d7-4066-a385-cbc895fb9dbe/
$ git branch -a
  git-annex
  job-9654895-sub-X1
  job-9654896-sub-X2
  job-9654897-sub-X3
  job-9654898-sub-X4
  job-9654899-sub-X5
  job-9654900-sub-X6
  job-9654901-sub-X7
  job-9654902-sub-X8
  job-9654903-sub-X9
  job-9654904-sub-X10
  job-9654905-sub-X11
  job-9654906-sub-X12
* master
```

Next, run `merge_outputs.sh` (again from the `analysis` directory):

```bash
$ bash code/merge_outputs.sh
```

The difference is that you'll have CSV files in the merge_ds/csvs directory:

```
ASLPREP_QC/
├── analysis
├── input_ria
├── merge_ds
│   ├── CHANGELOG.md
│   ├── code
│   ├── csvs
│   │   ├── sub-X1_aslprep_qc.csv -> ../.git/annex/objects/Fq/KK/MD5E-s438--a54abe84d4358d32e9890f31159e1856.csv/MD5E-s438--a54abe84d4358d32e9890f31159e1856.csv
│   │   |   3ba3bf880ed13d29b9af868dbd6133.csv/MD5E-s438--cc3ba3bf880ed13d29b9af868dbd6133.csv
│   ├── inputs
│   └── README.md
└── output_ria
```

These are the per-subject QC results, tracked in datalad. Again, don't tamper with these.
Instead, concatenate these single row CSVs into a table, which will contain one row per subject, by running the following command, also from the analysis directory:

```shell
$ bash code/concat_outputs.sh
```
---
**NOTE:**   For XCP, you will need to supply arguments in the form of all the tasks/spaces/bands/res you want:

```
$ bash code/concat_outputs.sh rest fsLR multi 1 OR comma-separated for multiple arguments, eg: bash code/concat_outputs.sh rest,fracback,face MNI152NLin6Asym,fsLR multi,single 1,2
```

---
Once you see `SUCCESS`, the output will be available in the root of the QC directory:

```
ASLPREP_QC
├── analysis
├── ASLPREP_QC.csv     #HERE IT IS!
├── input_ria
├── merge_ds
└── output_ria
```

```
XCP_QC
├── analysis
├── group_level_task-rest_acq-singleband_space-fsLR_desc-qc_bold.csv   #HERE IT IS!
├── input_ria
├── merge_ds
└── output_ria
```

# Run single subject testing on interactive node using bootstraps

Before you read on, please ensure that you have already bootstrapped your BIDS application. You can find an example bootstrap for fMRIPrep [here](https://github.com/PennLINC/TheWay/blob/main/scripts/cubic/bootstrap-fmriprep.sh).




## Set up necessary variables
In your `participant_job.sh`, you should have the following lines:
```
dssource="$1"
pushgitremote="$2"
subid="$3"
```
The variables are normally set when you run qsub_calls.sh as `$1`, `$2` and `$3`, but you don’t get that in an interactive run. Therefore for testing on one subjec on the interactive node, we want to specify the `dssource` (input source), `pushgitremote` (the path to the output branch for the job), and the `subid` (subject id). 

In order to obtain the correct output branch for the chosen subject, you would need to check out the file `qsub_calls.sh` and extract relevant information corresponding to the chosen subject. In your `qsub_calls.sh`, you should have something similar to the following lines:
```
qsub -cwd -v DSLOCKFILE=/cbica/projects/RBC/testing/mriqc/mriqc/analysis/.SGE_datalad_lock -N fpsub-X -e /cbica/projects/RBC/testing/mriqc/mriqc/analysis/logs -o /cbica/projects/RBC/testing/mriqc/mriqc/analysis/logs   /cbica/projects/RBC/testing/mriqc/mriqc/analysis/code/participant_job.sh   ria+file:///cbica/projects/RBC/testing/mriqc/mriqc/input_ria#ec535b2a-6328-4b4b-a575-a6a1ffd1f1b5 /cbica/projects/RBC/testing/mriqc/mriqc/output_ria/ec5/35b2a-6328-4b4b-a575-a6a1ffd1f1b5 sub-X
```
For this example, `subid` is `sub-X`, `dssource` is `ria+file:///cbica/projects/RBC/testing/mriqc/mriqc/input_ria#ec535b2a-6328-4b4b-a575-a6a1ffd1f1b5`
and `pushgitremot` is `/cbica/projects/RBC/testing/mriqc/mriqc/output_ria/ec5/35b2a-6328-4b4b-a575-a6a1ffd1f1b5`. You can choose any other subject and the same pattern applies.

```
dssource="ria+file:///cbica/projects/RBC/testing/mriqc/mriqc/input_ria#ec535b2a-6328-4b4b-a575-a6a1ffd1f1b5"
pushgitremote="/cbica/projects/RBC/testing/mriqc/mriqc/output_ria/ec5/35b2a-6328-4b4b-a575-a6a1ffd1f1b5"
subid="sub-X"
```
Copy and paste the above three lines into your terminal and hit enter.



Then you need to create a job branch for the chosen subject. Again in your `participant_job.sh`, you should have the following lines:
```
BRANCH="job-${JOB_ID}-${subid}"
mkdir ${BRANCH}
cd ${BRANCH}
```
When a job is submitted using [qsub](http://gridscheduler.sourceforge.net/htmlman/htmlman1/qsub.html), `JOB_ID` will get automatically assigned by the cluster. For interactive node testing, `JOB_ID` needs to be set manually and we recommend that you set `JOB_ID` to `test`. Otherwise the `set -u` will cause an error when you try to access the variable.

```
BRANCH="job-test-${subid}"
mkdir ${BRANCH}
cd ${BRANCH}
```

Copy and paste the above three lines into your terminal and hit enter.

## Clone and get the dataset content
Now we can obtain a new clone (copy) of the single subject dataset in the `${BRANCH}` directory.
```
datalad clone "${dssource}" ds
cd ds
git remote add outputstore "$pushgitremote"
git checkout -b "${BRANCH}"
datalad get -n "inputs/data/${subid}"
```


Copy and paste the above three lines into your terminal and hit enter.
You should now have `ds` as your working directory.

## Run the BIDS app on the chosen subject
```
datalad run \
    -i code/mriqc_zip.sh \
    -i inputs/data/${subid} \
    -i inputs/data/*json \
    -i pennlinc-containers/.datalad/environments/mriqc-0-16-1/image \
    --explicit \
    -o ${subid}_mriqc-0.16.1.zip \
    -m "mriqc:0.16.1 ${subid}" \
    "bash ./code/mriqc_zip.sh ${subid}"
```


Copy and paste the above three lines into your terminal and hit enter.
Now your BIDS app should be runnning on the chosen single subject! Monitor the terminal closely and if you get errors, don't panic! The benefit of testing on a single subject interactively is that you should clearly see where you get stuck.
