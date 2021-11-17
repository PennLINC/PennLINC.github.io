---
layout: default
title: Running Analysis Gears
parent: Flywheel
nav_order: 5
---

# Running analysis workflows

This tutorial covers how to run an analysis gear on many subjects. Like for most tutorials, you will need to be logged in to Flywheel and you will need to start an interactive python session. First, log into Flywheel via the command line interface (see https://docs.flywheel.io/hc/en-us/articles/360008162214 for details).

```bash
>>> fw login <yourapikey>
```

Then start an interactive python session (e.g. by typing ipython or python3.7 into the terminal). Once in the interactive session, import flywheel and create `Client`:

```python
>>> import flywheel
>>> fw = flywheel.Client()
```

Next, find the project you'd like to run the gear on. In this example we are working on a project called `gear_testing`, which is specified in the `fw.projects.find_first("label=gear_testing")` command.

```python
>>> project = fw.projects.find_first("label=gear_testing")
>>> print(project.label)
gear_testing

```

In the code above, if you get an error like `AttributeError: 'NoneType' object has no attribute 'label'` it means that Flywheel couldn't find a project with the label you specified.

## Finding a gear

Gears have a name and a label. The name is used to find the gear and the label is a human-readable description of the gear. This is how to list all the gear names and labels available on your Flywheel instance:

```python
>>> for gear in fw.get_all_gears():
...     print(gear.gear.name, ':', gear.gear.label)

...
export-dicom-file-info : Export DICOM File Header Values to CSV
fmriprep : fMRIPREP: A Robust Preprocessing Pipeline for fMRI Data
forwardmodel : forwardModel: non-linear fitting of models to fMRI data
dcm2niix : DCM2NIIX: dcm2nii DICOM to NIfTI converter
curate-bids : BIDS Curation
thickantscamke : Thickness_ANTS
ashsharpicv : AshsHarpICV
qsiprep-fw : QSIPREP: workflows for preprocessing and reconstructing q-space images
ldogstruct : ldogStruct: anatomical pre-processing for the LDOG project
fmriprep-fwheudiconv : fMRIPREP: A Robust Preprocessing Pipeline for fMRI Data [fw-heudiconv]
fmriprep-hpc : fMRIPREP: A Robust Preprocessing Pipeline for fMRI Data [fw-heudiconv]
...

```

Gears can be found using the `fw.lookup()` command. Find the algorithm you want and use the name (appears before the colon in the print out above):

```python
>>> fmriprep = fw.lookup('gears/fmriprep-fwheudiconv')
>>> print(fmriprep.gear.label)
fMRIPREP: A Robust Preprocessing Pipeline for fMRI Data [fw-heudiconv]

```

## Deciding on a name for your analysis

The actual analysis doesn't exist anywhere, just lots of data containers. It is good practice to use `datetime` objects and a descriptive name to label analyses so they can be found later for downloading. You should put the exact version of the gear in your analysis name, too.  Assuming you're continuing from the previous section, you could do something like this:

```python
>>> import datetime
>>> now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
>>> analysis_label = 'BOLD_Preproc_{}_{}_{}'.format(
...     now, fmriprep.gear.name, fmriprep.gear.version)
>>> print(analysis_label)
BOLD_Preproc_2020-02-04_12:40_fmriprep-fwheudiconv_0.2.2_1.5.2

```

This label will be used for analysis objects created by these gear runs.

## Setting gear configuration options

Gears have "Inputs" and "Configuration". Configuration is the data-independent choices you make when running an algorithm like "Should distortion correction be applied?" or "Should FreeSurfer be skipped?". Each gear has its own configuration, and you can see which options are available by printing the gear's config property:

```python
>>> print(fmriprep.gear.config)
{'save_intermediate_work': {'default': False,
  'type': 'boolean',
  'description': 'Zip and save working directory with intermediate files. [default=false]'},
 'force_syn': {'default': False,
  'type': 'boolean',
  'description': 'EXPERIMENTAL/TEMPORARY: Use SyN correction in addition to fieldmap correction, if available. [ default = false ]'},
 'bold2t1w_dof': {'default': 9,
  'enum': [6, 9, 12],
  'type': 'integer',
  'description': 'Degrees of freedom when registering BOLD to T1w images. 9 (rotation, translation, and scaling) is used by default to compensate for field inhomogeneities. Possible choices: 6, 9, 12. [default=9]'},
 'intermediate_folders': {'default': '',
  'type': 'string',
  'description': 'Space separated list of FOLDERS to retain from the intermediate work directory.'},
 ...
}
```

This is a lot of information, so let's look at one of the items in-depth. Consider the first option:

```python
'save_intermediate_work': {
    'default': False,
    'type': 'boolean',
    'description': 'Zip and save working directory with intermediate files [default=false]'
  }
```

In this case the configuration option is the *key*, `'save_intermediate_work'`. When you run the gear you can set these options with a configuration dictionary. This shows us that we keys we can use in our gear run's configuration dictionary

```python
>>> config_save = {'save_intermediate_work': True}
```
or
```python
>>> config_no_save = {'save_intermediate_work': False}
```

If we were to not specify a value for `'save_intermediate_work'` it would be set to the value listed as `'default'`. In other words,

```python
>>> config_default = {}
```

is the same as using `config_no_save`.

It is likely you will want to figure out what options you want to use specifically for your analysis. The purpose of each config option can be found in the `"description"` field. Here is an example config object for a `qsiprep-hpc` gear run:

```python
>>> config = {
...     "hmc_model": "eddy",
...     "use_syn_sdc": False,
...     'save_outputs': True,
...     'dwi_denoise_window': 5,
...     'unringing_method': 'mrdegibbs',
...     'do_reconall': False,
...     'combine_all_dwis': True,
...     'force_spatial_normalization': True,
...     'output_resolution': 2.0,
...     'output_space': 'T1w',
...     'sloppy': False
... }

```

## Attaching objects to a gear

Sometime files need to be attached to a gear. These can be files from acquisitions or outputs from previous analyses. In the simplest case the input will be a file attached to the project container. The easiest way to find the file you're looking for is to loop over all the files attached to the project until you find the one you're looking for.

```python
>>> for index_num, file_obj in enumerate(project.files):
...     print(index_num, ":", file_obj.name)
0 : controllability.json
1 : license.txt
2 : sample_heuristic.py
3 : CHANGES
4 : README
5 : audit_log-20191003-184048.csv
6 : gear_testing_heuristic.py
7 : participants.tsv
8 : selfreport_scales_redcap_v2.R
9 : selfreport_scales_redcap_20190524_cleaned.csv
10 : selfreport_scales_redcap_v3.R
11 : grmpy_heuristic_v3.py
12 : audit_log-20200109-154752.csv
13 : GRMPY_selfReportScoringCode_v4.R
```

This shows which index each file is located at. So if we wanted to use `license.txt` as the FreeSurfer license, we could specify it in the inputs like:

```python
>>> inputs = {
...    "freesurfer_license": project.files[1]
... }

```

### Attaching analysis objects from another gear

Analysis gears store their results in a Flywheel data container. This container could be a Acquisition, Subject, Session or Project. If the gear was run using the SDK, there was a keyword argument `destination=`, which specified a data container object. Suppose the analysis used a session container as its `destination`.

## Specifying a VM size for a gear

Different analysis pipelines will require different computing resources. Some of these are queued on the Penn *High Performance Computing (HPC)* system. These will typically have a gear name that ends with `-hpc`. All other gears run on the *Google Cloud Platform (GCP)*. GCP can send your job to a custom-sized virtual machine to run. The size of the VM (i.e. number of CPUs, memory and hard disk size) can be specified using the `tags` keyword argument:

```python
>>> fmriprep.run(analysis_label=analysis_label, tags=['vm-n1-highmem-4_disk-300GB_swap-30G'],
...              config=config, inputs=inputs, destination=ses)
```

Here the `'vm-n1-highmem-4_disk-300GB_swap-30G'` tag is telling the FlyWheel gear executor to use a specific gear. A list of the available gears is:

 * `'vm-n1-highmem-4_disk-300GB_swap-30G'` a.k.a. `'large'`
 * `'vm-n1-highmem-8_disk-1500G_swap-60G'` a.k.a. `'extra-large'`
 * '`vm-n1-standard-1_disk-300G_swap-30G`' a.k.a.  `'small'`


## Launching gears on sessions

You may not want to run your gear on every session in a project. Instead, you can filter through subjects so the gear only runs on those with the scans you want. For example, to run your gear only on sessions that contain an acqusition with 'acq-64dir_dwi' in the name:

```python

>>> sessions_to_run = []
>>> for session in project.sessions():
...     has_dwi = 'acq-64dir_dwi' in [acq.label for acq in session.acquisitions()]
...     if has_dwi:
...         sessions_to_run.append(session)
>>> len(sessions_to_run)
1329
```

The sessions with a DWI scan will all be in the `sessions_to_run` variable. (Other useful methods for identifying specific sessions/subjects of interest are to index the sub name in session.subject.label or the ses name in session.label).

Now you can actually launch gears on these sessions.


```python

analysis_ids = []
fails = []
for ses in sessions_to_run:
    try:
        _id = fmriprep.run(analysis_label=analysis_label,
                          config=config, inputs=inputs, destination=ses)
        analysis_ids.append(_id)
    except Exception as e:
        print(e)
        fails.append(ses)

```

You should keep track of the ids. For example, you can write out the analysis ids and failed sessions to files.

```python

with open('{}_{}_{}_analysisIDS.txt'.format(fmriprep.gear.name,fmriprep.gear.version,now), 'w') as f:
    for id in analysis_ids:
        f.write("%s\n" % id)

with open('{}_{}_{}_failSES.txt'.format(fmriprep.gear.name,fmriprep.gear.version,now), 'w') as a:
    for ses in fails:
        a.write("%s\n" % ses)

```

## Checking gear output files and gear runs

You can check what output files have been created in association with a specific analysis id.

```python

#get first analysis id by indexing into analysis_ids
aa = fw.get(analysis_ids[0]) #or can simply use fw.get('insert_full_id_here')

#look at what files are associated with this analysis id
aa.files

#list files associated with this analysis id
for file in aa.files:
    print(file.name)

#get sub associated with this analysis id
aa.files[0].name

```

You can additionally check whether or not a specific output file of interest (for example, an fmriprep or qsiprep .html file) has been generated for a list of analysis ids.

```python

#define new function
def run_succeeded(idnum):
    obj = fw.get(idnum)
    return len([f for f in obj.files if f.name.endswith('html.zip')]) > 0

#check whether html file has been generated for all ids in analysis_ids
for aa in analysis_ids:
    print(aa, run_succeeded(aa))

```

This will return something like:

5e52d18a6dea315a592a740c True

5e52d18b6dea315a592a740e False

## Cancelling mistakes

```python

jobs = fw.jobs.find('state=pending,gear_info.name="fw-heudiconv",destination.type="analysis"', limit=2000)


for job in jobs:

  # You can insert some logic here to

  # restrict based on other criteria as well

  # This will cancel the job

  job.change_state('cancelled')
```

## Launching gears with a single python script

The commands presented above can be integrated into a script and called collectively in order to run an analysis gear. See an example script [here](https://github.com/PennLINC/PennLINC.github.io/blob/master/code/examples/run_qsiprep-fw-hpc.py).

## Be Mindful of Costs!

## Munging Through a Large List of Jobs

If you ran a large batch of jobs, perhaps many times over,
it's inevitable that you will need to filter through all
of the analysis objects to make sure your runs completed.
These runs could have different labels, inputs, dates, or
other information that would differentiate them. You can
use the SDK to look around and enumerate whose jobs ran
successfully.

To set up, you need to get a list of your session objects
(and you can filter this list as needed):

```python
>>> import flywheel
>>> client = flywheel.Client()

>>> proj_label = "" # INSERT YOUR PROJECT LABEL HERE
>>> proj = client.projects.find_first('label="{}"'.format(proj_label))
>>> subs = proj.subjects()

>>> sessions = []
>>> for x in subs:
...     sessions.extend(x.sessions())
```
Recall that each session object (or whichever object you
ran an analysis on) has its analysis attached to it. You
may need to do a deep-retrieve to unpack the object, with
`session = client.get(<OBJECT_ID>)`.

```python
>>> sessions = [client.get(x.id) for x in sessions]
>>> len(sessions[0].analyses)
23
>>> [(x.label, x.job.state) for x in sessions[0].analyses]
[('fmriprep_SDK_002258_2020-01-10_15:27', 'cancelled'),
 ('fmriprep_SDK_002258_2020-01-10_15:49', 'failed'),
 ('fmriprep_SDK_002258_2020-01-13_10:31', 'failed'),
 ('fmriprep_SDK_002258_2020-01-13_11:55', 'cancelled'),
 ('fmriprep 01/13/2020 13:14:05', 'complete'),
 ('fmriprep_SDK_002258_2020-01-13_15:56', 'complete'),
 ('fmriprep-hpc 01/30/2020 10:56:46', 'complete'),
 ('XCP_task-emotionid_acq-acompcor_GSR_2020-02-06 15:36:15', 'complete'),
 ('XCP_task-emotionid_acq-acompcor_2020-02-06 15:43:52', 'complete'),
 ('XCP_SDK_TASK_2020-03-25 12:45:43.779480', 'cancelled'),
 ('XCP_SDK_TASK_2020-03-25 14:43:08.904064', 'cancelled'),
 ('XCP_SDK_TASK_2020-03-25 14:43:27.599757', 'cancelled'),
 ('XCP_SDK_TASK_2020-03-25 14:43:57.121093', 'cancelled'),
 ('XCP_SDK_TASK_2020-03-25 14:45:23.378621', 'cancelled'),
 ('XCP_SDK_TASK_2020-03-25 14:49:00.296253', 'complete'),
 ('XCP_SDK_TASK_GSR2020-03-30 14:20:07.652910', 'complete'),
 ('XCP_SDK_NO_TASK_REGRESS_GSR2020-04-28 16:44:24.909264', 'complete'),
 ('xcpengine-fw 04/28/2020 21:36:55', 'complete'),
 ('XCP_SDK_NO_TASK_REGRESS_GSR2020-04-29 10:14:31.933739', 'complete'),
 ('XCP_SDK_NO_TASK_REGRESS2020-04-30 14:09:52.702180', 'complete'),
 ('XCP_SDK_NO_TASK_REGRESS2020-05-01 10:15:13.199642', 'complete'),
 ('XCP_SDK_NO_TASK_REGRESS2020-05-01 11:49:42.771475', 'complete'),
 ('XCP_SDK_NO_TASK_REGRESS2020-05-01 13:48:19.794610', 'complete')]
```
That's a lot of analyses, and there's no easy way of
deciding which is the "correct" one. But fortunately it's
possible to filter them using a little bit of Python
gymnastics.

So let's say we want to get the output of the most recently
completed `fMRIPrep`. We can use
the `analyis.label`, the `analysis.job.state` attribute, and a `datetime` sort to filter that:

```python
>>> filtered_fmriprep = [x for x in sessions[0].analyses if 'fmriprep' in x.label and x.job.state == 'complete']
>>> len(filtered_fmriprep)
3
```

That's already considerably easier. Now to get the most recent successful run, sort:
```python
>>> filtered_fmriprep.sort(key=lambda x: x.created)

>>> most_recent_fmriprep = filtered_fmriprep.pop()

>>> most_recent_fmriprep.label
 'fmriprep-hpc 01/30/2020 10:56:46'
```

Boom! Now you can get outputs and such just as you did in the above sections.

You can use any of the analysis object's attributes to
filter your list of analyses. They're listed here:
```python
>>> dir(most_recent_fmriprep)
...
'add_note',
'add_tag',
'alt_discriminator',
'attribute_map',
'child_types',
'container_type',
'created',                       # the best option for datetime sorting
'delete_file',
'delete_file_classification',
'delete_file_info',
'delete_info',
'delete_note',
'delete_tag',
'description',
'discriminator',
'download_file',
'download_file_zip_member',
'download_tar',
'file_ref',
'files',
'gear_info',                    # You can check the gear version number here
'get',
'get_file',
'get_file_download_url',
'get_file_zip_info',
'get_files',
'id',
'info',
'inputs',
'items',
'job',                         # more info on the gear run
'keys',
'label',
'local_created',
'local_modified',
'modified',
'notes',
'parent',                      # You can use this to see what container type this analysis is attached to
'parents',
'positional_to_model',
'rattribute_map',
'read_file',
'read_file_zip_member',
'ref',
'reload',
'rename_tag',
'replace_file_classification',
'replace_file_info',
'replace_info',
'return_value',
'revision',
'swagger_types',
'tags',
'to_dict',
'to_str',
'update',
'update_file',
'update_file_classification',
'update_file_info',
'update_info',
'upload_file',
'upload_output',
'values']
```

The `job` attribute records more internal affairs:
```python
>>> dir(most_recent_fmriprep.job)
...
'alt_discriminator',
'attempt',
'attribute_map',
'change_state',
'child_types',
'compute_provider_id',
'config',
'container_type',
'created',
'destination',
'discriminator',
'failure_reason',
'gear_id',
'gear_info',           # You can use this to check the gear version string
'get',
'get_logs',
'group',
'id',
'inputs',              # You can use this to get a list of your input data
'items',
'keys',
'label',
'local_created',
'local_modified',
'modified',
'origin',
'positional_to_model',
'previous_job_id',
'print_logs',
'profile',
'project',
'rattribute_map',
'ref',
'related_container_ids',
'reload',
'request',
'retried',
'return_value',
'saved_files',          # you can use this to get a list of output data
'state',
'swagger_types',
'tags',
'to_dict',
'to_str',
'transitions',
'update',
'values']
```

Use these attributes to filter strings, integers, datetimes -- whatever you'd like!
