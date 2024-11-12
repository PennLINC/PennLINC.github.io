---
layout: default
title: Project Setup
parent: Lab Basics
nav_order: 4
---

# PennLINC Project Setup Guide

Each project at PennLINC has several key elements to facilitate collaboration and ensure reproducbility.
For clarity in naming, all elements should be named similarly-- often ```Lastname_ProjectName``` with CamelCasing,
where "Lastname" is the last name of the first author / trainee leading the project.
Links to much of the relevant software can be found in the lab [Software and Environments](https://pennlinc.github.io/docs/Basics/basics/) page.

## CUBIC Project Request
To request project space on CUBIC, you first need to submit a [New Project Request ticket](https://cbica-portal.uphs.upenn.edu/rt/SelfService/CreateTicketInQueue.html) ("Cluster - New Project" ticket). You must already have a [CUBIC account](URL HERE) to begin this process.

Before submitting this ticket, do the following:
- Send Ted an email requesting permission, even if he has already has given you permission verbally. This doesn't have to be long, just something like "I am writing to request permission to create [Project Name] on CUBIC." Ted will respond, approving this request. **Save a screenshot of Ted's response email**.
- Prepare a Data Management plain text (`.txt`) file (see below). You can draft this in Microsoft Word and save as plain text.

```
Project Name: [PROJECT NAME]						Date: [DATE]
Project PI: Satterthwaite
Data Manager (allowed to request quota changes): [FULL NAME] ([CUBIC NAME])
Users with write access (by login name): [ALL CUBIC NAMES OF MEMBERS NEEDING ACCESS FOR READ+WRITE]
Users with read-only access (by login name): [ALL CUBIC NAMES OF MEMBERS NEEDING ACCESS FOR READ ONLY (OPTIONAL)]
Project data directory: /cbica/projects/[PROJECT NAME]
Data source[s]: Penn Lifespan Informatics and Neuroimaging Center, University of Pennsylvania
Does the raw data contain PHI?* [Yes or No, depending on if PHI WILL BE ON CUBIC (no, it kept somewhere else)]
	IRB approval #: [IRB NUMBER HERE]
      Personnel approved to see PHI content:* 
      Does the project store PHI data (No or Yes with explanation): [No, if kept somewhere else]


Does the data have redistribution restrictions or is there a Data Use Agreement in place (No or Yes with explanation):
[NO OR YES WITH EXPLANATION]


Is the project the definitive reference source of the original data (No or Yes with explanation):
[E.G., YES IF THIS IS PROSPECTIVELY COLLECTED DATA, OR NO IF YOU ARE CLONING A PUBLICLY AVAILABLE DATASET]


Anticipated active lifespan of the project: [ESTIMATED TIME OF DATA COLLECTION AND ANALYSIS, A FEW YEARS IS A GOOD ESTIMATE]

Anticipated storage requirement over project lifespan:
Initial: [ASSUME 1-2 GB of DATA PER SUBJECT FOR MRI]
Ongoing: [ASSUME 7-10X INITIAL USE FOR POSTPROCESSING NEEDS]
Total: [INITIAL PLUS ONGOING]

Data management plan (what will be done with the project data after the anticipated lifespan):
[E.G., "After 2 years, the plan is to make it a shared dataset for Penn."]
*	 Changes to the PHI or IRB status require an update of this form
---------------

------------------------------------------------------------

---------------

------------------------------------------------------------
```
Then, request the ticket, filling out the request fields and attaching the data management txt file and approval screenshot. The ticket message does not need to be long, just something like "I am writing to request that my [NAME] project be created on CUBIC."


## GitHub repository

All code, from the beginning of the project, should be in a GitHub repository.
This is a prerequisite for reproducible neuroscience -- please start your project out on the right foot!
These repos should reside in the [PennLINC org](www.github.com/PennLINC), not your personal github.

{: .important-title }
> Use the Template!
>
> There is a GitHub repository template that you should use to create your project repository:
> <https://github.com/PennLINC/paper-template>.


## Project documentation on GitHub Pages

Careful tracking of your project is essential.
While well-commented code, reproducible analytic notebooks, and an archived Slack channel are very helpful,
an "overview" website also helps a lot to document how the different pieces of code fit together.
This can be easily made using markdown and GitHub Pages (like this one).
See the [project docs page](/docs/documentation/project-documentation) for how to do this with your project's GitHub repository.

{: .warning-title }
> Important
>
> Your project website is very important!
> It is what your replication buddy will use at pre-defined checkpoints for replicating your code;
> see the [project reproducibility guide](/docs/LabHome/ReproSystem) for more info.


## Slack channel

All projects in the lab are collaborative, and furthermore form a knowledge and code base for other subsequent projects.
A lot of valuable knowledge (esp re: troubleshooting) tends to be captured in correspondence.
As such, it is critical for the lab that this knowledge is not "locked away" in inaccessible repositories like private email inboxes or direct message channels on slack.
As such _nearly all_ project discussion should occur in a project specific slack channel; this will be created (by Ted) when the project is initiated.
Please try to avoid using direct message channels on slack for project communication.

Ted is a slack admin and can add you to the "BBL" slack, which encompasses all the labs in LiBI and the Psychosis and Development Section;
PennLINC is a member.

The main execption to this are documents (e.g., manuscripts) that need review; please send these directly to Ted via email.
See also the note on [Communication and Collaboration](coming soon).


### Zotero library

While some projects can be done locally on your laptop, many require more computing resources.
In general, we now reccomend projects use the PMACS LPC; see the [PMACS pages](/docs/pmacs) for details.
However, some projects may be best served by using the computational resources of CUBIC;
see the [CUBIC pages](/docs/cubic) for more details.
Regardless, each project should use a common directory structure to ensure reproducibility.
