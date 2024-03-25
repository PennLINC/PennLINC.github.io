---
layout: default
title: Informatics Training
parent: Lab Basics
nav_order: 2
has_toc: true
---

# Informatics Training
{: .no_toc}

This page outlines the onboarding process for core informatics tasks, including data curation, analysis, and software development, and is particularly geared towards new data analysts or graduate students. 


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

# Core Competencies
{: .no_toc}

The core competencies of informatics are split into 4 major units:

1. [Programming & Software Tools](#unit-1-programming--software-tools)

2. [Data Management, Curation](#unit-2-data-management-curation)

3. [Processing pipelines](#unit-3-processing-pipelines)


The units are designed around the day-to-day tasks of Informatics team members, with different tasks utilizing a number of competencies from each of these units. In a perfect world, Informatics team members are experts in all 3 units, but in practice, your eventual expertise will depend on your assigned projects within the lab, along with past experience, interests, and desire to learn.

In the sections below, we outline each major competency by asking simple, task-based questions, and provide our best recommended resource for learning each of the competencies, as well as a glossary of (optional) secondary resources. There is an estimated time to complete these, but don't feel locked into these time-frames. If you have previously developed one of these skills before, and can confidently answer a question already, feel free to briefly skim the resource.

---

## Unit 1: Programming & Software Tools

Being a competent programmer is fundamental to computational neuroscience. While we outline our most frequently used programming languages below, it's important to remember that languages come and go — understanding the principles of programming is more important than spending hours memorizing one language's idiosyncrasies.

### The Command Line

Working from the command line is a **must**, as we spend a large amount of time on computing clusters like [PMACS](/docs/pmacs) and [CUBIC](/docs/cubic). Using  the command line is a skill with increasing returns, and benefits you more the better you get at it - don't get discouraged if it feels slow at first.

> Q: How would you create a directory from the command line, move files into it, and loop over its contents?

> Q: How would you check that a set of directories all have a specific type of file, even though all the files are named differently?

> Q: How would you record the text output of a program in a file?

> Q: How would you make sure your shell always loads with the correct paths to programs set automatically?

We recommend RyansTutorials.net (the [Linux](https://ryanstutorials.net/linuxtutorial/) and [bash scripting](https://ryanstutorials.net/bash-scripting-tutorial/) sections) for this competency (3-5 hours).

Other resources:

- [w3 schools](https://www.w3resource.com/linux-system-administration/linux-commands-introduction.php)


### Python

Python is a powerful all-purpose language for data science. It is particularly popular in neuroimaging due to its low skill floor and high skill ceiling/extensibility — you can do anything from simply adding two numbers together, to building deep learning neuroimaging pipelines.

> Q: What are the basic data structures in Python programming? How do they differ? What scenarios are appropriate for using one particular data structure in comparison to others?

> Q: How would you read in a table in Python? How would you loop over the rows in a table?

> Q: What is a `class`? How would you list all of the available methods of a `class`? What's the difference between a `class`' method and a `class`' attribute?

> Q: How would you run a Python program? How would you check for errors? What is a `traceback`?

We recommend [Coursera](https://www.coursera.org/learn/python-crash-course#syllabus) for this part (> 8 hours), although Python is a *very* common language with many resources available:

- [RealPython](https://realpython.com/start-here/)
- [Codecademy](https://www.codecademy.com/learn/learn-python-3)
- [A handy lookup repo](https://github.com/rasbt/python_reference)

> Bonus: Python environments can get complicated fast ([relevant xkcd](https://xkcd.com/1987/)); learn about Python environment management with Conda [here](https://towardsdatascience.com/devops-for-data-science-making-your-python-project-reproducible-f55646e110fa).


### R

R is a similarly popular data science language, but tends to favor a slightly narrower use case: statistical analysis. While it is well-equipped to handle myriad programming tasks, R really shines once you are ready to work on tabular data, run statistical anaylsis on experiments, plot beautiful graphs and figures, and produce high-quality reports. R is the go-to language for the statistics portion of any scientific endeavour.

> Q: How would you simulate a random sampling of numbers? How would you plot that sample in a histogram?

> Q: What is a `Dataframe`? How would you create one from a CSV file?

> Q: What is "tidy" data? The Tidyverse? What are "verbs" in tidy R parlance?

> Q: How do you run a multiple regression model, interpret its output, and graph the results?

> Bonus: [Why is R so weird?](https://twitter.com/WhyDoesR)

We recommend *either* Roger Peng's [R Programming for Data Science](https://bookdown.org/rdpeng/rprogdatascience/), *or* [R4DS](https://r4ds.had.co.nz/) by Hadley Wickham. Both are long, so for the sake of time, focus on sections 1 through 15 of Peng, and sections 1 through 21 of Wickham (> 8 hours). Getting through the entirety of either book, however, is well worth the time if you want to be very familiar with R.

Other resources:

- [Swirl](https://swirlstats.com/students.html), an interactive prompt-based learning package. The intermediate courses including regression and data cleaning are particularly useful.

- [learnR4free](https://www.learnr4free.com/index.html) and [this blog](https://livefreeordichotomize.com/2020/07/02/so-you-want-to-learn-r/) collate a number of external resources

### Git & Github

Version control with Git and Github is essential for managing reproducible science. The Informatics team handles all of their projects using git, and collaboration on large projects is accomplished primarily through Github Pull Requests, so fluency with basic git commands and familiarity with a Github-based workflow are daily requirements.

> Q: What is version control? What kinds of files are appropriate for version controlling software?

> Q: What is the difference between a `commit` and a `push`?

> Q: What is a `branch`? How could one use a `branch` to manage different ideas/experiments in code/analysis?

> Q: What is a Pull Request? Why is it useful for collaboration?

While git is essential, it doesn't take very long to learn, and the basics quickly become second nature. We recommend [this](https://www.youtube.com/watch?v=SWYqp7iY_Tc) Github crash course (1 hour).

Other resources:

- [HappyGitWithR](https://happygitwithr.com/)

- An additional [tutorial](https://zenodo.org/record/3369466#.X1OTrGdKjJ-) that people have found useful in the past

- More resources from github about git can be found [here](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources)


### Reproducible science

We rely on several tools that are essential for reproducible science. 

-  Analytic notebooks.  All analyses should be conducted within reproducible analytic notebooks, without exception.  The two most widely used are [Jupyter](https://realpython.com/jupyter-notebook-introduction/) and [Rmarkdown](https://rmarkdown.rstudio.com/lesson-1.html). 

- [Containerization with Docker](https://ropenscilabs.github.io/r-docker-tutorial/01-what-and-why.html) is essential for building reproducible software that can be deployed in any environment.  We try to have all subject-level data processing tasks executed by containerized software to ensure reproducability.


[Jump to top](#informatics-training)

---

## Unit 2: Data Management & Curation

This section introduces the basic data types in neuroimaging, how they are stored, and what software pipelines are frequently used for preprocessing. These competencies are particularly important for Informatics team members.

---
NOTE: Some resources in this section, such as AndysBrainBook, provide you with sample data to work through. On the other hand, others in this unit walk through hands-on tasks that won't be possible until you've been assigned a project in the lab. If this is the case, you can revisit these interactive portions later. Until then, please still watch/read along to develop some familiarity with the software and workflows being demonstrated.

---

### Introduction to MRI Modalities

A good foundation in the basic physics of MRI, and how the physics extends to different *modalities* of MRI, is essential:

> Q: What is magnetic resonance imaging? What is the BOLD signal?

> Q: What is the difference between a structural and a functional image?

> Q: What is diffusion in MRI? What is ASL?

We recommend [MRI physics with Dylan Tisdall](https://www.youtube.com/watch?v=SwsH64PBBZE) (< 1 hour).

Other resources:

- MRI Physics series with [Geoff Aguirre](https://www.youtube.com/channel/UCQ6zwRPkmDrZj9N6Inl8UZw)
- Diffusion imaging from [Albert Einstein College of Medicine](https://www.youtube.com/watch?v=dW8Yh-c2xVY&ab_channel=AlbertEinsteinCollegeofMedicine)
- Various sections of [AndysBrainBook](https://andysbrainbook.readthedocs.io/en/latest/index.html) (using the search bar for keywords)
- [MRIQuestions]() (using the search bar for keywords)


### BIDS

Brain Imaging Data Structure is a data storage standard for neuroimaging. It describes how best to format and store neuroimaging data (and why it's important to do so). PennLINC expects nearly all of its data, both internal and publicly shared, to be in BIDS format — much of the work of the Informatics team is making sure this goal is being met across different projects.

> Q: What are the benefits of using BIDS?

> Q: What modalities are currently covered in BIDS? What happens if the data you have isn't covered in BIDS?

We recommend learning about BIDS straight from the source: the [official BIDS specification](https://bids-specification.readthedocs.io/en/stable/) (< 1 hour). It's not necessary to learn the BIDS specification for each imaging modality by rote, though.

Other resources:

- [AndysBrainBook](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/BIDS_Overview.html)
  

### Curating data with CuBIDS

Curating a BIDS dataset is incredibly important and surprisingly challenging.  However, the curation process is required before data can be processed using the pipelines detailed below.  We developed and support dedicated software -- CuBIDS -- for this task.  

[CuBIDS paper](https://www.pennlinc.io/_files/ugd/46db66_27b4a2b6f76541a2a511a367235b54dc.pdf)

[CuBIDS docs](https://cubids.readthedocs.io/en/latest/)




## Unit 3: Processing Pipelines

Before hypotheses can be tested, neuroimaging data needs to be preprocessed. There are a number of tools for preprocessing — each is appropriate for a particular modality or scan type, and each has its own set of features and limitations. You'll get to work very closely with one (or many) of these pipelines once assigned a project, so basic familiarity with the tools suffices for now.

### fMRI Data

For fMRI, we recommend `fMRIPrep`. Start with [this primer on fMRI Preprocessing](https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_04_Preprocessing.html), explaining what the different steps for preprocessing are and why they're necessary; then, take a look at the official [fMRIPrep readthedocs](https://fmriprep.org/en/stable/) (or jump to [this section of AndysBrainBook](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep.html)) to see how `fMRIPrep` is run.

Additionally, check out the [Nature Methods paper](https://www.nature.com/articles/s41592-018-0235-4) written for the software.

### BOLD post-processing with XCP-D

After having run `fMRIPrep`, your BOLD data is successfully pre-processed.  However, several steps are still required to produce the derived data that we analyze.  For analysis of intrinsic functional connectivity (assessing which brain regions are working together over time), additional denoising (cleaning) of the data is necessary, as well as calculating these *functional connectivity* measures themselves.  These tasks (and MANY others!) are accomplished with XCP-D (e.g., the Extensible Connectivity Pipelines - DCAN collab).  An earlier version of the software -- `XCPEngine`-- was initially developed by lab alumni data analyst Rastko Ciric (now a bioengineering graduate student at Stanford), and was expanded and revised by Dr. Azeez Adebimpe.  Subsequently, XCPEngine was refactored as XCP-D by Dr. Taylor Salo, Kahini Mehta, and many friends at the University of Minnesota in collaboration with Dr. Damien Fair .  


Check out the XCP-D [preprint](https://www.pennlinc.io/_files/ugd/bdbf09_292d766fd35743108aa1615b5b21b66d.pdf) and [docs](https://xcp-d.readthedocs.io/en/latest/).  

To learn more about the original `XCPEngine`, check out the [benchmarking](https://pubmed.ncbi.nlm.nih.gov/28302591/) or [Nature Methods](https://www.nature.com/articles/s41596-018-0065-y) papers.


### Diffusion Data

For diffusion imaging, we recommend `QSIPrep`, developed primarily by Dr. Matt Cieslak (manuscript [here](https://www.nature.com/articles/s41592-021-01185-5)). Learn about `QSIPrep` at its official [readthedocs site](https://qsiprep.readthedocs.io/en/latest/).

### ASL Data

For diffusion imaging, we recommend `ASLPrep`<sup>[1](#myfootnote1)</sup>, developed primarily by Dr. Azeez Adebimpe (manuscript in preparation). Learn about `ASLPrep` at its official [readthedocs site](https://aslprep.readthedocs.io/en/latest/).

