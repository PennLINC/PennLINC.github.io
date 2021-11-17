---
layout: default
title: Regional Quantification
parent: Tutorials
nav_order: 1
---


# Regional Quantification with NiLearn

## Author: Ellyn Butler

## Updated: May 7, 2021

## Replicator: TBD

## Goal: Quantify regional values using NiLearn

## Input data: Two 3D niftis in the same space, one a labeled image, and the other a modality that needs to be quantified

## Output: A numpy array of regional values in ascending order according to their index as defined in the labeled image

This tutorial demonstrates how to quantify regional values in an atlas. You will need a labeled image in the same space as the modality you want to quantify regionally. Here, I use a cortical thickness image as an example.

This tutorial is based on the quantification portion of the [antslongct](https://github.com/PennBBL/antslongct/blob/main/quantifyROIs.py) pipeline.

1. Load required libraries

```
import sys
import nibabel as nib
import pandas as pd
import numpy as np
import nilearn
from nilearn.input_data import NiftiLabelsMasker
```


2. Declare dummy subject and session labels

```
# You should provide as command line inputs for your own script
sub = 'sub-101'
ses = 'ses-STUDY1'
```

3. Load the labels in the subject's T1w space

```
atlas = nib.load(sub+'_'+ses+'_DKTlabels.nii.gz')
```


4. Load the image that needs regional quantification (cortical thickness here)

```
cort = nib.load(sub+'_'+ses+'_CorticalThickness.nii.gz')
```


5. Load the index to region name mapping

```
dkt_df = pd.read_csv('mindboggleCorticalLabels.csv')
```

6. Rename columns to be python-friendly

```
dkt_df = dkt_df.rename(columns={"Label.ID": "LabelID", "Label.Name": "LabelName"})
```

7. Get the integer values that correspond to each region in the DKT atlas

```
ints = dkt_df.LabelID.values
```

8. Get the names of the regions

```
names = dkt_df.LabelName.to_numpy()
names = [name.replace('.', '_') for name in names]
```

9. Load the labeled image and fit the masker object

```
masker = NiftiLabelsMasker(sub+'_'+ses+'_DKTIntersection.nii.gz')
masker.fit()
```

10. Quantify regional values!!!

```
cortvals = masker.transform(sub+'_'+ses+'_CorticalThickness.nii.gz')
```

11. Create column names

```
cort_names = ['mprage_jlf_ct_'+name for name in names]
colnames = ['sublabel', 'seslabel']
colnames.extend(cort_names)
```

12. Create a vector of values for the session's row in the csv

```
vals = [sub, ses]
vals.extend(cortvals.tolist()[0])
```

13. Output data as a csv

```
out_df = pd.DataFrame(data=[vals], columns=colnames)
out_df.to_csv(sub+'_'+ses+'_struc.csv', index=False)
```
