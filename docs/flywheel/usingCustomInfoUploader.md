---
layout: default
title: Custom Info Uploader
parent: Flywheel
nav_order: 6
has_toc: false
---
# General Custom Info To Flywheel Uploader

 This script takes as input a CSV file with the following characteristics:
 1. No Protected Health Information (PHI) in the file
 2. All columns are named
 3. The subject ID column is named "bblid"

 It then organizes the data into dictionaries and uploads it to each subject's Custom Info field on flywheel. The script can be called in the terminal by doing:
```
python customInfoUploader.py -d path/to/CSV -p name_of_project -n dict_name
```
For example, to upload data in a csv called "flavortown.csv" to my "GUY_FIERI" project on flywheel as a custom field called "recipes" I would do:
```
python customInfoUploader.py -d flavortown.csv -p GUY_FIERI -n recipes
```

*NOTE: Prior to uploading, please sign into a flywheel session in your environment. See here for instructions: https://flywheel-io.github.io/core/branches/master/python/getting_started.html*

See below for the script. You can also find it here: https://github.com/diegodav/general_customInfoUploader/blob/master/customInfoUploader.py

```
#####################################################################################
####                           Custom Info Uploader                              ####
####                           By: Diego G. Dávila                               ####
####                            Satterthwaite Lab                                ####
####               University of Pennsylvania School of Medicine                 ####
#####################################################################################
#
# This script takes as input a CSV file with the following characteristics:
# 1. No Protected Health Information (PHI) in the file
# 2. All columns are named
# 3. The subject ID column is named "bblid"
#
# It then organizes the data into dictionaries, and uploads it to each subject's Custom Info field on flywheel.
#
# The script can be called in the terminal by doing: python customInfoUploader.py -d path/to/CSV -p name_of_project -n dict_name
#
# *NOTE: Prior to uploading, please sign into a flywheel session in your environment. See here for instructions: https://flywheel-io.github.io/core/branches/master/python/getting_started.html


import sys
import csv
import numpy as np
import pandas as pd
import os
import argparse
import math


# Set up argument parsing for the required inputs
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--data', required = True) # the csv containing data
parser.add_argument('-p', '--project', required = True) # the name of the project you're uploading to
parser.add_argument('-n', '--name', required = True) # the desired name for the dictionary
inputs = parser.parse_args()

# Feed in the user inputs
path2data = inputs.data
project = inputs.project
name = inputs.name

# Read in the data
customData = pd.read_csv(path2data)

#turn the bblid field into string
customData.bblid = customData.bblid.astype('str')

# make the bblid column the index
customData.set_index('bblid', inplace=True)

# Turn the scored data.frame into a dictionary
fullDict = customData.to_dict(orient = 'index')

# Loop thorugh the newly created dictionary, and nest all the fields in their own dictionary for each subject
for x in fullDict:
    fullDict[x] = {'{}'.format(name): fullDict[x]}

# Replace NAs - uploading NAs to flywheel interferes with the GUI and makes objects not visible. This function replaces them with None, which flywheel should be able to handle.
def iter_replace_dict_nans(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, dict):
            iter_replace_dict_nans(value)
        elif pd.isna(value):
            input_dict[key] = None
iter_replace_dict_nans(fullDict)


## Attach To Each Subject On Flywheel ##
# Create an instance of flywheel and containers for sessions and subjects
import flywheel
projname = '{}'.format(project)
fw = flywheel.Client()
projectContainer = fw.projects.find("label={}".format(projname))
projectContainer = projectContainer[0]
sessions = projectContainer.sessions()
subjects = projectContainer.subjects()


#Attach the dictionaries to the appropriate session objects
for i in range(len(subjects)):
    bblid = subjects[i].label.lstrip("0") # removes any leading zeros there may be
    if bblid in fullDict:
        try:
            subjects[i].update_info(fullDict[bblid])
        except AssertionError as y:
             logger.setLevel(logging.DEBUG)
             logger.error("Subject not found.")
             logger.error(y)
        print ("Uploading {}'s Info".format(bblid))
    else:
        print('{} was not uploaded because it was not found in the input csv'.format(bblid))
```
