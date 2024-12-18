---
layout: default
title: Project Setup
parent: Project Workflow
nav_order: 1
---

# PennLINC Project Setup Guide

Each project at PennLINC has several key elements to facilitate collaboration and ensure reproducbility.
For clarity in naming, all elements (github, slack, cubic, etc) should be named similarly-- often ```Lastname_ProjectName``` with CamelCasing, where "Lastname" is the last name of the first author / trainee leading the project.


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

All projects in the lab are collaborative, and furthermore form a knowledge and code base for other subsequent projects. A lot of valuable knowledge (esp re: troubleshooting) tends to be captured in correspondence. As such, it is critical for the lab that this knowledge is not "locked away" in inaccessible repositories like private email inboxes or direct message channels on slack.
As such _nearly all_ project discussion should occur in a project specific slack channel; this will be created (by Ted) when the project is initiated. Please try to avoid using direct message channels on slack for project communication.  The main exception to this are documents (e.g., manuscripts) that need review; please send these directly to Ted via email. See also our notes on [Slack, Communication, & Collaboration](https://pennlinc.github.io/docs/LabHome/CommunicationAndCollaboration/).


### CUBIC Project

Nearly all projects in the lab will require the HPC resources provided by CUBIC.  Please see the [CUBIC](https://pennlinc.github.io/docs/cubic) documentation for details on project setup. 


### Notion Project

We reccomend that notes on your project -- including meeting notes, interim results, and links to code -- be stored in a [Notion](https://www.notion.so/) project.  When you joined the lab you should have been added to the PennLINC Notion Org. We are actively developing a project template for notion and suggest you use this + provide feedback. 


### Zotero library

Zotero is the most popular reference management tool in the lab. It integrates with Notion via [Notero](https://github.com/dvanoni/notero). 
