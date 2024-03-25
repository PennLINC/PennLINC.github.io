---
layout: default
title: Full-text Screening
parent: Meta-analysis
nav_order: 4
---

## 4. Full text screening

You will be doing full text screening offline on a spreadsheet in Google Drive (it will help later with filtering for records). You should expect this stage of the process to last for, at the minimum, 1.5 months, but on average, anywhere between 2-3 months, depending on the amount of papers to screen.

### 4.1. Setup

This setup creates a Google Drive folder that organizes the screened materials. You can refer to the [structural imaging chronic pain meta-analysis folder](https://drive.google.com/drive/folders/1syctHLpLzhEMUtkJZ7oSeYD34RhifYKl?usp=sharing) for an example.
1. Before going through full texts, create a **Screen** folder in Google Drive with the subdirectories **Ambiguous**, **Email**, and **Include**.  
  * These subdirectories will be where you put articles that you’re unsure about (ambiguous), you will email authors about later for more data (email), and you will include.
2. Next, create a spreadsheet to record the full text screening process. Here, you will create a spreadsheet titled [FullTextReview_[DATE]](https://docs.google.com/spreadsheets/d/1Jz-KXWTQtTDmV-IvvGW46NuCFnXEbHjqMcWppQ0MZBg/edit?usp=sharing) in the **Screen** folder.
  * To import your abstract records from Covidence onto this, go to the main page of your project. Click **Export**. Choose the Category **Full text review** and format **CSV**.
  * Now, in the Google Drive spreadsheet, copy the following columns from the exported CSV from Covidence: **Study**, **Tags**, and **Title**.
  * In the Google Drive spreadsheet, rename **Study** to **Citation** and **Tags** to **AbstractScreenNotes**. These will help identify articles and transfer any notes from the abstract screening process onto full text screening.
  * After, create the following headers to record decisions for full text screening: **Decision**, **ExclusionTag**, **AdditionalExclusionTags**, **Notes**.

You will now be using this spreadsheet to record full text screening. You can decide on which exclusion tags you want to use for recording reasons to exclude a study, but generally, the **Decision** column should contain either the decision to **Exclude**, **Include**, or **Email**. You can also put “Ambiguous” to highlight any full texts you’re unsure about (but change to another decision after).

### 4.2. Reference chasing previous meta-analyses
Before beginning full text screening, you should make sure to get references from previous meta-analyses or systematic reviews you’ve identified during the abstract screening process. Usually, there is a table of included papers in the review papers or this information is available in the supplementary section.
  * You should organize these included papers in a spreadsheet ([here](https://drive.google.com/open?id=1lU3IyLf3n4WCaKdhQAC93XbAb5K1g4toBfKZv7Nssn8) is an example).
  * After you’re done, copy over these the citation and title of these papers onto full text screening (you can take out duplicates later).
  * Make sure to note the number of records returned from this (and number of duplicates) since you will need this number for later.

### 4.3. Screening through full texts
For this process, you will sort full texts from the FullTextScreen spreadsheet to either **Include**, **Exclude**, or **Email** (authors for more data). These next few steps go through the process of deciding which tag makes sense and how to best document the process. As you go through papers, you should download any papers that you’re uncertain about, papers to include, and papers to email authors for more data. It can be brutal, but it can be made easier by developing a hierarchy of reasons to exclude an article.

#### 4.3.1. Decisions in the full text screening process
Here is the hierarchy of reasons to exclude that we applied when assessing articles for the structural imaging chronic pain meta-analysis (some may be applicable across all meta-analyses):

1. We first examined the **sample(s) studied**:
  * Did the patients in the patient group have a pain condition? If we weren’t sure whether a condition was classified as chronic pain, we asked the group for consensus.
  * Was there a control group -- and if so, were the controls healthy?
  * Were there at least 10 participants in each group?
2. Next, we examined whether there was our **measure of interest**. In this case, we were interested in structural MRI measures such as cortical thickness, surface area, gray matter density, VBM, etc. If the study only used DTI, task fMRI, or some other measure that didn’t include one of these measures, we excluded the study.
3. After, we read the methods section to look for information on whether the study did whole-brain analyses and whether the study used a statistical threshold that met our criterion. Here are examples of language to watch out for:
  * **Whole brain**: coverage of whole brain search comes at two levels -- the image acquisition stage or the analyses stage. If there’s uncertainty regarding whether a paper should be excluded on this basis, it is best to slack the channel for consensus.
    * Most of the time, a paper will say it “covers the whole brain” (not covering the cerebellum is ok). However, if it doesn’t cover the whole brain, it will say it optimized its imaging acquisition parameters to cover a certain brain area, leaving certain regions out of search. One example (taken from Müller et al., 2018) is language such as "started at the temporal pole up to the hand motor area."
    * A paper may also say it used a directed search mask, small-volume corrected threshold, or it only conducts ROI-based analyses. Be careful: some papers might not cover the whole brain in their primary analyses of interest, but they include additional analyses covering the whole brain.
  * **Statistical threshold**: If they mentioned either a voxel-height threshold of p < .001 or a cluster-corrected threshold of p < .05, we did not exclude the study on this basis. An example of a study that we would exclude would be the voxel-height threshold of p < .01 and cluster threshold of k > 10 (this means a cluster has to include greater than 10 nearby voxels). Experiments that don’t meet this criterion tend to be older studies prior to 2005.

If an article met any of the above conditions, we would label the article as **Exclude** in the decision column of the spreadsheet.

Finally, to consider an article for inclusion, we looked in the results section for the exact coordinates we would extract. This will sometimes be in a table, a figure (and/or its caption), or the Results section text. We then highlight this section and other relevant pieces of information from an Included paper we might want to extract later ([here’s](https://drive.google.com/open?id=1C-7BtK0dzSp4nhxKWY2uXr5xtoWt5ewc) an example paper).
  * *However*, sometimes an article might say they applied a certain type of analysis that we can use, but they did not provide the actual results. In this case, we should highlight this text and note this article as something to email the authors about. Label this article as “Email” in the decision column.

If an article can’t be conclusively classified as include/exclude/email, then note it as ambiguous.
