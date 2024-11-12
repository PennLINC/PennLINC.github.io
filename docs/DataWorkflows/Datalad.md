---
layout: default
title: Datalad
parent: Data Workflows
nav_order: 0
has_toc: false
---

[Datalad](https://handbook.datalad.org/en/latest/) is basically git for data. 

Building on top of Git and git-annex, DataLad allows you to version control arbitrarily large files in datasets, without the need for custom data structures, central infrastructure, or third party services.

- Track changes to your data
- Revert to previous versions
- Capture full provenance records
- Ensure complete reproducibility

<img src="/assets/images/datalad.svg">

### Installing Datalad 

1. The best way to install datalad on HPC systems like cubic is using conda. First, make sure Miniforge is installed in your project folder (see instructions [here](https://pennlinc.github.io/docs/cubic#installing-miniforge-in-your-project)).
2. Then, create an environment for this:
```bash
conda create -n dlad python=3.11
conda activate dlad
```
3. Then, install datalad:
`conda install datalad git git-annex`

Note that this page is still under construction and more information may be added at a later date. 