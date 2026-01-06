---
layout: default
title: Using R and Python
parent: CUBIC
nav_order: 6
---

# Using R on CUBIC

R is most comfortably used from VSCode/Cursor/RStudio on your local device.
However, processing of big data will have to take place on cubic without a gui.
Getting a recent R and the dependencies you need is most easily and reproducibly accomplished by creating an apptainer image with the libraries you need.

## Creating an R apptainer image

This workflow uses the `Apptainer.def` file format and the [r2u](https://eddelbuettel.github.io/r2u/) base image to easily install CRAN packages.
You create a file called `my-R-apptainer.def` that will look minimally like:

```
Bootstrap: docker
From: rocker/r2u:jammy

%help
    My custom R environment

%labels
    org.label-schema.name "My R Image"

%environment
    export DEBIAN_FRONTEND=noninteractive

%post
    set -e
    apt-get update \
        && apt-get install -y --no-install-recommends \
            r-cran-tidyverse \
        && apt-get clean \
        && echo 'options(bspm.sudo = TRUE)' >> /etc/R/Rprofile.site \
        && rm -rf /var/lib/apt/lists/*

%runscript
    echo "Custom R Container"
    echo "R version: $(R --version | head -n 1)"
    if [ $# -gt 0 ]; then
        exec "$@"
    else
        exec R
    fi
```

This creates a very simple R environment with tidyverse installed. 
You can install any package from CRAN or BioConductor by adding it to the section where `r-cran-tidyverse` is listed. 
BioConductor package names will look like `r-bioc-hdf5array`.
To get a usable apptainer sif file you will run

```bash
apptainer build my-r-image.sif my-R-apptainer.def
```

to enter an R session you can run

```bash
apptainer run my-r-image.sif
```

Or to execute an R script, as you would for running R in a SLURM job, you run

```bash
apptainer run my-r-image.sif Rscript path/to/your/script.R arg1 arg2
```