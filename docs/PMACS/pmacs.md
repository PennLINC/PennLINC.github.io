---
layout: default
title: PMACS
has_children: false
nav_order: 6
permalink: docs/pmacs
has_toc: true
---
# Using Penn Medicine Academic Computing Services (PMACS)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

This section gives an overview of how to get started on PMACS Limited Performance Computing (LPC) cluster. For additional information, check out the [LPC wiki](https://wiki.pmacs.upenn.edu/pub/LPC). NOTE: The full URL to the pmacs servers have not been included here. If you need to know the full URL, please ask on slack.

## Obtaining PMACS LPC Access
Send the lab's access manager (Tinashe) your Pennkey, full name, and Penn email, and have them fill a ticket and request access for you. When access has been granted, you will receive an email with a temporary password through SecureShare. Log in via [this link](https://reset.pmacs.upenn.edu/) with your temporary password and set a new PMACS password. Your Pennkey and new PMACS password will be used to ssh into the LPC and to access the PMACS help desk/ticketing system.

## Logging in to PMACS LPC
Once you've set up your login credentials for the PMACS LPC, you can SSH into the LPC from anywhere (even without Penn VPN). You can SSH into PMACS in two different ways, depending on what tasks you want to execute:

```bash
$ ssh -Y [username]@scisub.pmacs.upenn.edu #SSH only. No sftp. No outbound access. Can submit or check jobs.
$ ssh -Y [username]@sciget.pmacs.upenn.edu #SSH, but has outbound access to use git, svn, wget, et cetera to download data. Can *not* submit or check jobs.
```

Enter PMACS password when prompted.

Again, you can submit jobs on `scisub`, and you get interface with the outside world (e.g., using conda / pip install, wget) on `sciget`. We recommend also doing an SSH into `sciget7` as it seems to be the most up-to-date node:

```bash
$ ssh -Y [username]@sciget
$ ssh sciget7
```

In general, there is a set of software libraries and tools we expect you'll need, such as `R`, `conda`, and `FSL`; we've made these available for you in a module. To load this module, simply type the following:

```
$ xbash
$ source /project/bbl_projects/apps/default_modules.sh
```

You can also add the `source` line to your bash profile (add the line in the file `~/.bash_profile`) so that it loads automatically every time you sign in.

## Submitting tickets
Log in to the [PMACS Help Desk](https://helpdesk.pmacs.upenn.edu/) with PMACS credentials. Under “Quick Actions” click “Need help? Report it." Submit ticket under appropriate category.

## Making a project directory
New project directories must be created for you by PMACS LPC admin. To have a new project directory created, you need to submit a ticket. Log into the [PMACS Help Desk](https://helpdesk.pmacs.upenn.edu/) with PMACS credentials, and submit a "Systems" ticket specifying the desired project folder name (e.g. `grmpy_diffusion`) and who should have read access and read/write access to the folder (e.g. `bbllpc`). Once made, project directories can be found in `project/` (e.g. `/project/grmpy_diffusion`).

## Loading modules and accessing module software
Environment modules are used to load and unload available software (e.g. ANTs, mrtrix, R, ITK, dcm2niix, fsl, freesurfer, etc.). Hence, in order to use most software/applications that are available on PMACS, you must first load the appropriate module. To check which modules are available on PMACS, type `module avail`. To load a desired module, use `module load [modulename]`. Finally, to see what modules you have loaded, use `module list`.

For example, if I want to load python:
```bash
$ module load python # automatically loads latest version
$ python
$ exit()
```

Modules can be loaded and unloaded both in the log in node and in an interactive shell. You can access interactive shells via `ibash` (standard) or `xbash` (used for graphics, X11 forwarding enabled). In order to use some module software, however, you must be in an interactive shell!

For example:
```bash
$ module load mrtrix3/current
$ mrstats
```
will return -bash: mrstats: command not found

However,
```bash
$ ibash
$ mrstats
```
will now reveal help documentation for mrstats.

In what circumstances do you use `ibash` you ask? From the [LPC wiki](https://wiki.pmacs.upenn.edu/pub/LPC):

"Use the interactive shell to:
- Prepare you submit scripts
- Find apps, browse appl
- Work on anything you don’t have access to on the submit host
- Browse /project/group directory
- Prototype code and test apps"

## Requesting software installations
Open source free apps and most imaging software needs to be installed by PMACS admin. This means you can’t install R, Stata, or Python packages on your own. You can submit a “Systems” ticket at [PMACS Help Desk](https://helpdesk.pmacs.upenn.edu/) requesting that new software be installed.

## Installing Flywheel on your PMACS account
You can install the Flywheel command line interface (CLI) locally, which is helpful as the CLI version updates frequently. Follow these steps to install the Flywheel CLI and gain access to `fw` commands. Complete these steps on the log in node, not in an interactive shell.

1. Install miniconda in your home directory (`/home/[pmacs username]`):
```bash
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash ./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/software/pkg/miniconda3
```
2. Load miniconda
```bash
$ source $HOME/software/pkg/miniconda3/bin/activate # should be whatever folder miniconda3/bin/activate is in
```
3. Create flywheel python environment and activate it
```bash
$ conda create -n flywheel anaconda python=3
$ conda activate flywheel
```
4. Install flywheel-sdk
```bash
$ pip install flywheel-sdk
```
5. Install flywheel-cli
```bash
$ wget https://storage.googleapis.com/flywheel-dist/cli/12.1.1/fw-linux_amd64.zip
$ unzip fw-linux_amd64.zip
```
6. The fw executable should be in the linux_amd64 folder. Add this directory to your path so that the `fw` command is accessible from all locations
```bash
$ echo "export PATH=\$PATH:~/linux_amd64" >> ~/.bashrc
```
7. Log in to flywheel using your API key (obtained from your Flywheel User Profile)
```bash
$ fw login upenn.flywheel.io:$APIkey
$ fw status
$ You are currently logged in as <username> to upenn.flywheel.io
```

> Note: Sometimes `fw status` gets you this error message: `'Connection to upenn.flywheel.io timed out. (connect timeout=10)')': /api/auth/status`. In this case, logging out of PMACS and logging in again should fix the issue.

## Cloning and Updating GitHub Repos on PMACS
If you have already created an ssh private key for your PMACS account and have added it to both the ssh-agent on PMACS (~/.ssh/id_rsa and id_rsa.pub files) and to your GitHub account, you can clone, pull, and push git repositories using sciget and an available github module on PMACS.

Specifically, to clone and update repos you should first ssh in via sciget (rather than via scisub). Sciget allows connections to outbound networks.
```bash
$ ssh -Y [username]@sciget
```
Next, load a git-related module.
```bash
$ module load git/2.5.0 #or git-lfs/2.2.1
```
You can now use github as you normally would.

If you have not yet set up your PMACS ssh key, follow these instructions. You will only need to do this once.
1. Generate a new ssh key using your github-associated email.
```bash
$ ssh-keygen -t rsa -b 4096 -C "{YOUREMAIL@example.com}"
```
- When promted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
- When promted, enter a secure passphrase.

2. Add your ssh key to the ssh-agent
```bash
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_rsa
```

3. Add your ssh key to your GitHub account.
- Sign in to GitHub
- Click on your profile photo and click Settings
- Click SSH and GPG keys in the Settings sidebar
- Click New SSH Key. "Title": enter a relevant title for the new key (e.g. PMACS account). "Key": copy the text in your ~/.ssh/id_rsa.pub file (which should start with ssh-rsa and end with your email) and paste it into the Key text box. Click Add SSH Key.

## Mounting a PMACS project directory on your local machine
1. If you are using a Mac, first install [OSXFuse and SSHFS](https://osxfuse.github.io/).

2. Make an empty mount point folder on your local machine. Make sure that only the user (not group or others) have access to this mount directory!
```bash
$ mkdir /Users/<username>/ImageData/PMACS_remote
$ chmod 700 /Users/<username>/ImageData/PMACS_remote
```
3. Mount the desired PMACS directory to your newly created, local mount directory using sshfs and sciget
```bash
$ sshfs [username]@sciget:<my-folder-on-PMACS> <my-local-mount-folder> -o defer_permissions,volname=project
```
4. Unmount when done! You should run this unmount command from outside of the mount point.
```bash
$ diskutil umount force /Users/<username>/ImageData/PMACS_remote
```

## Enabling X11 forwarding
To use graphics on PMACS, make sure that you:
- Have [XQuartz](https://www.xquartz.org/) installed on your local Mac
- log in to scisub via ssh -Y
- use xbash for your interactive shell


## Transferring files to and from the LPC
- You can transfer files to and from PMACS with username@transfer. This can be used with SFTP, rsync, and scp. (You cannot use transfer for ssh).
- Sciget can be used with scp, but transfer is reccomended. As in:
```bash
$ [<username>@<source_server> ~]$ scp /data/jux/BBL/projects/multishell_diffusion/processedData/multishellPipelineFall2017/*/*/prestats/eddy/*_msRD.nii.gz <username>@transfer:/project/grmpy_diffusion/diffusion_metrics/
```
- Transferring from cluster-to-cluster instead of through your local machine will run orders of magnitude faster. This is particularly true if you happen to be in the midst of a global pandemic and are relying on your home wifi.
- Make sure you have full permissions for the destination you are writing to.

## Viewing niftis
- In order to use flseyes or afni to view images on a mac, in your local terminal, type:
```bash
$ defaults write org.macosforge.xquartz.X11 enable_iglx -bool true
```
- Restart your mac and then ssh onto PMACS, you should now be able to view images

## Using the batch system

PMACS uses IBM's Load Sharing Facility (LSF) to submit and monitor jobs. This is
very different from SGE used on CUBIC. The biggest differences are you will use
``bsub`` to submit jobs and ``bjobs`` to monitor jobs instead of SGE's ``qsub`` to
submit jobs and ``qstat`` to monitor jobs.

The documentation for LSF can be found [here](https://www.ibm.com/support/knowledgecenter/SSWRJV_10.1.0/lsf_welcome/lsf_welcome.html).

## Stop receiving e-mails for each job you submit via ``bsub``

By default, every time you submit a job on PMACS using ``bsub``, you will get an
e-mail with what would normally be in a log file. To suppress this behavior,
use the ``-o`` flag to specify the path to the log file.

```console
$ bsub -o ~/jobinfo.log ~/launch_freeqc.sh
```

Alternatively, or in addition, you can add the following line to your .bashrc.

```console
$ echo LSB_JOB_REPORT_MAIL=N >> ~/.bashrc
```

## Running MATLAB on PMACS

To run a MATLAB script on PMACS, simply do the following:

1. Compose your script, for example:
```matlab
addpath('/path/to/matlab/functions/')
runALE # main command to be executed
```
and save it, for instance as `runexperimental1.m`

2. Compose a bash script to launch MATLAB, like so:

```bash
  module load matlab/2018b # load matlab
  matlab  -nodisplay -nosplash  -r /path/to/scripts/runexperimental1 # note, there's no file extension (.m)
```
and save it too: `experiment1.sh`

3. Submit the bash script as a job with `bsub`

  ```sh
   bsub -q matlab_normal  /path/to/scripts/experiment1.sh
  ```
To  run an interactive session:

1. Run `bsub -Is -XF -q matlab_interactive 'bash'` from the initial login node.

2. Type `matlab` to open Matlab using X11, or `matlab -nodisplay` to run the session in the terminal.

## Running RStudio on PMACS

We have two ways of accessing RStudio on PMACS. It's not installed by default in
`modules`, but there are ways to scratch that itch for R users.

### X11

This is how to access RStudio with the least setup, but it suffers from the same
issues all other X11 solutions have -- poor graphic quality. Nevertheless, the
process is simple:

1. Temporarily source the central default modules if it is not in your bash profile
     ```bash
      $ source  /project/bbl_projects/apps/default_modules.sh
     ```

2. Activate rstudio enviroment
   ```sh
   $ conda activate rstudio
   ```
3. Get into interactive mode.
   ```sh
   $  xbash
   ```
4. Launch rstudio
   ```
   $ rstudio
   ```
5. Optional. if you want to use other version of R , for instance `R/3.6.3`.
   Load the module of that R and set rstudio to use that R before lunching the rstudio.
   ```sh
   $  module load R/3.6.3
   $  export RSTUDIO_WHICH_R=/appl/R-3.6.3/bin/R

   ```

### Port Forwarding with Singularity

This method leverages the [rocker project's](https://hub.docker.com/r/rocker/rstudio) awesome method of running RStudio in
a container and forwarding the graphics over SSH. The project is built in
Docker, but most HPCs tend to avoid using Docker for security purposes, and
instead vouch for Singularity, which works quite the same way. This setup is
admittedly slightly complicated, but if you want a true RStudio experience when
doing data science, the results can't be beat.

Pros:

- Real RStudio interface with no lag
- Graphics load instantly
- Computation is right where you need it

Cons:

- Complexity
- We're still figuring out how to set memory limits and how this will work with parallelised processes

Ok, let's get to the steps. The following sources helped me put together this
workflow: [1](https://divingintogeneticsandgenomics.rbind.io/post/run-rstudio-server-with-singularity-on-hpc/), [2](https://www.rocker-project.org/use/singularity/), [3]()

First, pick a port number. RStudio by default tries to set it at `8787`, so it's
safe to assume whenever you're on the cluster that someone is already using it.
Also, it's a good idea to use 3 separate terminals to supervise what you're doing. Let's call them `t1, t2, t3`.

1. Log in to `sciget` on `t1`.

```sh
# In this example I'm using 9999. DO NOT USE THIS. BIG SAD.
t1[localmachine]$ ssh -Y -L localhost:9999:localhost:9999 <username>@sciget
```

2. From `sciget`, login to the Singularity node on PMACS.

```sh
t1[<username>@sciget ~]$ ssh singularity01
```

3. On the Singularity node, fetch and set up the Singularity image.

```sh
# pull the docker image for tidyverse into singularity
t1[<username>@singularity01 ~]$ singularity pull --name rstudio.simg docker://rocker/tidyverse:latest

# convert this to a "sandboxed" writable image; you can hit "y" at the prompt to overwrite or change the name in the call
t1[<username>@singularity01 ~]$ singularity build --sandbox rstudio.simg rstudio.simg
```

4. Launch the Singularity container and run RStudio (remember to specify a unique port).

```sh
# use the ampersand to run in the background, or else you won't be able to do anything on this terminal until you quit singularity


t1[<username>@singularity01 ~]$ singularity exec --writable rstudio.simg rserver --www-address=127.0.0.1 --www-port 9999 &

# you can find out what ports are currently in use with this command
t1[<username>@singularity01 ~]$ netstat -tunlp

# check for any rstudios
t1[<username>@singularity01 ~]$ netstat -tunlp | grep rserver
```

5. On `t2`, login to `sciget` and "listen" to the port from Singularity.

```sh
# I tend to just repeat the port numbers because I forget which is which
t2[localmachine]$ ssh -Y <username>@sciget
t2[<username>@sciget ~]$ ssh -NfL localhost:9999:localhost:9999 singularity01
```

6. On `t3`, "listen" to the port from `sciget`.

```sh
t3[localmachine ~]$ ssh -NfL localhost:9999:localhost:9999 singularity01
```

7. Open RStudio in your browser.

Visit `localhost:9999` in Chrome or Firefox.

You should now be in an RStudio GUI with access to any directory you want. The R
installation is _within_ the folder called `rstudio.simg` (it's a Singularity
image that we converted into a directory in step 3), so you are able to manage your
own packages in there. If need be, you could do this setup multiple times and
have RStudio images for each project directory on PMACS.

8. Close each process you're running.

When you're done, use RStudio to close this safely -- hit the orange button in
the top right corner. This may shutdown the `rserver` process, but not the `singularity exec`
you called in `t1`. Go to `t1` and `kill` this manually:

```
t1[<username>@singularity01 projects]$ ps - x
PID TTY      STAT   TIME COMMAND
47110 ?        S      0:00 sshd: <username>@pts/0
47111 pts/0    Ss     0:00 -bash
48226 pts/0    Sl     0:00 Singularity runtime parent
48242 pts/0    Sl     0:01 rserver --www-address=127.0.0.1
49089 pts/0    R+     0:00 ps -x
t1[<username>@singularity01 projects]$ kill 48242 && kill 48226
```

Likewise, make sure you `kill` your port forwarding commands in `t2` and `t3`.
When you come back to continue working, loop back to step 4.

## Running data processing pipelines on PMACS

Data processing pipelines, such as [fmriprep](https://fmriprep.org/en/stable/) and [qsiprep](https://qsiprep.readthedocs.io/en/latest/), can be run easily by creating singularity images on PMACS. Below steps use qsiprep as an example, but they can be applied to other pipelines as well.

### Creating singularity images from dockerhub on PMACS

1. Log onto **sciget**
   ```bash
   $ ssh -Y <user>@sciget
   ```
2. Connect to singularity
   ```bash
   $ ssh singularity01
   ```
3. Pull the singularity image to PMACS and exit
   ```bash
   $ singularity pull docker://pennbbl/qsiprep:0.12.2
   $ exit
   ```
4. Move the qsiprep image (in this case *qsiprep_0.12.2.sif*) to an *images* directory in your project directory

### Running the container on PMACS

Before running the qsiprep container on PMACS, first [get a freesurfer license](https://surfer.nmr.mgh.harvard.edu/registration.html). The license is necessary to run qsiprep without any error. Save the license also in the *images* directory and run the following command:

```bash
$ singularity run --cleanenv -B </path/to/project/directory>/data:/home/<user>/data,\
$ </path/to/project/directory>/images/license.txt:/appl/freesurfer-6.0.0/license.txt,\
$ </path/to/output/directory>:/home/<user>/<output directory name> \
$ </path/to/project/directory>/images/qsiprep_0.12.2.sif \
$ --fs-license-file /appl/freesurfer-6.0.0/license.txt \
$ --work-dir </path/to/working/directory> \
$ --output-resolution <value> \
$ </path/to/project/directory>/data \
$ </path/to/output/directory> \
$ participant
```
There are several parts to this command:

* *--cleanenv* option means that we don't want to pass the host environment to the container (visit [Environment and Metadata](https://singularity.lbl.gov/docs-environment-metadata) for more)
* *-B* is an argument to bind paths; simply put, *</path/to/project/directory>/data* will be called as */home/<user>/data* in the container (visit [Bind Paths](https://singularity.lbl.gov/docs-mount#specifying-bind-paths) for more)
* *--output-resolution* specifies the isotropic voxel size in mm the data will be resample to after preprocessing (for more information on the arguments [see qsiprep documentation](https://qsiprep.readthedocs.io/en/latest/usage.html#command-line-arguments))
