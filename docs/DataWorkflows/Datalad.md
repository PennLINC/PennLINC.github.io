---
layout: default
title: Datalad
parent: Data Workflows
nav_order: 0
has_toc: false
---

[Datalad](https://handbook.datalad.org/en/latest/) is basically GitHub for data. 

Building on top of Git and git-annex, DataLad allows you to version control arbitrarily large files in datasets, without the need for custom data structures, central infrastructure, or third party services.

- Track changes to your data
- Revert to previous versions
- Capture full provenance records
- Ensure complete reproducibility

### Installing Datalad 

1. The best way to install datalad on HPC systems like cubic is using conda. First, make sure Miniconda is installed in your project folder (see instructions [here](https://pennlinc.github.io/docs/cubic#installing-miniconda-in-your-project-the-hard-way)).
2. Then, create an environment for this:
`conda create -n dlad python=3.10`
`conda activate dlad`
3. Then, install datalad:
`conda install -c conda-forge datalad`

Note that this page is still under construction and more information may be added at a later date. 