---
layout: default
title: A Typical Setup for Science
parent: Computation Basics
nav_order: 1
has_toc: true
---

# A Typical Setup for Science

This page outlines how the modal PennLINC lab member typically sets up their
computer, etc. for day-to-day science.

The descriptions on this page will not apply to everyone equally,
but we hope that it gives you a sense of how most lab members work.


## Laptop

Most lab members use a lab-supplied Apple laptop for their daily work.
The laptop should be configured by UPenn IT (PMACS, then Andrew Zitelli) to have the basic
software installed and configured.
This should include, at a minimum, the VPN client needed to access CUBIC.

Most lab members will also install additional software on this machine,
so that they can use it for their own projects.

Common tasks that we do entirely on our laptops (rather than using the laptop to interace with CUBIC) include:

- Creating figures for papers, presentations, etc.
- Interacting with imaging data, such as by loading it into a viewer like FSLEyes or ITKSnap.
- Running analyses on tabular/summary data generated on CUBIC,
  such as by using R or Python.
- Writing up a manuscript, or other documents.
- Interacting with the lab on Slack, Zoom, Notion, etc.
- Email, calendar, other admin tasks.


## Project Code Development

Most lab members will need to write code that gets run both on their local machine and on CUBIC.

We recommend using a code editor like VSCode or Cursor to develop your code locally,
then pushing changes to a GitHub repository, pulling those changes onto CUBIC using `git`,
and then running the code on CUBIC.
You can also push changes from CUBIC back to GitHub, and then pull those changes onto your local machine,
though editing code on CUBIC is more difficult, because you will need to use a terminal-based editor like nano or vim.

See the pages on SSH keys, git, and GitHub for more information on how to set up and use these tools.

We do not recommend directly copying code from your local machine to CUBIC.
While this may be easier in the short term, it will make it much more difficult to track changes to the code,
and to reproduce the analysis.


## Interacting with Data

We store most of our data on CUBIC, and we recommend doing most of your data analysis there as well.

However, some tasks are easier to do on your local machine, such as visualizing imaging data or creating figures.
For small data transfers, smb is a good option (see the [data transfer page](https://pennlinc.github.io/docs/cubic/data-transfer/) for more information).
smb (pronounced "samba") allows you to mount a directory on CUBIC as a local drive on your machine,
so you can access the data as if it were local.

For larger data transfers, we recommend using `scp` or `rsync`.
These commands allow you to transfer files between your local machine and CUBIC.

See the pages on data transfer for more information on how to set up and use these tools.

Please be aware that many files on CUBIC will contain sensitive information,
and you should not share these files with anyone outside of the lab.
This is especially true for certain datasets, such as ABCD or HBCD.
For open datasets, like those we download from OpenNeuro, it is less of a concern.


## Sharing Data with Collaborators

We often share data with collaborators who do not have access to CUBIC.
Always check with Ted before sharing any data with collaborators.

We recommend using Box to share data with collaborators,
as UPenn gives us a lot of free storage and it is safe to use.
