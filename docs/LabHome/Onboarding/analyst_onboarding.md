---
layout: default
title: Informatics Training
parent: Lab Basics
nav_order: 2
has_toc: true
---

# Informatics Training
{: .no_toc}

The Informatics team plays a significant role in PennLINC's scientific engine. This page outlines the onboarding process for informatics work, including data curation, analysis, and software development, and is particularly geared towards new data analysts. The goal of this section is to provide the resources necessary to develop the **core competencies** for informatics at PennLINC. Note that there is no expectation that you master *all* of the competencies below in one sitting - just that you are familiar with how to go about accomplishing these tasks (or at least google your way through it).


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

4. [Hypothesis Testing & Analysis]() (Coming Soon!)

The units are designed around the day-to-day tasks of Informatics team members, with different tasks utilizing a number of competencies from each of these units. In a perfect world, Informatics team members are experts in all 3 units, but in practice, your eventual expertise will depend on your assigned projects within the lab, along with past experience, interests, and desire to learn. All team members should be quite familiar with the skills described in units 1 & 2, and because of the large knowledge base, team members tend to specialize in specific analytic pipelines (unit 3) and analytic techniques (unit 4).

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


### The Flywheel Imaging Database

Neuroimaging produces vast amounts of data.  Traditionally, this data was dumped onto a unmanaged file system, which created obvious problems for searchability, reproducibility, and scalability.  UPenn now uses the Flywheel platform, which allows data to be "reaped" directly from the scanner to a managed database environment.  Imaging data is stored in "projects", curated to BIDS specifications (see above), allowing containerized analytic pipelines to analyze the data in a fully reproducible manner.   

> Q: How is data in Flywheel structured? What are the relationships between different `containers`?

> Q: How would you view a particular scan on the website, given the session and subject labels? How would you find the same data programmatically?

> Q: How would you edit metadata for an entire collection of subjects?

> Q: What is a `gear`? How would you run `gears` (both on the website and programmatically)?

There are admittedly a large number of Flywheel resources that are not (yet) organized optimally. It's recommended that you follow the order below:

- [General overview](https://docs.flywheel.io/hc/en-us/sections/360001703554-Flywheel-Overview) and the [Overview Webinar](https://docs.flywheel.io/hc/en-us/articles/360044328514-Webinar-series-Intro-to-Flywheel) (1 hour)
- [SDK Webinar](https://docs.flywheel.io/hc/en-us/articles/360044853993-Webinar-series-Intro-to-the-Flywheel-SDK) (1 hour)
- [BIDS on Flywheel](https://docs.flywheel.io/hc/en-us/articles/360008162154-BIDS-Overview) (< 1 hour)
- [Running Gears](https://pennlinc.github.io/docs/flywheel/sdk_running/) (< 1 hour)


### BIDS Curation on Flywheel

As mentioned, a major task for the Informatics team is the curation of data into BIDS. This competency lets you to accomplish this on Flywheel using an internal tool called `fw-heudiconv`, developed and maintained by Tinashe Tapera.

> Q: What is a BIDS heuristic? How would you create a heuristic for `fw-heudiconv`?

> Q: How do you run `fw-heudiconv`?

> Q: How would you change something you've curated?

`fw-heudiconv` has been documented internally:

- [On readthedocs](https://fw-heudiconv.readthedocs.io/en/latest/overview.html)
- [On this site!](/docs/flywheel/bids/#step-by-step-bids-curation-with-fw-heudiconv)

(< 1 hour)

[Jump to top](#informatics-training)

---

## Unit 3: Processing Pipelines

Before hypotheses can be tested, neuroimaging data needs to be preprocessed. There are a number of tools for preprocessing — each is appropriate for a particular modality or scan type, and each has its own set of features and limitations. You'll get to work very closely with one (or many) of these pipelines once assigned a project, so basic familiarity with the tools suffices for now.

### fMRI Data

For fMRI, we recommend `fMRIPrep`. Start with [this primer on fMRI Preprocessing](https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_04_Preprocessing.html), explaining what the different steps for preprocessing are and why they're necessary; then, take a look at the official [fMRIPrep readthedocs](https://fmriprep.org/en/stable/) (or jump to [this section of AndysBrainBook](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep.html)) to see how `fMRIPrep` is run.

Additionally, check out the [Nature Methods paper](https://www.nature.com/articles/s41592-018-0235-4) written for the software.

### Diffusion Data

For diffusion imaging, we recommend `QSIPrep`, developed primarily by Dr. Matt Cieslak (manuscript in preparation). Learn about `QSIPrep` at its official [readthedocs site](https://qsiprep.readthedocs.io/en/latest/).

### ASL Data

For diffusion imaging, we recommend `ASLPrep`<sup>[1](#myfootnote1)</sup>, developed primarily by Dr. Azeez Adebimpe (manuscript in preparation). Learn about `ASLPrep` at its official [readthedocs site](https://aslprep.readthedocs.io/en/latest/).

### BOLD post-processing: Functional Connectivity & Task fMRI

After having run `fMRIPrep`, your BOLD data is successfully pre-processed.  However, several steps are still required to produce the derived data that we analyze. For task fMRI, for example, one post-processing step is running a general linear model that represents the task being done by the participant in the scanner. For analysis of intrinsic functional connectivity (assessing which brain regions are working together over time), additional denoising (cleaning) of the data is necessary, as well as calculating these *functional connectivity* measures themselves.  These tasks (and MANY others!) are accomplished by the eXtensible Connectivity Pipelines (`XCPEngine`).   `XCPEngine` was initially deveoped by lab alumni data analyst Rastko Ciric (now a bioengineering graduate student at Stanford), and has been revised, expanded, and maintained by Dr. Azeez Adebimpe.  Because it was one of the primary utilities developed to be compatible with fMRIPREP, it is currently widely used in labs around the world (with tens of thousands of executions per month). Learn more about `XCPEngine` at its official [readthedocs site](https://xcpengine.readthedocs.io/), or by reading the [benchmarking](https://pubmed.ncbi.nlm.nih.gov/28302591/) or [Nature Methods](https://www.nature.com/articles/s41596-018-0065-y)  papers.

[Jump to top](#informatics-training)

---

# Hypothesis Testing & Analysis

This section is currently still in development.

[Jump to top](#informatics-training)

---

# Epilogue

These *core competencies* detailed above may seem overwhelming. There is a lot of information and readers may be coming from different scientific backgrounds, with different levels of experience. Some of the terminologies used in neuroimaging can feel like jargon, and it doesn't help that PennLINC, and the University itself, may have their own unending lists of foreign words, phrases, tools, softwares...

*Don't panic*.

These resources are here for *everyone's* reference, and always will be. It's not expected that you will breeze through all of the above in one sitting, especially in addition to other lab-wide onboarding tasks. Instead, remember:

- **Work at a comfortable pace**: fast enough to get through the material, but not so fast that you don't get to appreciate the material.
- **Reach out for help**: don't spend so long on a problem that it consumes your entire day. The sites listed may not always be perfect resources for learning, and sometimes more assistance is necessary.
- **Google is your friend**: don't hesitate to go outside of our recommended list/glossary of resources when you come across a word you don't recognize or can't make sense of (see [MRIQuestions](http://mriquestions.com/index.html))
- **You'll get your hands dirty eventually**: it's normal to feel like you haven't developed a competency when you haven't yet actually *run* some of these tools and programs.
- **Contribute**: science gets better when we do it together. If you find a superior/additional resource for learning these competencies, or simply find errors that need to be fixed, don't hesitate to [contribute](/docs/Contributing/documentation_guidelines/) to this document.

# *Good luck!*
{: .no_toc}

---
<a name="myfootnote1">1</a>: Are you starting to notice a pattern? The reason for this is that *Prep* workflows are all built using a neuroimaging framework called [NiPype](https://nipype.readthedocs.io/en/latest/index.html); advanced users are encouraged to check it out.
