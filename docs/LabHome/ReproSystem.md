---
layout: default
title: Project Reproducibility Guide 
parent: Lab Basics
nav_order: 6
---


# PennLINC Project Reproducibility Guide 

### 1. Replication buddy. 

Identify a replication buddy at the start of the project.  This is usually the second or third author.  This is a lot of work, so replication buddy must “buy in” for real, and have approval of their direct supervisor.  The replication buddy should keep a separate folder in the project repo labeled “ReplicationCode” for all code used in the replication process.


### 2. Sample selection.

Make sure your sample selection procedure is written as code (not done manually), ideally in readable analytic notebook. This document should track what subjects are removed, for what reason, and what the composition of the resultant sample is as a result.   Write out the methods paragraph and the resultant demographics table at this point  This is one of the most common places error occur, which is particularly unfortunate as all downstream analyses are impacted by sample selection.  All QA files should be pulled from the data freeze folder for the study.

_True replication (first):_ buddy works from the text in the methods section and data freeze files to ensure that the subject list generated is the same.   This is usually <20 lines of code.
  
_Technical replication (second):_ buddy looks over code notebook to make sure it makes sense, and subject list is reproducible.


### 3. Subject level data.

Subject level data should always come from either a flywheel project where containerized gear have been run (better) or an approved data freeze (legacy data)
   
_Project lead re-replicates a small sub-sample of data._ In general, it is good practice to know where your data comes from if your name is first on the paper.  This can be as simple as executing the container/gear and making sure you get the same results for a handful of subjects, but ideally you should udnerstand how the pipeline works and was configured prior to being run. 

_Replication of additional derivatives._ Many papers require generation of additional derivatives that use data in the data freeze as input.  This step should be written in code, and replicated by buddy using well-commented code.  Data that is broadly useful across projects (e.g., networks, NMF components, etc) _should then be attached to  the flyhweel project (or data freeze) following replication_, with appropriate additional documentation as needed.


### 4. Initial Results.  

Once there is an initial finding that will form the basis for a paper, your buddy should replicate it.  This prevents a lot of work going into refining a story and writing a paper when an error has occurred.  This is subjective, so it is incumbent on project lead to be on the lookout for this “main result” as the project evolves.  As before, write the methods paragraph for this so buddy can perform both a true/complete and technical replication.  

_True replication (first):_ analysis result is replicated from methods section with new code written by replication buddy.  This may not be possible for truly complex / novel analytic tools, but that is a special case, and often reflects poor coding / documentation.

_Technical replication (second):_ buddy looks over analysis code (ideally as a RMarkdown file) to make sure it makes sense, and executes it to check that the main result is fully reproducible. Feedback on code readability is key. 


### 5. Final Results.  

At this point, the paper is approaching final form.  The project lead should have a detailed wiki that allows the replication buddy to perform all steps below with minimal interaction / questions of the lead.  As the wiki and code from the repo will be submitted with the paper, it is critical that this be carefully edited and curated to ensure broad readability.  This may require cloning the repo and using a very slimmed down version of it (that does not include as much "junk" as main project before results were finalized). The replication buddy should focus on true replication of one (or more) selected major final findings, technical replication of all findings, and provide detailed comments on code/wikis prior to submission.  

_Verify input data stability._  It is obvious that replication won't work unless nothing has changed in code used for subject selection or subject-level data processing.  This of course would invalidate the steps taken above.  It is *critical* for project lead and buddy to jointly verify this, as this is a common source of error.

_True replication of major findings._  Often, true/complete replication of all findings using de novo code is difficult.  Thus, the project lead and faculty supervisor should identify a handful of key results to be replicated with new code.  This may be the same analyses as for the initial results (above) but often things small changes to the analyses have occurred since the initial findings—so it is good to check.

_Technical replication and review of all findings._ This should be as comprehensive as possible.  Given that an error in figure 7B still leads to an errata (esp if broadcast on twitter), it is in all of our interest to make sure that all results are fully reproducible.  

_Feedback on code and wiki._  The buddy should provide detailed feedback on the wiki and code. As technical replication is attempted, detailed notes should be left as new comments in the code/wiki where there is any lack of clarity.  
 
