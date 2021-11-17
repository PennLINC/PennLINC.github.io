---
layout: default
title: Data Extraction
parent: Meta-analysis
nav_order: 5
---

## 5. Coordinate data extraction
Data extraction involves two processes: extracting information about each experiment included and the coordinate data to analyze. Information about each study helps with assessing potential sub-analyses to conduct (for later use) while coordinate data is ALE’s input for analyses.

This stage of the process can last anywhere between 1-1.5 months.

### 5.1. Extracting experiment information
To start, go to your Google Drive project folder and create a spreadsheet titled **StudyInformation**. You should have the following columns:
  * Your first and second columns should be all the **citations** and **titles** of articles you’ve marked for inclusion.
  * The third column should be the **table, figure, or section of results you are going to extract coordinate data from**.
  * The rest of the columns will depend on the experiment information you will want to extract. Here are examples of past columns from pain:
    * **Sample size**: this would also be important for ALE analyses
    * **Coordinate space (MNI or Tal)**: you will also use this for ALE analyses. This can be tricky, but the information is generally in the coordinate data table, results section, or methods section under analyses.

In certain cases when this is unknown, we'd also extract the following:
* Patient condition
* Diagnostic procedure
* Patient medication status
* Stimulus modality (e.g., thermal, mechanical, electrical, or chemical pain)
* Location of stimulation

There’s no sure fire way to do this, so the best you can do is look for consistent pieces of information that keep popping up in each article. Make sure, however, that you use consistent names for categories of studies you’re noticing. For example, for every pain paradigm that used a stimulus related to temperature, we’d use the tag **thermal** for the modality column (rather than calling one experiment **thermal** and another **temperature related**).

### 5.2. Extracting coordinate data

This part is very straightforward -- you will just be extracting the X, Y, Z coordinates for each experiment included. The tricky part will come when you do sub-analyses. To set up here, go to your Google Drive project folder and create a spreadsheet titled [CoordinateData](https://github.com/PennLINC/Xu_fMRIChronicPain/blob/master/ale/painCoords_20200113.xls). Next, create the columns **Name**, **n**, **X** **Y**, **Z**, “Space”.
* **Name** refers to the citation of the experiment you’re extracting data from
* **n** refers to sample size (in patients vs. controls contrasts, use sample size of patients)
* **X,Y,Z** are the XYZ coordinates
* **Space** refers to whether the experiment used MNI or Tal.
* Lastly, have a column at the end that just says **Main**. This indicates that these coordinates will be used for your main analyses. The hyperlinked example above uses **abberant** to indicate analyses will be used for **abberant** analyses (which was the main analyses in the paper -- however, you can just use the tag **main**).

If an article has multiple relevant contrasts for your main analyses, combine all the contrasts together into one set of coordinates for the study. For example, if an article had 2 pain experiments of interest (one heat pain paradigm and another cold pain paradigm), I’d group the two coordinate sets together and treat them as one experiment.

#### Sub-analyses Coordinates
For sub-analyses, these coordinate sets will be separate. The best way to conduct sub-analyses will be to create another spreadsheet for each sub-analyses (e.g., [perceptualData](https://github.com/PennLINC/Xu_fMRIChronicPain/blob/master/ale/perceptualData_2020-01-21.xls)).

The only difference between your sub-analyses spreadsheets and the main **CoordinateData** spreadsheet is the sub-analyses will include more additional columns at the end called **Tags**. This just refers to how you categorize the experiment (e.g., **patient > control**, **control > patient**).

In the past, I’ve used one big spreadsheet for all sub-analyses, but this ended up becoming more of a mess than separate spreadsheets. If you did want to do one big spreadsheet, you can just add other columns like **Tag1**, **Tag2**, etc. to include other pieces of information. Just be careful not to double count experiments from the same paper when you perform certain sub-analyses. For example, if you have an all-female experiment with both a heat and cold pain paradigm, you would create 3 sets of coordinates
1. Heat pain only coordinates (with nothing in the other Tag columns except **heat**)
2. Cold pain only coordinates (with nothing in the other columns except **cold**)
3. All coordinates (with only the tag **female** in one column but nothing else in the others)).
This will allow you to use different coordinate sets for **heat** only, **cold** only, and **female** only sub-analyses.

You can refer to the [healthy pain meta-analysis coordinates](https://github.com/PennLINC/Xu_PainHealthy/blob/master/EickhoffALE/data/painHealthyCoords_20190426.xls) for examples of a big spreadsheet divided into separate sub-analyses.

Finally, make sure to keep count of coordinate datasets extracted and how many coordinate datasets you expect in each! You can do this in R by reading in the spreadsheet and these few lines of code:

```
# Main Coordinates

coordinateDataSet %>%
group_by(Name, n, X, Y, Z, Space) %>%
summarize(n())

# Sub-analyses Coordinates

subCoordinateDataSet %>%
group_by(Name, n, X, Y, Z, Space, Tag1) %>%
summarize(n())
```
