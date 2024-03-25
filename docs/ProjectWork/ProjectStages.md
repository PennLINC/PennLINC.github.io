---
layout: default
title: Stages of a Project
parent: Projects
nav_order: 2
---

# Stages of a Project at PennLINC

There is no such thing as a "quick" scientific project.
All projects take careful planning and follow a stereotyped process.
Understanding the life cycle of a project is critical for ensuring feasibility, avoiding surprises, and maximizing fun.
Given how long any project takes (approx ~1y minimum) it is essential that every project be carefully thought-out to justify the investment.
As ever, the most important question is "What is the question?"


### 1)	Set up the infrastructure

Each project in the lab has a well-defined infrastructure.
See relevant pages, including:

1. [Project setup overview](/docs/LabHome/ProjectSetup/)
2. [Project setup on CUBIC](/docs/cubic)
3. [Project reproducibility guide](/docs/LabHome/ReproSystem/)
4. [Guide to weekly project meetings](/docs/LabHome/ProjectMeetings/)


### 2)	Define initial hypotheses

The ultimate impact of any project is largely determined by the question being asked.
Spending two years chasing down the answer to a question that is not very interesting is a recipe for disappointment.
Start broad (“forest”) and try to identify questions at a conceptual (rather than methodological) level that are likely to be of broad interest to the field.
It is good to write this down at this stage, even if it is muddy and needs refinement.
Strongly consider pre-registration on OSF and prospectively identify potential replication datasets.


### 3)	Conduct a literature review

This step is skipped at one’s peril.
Nothing is worse than sitting down to write a paper and then realizing only at that late stage that the question was largely answered by a study you were not aware of.
A literature review also is critically important in sharpening hypotheses in order to maximize the potential impact of the question being asked.
As the first author, it is important to internalize that you need to rapidly become the expert on the topic of the project—do not trust your faculty mentor to be aware of all relevant literature.
Often the whole reason for a new project is that it is a new area that the faculty member is not an expert in.
Try to be comprehensive at this stage, and use a reference manager to stay organized.
Reading abstracts and examining figures is a way to rapidly get the sense of a new field.
This broad overview is usually followed by an extremely detailed examination of the most relevant half-dozen articles.
All literature reviews should be conducted using a reference management system.
Many in the lab prefer Zotero (and our documentation references it specifically).


### 4)	Sharpen hypotheses and outline testable predictions in an analysis plan

As noted above, the “what is the question?” is always the most important question.
At this stage, the over-arching hypothesis should be able to be concisely stated.
It is a good idea to literally write this down, as it will appear in the last paragraph of your introduction.
Next, one needs to operationalize how this hypothesis will be tested according to specific predictions that are linked to a defined analytic plan.
It is useful to imagine that everything in the study “works” and you get your dreamt-of results.
What tests do you need to do to generate these results?


### 5)	Prospectively identify collaborators & co-authors

Authorship on papers is a frequent source of conflict in other labs.
The best way to avoid conflict, enhance transparency, and accelerate collaborations is to identify collaborators who will be co-authors on the final paper prospectively.
An important q is: Who do you need involved to get this project done?
Explicitly inviting someone to collaborate rather than just peppering them with questions will often help things go smoother.
While the number of collaborators may grow (a bit) as the project develops, most of the time most collaborators are fairly obvious from the beginning.
Do not be afraid to discuss author order on large collaborative projects with the faculty lead (if they do not bring it up prospectively-- which they should).
At a minimum, the first, second (usually: your replication buddy, see below), and last author should be identified at the start of a project.


### 6)	Identify a replication buddy

The lab standard is now to release all analysis code.
To ensure reproducibility, all results should be replicated by an independent member of the lab at multiple stages (see below).
The replication buddy should be involved in the project from the beginning, and usually is the second author on the paper.
This is a lot of work and should not be taken on lightly; also think ahead for a long project and ensure that the buddy will be present in the lab for the anticipated duration of the project.
See the [Project Reproducibility Guide](/docs/LabHome/ReproSystem) for more information.


### 7)	Assess data availability & ensure data access

Before one spends too much time on a project, one should ensure that the necessary data is available.
This step arguably should come earlier.
Much of the impact of a paper is determined by the sample size; small samples reduce statistical power and preclude many methods being used.
In particular, pay attention to key subject level variables such as demographics, symptom scores, diagnoses.
If the imaging data has already been processed and QA’d, it is a good to check how big your sample will be after QA (see also “inclusion criteria and sample construction” below).
Finally, note that all projects should receive explicit written approval from the study PI who collected the data prior to beginning.
For the PNC, this includes approval of the data access committee, which meets once per month; please account for this process with regards to timeline / deadlines.


### 8)	Process & QA imaging data

If data has not already been processed, this is an important and sometimes time-consuming step.
We prefer a highly-structured process for image processing to ensure reproducibility using XCP-based modules whenever possible.
See XCP documentation for further information (this is a bit of a work in progress at the moment).
Note that a sub-sample (usually n~10) of subject level data should replicated, and the main subject-level derivatives produced by the pipeline should be placed in a read-only data freeze for the dataset.
For most projects, analyses should only use replicated data that is pulled directly from this data freeze folder.
See the [Project Reproducibility Guide](/docs/LabHome/ReproSystem) for more information.


### 9)	Clearly define inclusion criteria and construct sample in a reproducible manner

It cannot be over-emphasized how critical this step is, as changes in the inclusion criteria will inevitably require re-doing all analyses as the sample changes.
Similarly, the reproducibility of results depends on the reproducibility of the sample selection procedure.
Thus, this step should use code to pull in data from the data freeze folder, and arrive at the final sample by filtering the data using clear QA codes.
It is a good idea to explicitly go over this step—and the code—with both your replication buddy and the faculty mentor.


### 10)	Data analysis and documentation

This stage is usually the longest, and varies considerably by project.
Regardless, organization pays off: keeping code clean + well commented, keeping all code on GitHub.
Updating your project repo daily guards against both lost work or the risk of nasty code excavation job at the replication stage (next).
In general all analytics should use reproducible, well commented notebooks.


### 11)	 Replicate interim results

As detailed in the [Project Reproducibility Guide](/docs/LabHome/ReproSystem), once a “main result” that will be the organizing hook for a paper is revealed, it is a good idea to call your replication buddy.
Cleaning your code and having them provide both a “true” replication (taking input data and running a model with their own code) and a “technical” replication (i.e., stepping through your code) is advised to make sure errors are caught before a paper is written.
(Often, around this stage, a project is presented at a conference—see the conference wiki for more information).


### 12)	 Paper first steps: abstract & figure outline

The scientific narrative of a paper should be readily apparent from the abstract and figures.
Before deciding that analyses are “done” it is good to write the abstract and make an outline (in text) of what the figures will show.
Often times this step reveals that something is missing, and one or two more analyses need to be done.


### 13)	 Create draft figures

It is often good to create draft figure panels for the entire paper before polishing them to high gloss for publication.  These figures should be made reproducibly so they can be replicated (in the next step).  Making beautiful final figures before replication is not efficient. Bottom line?: Initial draft figures should be reproducible rather than gorgeous.


### 14)	 Final reproducibility check: Clean code, make GitHub repo, companion wiki, and replicate final results

At this step, one has all the code and results in hand.  Before writing (or as it begins), it is important to make a clean GitHub repo that will be submitted with the paper, along with a companion wiki that patiently steps interested readers through this code and allows them to reproduce your work.  Once this is complete, send the wiki and repo to your replication buddy, who will check your work (see [Project Reproducibility Guide](/docs/LabHome/ReproSystem)).   Note that it is imperative to repeat this process if results change in the writing process below; analyses added at a late stage when one is trying to get the paper out the door tend to be more likely to be problematic.


### 15)	Make final figures & write text

It is strongly suggest reading this article by Konrad Cording prior to starting your paper: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619.

For writing style, we tend to prefer our prose to be "clear" over "pretty".  For a great book on clear writing, I strongly reccomend "Writing for Busy Readers" by Todd Rogers & Jessica Lasky-Fink; Ted is happy to buy team members a copy.

In general, the workflow for paper review that we follow is below.  While a given step is "on Ted's Desk", it makes sense to work on the next step. In general, it is strongly preferred to jointly review an outline for each section before the text is written.

1) Review abstract + figures + figure legends.
3) Methods section
4) Results section
5) Introduction
6) Discussion

In general our papers tend to have a lot of co-authors so writing the paper in either a google doc OR microsoft word online is suggested.
This will make the process of integrating co-author changes much less painful; we discourage distributing word docs as an attachment.


### 16)	Polish text with faculty mentor

Experience suggests that the number of draft iterations is one of the dominant factors in how good the final text of a paper is.
Expect 3-5 rounds of revision of the text with your faculty mentor prior to sending the paper to co-authors.
Typically, Ted will send ~2 rounds of "bubble comments" before  text edits are tracked.
Tracking changes and careful version control at this phase is of course key.
Saving paper versions with a date suffix (in format YYYYMMDD) and co-author comment suffix (in format `_tsComments`) tends to help.

### 17)	Send to co-authors and integrate feedback

Once you and Ted sign off on a draft, it is time to send it to co-authors.
Here is an example email-- there are several key elements including target journal, timeline, funding acknolwedgments, conflict of interest / disclosures, and written approval.
When sending co-authors the paper as a google doc, just be explicit that they are to track changes using the "suggesting" mode (screenshots are helpful to include!).

```

Hi everyone!


We are excited to share with you and get your feedback on `Manuscript Title`.
Many thanks to everyone for the huge collaborative effort here.
Given the many contributors, we are distributing this manuscript as a google doc to help with version control.
We kindly ask for your effort on several things:


* Please track changes: please ensure that you are in “suggesting” (not “editing”) mode (see box in upper right of toolbar as well as screenshot below).

* Please check if your name and affiliations are correct on the title page

* Please add any relevant funding sources to the "Acknowledgements" section

* If you have any competing interests to declare, please add them to the "Declaration of interest" section

* Even if you don't have any comments, we nonetheless request ask you to reply to this email with your written approval.


We ask that you submit your feedback in the next 14 days. Once we have integrated your feedback, we will submit this a preprint (to BioRxiv) and then to `Journal X`.
If more time is needed, please just reach out and let us know.

Here is the link to the manuscript {insert link}; again, please switch to "Suggesting" mode to track changes.

```

We usually allow ~1-2 weeks for co-authors to provide feedback on a paper.
For those who do not reply in the specified window, usually the faculty lead will send a reminder email.


### 18)	Submit paper, code, & post on a preprint server

After (typically) years of work, you are now ready to submit the paper.
One reminder is that the final built PDF should be proof-read many times.
Egregious formatting errors or typos are often caught at this stage.
Furthermore, pay careful attention to the quality of the figures in the built PDF.
Note that if figures are large, the journal will downsample these considerably when making the PDF.
Note that many reviewers will not click on the “high resolution figure” link available to them—they will just use what is in the built PDF.
It is a bummer when we work hard to make gorgeous figures, and then what the reviewers see are poorly rendered due to downsampling.
While this depends in part on the figure type that the journal accepts, one way around this is to submit figures as compressed PDFs—there is free software available for this.
Once the paper is submitted to the journal, it is a good idea to put it on a preprint server as well (arxiv, biorxiv, etc; NB: biorxiv does NOT allow you to remove preprints—only update them).
Use of preprints will help generate enthusiasm for the work even while it is stuck in peer review, prevent others from “scooping” you (esp w/ public datasets), and also increases transparency.
Feel free to tweet the link when it is up.

As noted above, it is the lab standard to submit all analysis code (in the form of a GitHub repo) along with the paper.
Please make sure the repo submitted with the paper is *clean*, and does not include old code for parts of the project that did not pan out / were not included in the final manuscript.
Including old code is a good way to confuse reviewers and others interested in reproducing your work.
One way to do this is to make a new public repo that only uses a subset of code from the original working repo.

Please advertise new preprints on Twitter, and post them on the main pennlinc.io publications page; see instructions in the #pennlinc_website channel on slack (pinned).


### 19)	Revise & resubmit / Repeat as needed

Peer review is a slog: there is no way to spin it otherwise.
To use a football analogy, the first submission is like being on the 20-yard line—certainly not the 1-yard line.
Dogged persistence and a thick skin is critical for navigating peer review.
In general, it is almost always better to “show them with data” and perform any additional analyses requested.
Even if rejected, it is generally useful to try to address the reviewers’ comments in the subsequent (new) submission, as it is quite possible you will get the same reviewer at the next journal.
This stage is often the part of the project that requires the most intense work in order to meet revision deadlines.
Quick turn-around for revision and resubmissions is very important to prevent the project from stalling.


### 20)	Celebrate and disseminate

Congrats! Your paper was accepted.
Next, make sure it reaches as many eyes as possible, through mechanisms especially twitter; updating the thread from when the preprint went up is usually a good idea.
Make sure the final version of the paper is posted on the pennlinc.io "publications" page (see the #pennlinc_website slack channel).
