---
layout: default
title: Data Sharing
parent: Data Workflows
nav_order: 5
has_toc: false
---

# Policies for requesting/sharing data
{: .highlight-title }
> Important
>
> This page conceptualizes what data sharing may look like after post-bac data analysts are no longer on the informatics team.


### Internal collaborations

1. Speak to Ted about the data required and confirm what is needed for the request
2. Nail down inclusion criteria
3. Post on the `#informatics` Slack channel, tagging a point-person flagged by Ted to ask for the data
4. Communicate with the point-person on an **open channel** to determine the best way to get data


#### For data on CUBIC

- Make sure to work in a relevant project/ create a new one as needed
- Make a directory formatted as follows: `LastName_ProjectName_Year` and work inside the directory if you are using an old project
- Filter data by inclusion criteria


#### For data on PMACS

- Transfer ALL data to a relevant CUBIC project/ create a new project as needed via `datalad clone`, as described [here](https://pennlinc.github.io/docs/DataTasks/FetchingYourData/)
- Make a directory formatted as follows: `LastName_ProjectName_Year` and work inside the directory if you are using an old project
- Filter data by inclusion criteria
- Make sure to `datalad get` all data that meet inclusion criteria/are needed for analyses before running any pipelines on the data - running numerous `datalad get` commands during a pipeline can take down PMACS


### External collaborations

The transfer method on what softwares our collaborators have access to.
We often use Box, zipping data before uploading it (using `tar -czvf <ArchiveName>.tar.gz <PathToFile>"`)

Other methods may be necessary and this is a case-by-case basis.

General guidelines for external data sharing are as below:

1. When sharing datasets, we will send ALL data available.
2. Inclusion criteria will be decided by us before the data transfer, and shared with the data recipients.
3. Data recipients will confirm the inclusion criteria.

{: .note-title }
> Note
>
> If someone wants ABCD data, we will interactively zoom call with them to get a transfer set up.
> This is not data we will transfer.

Make sure to communicate about the status of the project and keep collaborators in the loop,
also being available for questions after the data is successfully transferred.
