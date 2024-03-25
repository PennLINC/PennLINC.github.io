---
layout: default
title: ALE
parent: Meta-analysis
nav_order: 6
---

## 6. Activation Likelihood Estimation (ALE)
These [papers about ALE](https://drive.google.com/drive/folders/10P_qhwr1_x3HRewvobKyMs6hwvHQoWF1?usp=sharing), the [Healthy Pain GitHub Repo Wiki](https://github.com/PennBBL/Xu_PainHealthy/wiki/Xu_PainHealthy), and [fMRI Chronic Pain GitHub Repo Wiki](https://github.com/PennLINC/Xu_fMRIChronicPain/wiki) will be great resources for understanding this process.

ALE is the algorithm we use to quantitatively synthesize our coordinate data. Refer to the [methods section of our previous meta-analysis](https://www.sciencedirect.com/science/article/abs/pii/S0149763419308656?fbclid=IwAR3IrTUwZ_aP3FPhNhL51L1kgsOZE8rYXisKiloXoyqGiiRIuRSyBblhTEY) for more information and a brief summary on how this algorithm works. These instructions largely outline the steps taken in the previous two meta-analyses and highly refer to them for more information.

Depending on which analyses we decide to finally include, this stage of the process can last anywhere between 1.5-2 months.

### 6.1. Setup
(copied from [Healthy Pain GitHub Repo Wiki](https://github.com/PennBBL/Xu_PainHealthy/wiki/Xu_PainHealthy))

Prior to analyses, do the following:
1. Download all the scripts from [Healthy Pain GitHub Repo](https://github.com/PennBBL/Xu_PainHealthy/wiki/Xu_PainHealthy).
2. Create a main directory for your analyses and two other directories (1 named **clusterNifti** and another named **DataMatlab**). Put all the scripts into the main directory.
3. Download the [dependencies](https://github.com/PennBBL/Xu_PainHealthy/tree/master/dependencies/wrappers) directory into the main directory for analyses.
4. Download the [SPM](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/), [Anatomy Toolbox](https://www.fz-juelich.de/inm/inm-1/EN/Forschung/_docs/SPMAnatomyToolbox/SPMAnatomyToolbox_node.html), and [BrainNet](https://www.nitrc.org/projects/bnv/).
5. Move the folders associated with those files in the downloaded [dependencies](https://github.com/PennBBL/Xu_PainHealthy/tree/master/dependencies) directory.
6. In your main directory for analyses, download [EickhoffALE](https://github.com/PennBBL/Xu_PainHealthy/tree/master/EickhoffALE), [ExtractClusters](https://github.com/PennBBL/Xu_PainHealthy/tree/master/ExtractClusters), and [figureTemplates](https://github.com/PennBBL/Xu_PainHealthy/tree/master/figureTemplates).
7. Move your created directory **clusterNifti** into [ExtractClusters](https://github.com/PennBBL/Xu_PainHealthy/tree/master/ExtractClusters).
8. Move your created directory **DataMatlab** into [EickhoffALE](https://github.com/PennBBL/Xu_PainHealthy/tree/master/EickhoffALE).
8. Download *just* the **.nii** files used for computing ALE from this [link](https://github.com/PennLINC/Xu_fMRIChronicPain/tree/master/ale/MaskenEtc). Move this directory into **EickhoffALE/MaskenEtc**.
9. Download [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation).

*NOTE*: Preserving this directory structure will better ensure scripts work properly and results are in the expected locations.

After you’re done, create a folder in the **EickhoffALE** folder titled **DataMatlab** and another one named **DataRaw**. Leave these empty for now.

Now that you’re done with setup, download your coordinate data spreadsheets made from section 5 (Data Extraction) as a **.xls** file and move them to the **EickhoffALE** folder. You will next proceed to make a contrasts **.xlsx** file to define your analyses.

*Please note that EickhoffALE is named [ale]() in the [fMRI Chronic Pain meta-analysis GitHub repo](https://github.com/PennLINC/Xu_fMRIChronicPain) -- they are essentially the same scripts, just named differently!*

#### 6.1.1. Contrasts spreadsheet
You can find general information about this in the Eickhoff's documentation [here](https://drive.google.com/file/d/1qitRyyoJYwzjPe0D1p72uiYwGi-5ZJJP/view?usp=sharing).

The contrasts spreadsheet should model the [one from the fMRI Chronic Pain GitHub repo](https://github.com/PennLINC/Xu_fMRIChronicPain/blob/master/ale/pain_20200113.xlsx). Essentially, you will have the following columns on this spreadsheet:
* The first column that defines the name of the analyses you are conducting. It will also correspond to what your resulting meta-analytic map will be named.
* The next column will be the coordinate spreadsheet you are referring to. Note: You are ending it with **.mat** rather than **.xls** (e.g., **coordinateData.mat**). This is because when you input your spreadsheet, a **.mat** file will be made for MATLAB to easily read information about your coordinate data spreadsheet.
* The third column specifics what type of analyses you are conducting. Write `M` for main effects or `C` for contrasts (in this case, contrast means you want to look at the difference between two main effects maps).
* If you are doing `C`, then have the next row of the entry be the other effect you are contrasting the first one from (see example in spreadsheet).
* Put `+` for the fourth column. It just means you want the output to pop up as it runs. You can put `-` if you don’t want that.
Put the name of a tag for the fifth column. For example, if you are analyzing all pain studies, put “allPain” -- this refers to how you name this tag in the coordinate dataset.
* If you are conducting ROI-based analyses, put `$nameOfMask.nii` on this column (changing **nameOfMask.nii** to the actual name of the binary mask -- see section on **ROI-Based analyses** below). If you want to do both ROI-based analyses and main effects analyses, you can still put this in that column -- both analyses will be outputted.

Save this contrast spreadsheet in as a .xlsx file in the **EickhoffALE** folder.

#### 6.1.2. WINDOWS-SPECIFIC INSTRUCTIONS

These scripts are optimized for Mac OS. If you are operating from a Windows OS, you will need to follow these additional steps:
1. Download Visual Studio for C++: https://visualstudio.microsoft.com/vs/features/cplusplus/
2. Download additional documents specific to Windows in the Windows_Specific folder from the Chronic Pain fMRI GitHub Repo. Move these files into your **EickhoffALE** folder.
3. Run the following commands in MATLAB beforehand:
```
mex -setup
mex 'tfceMex.c'
mex 'tfceMex_pthread.c'
```
You are now all set for running the ALE scripts! One other caveat with Windows is you will need a way to unzip **.gz** files. We recommend the program WinRAR for this.

## 6.2. Running ALE
To run ALE, open MATLAB and follow the [runALE.m](https://github.com/PennLINC/Xu_fMRIChronicPain/blob/master/runALE.m) script found from the GitHub repo. Essentially, for each analysis, you will have one line that reads in the coordinate data input and another that actually analyzes what you’ve specified in the spreadsheet. Here is a break down of the code:

These few lines make sure all the proper directories are in your pathway.
```
myPath=genpath(pwd);
setup(myPath);
```
This line reads the coordinate data.  
```
ale_inputCoords(‘coordinateData.xls`);
```
And this one reads which spreadsheet to analyze.
```
ale_estimateALE('contrastsSpreadsheet.xlsx');
```

The output of these results are located in a new subdirectory named **ALE** in the **EickhoffALE** folder. These two functions can be found in the **Dependencies/wrappers** folder for more information (they essentially utilize the scripts in **EickhoffALE**).

### ROI-Based analyses

To conduct ROI-based analyses (i.e., looking at the ALE scores inside a search mask), do the following to create a mask:
1. Binarize the mask of interest using the following command:
```
fslmaths "NAME_OF_ORIGINAL_FILE.nii.gz" -bin "NEW_NAME_MASK.nii.gz"
```
2. Move the **NEW_NAME_MASK.nii.gz** outputted from the command into the **EickhoffALE** folder.
3. Unzip this file. You can just double click this in Mac OS or use WinRAR in Windows OS.

After doing these steps, as mentioned above, you can just add the `$nameOfMask.nii` column in your contrasts spreadsheet.

### 6.3. Outputs
The results will be saved in the folder ALE inside EickhoffALE. Here, you will find the following folders:
* **Contribution** -- this folder will contain text files with coordinates representing the center of gravity for significant clusters converging in activation. You will also see a percentage discussing the contribution of each experiment to the meta-analytic results. *If you see nothing here, that means you have null results.*
* **Results** -- this folder will contain your thresholded maps. Currently, all maps are thresholded at a voxel-height of p < .001 (uncorrected) but further cluster-corrected. We recommend using the map with the suffix **_cFWE05**, as this map contains maps that are also thresholded at p < .05 FWE-corrected at the cluster-level.
* **Foci** -- this folder contains maps showing foci (0 in regions without coordinate results reported and 1 in regions with coordinate results reported).
* **VolumeZ** -- this folder contains maps showing foci with the 3-D Gaussian kernel smoothed over. These are your unthresholded maps.
* **Contrasts** -- this folder contains maps of clusters showing significant differences between any between-experiment contrasts indicated in your spreadsheet (e.g., thermal pain vs. non-thermal pain).
* **Conjunctions** -- this folder contains maps of conjunctions showing overlap between any between-experiment contrasts indicated in the spreadsheet (e.g., thermal pain AND non-thermal pain).
* **ROIresults** -- if you conducted ROI-based analyses, you will find a **.ps** file and a **.pdf** file with the name of your effect of interest. Don't fret if you don't have the PDF file -- you can view a **.ps** file using any Photoshop viewer (several online) and just export it.
  * The left histogram in this file shows the observed sum of ALE scores within the mask compared to a null distribution of summed ALE scores randomly distributed across the brain. If this value is significant, this shows an overall set-level convergence.
  * The right histogram shows whether the maximum ALE score within the search mask exceeds the maximum ALE score (within the search mask) of a null distribution of random spatial distribution. If this value is significant, this indicates convergence at the voxel-level at some location within the mask.

### 6.4. What to Report

#### Significant Results
If you have significant results, you will want to follow the guide in [Healthy Pain Meta-analysis GitHub Wiki](https://github.com/PennLINC/Xu_PainHealthy/wiki/Xu_PainHealthy) for all your analyses, as we mainly use FSL to extract coordinates and statistics from significant clusters. Below is a brief outline of what to expect to report and where in the wiki information on this is discussed.

##### Main Effects

These refer to your meta-analyses of interest (e.g., main effect of pain, sub-analyses of thermal pain, etc.). Here, you want to have the following:
* **Peak voxel coordinates and statistics**. You first want to threshold and extract cluster statistics from your main effects images. These images end in the suffix **_cFWE05.nii** and are located in the **ALE/Results folder**. To do this, run a bash script similar to the one outlined in step 3 of the Healthy Pain Meta-analysis GitHub Wiki: [mainEffectsConjunctionClusters_20190328.sh](https://github.com/PennBBL/Xu_PainHealthy/blob/master/mainEffectsConjunctionClusters_20190328.sh). This extracts both the main effects clusters and any conjunction map clusters.
* **Anatomical or functional region labels** corresponding to the coordinates. You can use FSL to do this or Anatomy Toolbox.
  * To use FSL, complete the following steps:
    * Open your terminal and type in `fsleyes nifti_image.nii` while replacing `nifti_image.nii` with the thresholded map. You then want to also open up an MNI152 template.
    * Next, on the top of the whole computer screen, go to **Settings** > **Ortho View 1** > **Atlas Panel**.
    * You can now click around in your significant regions to find the labels corresponding to your significant areas (would recommend Harvard-Oxford Cortical and Subcortical Atlas).
  * To use Anatomy Toolbox, you can follow the steps in Section 4 (Anatomically Labeled Clusters) in the [Healthy Pain Meta-analysis GitHub Wiki](https://github.com/PennLINC/Xu_PainHealthy/wiki/Xu_PainHealthy).
    * This step involves using various scripts in the R project [ExtractClusters/clusterTexts/clusterText.Rproj](ExtractClusters/clusterTexts/clusterText.Rproj). If you go down this path, I would recommend extracting clusters from between-experiment contrasts first (see **Contrasts** section below) so that you can get the clusters from between-experiment contrast analyses, conjunction analyses, and main effects.
* **The image displayed on a brain**. You can create brain images using BrainNet for surfaces and FSL for axial views.
  * To create views in BrainNet this, You can make something similar to the script [painHealthyBrainFigures.m](https://github.com/PennLINC/Xu_PainHealthy/blob/master/painHealthyBrainFigures.m) to generate a lot of figures at once. This script calls several functions to create these brain images. If you don't have a lot of brains to display, you can just use the GUI version of BrainNet by opening `BrainNet` on the MATLAB terminal.
  * To create axial views, download a nice MNI152 template. Then, type in the following commands and you should be able to view this.
```
fsleyes INPUT_IMAGE.NII mniTemplate.nii
```

* **Peak voxel coordinates**. You can look at section 3, step 1 of the [GitHub Wiki](https://github.com/PennLINC/Xu_PainHealthy/wiki/Xu_PainHealthy) to use FSL to extract clusters. Output of thresholded nifti images from the positive and negative contrasts (separately) are in the created folder **ExtractClusters/clusterNifti/threshContrasts**.
* **Contribution.** You should report the citations of the individual experiments that contributed to the results as a supplementary file. You can find this information in the **Contribution** folder.


##### Contrasts

Contrasts refer to looking at the difference between two meta-analytic maps (e.g., thermal pain vs. non-thermal pain). You will more or less go through the same process as Main Effects. However, this step is tricky because we mainly used FSL to get the coordinates and statistics for the positive contrasts (i.e., thermal pain > non-thermal pain) and the negative contrasts (i.e., thermal pain < non-thermal pain).
* **Peak voxel coordinates and statistics.** Follow Section 3, step 2 of the [Healthy Pain GitHub wiki](https://github.com/PennLINC/Xu_PainHealthy/wiki/Xu_PainHealthy) to extract significant clusters from between-experiment contrast maps.
  * Output of thresholded nifti images from the positive and negative contrasts (separately) are in the created folder **ExtractClusters/clusterNifti/threshContrasts**.
  * You should now use the niftis located in **ExtractClusters/clusterNifti/fullThreshContrasts** while text files of significant results are located in **ExtractClusters/clusterTexts/thresh**.
* For anatomical labels, you can follow the same steps as Main Effects mentioned above.

##### Conjunction
* Conjunction analyses are saved in **Conjunctions**. If you used the same script as you did in Main Effects, you will get automatically get the conjunction results.

#### Null Results

The best wiki to follow for this is the [Chronic pain fMRI meta-analysis](https://github.com/PennLINC/Xu_fMRIChronicPain). If you have null results, you will want to show the distribution of foci as well as unthresholded z-maps in your paper. This will help assess where the origin of the null results may come from. *You may also want to consider conducting ROI-based meta-analyses if you see a cluster of regions in your unthresholded maps.*

##### Unthresholded Maps

Unthresholded maps are located in the **VolumeZ** folder. You can display them on surfaces using **BrainNet** in a similar manner as above.
* Load them as the **mapping image** and **BrainNet_ICBM152.nv** as the surface file.
* Threshold the image to positive values only for display. This is done by going to **BrainNet_Option** > **Volume** > **Display: Positive only**.

Axial view of images can be generated using fsleyes similar to above. Images should be thresholded to positive values only.

##### Distribution of foci

Foci can be found in the **Foci** output folder. You can display them in BrainNet by creating a **.node** file. To do this, complete the following steps:
1. Using your coordinate data, create a file of just your XYZ coordinates in a manner similar to [this file](https://github.com/PennLINC/Xu_fMRIChronicPain/blob/master/coordinates_20200131.csv).
2. Modify with your coordinate spreadsheet name and run [this script](https://github.com/PennLINC/Xu_fMRIChronicPain/blob/master/tal2mni_coordinates_20200131.m) to make sure your coordinates are all in MNI space.
3. Once you have the outputted spreadsheet, create three new columns next to the MNI coordinates.
  * In the first new column, type `1` for all coordinates. You can add modularity to this by using different numbers to define different categories. For example, we used `1`in the fMRI chronic pain meta-analysis to indicate "patient > control" contrast and `0` for all coordinates that are "control > patient" contrast.
  * In the second new column, type `1`.
  * In the third new column, type `-`.
4. After you're done editing the spreadsheet, copy and paste the MNI coordinates under the columns **mni_x**, **mni_y**, and **mni_z** into a text editor **as well as the three new columns generated**.
  * If you use TextEditor in MacOS, enter `command+shift+t` first to make it unformatted text editing.
  * Make sure to delete the column header (i.e., the first row that contains the column names mni_x, mni_y, and mni_z), and then save this file as **coordinates.node**.
5. You can now load this onto BrainNet. In BrainNet, choose **BrainNet_ICBM152.nv** as the **surface figure** and choose **coordinates.node** for **Data file (node)**. If you want modularity, under **Node** in Options, go to **Color** and choose the option **Modular**. In **Modular**, click **More** and select your desired colors.  
6. Finally, click "OK" and generate the figure.

To do create axial views in FSL, you will first have to dilate the foci using the following command in the terminal.

```
fslmaths INPUT_FOCI.nii -nan -kernel boxv 3x3x3 -dilD OUTPUT_NAME.nii.gz
```
You can then open the output of this in fsleyes and play with the colors.

### 6.5. Final Notes

If you're ever confused on where to start, always make sure to either read past papers, GitHub repo wikis, or this documentation! On a final note, in whatever way you can, I'd highly recommend you also make two important figures whenever you report your results:
1. **PRISMA chart**: You can easily find this online or edit a template on your own. This helps readers look at the flow from database search to meta-analysis.
2. **Table of included experiments**: Pretty self-explanatory. You can use the information from your data extraction of study information for this.  

Good luck!
