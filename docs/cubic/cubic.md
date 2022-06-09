---
layout: default
title: CUBIC
nav_order: 7
has_children: true
permalink: docs/cubic
has_toc: false
---

# Using the CUBIC Cluster
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The cubic cluster is a very powerful set of servers that we can use for computing. Although they are running Linux, familiarity with Linux does not mean that you will be able to effectively use CUBIC. This section details how to get up and running on the CUBIC cluster. In general we now recommend using [PMACS](https:https://pennlinc.github.io/docs/pmacs) for specific analysis projects, and reserve CUBIC for use as a high-performance compute engine for large batches of containerized jobs that are launched from Flywheel.  However, for specific projects (esp collaborations with CBICA), it may make sense to have your project live on CUBIC.

## Setting up your account

To get login credentials for CUBIC, you must have already a Penn Medicine account (i.e. an @pennmedicine.upenn.edu email). Once you do, ask the lab's PMACS/CUBIC manager to create a ticket asking for a new CUBIC account. You will receive an email with your login credentials and other instructions. Once you are granted login credentials for CUBIC, you will be able to connect from inside the Penn Medicine network using SSH. To access the network remotely, follow [instructions to install the client](http://www.uphs.upenn.edu/network/index_vpn.html). If you can successfully authenticate but are blocked from access, you may need to contact someone to put you on an exceptions list.

Once inside the Penn network, the login to CUBIC looks like this:

```python
$ ssh -Y username@cubic-sattertt
```
You use your UPHS password to login. On success you will be greeted with their message and any news:

```
                               Welcome to


                   #####   ######   ###   #####      #
                  #     #  #     #   #   #     #    # #
                  #        #     #   #   #         #   #
                  #        ######    #   #        #     #
                  #        #     #   #   #        #######
                  #     #  #     #   #   #     #  #     #
                   #####   ######   ###   #####   #     #

                  =======================================
            Center for Biomedical Image Computing and Analytics



				**** Reminder ****

		The login nodes are shared by all users and are intended
		for interactive work only. Long-running tasks requiring
```

You can hit the space bar to read all of this or `q` to exit.

## Project Directory Access Request

Once you have access to CUBIC, you may need to start a project in a new directory. Visit [this wiki](https://cbica-wiki.uphs.upenn.edu/wiki/index.php/Research_Projects#Project_Creation_Request) for more, or follow along below.

First you need to fill out the data management document available [here](https://cbica-wiki.uphs.upenn.edu/wiki/images/Project_data_use_template.doc). This document will ask you for a number of details about your project, including the data's source and estimates about how much disk space you will need over a 6 month, 12 month, and 24 month period, and the estimated lifespan of the data ( 🤷). You will also need to provide the CUBIC usernames for everyone you want to have read and/or write access to the project — getting this done ahead of time is strongly recommended because, as you can imagine, requesting changes after-the-fact can be a bother.

Additionally, you will need to be familiar with:

- Whether or not the data has an IRB associated with it and who has approval
- Whether or not the data is the *definitive* source
- Whether or not you have a data use agreement
- What will happen to the data at the end of its expected lifespan on the cluster

This document must be saved as a `.txt` file and before being submitted with your request.

Finally, you will need approval from your PI. This involves sending an email to the PI with a written blurb to the effect of "Do you approve of this project folder request", to which the PI only needs to respond "Yes, approved". Once you've got this you can screenshot the conversation (include the date in frame) and save that as an image.

With these two documents, you can now submit the request via the the [Request Tracker](https://cbica-infr-vweb.uphs.upenn.edu/rt/) — you'll need your CBICA/CUBIC login credentials for this.

<img src="/assets/images/request-tracker.png" alt="">

Open a new ticket and, like applying for a job, **FILL OUT THE REQUEST WITH THE EXACT SAME INFORMATION AS YOU JUST FILLED IN THE DOCUMENT.** 😓

<img src="/assets/images/new-project-request.png" alt="">

Lastly, attach your supporting documents.

The process for accessing an existing project is similar, but fortunately you will not have to fill out a new data management document; only the PI approval and filling of the online ticket is required. You should receive an email from CBICA confirming your request, and you can always return to the [Request Tracker](https://cbica-infr-vweb.uphs.upenn.edu/rt/) to see the status of your ticket.


## File permissions on CUBIC

Unlike many shared computing environments, read and write permissions are *not* configured using groups. Instead, individual users are granted access to data on a project-by-project basis. For example, if you are a member of the project `pnc_fixel_cs` you will not be able to read or write directly to that project's directory (which will be something like `/cbica/projects/pnc_fixel_cs`).

To access a project's files you have to log in as a *project user*. This is done using the `sudo` command after you have logged in as your individual user. In this example you would need to use `sudo` to log in as the `pncfixelcs` user and run a shell. Note that underscores in the project directory are removed when logging in as the project user. By running

```bash
$ sudo -u pncfixelcs sudosh
```

and entering the same UPHS password you used to log in to your individual user account. You can see that the project user has their own environment:

```bash
$ echo $HOME
/cbica/projects/pnc_fixel_cs
```

This means that the user will have their own startup scripts like `.bashrc` and `.bash_profile` in their `$HOME` directory.

### Keypress issues

Sometimes after logging in as a project user, you will find that you have to type each character twice for it to appear in your terminal. If this happens you can start another shell within your new shell by running `bash` or `zsh` in your new bash session. This usually creates a responsive shell.

## Configuring a CUBIC account

Note that individual user accounts typically have very little hard drive space allotted to them. You will likely be doing all your heavy computing while logged in as a project user. This means that you will want to configure your *project user* account with any software you need. This example we will use the `xcpdev` account as an example. First, log in as the project user:

```bash
$ sudo -u xcpdev sudosh
```

Let's see what is in this directory:

```bash
$ ls -al .
total 14
drwxrws---.   7 xcpdev xcpdev      4096 Feb 12 19:44 ./
drwxr-xr-x. 215 root   root        8192 Feb 10 16:06 ../
-rw-------.   1 xcpdev xcpdev        14 Oct  9 16:52 .bash_history
-r--r-x---.   1 xcpdev xcpdev       873 Jul  9  2018 .bash_profile*
-r--r-x---.   1 xcpdev xcpdev      1123 Jul  9  2018 .bashrc*
drwsrws---.   2 xcpdev xcpdev      4096 Aug 19 14:13 dropbox/
lrwxrwxrwx.   1 xcpdev xcpdev        17 Oct  9 16:52 .java -> /tmp/xcpdev/.java/
drwxr-s---.   3 xcpdev xcpdev      4096 Oct  9 16:52 .local/
drwxr-s---.   2 xcpdev xcpdev      4096 Oct  9 16:52 perl5/
drwxr-s---.   2 xnat   sbia_admins 4096 Jan  6 23:47 RAW/
drwxr-s---.   2 xcpdev xcpdev      4096 Jul  9  2018 .subversion/
-rw-r-----.   1 xcpdev xcpdev         0 Oct  9 16:52 .tmpcheck-cubic-sattertt
-rw-r-x---.   1 root   root        2360 Jul  9  2018 xcpDev_Project_Data_use.txt*
```

Notice that .bashrc is not writable by anyone. We'll need to change this temporarily so we can configure the environment. To do so, run

```bash
$ chmod +w .bashrc
$ ls -al .
...
-rw-rwx---.   1 xcpdev xcpdev      1123 Jul  9  2018 .bashrc*
...
```

and we can see that the file is now writable.

### Quick fixes for annoying behavior

By default, CUBIC replaces some basic shell programs with aliases. In your `.bashrc` file you can remove these by deleting the following lines:

```bash
alias mv="mv -i"
alias rm="rm -i"
alias cp="cp -i"
```

Additionally, you will want to add the following line to the end of `.bashrc`:

```bash
unset PYTHONPATH
```

We recommend that when you launch a script requiring
your `conda` environment and packages, you add `source activate <env>` to the top
of your script. To change the default installation for a given software
package, prepend the path to your `$PATH` and source your `.bashrc`:

```bash
echo PATH=/directory/where/your/installation/lives:${PATH} >> ~/.bashrc
source ~/.bashrc
```

## Installing miniconda in your project (The easy way)

For simple use of a Python interpreter managed by `conda`, you can use the installed module(s) like `module load python/anaconda/3`. To install your own version with more customization, follow below.
## Installing miniconda in your project (The hard way)

You will want a python installation that you have full control over. After logging in as your project user and changing permission on your `.bashrc` file, you can install miniconda using

```bash
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-Linux-x86_64.sh
```

You will need to hit Enter to continue and type `yes` to accept the license terms. The default installation location is fine (it will be `$HOME/miniconda3`). Sometimes you will run into a memory error at this step. If this happens, just log out and log back in and the issue should be remediated. This can be avoided in the first place by, when sshing into cubic, logging into `*login4`.

When prompted if you want to initialize miniconda3, respond again with `yes`

```bash
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> yes
```

For the changes to take place, log out of your sudo bash session and your second bash session, then log back in:

```bash
$ exit
$ sudo -u xcpdev sudosh
(base) $ which conda
~/miniconda3/bin/conda
```

You will notice that your shell prompt now begins with `(base)`, indicating that you are in conda's base environment.

There will be a permission issue with your conda installation. You will need to change ownership of your miniconda installation. To fix this run

```bash
$ chown -R `whoami` ~/miniconda3
```

When you launch jobs on cubic, they will autmoatically use cubic's base conda environment instead of your project user's miniconda installation. To fix this, you will need to initialize miniconda for a bash script submitted to qsub by running

 ```bash
$ source ~/miniconda3/etc/profile.d/conda.sh
```

Let's create an environment we will use for interacting with flywheel.

```bash
$ conda create -n flywheel python=3.7
$ conda activate flywheel
$ pip install flywheel-sdk
```

## Installing the flywheel CLI tool

To install the Flywheel CLI tool on CUBIC, you will again need to be logged in as your project user and have a writable `.bashrc`. Now create a place to put the `fw` executable.

```bash
$ cd
$ mkdir -p software/flywheel
$ cd software/flywheel
```

Flywheel will complain if your version is out of date, so best to find the latest version and download that. You can find the latest version by [logging into flywheel](Upenn.flywheel.io). Once you've logged in, in the upper-right corner, select your account menu, and select Profile. Scroll down to the Download Flywheel CLI section, and you should see the latest version (e.g. 10.7.3). In the first line below, replace `<version>` with the version number you just found (e.g. `https://storage.googleapis.com/flywheel-dist/cli/10.7.3/fw-linux_amd64.zip`).

```bash
$ wget https://storage.googleapis.com/flywheel-dist/cli/<version>/fw-linux_amd64.zip
$ unzip fw-linux_amd64.zip
$ echo "export PATH=\$PATH:~/software/flywheel/linux_amd64" >> ~/.bashrc
$ exit
$ exit
$ sudo -u xcpdev bash
$ bash
$ fw login $APIKEY
```

where `$APIKEY` is replaced with your flywheel api key. You can find your personal api key in your account profile (same place you went for the version #) by scrolling all the way to the bottom.

## Checking that your python SDK works

After running the `fw login` command from above you can activate your `flywheel` conda environment and check that you can connect:

```bash
$ conda activate flywheel
$ python
```

and in python

```python
>>> import flywheel
>>> fw = flywheel.Client()
```

If there is no error message, you have a working Flywheel SDK!

## Finalizing your setup

After all these steps, it makes sense to return your .bashrc to non-writable mode

```bash
$ chmod -w ~/.bashrc
```

## Downloading data from flywheel to CUBIC

The following script is an example of download the output of a flywheel analysis to CUBIC

```python
import flywheel
import os

fw = flywheel.Client()

project = fw.lookup('bbl/ALPRAZ_805556') # Insert your project name here
subjects = project.subjects() # This returns the subjects that are in your project

# This is a string that you will use to partial match the name of the analysis output you want.
analysis_str = 'acompcor'

for sub in subjects:
    """Loop over subjects and get each session"""
    sub_label = sub.label.lstrip('0') #Remove leading zeros

    for ses in sub.sessions():
        ses_label = ses.label.lstrip('0') #Remove leading zeros
        """Get the analyses for that session"""
        full_ses = fw.get(ses.id)
        these_analyses = [ana for ana in full_ses.analyses if analysis_str in ana.label]
        these_analyses_labs = [ana.label for ana in full_ses.analyses if analysis_str in ana.label]
        if len(these_analyses)<1:
             print('No analyses {} {}'.format(sub_label,ses_label))
             continue
        for this_ana in these_analyses:
            """Looping over all analyses that match your string"""
            if not this_ana.files:
                # There are no output files.
                continue

            outputs = [f for f in this_ana.files if f.name.endswith('.zip')
                and not f.name.endswith('.html.zip')] # Grabbing the zipped output file
            output = outputs[0]

            # I am getting this ana_label to label my directory.
            ## You may want to label differently and/or
            ## change the string splitting for your specific case.
            ana_label = this_ana.label.split(' ')[0]

            dest = '/cbica/projects/alpraz_EI/data/{}/{}/{}/'.format(ana_label,sub_label,ses_label) #output location
            try:
                os.makedirs(dest) # make the output directory
            except OSError:
                print(dest+" exists")
            else: print("creating "+dest)
            dest_file = dest+output.name
            if not os.path.exists(dest_file):
                """Download output file if it does not already exist"""
                print("Downloading", dest_file)
                output.download(dest_file)
                print('Done')
```

We can run this script using qsub and the following bash script.
Providing the full path to python is important! Your path may be different depending on install location. Obviously the name of your python script may also be different.

```bash
#!/bin/bash
unset PYTHONPATH
~/miniconda3/envs/flywheel/bin/python download_from_flywheel.py
```

## Mounting CUBIC on your local machine

One way to interact with CUBIC files is to _mount_ the server on to your filesystem. This can be useful for quickly moving a small number of files back and forth
(for example with NIfTIs you want't to view). It's _not_ meant for large file management or version control purposes (see the next section for solutions for those).

To mount a directory, (on Mac), use the `samba` server along with Mac's built in server connector. Follow this [short link](https://support.apple.com/en-gb/guide/mac-help/mchlp1140/mac#:~:text=Connect%20to%20a%20computer%20or%20server%20by%20entering%20its%20address,Click%20Connect.) to see how; when prompted to
select a server address, use:

```
smb://cubic-share.uphs.upenn.edu
```

Along with your CUBIC credentials. This is the most seamless method and will likely have better long term support, but again is mostly useful for opening
your home directory, and moving a handful of files about. For more demanding file transfers, including moving files to projects, see the next section.

## Moving data to and from CUBIC

Because of CUBIC's unique "project user" design, the protocol for moving files to CUBIC is a bit different than on a normal cluster. It is possible to move files to CUBIC by conventional means, or through your mount point, but this can cause annoying permissions issues and is not recommended.

Note that you will need to be within the UPenn infrastructure (i.e. on VPN or on campus) to move files to and from CUBIC.

### Moving files to CUBIC
All project directories will include a folder called `dropbox/` in the project home directory. Depositing files into this folder will automatically make the project user the owner of the file. Please note, however, that this ownership conversion is not always instantaneous and can take a few minutes, so be patient. Note also that anyone in the project group can move files into this folder. Finally, keep in mind that the dropbox can only contain 1GB or 1000 files at any given time.

`scp` is the recommended command-line transfer software for moving files onto and off of CUBIC. One need only specify the file(s) to move and the CUBIC destination. See the example below, where `<...>` indicates user input:

`scp </path/to/files*.nii.gz> <username>@cubic-sattertt:/cbica/projects/<project_dir>/dropbox/`

This command would copy all `nii.gz` files from `/path/to/` into the `dropbox/` folder of your project directory. Note that you are entering your CUBIC username in the destination, not your project username (confusing, I know).

Moving files directly to a non `dropbox/` folder on CUBIC with scp or your mount point *is* possible for a user with project directory write permissions, though is not recommended. Such files will retain the ownership of the CUBIC user who transferred the files, and permissions can only be changed by that user or a user with sudo priveleges.

### Moving files from CUBIC
This is much simpler. One can simply use scp (or rsync, or whatever) to copy files from a source on cubic to their local destination. E.g.

`scp <username>@cubic-sattertt:/cbica/projects/<project_dir/path/files.csv> </local/path/to/put/files/>`

It is also possible to copy files through the mount point, but this would be quite slow and is not really the purpose of the mount point.


##  Using R/R-studio and Installation of R packages

1. Currently  R-3.6 is installed on CUBIC. If you are satisfy with R-3.6, go to step 2 below. However, you can install another R version in any directory of your choice, usually home directory `/cbica/home/username`.
To install R in your desired directory, follow the following steps.

   ```bash
   $ module load curl/7.56.0 # load the libcurl library
   $ wget http://cran.rstudio.com/src/base/R-3/R-3.4.1.tar.gz #e.g R-3.4.1
   $ tar xvf R-3.4.1.tar.gz
   $ cd R-3.4.1
   $ ./configure --prefix=$HOME/R  --enable-R-shlib #$HOME/R is where R will be installed
   $ make && make install

   ```

     Then, installation of R is complete.
    To run R, add `$HOME/R/bin` to your PATH. Then, shell commands like R and Rscript will work.
   ```bash
    echo export PATH="$HOME/R/bin:$PATH" >> .bash_profile or .bashrc # add R to bash
   ```

    >You can load higher version of `gcc` compiler if required for some R version.
   ```bash
    $ module load gcc/version-number
   ```

2. You can install any R-packages of your choice. It require adding library path in `.Rprofile` . For example.
    ```R
       .libPaths('/cbica/home/username/R`)
    ```
    You can have more than one R-packages directory.
3. You can also use r-studio on CUBIC  by simply load rstudio using `module`.

     ```bash
      $ module load R-studio/1.1.456
      $ rstudio & # enjoy the R and Rstudio, it works
     ```

Alternatively, you can use containers:

the neuroR container on [docker hub](https://hub.docker.com/r/pennsive/neuror) has R and many neuroimaging packages installed, which is also available as an environment module on CUBIC:
```sh
module load neuroR/0.2.0 # will load R 4.1
```
2. R Studio (with the same neuroimaging packages as neuroR) is also available on docker hub, but not as an environment module, so you need to pull it yourself before running it:
```sh
singularity pull docker://pennsive/rstudio:4.1
# see https://sylabs.io/guides/3.0/user-guide/running_services.html for more on running services in singularity
# command follows format:
# [command]                                                     [image]           [name of instance]
singularity instance start -e -B $TMPDIR:/var -B $HOME:/root    rstudio_4.1.sif   my-running-rstudio
# $PORT must be the number you used to create the ssh tunnel, e.g. ssh -q -L${PORT}:127.0.0.1:${PORT} user@cubic-sattertt
SINGULARITYENV_PORT=$PORT singularity run instance://my-running-rstudio
# other singularity service commands:
singularity instance list
singularity instance stop --all
```

## CPUs, Nodes, & Memory

CUBIC has:

- 168 compute nodes

- 4840 CPUs

- 58 TB of RAM

Each node has 2CPUs with 16-24 cores.
### Specifying CPUs on a node

In order to prevent your jobs from dying without the cluster giving errors or warnings, there are several steps that can be taken:

1. Include `-e` in the code to make sure that the environment is clean. It will also be important to check the `.e` log for the environment to spot potential warning that will specify whether or not the environment is corrupted.
2. Check for a core dump to identify whether there are certain jobs that did not go through:
	If there is a `core.XXX` file then the job definitely exited unusually.
3. Some jobs may be killed on cubic if the job is allocated to nodes where the number of CPUs specified in the code is less than the total available CPUs on that node. While it is not possible to select a particular node on CUBIC, it is possible to specify the requirement for submission so that it matches the nodes themselves. It is possible to specify the number of CPUs to be used during submission with the following code:

	a. `qsub -pe threaded N -l h_vmem=XG,s_vmem=YG`
	where `X` and `Y` represent numbers and `N` is the number of CPUs.
	`h_vmem` is the hard limit of the memory up to which the job can consume, and `s_vmem` is the soft virtual memory that is the minimum requested to run the job.

	b. 	`qsub -pe threaded N-M`
	where `N-M` speicify a range of CPUs and `M>N`

### Errors with Allocating Memory/Memory Overflow

Here is an example of a memory allocation error message:

`mmap cannot allocate memory failed (/gpfs/fs001/cbica/projects/RBC/Pipeline_Timing/cpac_1.7.1.simg), reading buffer sequentially…`

If you see this:

- Make sure in this case that everything is in the right directory.

- Make sure that the allocation of memory is specified. Example: `mem_gb 20`

- Make sure that the memory is being requested in the cluster itself and not just specified in the code:
`qsub -l h_vmem=22.5 , s_vmem=22G testrun.sh`

Note that the use of `h_vmem` adds 2.5 GBs to the original `mem_gb` specification. This is to remain on the safe side of memory specification to the cluster as the cluster will kill any job that uses more than the requested memory space when requesting hard memory (`h_vmem`). This function is used to save space on the cluster such that several jobs can be run simultaneously but is only advised to be used when the user is sure about the memory specification needed.

Note that `s_vmem` adds only 2 GBs to the original `mem_gb` specification. This is because soft memory has more flexibility than hard memory specifications. This is recommended to be used when the exact memory required by each subject is not concretely known so as to diminish the risk of the job being killed by accident.

## Running X11 Sessions
Sometimes you'll want to run an application on CUBIC that requires a GUI. In order to be able to view and interact with GUIs from remote applications, you can use X11 to provide a display window.

To get started, you'll probably need to download [XQuartz](https://www.xquartz.org/) (if your local machine is a Mac) or [Xming](http://www.straightrunning.com/XmingNotes/) (for Windows). More information on setting up - as well as detailed instructions for configuring/using Xming - can be found [here](https://cets.seas.upenn.edu/answers/x11-forwarding.html). If you're running Linux, congratulations, should already be good to go. 

To start a X session on CUBIC project user:
1. If you're on a Mac, make sure XQuartz is installed and running. From the terminal, ssh to your account: 
```bash
$ ssh -Y yourusername@cubic-sattertt
```
2. Log into the project user with sudox:
```bash
$ sudox -u projectusername -i
```
3. Load your application from the command line, and the GUI will open

More information on running sudox as project user on CUBIC is available [here](https://cbica-wiki.uphs.upenn.edu/wiki/index.php/Research_Projects#Graphical_Commands_as_Project_Pseudo-User)

## GUIs

On the Satterthwaite Lab node, you can access graphical user interfaces for apps like Afni by launching your session like:

```shell
ssh -X -Y
```

This has been tested only on Mac using the XQuartz utility -- see [here](https://www.cyberciti.biz/faq/apple-osx-mountain-lion-mavericks-install-xquartz-server/) for more on XQuartz.

## Additional information about CUBIC
[This page](https://cbica-wiki.uphs.upenn.edu/wiki/index.php/Research_Projects) has tons of other useful information about using CUBIC. Anyone who plans on using CUBIC regularly should probably browse it. Also, when troubleshooting, make sure the answer to your question isn't on this page before asking others. Note that you will need to be within the UPenn infrastructure (i.e. on campus or using a VPN) to view this page.
