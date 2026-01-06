---
layout: default
title: Using R and Python
parent: CUBIC
nav_order: 6
---

# Using R/R-studio and Installation of R packages on CUBIC

## Use R and RStudio on CUBIC directly
1. Currently  R-4.2.2 is installed on CUBIC. If you are satisfied with R-4.2.2, simply load it with `module load R/4.2.2`, and directly go to step 2 below. However, you can install another R version in any directory of your choice, usually home directory `/cbica/home/username`.
To install R in your desired directory, follow the following steps.

   ```bash
   module load curl/7.56.0  # load the libcurl library
   wget http://cran.rstudio.com/src/base/R-4/R-4.2.2.tar.gz #e.g R-4.2.2
   tar xvf R-4.2.2.tar.gz
   cd R-4.2.2
   ./configure --prefix=$HOME/R  --enable-R-shlib #$HOME/R is where R will be installed
   make && make install

   ```

     Then, installation of R is complete.
    To run R, add `$HOME/R/bin` to your PATH. Then, shell commands like R and Rscript will work.
   ```bash
    echo export PATH="$HOME/R/bin:$PATH" >> .bash_profile or .bashrc # add R to bash
   ```
   To run R:
   ```bash
   module load R
   R
   ```

    >You can load higher version of `gcc` compiler if required for some R version.
   ```bash
    module load gcc/version-number
   ```

2. You can install R-packages of your choice.
   It requires adding library path in `.Rprofile` .
   You also may need to specify the base URL(s) of the repositories to use.
   Furthermore, you should specific lib.loc when loading packages.
   Note that some packages, such as "tidyverse", have run into a lot of issues when trying to install directly onto CUBIC.
   See [next section](#use-a-docker-image-containing-r-packages-on-CUBIC) for a workaround.

    ```R
       .libPaths('/cbica/home/username/Rlibs`)
       install.packages("package_name", repos='http://cran.us.r-project.org', lib='/cbica/home/username/Rlibs')
       library(package_name, lib.loc="/cbica/home/username/Rlibs")

    ```
    You can have more than one R-packages directory.

3. You can also use r-studio on CUBIC  by simply load rstudio using `module`.

     ```bash
      module load R-studio/1.1.456
      rstudio & # enjoy the R and Rstudio, it works
     ```
4. If you are working with large amounts of data, you may want to submit a job in R. Make sure the packages you need in you Rscript are installed properly and remember to specify 'lib.loc' when loading libraries in your .R file. Write your bash script:
      ```sh
      #!/bin/bash
      Rscript --save /cbica/projects/project_name/script_name.R
      ```

And submit your job, for example:
      ```sh
      qsub -l h_vmem=25G,s_vmem=24G bash_script.sh
      ```


## Use a Docker Image containing R packages on CUBIC

If you run into issues installing your needed R packages on CUBIC, you can use a Docker image that contains a number of R packages already.
For example, if you have a huge analysis in R that requires you to submit a job on CUBIC, but you can't successfully install your R packages of interests onto CUBIC, this method is a great workaround.

This [docker-R github repo](https://github.com/PennLINC/docker_R) contains documentation on how you can either 1) directly use [a publicly available Docker image](https://hub.docker.com/r/pennlinc/docker_r) that contains a bunch of R packages already, or 2) build your own Docker image with the specific packages you need.
After setting up your Docker image, you can submit a job on CUBIC to run all the Rscripts you want!
For details, please see instructions [here](https://github.com/PennLINC/docker_R).


Alternatively, you can use other containers:

the neuroR container on [docker hub](https://hub.docker.com/r/pennsive/neuror) has R and many neuroimaging packages installed, which is also available as an environment module on CUBIC:
```sh
module load neuroR/0.2.0 # will load R 4.1
```

# Using Python on CUBIC

 Sure, you could install your own python (and you can!), but if you want to just use one that works well with PennLincKit, all you have to do is the following

If you want it to be your default:
```bash
echo 'export PATH="/cbica/home/<username>/anaconda3/bin:$PATH"' >> ~/.bashrc
```
If you want it for a session:
```bash
export PATH="/cbica/home/<username>/anaconda3/bin:$PATH"
```

