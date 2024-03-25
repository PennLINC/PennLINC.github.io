---
layout: default
title: Getting Static Data from PMACS
parent: Data Workflows
nav_order: 2
has_toc: true
---

# What is static data?
{: .no_toc}

When we've finalized a data resource, we share it with authorized lab members from
the `/static` mount. If you're thinking "I'd like to get the
region time series from dataset X", or "I need the entire results from qsiprep for
dataset Y," this is the best way to do it!

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


# Ensure you have a PMACS account and membership to the data group

You need a
[PMACS](/docs/PMACS/pmacs.md#using-penn-medicine-academic-computing-services-pmacs)
account to access static datasets. If you do not have an account, you need your
PI to open a ticket in the [PMACS helpdesk](https://helpdesk.pmacs.upenn.edu/).

Once you have a PMACS account you will need to open a ticket to request access
to the specific datasets you want.  You can see a [list of available
data](https://pennlinc.github.io/docs/DataWorkflows/AvailableStaticData/).
Suppose you want access to the HBN and PNC data (the dataset is listed in the
leftmost column), include in the ticket

```
Please add my PMACS account to the LINC_PNC and LINC_HBN groups.
```

This ticket should also be submitted by your PI.

---
**⚠️ ⚠️ WARNING ⚠️ ⚠️**

Datasets are subject to data use agreements and terms of use. Before access is
granted to any static dataset, you must prove that you are qualified to access
it *when you ask your PI to create the PMACS helpdesk ticket*. This can be an
email showing your connectomedb access (for HCP-YA) or similar.

---

## Checking your PMACS account

You should check your PMACS account before you try to clone any static data.
First ensure that you can log into pmacs with a normal SSH session. This
verifies that you have the correct username and password. Consult with the 
Informatics Team or your PI to obtain the name of the login node you should use.

```
$ ssh [username]@[login node name].pmacs.upenn.edu
```

Once you have verified that you can access the login node, check that you have access to
the group for the static data you want to access by running the `groups` command.

```
$ groups
... LINC_NKI LINC_HBN LINC_CCNP LINC_HRC LINC_HCPD LINC_PNC LINC_PACCT...
```

The `LINC_` groups provide read-only access to that dataset's static data.

Finally, use this command to force a recent version of git to be used for all
sessions:

```
$ echo 'module load git' >> ~/.bashrc
```

# Clone the static data

in order to get the data to your computer or in your CUBIC project directory, you need to ensure 3 things:

  1. You have a PMACS account and the account has been added to the relevant data group (see above)
  2. Your computer is on the [UPHS VPN](/docs/cubic/cubic.md#setting-up-your-account) or the
     [PMACS VPN](/docs/PMACS/pmacs.md#logging-in-to-pmacs-lpc)
  3. You have datalad, git and git-annex installed on your computer
  4. You have verified that you have your PMACS accound set up (see above section)
  2. You have [datalad](./Datalad.md), git and git-annex installed on your computer or on your CUBIC project directory 
  5. If you're planning to download data into your CUBIC project directory, you are logged in to CUBIC project [user](../cubic/cubic.md)

If these conditions are met, you're ready to access some data! 

If these conditions are met, you're ready to access some data!
Generally, datasets can be in two different formats:
- unzipped: this type of dataset allows to access all different subdirectories and files of all participants directly
- zipped: this type of dataset has one zip file per participant. This allows more efficient storing, and requires a few extra steps to figure out what kinds of files are available and to download them.

Ways of looking at and then getting each type of dataset are explained below.

# Getting an unzipped dataset
Suppose I'd like to see the regional time series data for CCNP. Checking the
[list of available datasets](/docs/DataWorkflows/AvailableStaticData.md#available-static-datasets) I
see the `Clone URL` column lists `LINC_CCNP#~XCP_unzipped` for this resource.

Items in the `Clone URL` are used to get a clonable address for the data. The
value gets appended to
`ria+ssh://[username]@[login node name].pmacs.upenn.edu:/static/`, where
`[username]` is replaced with your PMACS username (without brackets) and
`[login node name]` is replaced with the name of the PMACS login node you will be accessing. 
`Consult with the Informatics Team or your PI to obtain the login node name you should use. 
`I can then clone this data with the command

```
$ datalad clone ria+ssh://[username]@[login node name].pmacs.upenn.edu:/static/LINC_CCNP#~XCP_unzipped CCNP_xcpd
```

You will be asked for your PMACS account password:

```
[username]@[login node name].pmacs.upenn.edu's password:
```

after which, you will see some `[INFO   ]` messages that look scary, but are harmless and expected.
They will look something like:

```
[INFO   ] scanning for annexed files (this may take some time)
[INFO   ] RIA store unavailable. -caused by- file:///some/file/path/ria-layout-version not found, self.ria_store_url: ria+file:///some/file/path/output_ria, self.store_base_pass: /some/file/path/output_ria, self.store_base_pass_push: None, path: <class 'pathlib.PosixPath'> /some/file/path/output_ria/ria-layout-version -caused by- [Errno 2] No such file or directory: '/some/file/path/ria-layout-version'
[INFO   ] Reconfigured output-storage for ria+ssh://[username]@[login node name].pmacs.upenn.edu:/static/LINC_CCNP
[INFO   ] Configure additional publication dependency on "output-storage"
configure-sibling(ok): . (sibling)
install(ok): /my/current/workingdir/CCNP_xcpd (dataset)
action summary:
  configure-sibling (ok: 1)
  install (ok: 1)
```

As long as you see `install(ok)`, you have succeeded. Now you can take a look
around the dataset you just got.

```
$ cd CCNP_xcpd
$ ls
sub-colornest001
sub-colornest002
...
sub-colornest195
```

This directory contains all the outputs from xcp_d for each subject. 

## Figuring out what data is available (single participant)

Now, let's see if we can find the actual file we want to get for each subject. We can see all the files for a single subject with `find`

```
$ find sub-colornest001

find sub-colornest001
sub-colornest001
sub-colornest001/ses-1
sub-colornest001/ses-1/anat
sub-colornest001/ses-1/anat/sub-colornest001_ses-1_rec-refaced_space-MNI152NLin6Asym_desc-preproc_T1w.nii.gz
sub-colornest001/ses-1/anat/sub-colornest001_ses-1_rec-refaced_space-MNI152NLin6Asym_desc-preproc_dseg.nii.gz
sub-colornest001/ses-1/func
...
sub-colornest001/ses-1/func/sub-colornest001_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv
...
sub-colornest001/figures/sub-colornest001_ses-1_task-rest_run-2_space-fsLR_desc-postcarpetplot_bold.svg
sub-colornest001/figures/sub-colornest001_ses-1_task-rest_run-2_space-MNI152NLin6Asym_desc-preprocessing_res-2_bold.svg
sub-colornest001/figures/sub-colornest001_ses-1_task-rest_run-2_space-fsLR_desc-bbregister_bold.svg
```

I see that the atlas I want (Gordon) can be found for each subject with a pattern. 

## Getting files for the entire dataset
To actually transfer these files, I need to tell datalad to fetch them from PMACs. This is done with the following command:

```
$ datalad get sub-*/ses*/func/sub-*space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv -J 3
```

**NOTE** that the `-J 3` will create 3 subprocesses that will download the data
*in parallel. If you have
access to more CPUs then feel free to increase this number. If you are in an
environment that limits your resources you can omit this flag and a single
process will be used. This command may take some time to run. At the end you
will see a message like:

You may be asked for your password if you haven't set up an [SSH key](https://pennlinc.github.io/docs/Basics/sshKeys/).

```
[username]@[login node name].pmacs.upenn.edu's password:
get(ok): sub-colornest112/ses-1/func/sub-colornest112_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest042/ses-1/func/sub-colornest042_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest083/ses-1/func/sub-colornest083_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest094/ses-1/func/sub-colornest094_ses-1_task-rest_acq-VARIANTObliquity_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest034/ses-1/func/sub-colornest034_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest142/ses-1/func/sub-colornest142_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest095/ses-1/func/sub-colornest095_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest067/ses-1/func/sub-colornest067_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest165/ses-1/func/sub-colornest165_ses-1_task-rest_acq-VARIANTObliquity_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
get(ok): sub-colornest129/ses-1/func/sub-colornest129_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file) [from output-storage...]
  [379 similar messages have been suppressed; disable with datalad.ui.suppress-similar-results=off]
action summary:
  get (ok: 389)
```


# Use the data

Since we're working with *static* data, we don't want to change it in any way.
Therefore, you should create a directory for your code outside of the cloned
data. Picking up where we left off, we move a directory up and create a
directory for our analysis.

```
$ cd ..
$ mkdir my_analysis_project
```

Write your code inside the `my_analysis_project`, accessing the data in
`../CCNP_xcpd`.


## Clean up the data

If you cloned your data to a location where file storage is expensive (eg
[CUBIC](/docs/cubic)) you don't want your input data sitting around after you've
extracted what you need from it.  Datalad makes this easy for us - we `drop` the
data content from our clone.

```
$ cd CCNP_xcpd
$ datalad drop --nocheck .

drop(ok): sub-colornest001/ses-1/func/sub-colornest001_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest001/ses-1/func/sub-colornest001_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest002/ses-1/func/sub-colornest002_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest002/ses-1/func/sub-colornest002_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest003/ses-1/func/sub-colornest003_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest003/ses-1/func/sub-colornest003_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest004/ses-1/func/sub-colornest004_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest004/ses-1/func/sub-colornest004_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest005/ses-1/func/sub-colornest005_ses-1_task-rest_run-1_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
drop(ok): sub-colornest005/ses-1/func/sub-colornest005_ses-1_task-rest_run-2_space-MNI152NLin6Asym_atlas-Gordon_desc-timeseries_res-2_bold.tsv (file)
  [379 similar messages have been suppressed; disable with datalad.ui.suppress-similar-results=off]
drop(ok): . (directory)
action summary:
  drop (ok: 390)
```

This can take a long time to run, but is a great way to make sure that a
fetchable reference to your input data is preserved while disk space is saved.
Critically, the reference to the EXACT version of the file you used in your
analysis will be fetched if you need to
[access the data again](#clone-the-static-data).

# Getting a zipped dataset

The following walkthrough should help you unzip your data if it is a zipped dataset. These lines of code can be customized per your needs to unzip some or all subjects and then some or all files: 

Before running a loop for all participants of a dataset, you probably first want to figure out what data is available, and which files you’d want to get. Most datasets are zipped, so here is a walkthrough for a single subject. In this case, we’re interested in getting fMRIPrep data from PNC, which is zipped and stored on PMACS. 

## Figuring out what data is available (single participant)

Once data is cloned from PMACS, let’s `cd` into to it to see what’s there: 

```bash
sub-DobbySockster_fmriprep-20.2.3.zip@     
sub-HarryPotter_fmriprep-20.2.3.zip@
sub-NevilleLongbottom_freesurfer-20.2.3.zip@   
```

The folder contains a bunch of folders and simlinks to zipped participants. 

### Step 2: Get and unzip a participant

The next step is to get and unzip data for one participant to figure out what files are available. 

```bash
# make directory to store unzipped files
mkdir -p /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped
mkdir -p /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped

# define a specific participant file 
file="sub-NevilleLongbottom_fmriprep-20.2.3.zip"

# get the file for one specific participant
datalad get $file -J 8 # runs the job on 8 threads
```

The output of datalat get will look like this: 

```bash
It is highly recommended to configure Git before using DataLad. Set both 'user.name' and 'user.email' configuration variables.
Total:   0%|                                                                                | 0.00/1.19G [00:00<?, ? Bytes/s]
dumbledore@[login node].pmacs.upenn.edu's password:
```

Before starting the download, the system will ask for your PMACS (note: not CUBIC!) password. Type it in and it will start showing a progress bar for the download. Eventually, you know that the download is successful when you see this output: 

```bash
get(ok): sub-NevilleLongbottom_fmriprep-20.2.3.zip (file) [from output-storage...]
```

Next, let’s copy the zipped data to another directory outside of the official datalad clone so that we're keeping things separate from the cloned folder, and then unzip it and save that into our unzipped folder: 

```bash
# copy the zip
cp $file /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped

# unzip the files outside of the datalad clone
unzip "/cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped/$file" -d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/
```

The output of the unzipping will look something like this: 

```bash
Archive:  /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped/sub-NevilleLongbottom_fmriprep-20.2.3.zip
[...]
   creating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/fmriprep/sub-NevilleLongbottom/ses-PNC1/anat/
  inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/fmriprep/sub-NevilleLongbottom/ses-PNC1/anat/sub-NevilleLongbottom_ses-PNC1_acq-refaced_desc-aparcaseg_dseg.nii.gz
[...]
   creating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/fmriprep/sub-NevilleLongbottom/ses-PNC1/func/
[...]
  inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/fmriprep/sub-NevilleLongbottom/ses-PNC1/func/sub-NevilleLongbottom_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries.nii
```

Let’s say we’re interested in just getting the 91k bold dtseries nifti. 

```bash
# get the subject ID out of the zip file name (sub-NevilleLongbottom)
sub=${file%_*}

# unzip just one specific file (bold nifti)
unzip -j "$file" "fmriprep/$sub/ses-PNC1/func/${sub}_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries.nii" \
	-d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/$sub
```

The output will look like this: 

```bash
Archive:  sub-NevilleLongbottom_fmriprep-20.2.3.zip
  inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/sub-NevilleLongbottom/sub-NevilleLongbottom_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries.nii
```

Note that you can also unzip a couple of files with a certain path structure by using wildcards. For example, we can download all bold dtseries files with different extensions: 

```bash
unzip -j "$file" "fmriprep/$sub/ses-PNC1/func/${sub}_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries*" -d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/$sub
```

This will download all available files with this path structure, here a nifti and a json: 

```bash
inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/sub-NevilleLongbottom/sub-NevilleLongbottom_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries.json
inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/sub-NevilleLongbottom/sub-NevilleLongbottom_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries.nii
```

Alternatively, you can place the wildcard elsewhere, for instance to get all types of tasks (rest, etc.): 

```bash
unzip -j "$file" "fmriprep/$sub/ses-PNC1/func/${sub}_ses-PNC1_task-*_space-fsLR_den-91k_bold.dtseries.nii" -d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/$sub

```

This downloads several dtseries, for `frac2back`,  `idemo` and `rest` tasks : 

```bash
Archive:  sub-NevilleLongbottom_fmriprep-20.2.3.zip
  inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/sub-NevilleLongbottom/sub-NevilleLongbottom_ses-PNC1_task-frac2back_space-fsLR_den-91k_bold.dtseries.nii
  inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/sub-NevilleLongbottom/sub-NevilleLongbottom_ses-PNC1_task-idemo_space-fsLR_den-91k_bold.dtseries.nii
  inflating: /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/sub-NevilleLongbottom/sub-NevilleLongbottom_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries.nii
```

Now that we figured out what files are available for a given participant, let’s “drop” the zipped participant data. This doesn’t do anything to the original data on PMACS, but just removes the downloaded data in the cloned dataset in your project directory, which saves space.

```bash
# drop the file
datalad drop --nocheck $file
```

This is what the output should look like: 

```bash
It is highly recommended to configure Git before using DataLad. Set both 'user.name' and 'user.email' configuration variables.
drop(ok): sub-NevilleLongbottom_fmriprep-20.2.3.zip (file)
```

## Getting files for the entire dataset

Now that we know how to look for available data in a zipped static PMACS dataset, we’re ready to scale things up and download all required data for the whole dataset!

Here's how this may look unzipping on a larger scale: 



```bash
#!/bin/bash
# conda activate dlad

# clone static data of interest from PMACS, here LINC_PNC#~FMRIPREP_zipped, 
# but can be replaced with anything in the "Clone URL" column here https://pennlinc.github.io/docs/DataTasks/AvailableStaticData/
datalad clone ria+ssh://dumbledore@[login node].pmacs.upenn.edu:/static/LINC_PNC#~FMRIPREP_zipped /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/datalad


# The clone files exist only remotely until we get them locally, so once we have a clone of the data, we need to "datalad get" the files we are interested in. 
cd /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/datalad

# to see the history of what happened to a zipped dataset (i.e. get simlinks without actually getting the data locally)
# datalad get -n .

# ----------------------------------------
## get a few subjects for testing ###
# ----------------------------------------

subject_ids=("HarryPotter","LordVoldemort","NevilleLongbottom")

for id in "${subject_ids[@]}"; do
	# get filename
	file="sub-${id}*zip"

	# make directory to store unzipped files
	mkdir -p /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped
	mkdir -p /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped

	# get the file
	datalad get $file -J 8

	# copy the zip to another directory outside of the official datalad clone so that I'm not messing with it
	cp $file /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped

	# unzip the files outside of the datalad clone
	unzip "/cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped/$file" -d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/

	# # drop the file
	datalad drop --nocheck $file

done

# -------------------------------------------------
#### get zip files for the entire PNC dataset #####
# -------------------------------------------------

for file in *zip ; do

	sub=${file%_*}
	datalad get $file -J 8

 	# unzip the zip 
	unzip "/cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/zipped/$file" -d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/unzipped/

 	# unzip specific files only (needs tweaking if want specific files, example here)
 	# unzip -j "$file" "fmriprep/$sub/ses-PNC1/func/${sub}_ses-PNC1_task-rest_acq-singleband_space-fsLR_den-91k_bold.dtseries*" -d /cbica/projects/hogwarts/data/PNC/PNC_fMRIPrep_v20_2_3/$sub

	# drop the file
	datalad drop --nocheck $file

done
```

## SSH Keys from cubic project uses to pmacs personal users: NOT ALLOWED!

This is not allowed! SSH keys would give all those access to the cubic project user
access to the key owner's pmacs account. This is too dangerous and therefore ssh key
use is not allowed from a cubic project user to a pmacs personal user account.

This unfortunately means you will need to enter your password to copy over the data.
To minimize password entry, try to `datalad get` files using file glob patterns
and using the `-J` flag to download content in parallel.



