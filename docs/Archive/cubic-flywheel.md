---
layout: default
title: CUBIC-flywheel
parent: archive
nav_order: 6
has_toc: true
---

## Installing the flywheel CLI tool

To install the Flywheel CLI tool on CUBIC, you will again need to be logged in as your project user and have a writable `.bashrc`. Now create a place to put the `fw` executable.

```bash
$ cd
$ mkdir -p software/flywheel
$ cd software/flywheel
```

Flywheel will complain if your version is out of date, so best to find the latest version and download that. You can find the latest version by [logging into flywheel](Upenn.flywheel.io). Once you've logged in, in the upper-right corner, select your account menu, and select Profile. Scroll down to the Download Flywheel CLI section, and you should see the latest version (e.g. 10.7.3). In the first line below, replace `<version>` with the version number you just found (e.g. `https://storage.googleapis.com/flywheel-dist/cli/10.7.3/fw-linux_amd64.zip`).

```bash
$ wget https://storage.googleapis.com/flywheel-dist/cli/<version>/fw-linux_amd64.zip
$ unzip fw-linux_amd64.zip
$ echo "export PATH=\$PATH:~/software/flywheel/linux_amd64" >> ~/.bashrc
$ exit
$ exit
$ sudo -u xcpdev bash
$ bash
$ fw login $APIKEY
```

where `$APIKEY` is replaced with your flywheel api key. You can find your personal api key in your account profile (same place you went for the version #) by scrolling all the way to the bottom.

## Checking that your python SDK works

After running the `fw login` command from above you can activate your `flywheel` conda environment and check that you can connect:

```bash
$ conda activate flywheel
$ python
```

and in python

```python
>>> import flywheel
>>> fw = flywheel.Client()
```

If there is no error message, you have a working Flywheel SDK!

## Finalizing your setup

After all these steps, it makes sense to return your .bashrc to non-writable mode

```bash
$ chmod -w ~/.bashrc
```

## Downloading data from flywheel to CUBIC

The following script is an example of download the output of a flywheel analysis to CUBIC

```python
import flywheel
import os

fw = flywheel.Client()

project = fw.lookup('bbl/ALPRAZ_805556') # Insert your project name here
subjects = project.subjects() # This returns the subjects that are in your project

# This is a string that you will use to partial match the name of the analysis output you want.
analysis_str = 'acompcor'

for sub in subjects:
    """Loop over subjects and get each session"""
    sub_label = sub.label.lstrip('0') #Remove leading zeros

    for ses in sub.sessions():
        ses_label = ses.label.lstrip('0') #Remove leading zeros
        """Get the analyses for that session"""
        full_ses = fw.get(ses.id)
        these_analyses = [ana for ana in full_ses.analyses if analysis_str in ana.label]
        these_analyses_labs = [ana.label for ana in full_ses.analyses if analysis_str in ana.label]
        if len(these_analyses)<1:
             print('No analyses {} {}'.format(sub_label,ses_label))
             continue
        for this_ana in these_analyses:
            """Looping over all analyses that match your string"""
            if not this_ana.files:
                # There are no output files.
                continue

            outputs = [f for f in this_ana.files if f.name.endswith('.zip')
                and not f.name.endswith('.html.zip')] # Grabbing the zipped output file
            output = outputs[0]

            # I am getting this ana_label to label my directory.
            ## You may want to label differently and/or
            ## change the string splitting for your specific case.
            ana_label = this_ana.label.split(' ')[0]

            dest = '/cbica/projects/alpraz_EI/data/{}/{}/{}/'.format(ana_label,sub_label,ses_label) #output location
            try:
                os.makedirs(dest) # make the output directory
            except OSError:
                print(dest+" exists")
            else: print("creating "+dest)
            dest_file = dest+output.name
            if not os.path.exists(dest_file):
                """Download output file if it does not already exist"""
                print("Downloading", dest_file)
                output.download(dest_file)
                print('Done')
```

We can run this script using qsub and the following bash script.
Providing the full path to python is important! Your path may be different depending on install location. Obviously the name of your python script may also be different.

```bash
#!/bin/bash
unset PYTHONPATH
~/miniconda3/envs/flywheel/bin/python download_from_flywheel.py
```
