---
layout: default
title: Data Transfer
parent: CUBIC
nav_order: 3
has_toc: true
---

{:toc}

# Interacting with CUBIC: data analysis and data transfer

You have two resources to interact with data.
You can use CUBIC or you can use your local computer to manipulate data.
Both of these have unique advantages.
CUBIC is a huge and largely non-interactive high performance computing cluster, and your laptop has beautiful graphics and is completely controlled by you.

You’ll have to move data back and forth between these two resources.
This section outlines 3 different approached to do this.


## Method I: (non-interactive)

Because of CUBIC's unique "project user" design, the protocol for moving files to CUBIC is a bit different than on a normal cluster.
It is possible to move files to CUBIC by conventional means, or through your mount point, but this can cause annoying permissions issues and is not recommended.

Note that you will need to be within the UPenn infrastructure (i.e. on VPN or on campus) to move files to and from CUBIC.


### Copying files to CUBIC

All project directories will include a folder called `dropbox/` in the project home directory.
Depositing files into this folder will automatically make the project user the owner of the file.
Please note, however, that this ownership conversion is not always instantaneous and can take a few minutes, so be patient.
Note also that anyone in the project group can move files into this folder.
Finally, keep in mind that the dropbox can only contain 1GB or 1000 files at any given time.

`scp` is the recommended command-line transfer software for moving files onto and off of CUBIC.
One need only specify the file(s) to move and the CUBIC destination.
See the example below, where `<...>` indicates user input:

`scp </path/to/files*.nii.gz> <username>@CUBIC-sattertt:/cbica/projects/<project_dir>/dropbox/`

This command would copy all `nii.gz` files from `/path/to/` into the `dropbox/` folder of your project directory.
Note that you are entering your CUBIC username in the destination, not your project username (confusing, I know).

Moving files directly to a non `dropbox/` folder on CUBIC with scp or your mount point *is* possible for a user with project directory write permissions, though is not recommended.
Such files will retain the ownership of the CUBIC user who transferred the files, and permissions can only be changed by that user or a user with sudo privileges.


### Copying files from CUBIC

This is much simpler. One can simply use scp (or rsync, or whatever) to copy files from a source on CUBIC to their local destination. E.g.

`scp <username>@CUBIC-sattertt:/cbica/projects/<project_dir/path/files.csv> </local/path/to/put/files/>`

It is also possible to copy files through the mount point, but this would be quite slow and is not really the purpose of the mount point.


## Method II: Mounting CUBIC in your local machine (interactive)

### Mounting CUBIC on your local machine using smb

One way to interact with CUBIC files is to _mount_ the server on to your filesystem. This can be useful for quickly moving a small number of files back and forth
(for example with NIfTIs you want't to view). It's _not_ meant for large file management or version control purposes (see the next section for solutions for those).

To mount a directory, (on Mac), use the `samba` server along with Mac's built in server connector.
Follow this [short link](https://support.apple.com/en-gb/guide/mac-help/mchlp1140/mac#:~:text=Connect%20to%20a%20computer%20or%20server%20by%20entering%20its%20address,Click%20Connect.) to see how;
when prompted to select a server address, use:

```
smb://cubic-share.uphs.upenn.edu/cbica/
```

Along with your CUBIC credentials. This is the most seamless method and will likely have better long term support, but again is mostly useful for opening
your home directory, and moving a handful of files about. For more demanding file transfers, including moving files to projects, see the next section.


### Mounting CUBIC on your local machine using FUSE

1. If you are using a Mac, first install [OSXFuse and SSHFS](https://osxfuse.github.io/).

2. Make an empty mount point folder on your local machine. Make sure that only the user (not group or others) have access to this mount directory!
```bash
cd
mkdir -p cbica/projects/<project_name>
chmod 700 cbica/projects/<project_name>
```

3. Mount the desired CUBIC directory to your newly created, local mount directory using SSHfs and CUBIC-sattertt
```bash
SSHfs -o defer_permissions <username>@CUBIC-login.uphs.upenn.edu:/cbica/projects/<project_name>/ /cbica/projects/<project_name>/
```
4. Unmount when done! You should run this unmount command from outside of the mount point.
```bash
cd   # just to make sure we are not inside the mount dir

umount /cbica/projects/<project_name> # note that command is not "unmount"!!
```

5. Make an alias for mounting project directory:
```bash
alias alias_name="SSHfs -o defer_permissions <username>@CUBIC-login.uphs.upenn.edu:/cbica/projects/<project_name> /cbica/projects/<project_name>/"
```


## Method III: Accessing CUBIC via live coding with RStudio or Python (interactive)

### R: Set up and run RStudio instance

Use the following tutorial to set up and run a simple RStudio instance on the cluster. This method of using RStudio with CUBIC is highly recommended for most purposes.

Usage:

0. Log in to the cluster with a port forwarding number. This number must be unique and not shared with anyone (especially important if there are multiple users on a project user). Note that you pick this port forwarding number (i.e. 1337).

```shell
SSH -L localhost:<PORTNUMBER>:localhost:<PORTNUMBER> username@clusterip
```

If you're on PMACS, please make sure to log in *twice*; once onto `bblsub` (as above), and then once more onto the singularity enabled node:

```shell
SSH -L localhost:<PORTNUMBER>:localhost:<PORTNUMBER> singularity01
```

1. Get a compatible singularity image with `rserver` installed

```shell
singularity pull --name singularity-rstudio.simg shub://nickjer/singularity-rstudio
```

2. Clone this repository in an appropriate location in your project

```shell
git clone https://github.com/PennLINC/pennlinc_rstudio.git
```

3. Go to the directory and run the script with your image and port number as input

```shell
cd pennlinc_rstudio
./startup_rstudio.sh <PATH/TO/SINGULARITY/IMAGE.simg> <PORTNUMBER>
```

4. Visit this address in a web browser:

```
localhost:<PORTNUMBER>
```

By default, it uses the `rocker:tidyverse` base image (we will install neuroimaging packages in future).

Side effects:

- The script will create an authorisation key with `uuid` in the user's `$HOME/tmp` directory if it does not exist; this also applies to the project user on CUBIC
- The Singularity instance will remain running unless explicitly stopped with `singularity instance stop`
- R package installations are made to the user's local R location unless explicitly changed.
- Be aware of login nodes on CUBIC -- if you start an RStudio instance with port X on login node 1, and are unexpectedly disconnected from the cluster, that port may be blocked until you can stop the instance on login node 1



# Getting data from flywheel
The source data for some projects may exist on flywheel.
After you've made a flywheel account (go to [upenn.flywheel.io/](https://upenn.flywheel.io/) in Google Chrome) and have been added to the project, navigate to your profile.

### Download the flywheel CLI
Under your profile near the top you should see a section titled 'Flywheel CLI'.
Download the classic CLI for Linux. Unzip the file and follow instructions elswhere on this page to transfer the `fw` executable to your cubic project directory's `~/bin/` path.
At the very bottom of the flywheel profile page, you will see a section titled 'Flywheel Access' and in it a button 'Generate API Key'. Click that button, give your key a name and an expiration date.
Copy the key and save it somewhere safe.

### Building your own glibc on cubic
At the time of these instructions, cubic's `glibc` library version is incompatible with the flywheel CLI.
To circumvent this problem, you will need to download a build your own glibc library to use with flywheel.

#### Load updated make and devtoolset
```bash
module avail make
module load make/<latest_version> ## was 4.3 at the writing of these instructions

module load devtoolset/9
```

#### Create a directory to store glibc source code
```bash
mkdir -p $HOME/bin/glibc
cd $HOME/bin/glibc
```

#### Download and extract glibc
```bash
wget http://ftp.gnu.org/gnu/libc/glibc-2.34.tar.gz
tar -xvzf glibc-2.34.tar.gz
cd glibc-2.34
```

#### Configure and build glibc
```bash
export CFLAGS="-O2"
export CXXFLAGS="-O2"
mkdir build
cd build
../configure --prefix=$HOME/bin/glibc-2.34
make -j$(nproc)
make install
```

The configure and build should take some time.

### Calling fw
Now you should be ready to login to flywheel.
First you'll need to unset your `LD_LIBRARY_PATH` to avoid calling cubic's default glibc.
Now is when you'll need your API key as well.

```bash
unset LD_LIBRARY_PATH # Do not use old GLIBC
~/bin/glibc-2.34/lib/ld-linux-x86-64.so.2 \ # Use new GLIBC
~/bin/fw login YOUR-API-KEY
```

Now you're logged in!
From here you may download specific files or sync the full project.
See flywheel's [documentation](https://docs.flywheel.io/CLI/) for more details.

Note: it's recommended that you use `fw sync` if you want the full project (or even most of it).
The `-m` flag is also advised if you want to get all of the subject/session level metadata.

#### Setting up an alias (optional)
It may be worth it to create an alias if you plan to use `fw` regularly. For example, in .bashrc, you can have:
```bash
alias fww="unset LD_LIBRARY_PATH;~/bin/glibc-2.34/lib/ld-linux-x86-64.so.2 ~/bin/fw"
```
