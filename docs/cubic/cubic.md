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

# Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The CUBIC cluster is a very powerful set of servers that we can use for computing. Although they are running Linux, familiarity with Linux does not mean that you will be able to effectively use CUBIC. This section details how to get up and running on the CUBIC cluster. In general we now recommend using [PMACS](https:https://pennlinc.github.io/docs/pmacs) for storing specific analysis projects, and reserve CUBIC for use as a high-performance compute engine for large batches of containerized jobs that are launched from Flywheel.  However, for specific projects (esp collaborations with CBICA), it may make sense to have your project live on CUBIC.

# Setting up your account

To get login credentials for CUBIC, you must have already a Penn Medicine account (i.e. an @pennmedicine.upenn.edu email). Once you do, ask the lab's PMACS/cubic manager (you can ask who this on the #informatics channel on Slack) to create a ticket asking for a new CUBIC account. You will receive an email with your login credentials and other instructions. Once you are granted login credentials for CUBIC, you will be able to connect from inside the Penn Medicine network using SSH. To access the network remotely, follow [instructions to install the client](http://www.uphs.upenn.edu/network/index_vpn.html). If you can successfully authenticate but are blocked from access, you may need to contact someone to put you on an exceptions list.

Once inside the Penn network, the login to CUBIC looks like this:

```python
$ SSH -Y username@CUBIC-sattertt
```
You use your UPHS password to login.

# Project Directory Access Request

Once you have access to CUBIC, you may need to start a project in a new directory. You can find the CBICA Wiki, which covers project creation instructions (also described below), through the [PennMedicine Remote Access Portal](https://pennmedaccess.uphs.upenn.edu/). After logging in with your UPHS credentials, you can find the CBICA Wiki under "Corporate Resources." 
 

First you need to fill out the data management document available [here](https://cbica-wiki.uphs.upenn.edu/wiki/images/Project_data_use_template.doc). If this link doesn't work for you, you can find this document on the CBICA Wiki: `Main Page > Research projects > 3 Access/New Project Creation > Project Creation Request`. This document will ask you for a number of details about your project, including the data's source and estimates about how much disk space you will need over a 6 month, 12 month, and 24 month period, and the estimated lifespan of the data ( 🤷). You will also need to provide the CUBIC usernames for everyone you want to have read and/or write access to the project — getting this done ahead of time is strongly recommended because, as you can imagine, requesting changes after-the-fact can be a bother.

Additionally, you will need to be familiar with:

- Whether or not the data has an IRB associated with it and who has approval
- Whether or not the data is the *definitive* source
- Whether or not you have a data use agreement
- What will happen to the data at the end of its expected lifespan on the cluster

This document must be saved as a `.txt` file and before being submitted with your request.

Finally, you will need approval from your PI. This involves sending an email to the PI with a written blurb to the effect of "Do you approve of this project folder request", to which the PI only needs to respond "Yes, approved". Once you've got this you can screenshot the conversation (include the date in frame) and save that as an image.

With these two documents, you can now submit the request via the the CBICA Request Tracker. Similar to the CBICA Wiki, you need to access the Request Tracker through the [PennMedicine Remote Access Portal](https://pennmedaccess.uphs.upenn.edu/), then click CBICA Request Tracker. You'll need your CBICA/cubic login credentials for this (same as UPHS credentials).

<img src="/assets/images/request-tracker.png" alt="">

Open a new ticket and, like applying for a job, **FILL OUT THE REQUEST WITH THE EXACT SAME INFORMATION AS YOU JUST FILLED IN THE DOCUMENT.** 😓

<img src="/assets/images/new-project-request.png" alt="">

Lastly, attach your supporting documents.

The process for accessing an existing project is similar, but fortunately you will not have to fill out a new data management document; only the PI approval and filling of the online ticket is required. You should receive an email from CBICA confirming your request, and you can always return to the Request Tracker to see the status of your ticket.


# File permissions on CUBIC

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

# Configuring a CUBIC account

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
-rw-r-----.   1 xcpdev xcpdev         0 Oct  9 16:52 .tmpcheck-CUBIC-sattertt
-rw-r-x---.   1 root   root        2360 Jul  9  2018 xcpDev_Project_Data_use.txt*
```

Notice that `.bashrc` is not writable by anyone. We'll need to change this temporarily so we can configure the environment. To do so, run

```bash
$ chmod +w .bashrc
$ ls -al .
...
-rw-rwx---.   1 xcpdev xcpdev      1123 Jul  9  2018 .bashrc*
...
```

and we can see that the file is now writable.

## Quick fixes for annoying behavior

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

We recommend that when you launch a script requiring your `conda` environment and packages, you add `source activate <env>` to the topof your script. To change the default installation for a given software
package, prepend the path to your `$PATH` and source your `.bashrc`:

```bash
echo PATH=/directory/where/your/installation/lives:${PATH} >> ~/.bashrc
source ~/.bashrc
```

# Installing miniconda in your project

You will want a python installation that you have full control over. After logging in as your project user and changing permission on your `.bashrc` file, you can install miniconda using

```bash
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-Linux-x86_64.sh
```

You will need to hit Enter to continue and type `yes` to accept the license terms. The default installation location is fine (it will be `$HOME/miniconda3`). Sometimes you will run into a memory error at this step. If this happens, just log out and log back in and the issue should be remediated. This can be avoided in the first place by, when SSHing into CUBIC, logging into `*login4`.

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

When you launch jobs on CUBIC, they will autmoatically use CUBIC's base conda environment instead of your project user's miniconda installation. To fix this, you will need to initialize miniconda for a bash script submitted to qsub by running

 ```bash
$ source ~/miniconda3/etc/profile.d/conda.sh
```

Let's create an environment we will use for interacting with flywheel.

```bash
$ conda create -n flywheel python=3.7
$ conda activate flywheel
$ pip install flywheel-sdk
```

Note: For simple use of a Python interpreter managed by `conda`, you can use the installed module(s) like `module load python/anaconda/3`. But it is highly recommended to install miniconda as described above.

# Interacting with CUBIC: data analysis and data transfer

You have two resources to interact with data. You can use CUBIC or you can use your local computer to manipulate data. Both of these have unique advantages. CUBIC is huge and largely non-interactive high performance computing cluster, and your laptop has beautiful graphics and is completely controlled by you.

You’ll have to move data back and forth between these two resources. This section outlines 3 different approached to do this.

## Method I: (non-interactive)

Because of CUBIC's unique "project user" design, the protocol for moving files to CUBIC is a bit different than on a normal cluster. It is possible to move files to CUBIC by conventional means, or through your mount point, but this can cause annoying permissions issues and is not recommended.

Note that you will need to be within the UPenn infrastructure (i.e. on VPN or on campus) to move files to and from CUBIC.

### Copying files to CUBIC
All project directories will include a folder called `dropbox/` in the project home directory. Depositing files into this folder will automatically make the project user the owner of the file. Please note, however, that this ownership conversion is not always instantaneous and can take a few minutes, so be patient. Note also that anyone in the project group can move files into this folder. Finally, keep in mind that the dropbox can only contain 1GB or 1000 files at any given time.

`scp` is the recommended command-line transfer software for moving files onto and off of CUBIC. One need only specify the file(s) to move and the CUBIC destination. See the example below, where `<...>` indicates user input:

`scp </path/to/files*.nii.gz> <username>@CUBIC-sattertt:/cbica/projects/<project_dir>/dropbox/`

This command would copy all `nii.gz` files from `/path/to/` into the `dropbox/` folder of your project directory. Note that you are entering your CUBIC username in the destination, not your project username (confusing, I know).

Moving files directly to a non `dropbox/` folder on CUBIC with scp or your mount point *is* possible for a user with project directory write permissions, though is not recommended. Such files will retain the ownership of the CUBIC user who transferred the files, and permissions can only be changed by that user or a user with sudo priveleges.

### Copying files from CUBIC
This is much simpler. One can simply use scp (or rsync, or whatever) to copy files from a source on CUBIC to their local destination. E.g.

`scp <username>@CUBIC-sattertt:/cbica/projects/<project_dir/path/files.csv> </local/path/to/put/files/>`

It is also possible to copy files through the mount point, but this would be quite slow and is not really the purpose of the mount point.

## Method II: Mounting CUBIC in your local machine (interactive)

### Mounting CUBIC on your local machine using smb
 
One way to interact with CUBIC files is to _mount_ the server on to your filesystem. This can be useful for quickly moving a small number of files back and forth
(for example with NIfTIs you want't to view). It's _not_ meant for large file management or version control purposes (see the next section for solutions for those).

To mount a directory, (on Mac), use the `samba` server along with Mac's built in server connector. Follow this [short link](https://support.apple.com/en-gb/guide/mac-help/mchlp1140/mac#:~:text=Connect%20to%20a%20computer%20or%20server%20by%20entering%20its%20address,Click%20Connect.) to see how; when prompted to
select a server address, use:

```
smb://cubic-share.uphs.upenn.edu/cbica/
```

Along with your CUBIC credentials. This is the most seamless method and will likely have better long term support, but again is mostly useful for opening
your home directory, and moving a handful of files about. For more demanding file transfers, including moving files to projects, see the next section.

### Mounting CUBIC on your local machine using FUSE

1. If you are using a Mac, first install [OSXFuse and SSHFS](https://osxfuse.github.io/).

2. Make an empty mount point folder on your local machine. Make sure that only the user (not group or others) have access to this mount directory!
```bash
$ cd 
$ mkdir -p cbica/projects/<project_name> 
$ chmod 700 cbica/projects/<project_name> 
```

3. Mount the desired CUBIC directory to your newly created, local mount directory using SSHfs and CUBIC-sattertt
```bash
$ SSHfs -o defer_permissions <username>@CUBIC-login.uphs.upenn.edu:/cbica/projects/<project_name>/ /cbica/projects/<project_name>/
```
4. Unmount when done! You should run this unmount command from outside of the mount point.
```bash
$ cd   # just to make sure we are not inside the mount dir

$ umount /cbica/projects/<project_name> # note that command is not "unmount"!!
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

### Python: Working with Visual Code Studio

#### Prerequisite

You will need [SSH keys](https://pennlinc.github.io/docs/Basics/SSHKeys/) set up, a PMACS or CUBIC account (with VPN).

#### General Principles & Motivation

1. We want to code interactively with zero lag in a format that encourages documenting your code
2. We want the software and data we are using to be on the cluster, preventing version issues or having to download a test set to your local machine
3. We want it to cooperate with all of CUBIC's nuances
3. We want it to be easy!

This means we are going to not use X11 at all. Why? Because running graphics on the cluster, and then having them sent to your local screen, is very laggy and not dependable.

#### Code Server

There are many viable IDEs for interactive coding, and a very popular/accessible one is [VSCode](https://code.visualstudio.com/). It's packed with features, plugins, and themes that make writing code fun and easy. Internally, it's a nodejs app
written in React and runs on Chrome, which technically means it's a server. Indeed, a group called [Coder](https://coder.com/)
have already developed and released the application for _just the backend server_, that users can easily run as an app
on their machine and send the pretty graphics to a browser themselves. That's what we're going to do here using singularity
and SSH port forwarding.

{: .note-title }
> ##### Why not just use VSCode Remote?
>
>[VSCode-Remote](https://code.visualstudio.com/docs/remote/remote-overview) is VSCode's built-in shipped method for
working on remote servers. It's well documented, and works just fine as is, but our setup on CUBIC makes it challenging
to use VSCode remote. The main issue is that the remote server it runs can only have access to the first user who logs in,
which is not how CUBIC's project user setup works. You end up with a VSCode running from your personal user trying to modify and write files or submit jobs for a project user. We've tried setting up [jump hosts](https://www.doc.ic.ac.uk/~nuric/coding/how-to-setup-vs-code-remote-SSH-with-a-jump-host.html),
[proxy commands](https://stackoverflow.com/questions/57289351/is-it-possible-to-create-a-proxy-in-remote-SSH-visual-studio-code), and brute forcing a user change with [RemoteCommand](https://github.com/microsoft/vscode-remote-release/issues/690) -- none of the methods worked on CUBIC. Code Server is our next best bet.

#### Installation

Before doing any installation or running any singularity image, please make sure you are using CUBIC as a project user:
```shell
sudo -u <project_username> sudosh
```

First, we're going to install the necessary requirements for running the app. So go ahead and log in to CUBIC and head to
an appropriate project directory (yes, this works for multiple CUBIC project users) or your user directory.

First, you'll want to install Node using NVM (Node Version Manager). I'd suggest creating a `software` directory to manage
all of this, and download the installation of NVM:

```shell
# make sure bashrc is writable
cd ~
chmod +w .bashrc

mkdir ~/software && wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

This post script ensures it's available; copy-paste and run:
```shell
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

Lastly, exit and re-login to the terminal, and check everything went well with:

```shell
nvm -v
```

Next, install Node version 16 (the version is important):

```shell
nvm install --lts # install node
nvm install 16    # version number updated on 11/7/22

node -v           # check the version
```

From here, you can install the underlying `code-server` application:

```shell
npm install -g code-server --unsafe-perm # unsafe is necessary on CUBIC for permissions reasons
```

If there is error message from above command, try these instead:

```shell
npm install -g yarn
yarn add code-server
```


At this point, you're ready to run `code-server`, but you can only do it as a
_service_, and for that we use singularity. Let's set up the necessary singularity image.

```shell
mkdir -p ~/software/singularity_images && cd ~/software/singularity_images
singularity pull docker://codercom/code-server
```

That's it! You're ready to code with `code-server`.

#### Basic Use of Code Server

You can take a look at the options available for `code-server` really quickly with `singularity exec`:

```shell
singularity exec ~/software/singularity_images/code-server_latest.sif code-server -h
```

What we want to do is start a singularity instance to run the service, and then execute the app
in that instance. You also want to make sure `code-server` has access to things like CUBIC's tempdir:

```shell
singularity instance start \
    --bind $PWD,$TMPDIR \
    ~/software/singularity_images/code-server_latest.sif \
    my-vscode # You can name the instance anything you want
```

You can name the instance anything you want; if you're working in a CUBIC project directory
with multiple users, you can log in to the project user and name your instance with your own
name to differentiate it from other users. You can always check what singularity instances
are running with `singularity instance list`.

Now, in that instance, start running code-server:

```
PORT=8767

singularity exec \
    --bind $PWD,$TMPDIR \
    instance://my-vscode \
    code-server \
    --port $PORT &         # use & so you can run in the background and continue using the shell

# expect a printout with node runtime
```

The `PORT` argument is important; it must be a number of 4-5 digits that is unique to you. The reason
being that this is the "channel" that your local machine will use to send inputs and outputs back and forth
to the running singularity instance. So pick one number, and stick with it.

Lastly, open a new terminal window to manage the `PORT` and link it with the same number:

```
SSH -L localhost:8767:localhost:8767 <username>@CUBIC-sattertt    # change <username> to your CUBIC username

# this process must remain running so don't `ctrl`+`c` it until you're done working
```

Now, in your web browser locally, visit `localhost:YOURPORT` (in this example, `localhost:8767`).
If you see this screen, you're in business:

<img src="/assets/images/vscode_login.png" alt="login">

To login, go back to your terminal and find the password in the config file and input:

```shell
# please first make sure you have logged in as CUBIC project user, instead of personal user (as the config.yaml is saved in project user folder):
# sudo -u <project_username> sudosh

cat ~/.config/code-server/config.yaml
```

Here we are, editing code on CUBIC with the beautiful VSCode IDE:

<img src="/assets/images/vscode_running.png" alt="login">

Let's confirm that you are a project user (instead of using your personal account): Open a terminal (click icon at the corner of top left -> Terminal --> New Terminal), type `whoami`. You should see the project user name, instead of your personal username. This is very important - otherwise, you're editing the files using your personal account, and creating potential permission issues.

`code-server` is almost exactly VSCode, so if you want to make the most of this powerful IDE,
visit [their intro guide](https://code.visualstudio.com/docs/getstarted/tips-and-tricks).

#### Caveats & Limitations

1. VSCode has a great interface for git, but will struggle to manage a very large directory that's tracked by
git; be prepared for it to notify you if you, for example, open a BIDS directory tracked with datalad

2. The integrated terminal is a shell opened by Singularity, so it does not source your `bashrc`/`bash_profile`.
This means some of your installed command line programs may not be accessible. Keep your normal terminal open alongside
your `code-server` GUI for best practices.

3. All users in a project share the same `~/.config/code-server/config.yaml`, so the password is not unique by default.
It is possible to deactivate authentication when you start the server with `--auth none`, and it's also possible
to point to a specific config file with `--config` that you could use to keep your own password (untested).

4. Similarly, with VSCode extensions, it's recommended to store your extensions in a specific directory
if you expect to share the project directory. You can then point to it with `--user-data-dir` and `--extensions-dir`.
This is arguably less seamless than [VSCode-Remote](https://code.visualstudio.com/docs/remote/remote-overview) functionality, but we believe this is a better workaround because
VSCode-Remote is not fully functional in our case.

Speaking of extensions...

#### Basic extensions

Max put together a great list of extensions [here](https://raw.githubusercontent.com/PennLINC/PennLINC.github.io/master/docs/Basics/vs-code-extension-list_mb.txt); check them out and install them with the Extensions Tab.

For example, with VSPapaya, you can open NIfTIs and DICOMs:

<img src="/assets/images/vspapaya.png" alt="vspapaya">

You get great integration with Git using the Git Extension pack

<img src="/assets/images/vscode_git_tree.png" alt="git">

The most important, however, is how to enable interactive, REPL style programming for active debugging and data
analysis. We do this with `conda`.

#### REPL (Interactive Programming)

You can code in Jupyter Notebooks right in `code-server`. First, ensure that you have a [conda environment setup](http://pennlinc.github.io/docs/cubic#installing-miniconda-in-your-project-the-hard-way).
Once you're ready, start up your `code-server` and make sure the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) is installed. Use the command palette (`cmd`+`shift`+`p`) to search for Jupyter interpreters.

<img src="https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/OpenCommandPalatte.gif" alt="cmdpalette">

In the command palette, simply type `interpreter`, and select "Jupyter: Select interpreter to start Jupyter server".

If you have `conda` set up correctly, your `code-server` should begin listing what conda environments you have
and the different versions of Python that are available. Once you've picked one, you can then run/debug a Python file
in a Jupyter kernel, debug files with the built-in debugger, develop Jupyter notebooks, etc.

<img src="/assets/images/vscode_features.png" alt="all features!">

#### Closing the Server

If you disconnect from CUBIC unexpectedly, the process running `code-server` (the `singularity exec`) will be killed, so
actively running Jupyter kernels will be lost. Generally, though, if the `singularity instance` service is still running,
unsaved files can still be recovered (always save your work though, of course). To stop the server, find the process _within_ the singularity instance, and kill it:

```shell
singularity exec instance://my-vscode ps -x

##   PID TTY      STAT   TIME COMMAND
##     1 ?        Sl     0:00 sinit
##    16 pts/112  Sl+    0:01 /usr/lib/code-server/lib/node /usr/lib/code-server --port 8767
##    40 pts/112  Sl+    0:38 /usr/lib/code-server/lib/node /usr/lib/code-server --port 8767
##    52 pts/112  Sl+    0:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/out/bootstrap-fork --type=ptyHost
##   700 pts/112  Sl+    0:11 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/out/bootstrap-fork --type=extensionHost --uriTrans
##   711 pts/112  Sl+    0:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/out/bootstrap-fork --type=fileWatcher
##   874 pts/112  Sl+    0:00 /cbica/home/taperat/miniconda3/envs/flywheel/bin/python /cbica/home/taperat/.local/share/code-server/extensions/
##   886 pts/112  S+     0:00 /cbica/home/taperat/miniconda3/bin/python /cbica/home/taperat/.local/share/code-server/extensions/ms-python.pyth
##   914 pts/117  Ss     0:00 /bin/bash
##  1063 pts/117  S+     0:00 /cbica/home/taperat/miniconda3/envs/flywheel/bin/python
##  1151 pts/112  R+     0:00 /bin/ps -x

singularity exec instance://my-vscode kill 16 # kill the node code-server process
```

If you are happy with your work and your project, and don't plan to come back to it for a while, make sure
to kill the singularity instance to free up compute resources

```shell
singularity instance stop my-vscode
```

#### Conclusion

We encourage you to try out interactive programming with `code-server`. It's a great tool for data science that we
hope you'll take advantage of and customize for your work. If you have any trouble running it, improvements to suggest, or want to share a cool
workflow or extension, please do so on the slack informatics channel or in our [issues page](https://github.com/PennLINC/PennLINC.github.io/issues). Many thanks to [this blog](https://isaiahtaylor.medium.com/use-vs-code-on-a-supercomputer-15e4cbbb1bc2) for demonstrating
this first.

# Using R/R-studio and Installation of R packages on CUBIC
 
## Use R and RStudio on CUBIC directly 
1. Currently  R-4.2.2 is installed on CUBIC. If you are satisfied with R-4.2.2, simply load it with `module load R/4.2.2`, and directly go to step 2 below. However, you can install another R version in any directory of your choice, usually home directory `/cbica/home/username`.
To install R in your desired directory, follow the following steps.

   ```bash
   $ module load curl/7.56.0  # load the libcurl library
   $ wget http://cran.rstudio.com/src/base/R-4/R-4.2.2.tar.gz #e.g R-4.2.2
   $ tar xvf R-4.2.2.tar.gz
   $ cd R-4.2.2
   $ ./configure --prefix=$HOME/R  --enable-R-shlib #$HOME/R is where R will be installed
   $ make && make install

   ```

     Then, installation of R is complete.
    To run R, add `$HOME/R/bin` to your PATH. Then, shell commands like R and Rscript will work.
   ```bash
    echo export PATH="$HOME/R/bin:$PATH" >> .bash_profile or .bashrc # add R to bash
   ```
   To run R:
   ```bash
   $ module load R
   $ R
   ```

    >You can load higher version of `gcc` compiler if required for some R version.
   ```bash
    $ module load gcc/version-number
   ```

2. You can install R-packages of your choice. It require adding library path in `.Rprofile` . You also may need to specify the base URL(s) of the repositories to use. Furthermore, you should specific lib.loc when loading packages. Note that some packages, such as "tidyverse", have run into a lot of issues when trying to install directly onto CUBIC. See [next section](#use-a-docker-image-containing-r-packages-on-CUBIC) for a workaround.

    ```R
       .libPaths('/cbica/home/username/Rlibs`)
       install.packages("package_name", repos='http://cran.us.r-project.org', lib='/cbica/home/username/Rlibs') 
       library(package_name, lib.loc="/cbica/home/username/Rlibs")

    ```
    You can have more than one R-packages directory.
    
3. You can also use r-studio on CUBIC  by simply load rstudio using `module`.

     ```bash
      $ module load R-studio/1.1.456
      $ rstudio & # enjoy the R and Rstudio, it works
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
If you run into issues installing your needed R packages on CUBIC, you can use a Docker image that contains a number of R packages already. For example, if you have a huge analysis in R that requires you to submit a job on CUBIC, but you can't successfully install your R packages of interests onto CUBIC, this method is a great workaround. 

This [docker-R github repo](https://github.com/PennLINC/docker_R) contains documentation on how you can either 1) directly use [a publicly available Docker image](https://hub.docker.com/r/pennlinc/docker_r) that contains a bunch of R packages already, or 2) build your own Docker image with the specific packages you need. After setting up your Docker image, you can submit a job on CUBIC to run all the Rscripts you want! For details, please see instructions [here](https://github.com/PennLINC/docker_R).


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

# Using "screen" on CUBIC

Note: `screen` sessions must be run under `CUBIC-sattertt`.

## Why "screen"

Have you ever faced the scenario where you are testing a script interactively on the login node of your remote machine, and suddenly the VPN connection drops and your work is lost? Luckily, there is a Linux utility called `screen` on the `sattertt` login node that allows us to resume sessions that otherwise would be lost. 


`screen` comes in handy when you want to let stuff run in the background without having to maintain a VPN or SSH connection. For example, let's say you want to submit many jobs to CUBIC at once. Since it can take a few minutes for each job to submit, you'd need to hold your VPN connection and your terminal window open for many hours if you're submitting several hundreds or even thousands of jobs. This is unrealistic for several reasons: your VPN connection is very likely to occassionally get dropped; your wifi connection might fail; you might accidentally close a terminal window; or maybe you just don't want to be biking down the Schuylkill river trail with your laptop open. In any case, you don't want to have to start all over or figure out where it left off if something interrupts your job submissions. 

The `screen` command will allow you to safely run whatever you need even without maintaining a connection and then return to check in on your process later. 

## What is "screen"

`screen` is a terminal window manager. When you call the screen command, it creates a separate window where you can work as you would in a normal terminal window. `screen` is already installed in the `sattertt` node. 

## Start a session
You can type `screen` to start a screen session. 

If you want to specify a meaningful name for the session in place of the default `CUBIC-sattertt` suffix, you can use the `-S` flag as in `screen -S [session_name]`. Type `man screen` for more information. If you are interested, you can also check out the [official GNU screen documentation](https://www.gnu.org/software/screen/manual/screen.html#Overview) for more customization tips.

Here I am creating a new screen session with the name `example`.

```bash
(base) [username@CUBIC-sattertt ~]$ screen -S example 
```


Note that it should say something like `[screen 0: username@CUBIC-sattertt:~]` on the terminal tab bar after creating the session.


You can use `screen -ls` to ensure that the screen session has been started.

```bash
(base) [username@CUBIC-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Attached)
1 Socket in /var/run/screen/S. 

```
## Detach a session

As previously mentioned, programs launched in a screen session would continue to run when their window is closed or when the screen session is detached from the terminal. 

The reason is because `screen` makes it possible for you to leave a terminal window (detach) and return to it later (reattach). This can come in handy when you are `rsync`-ing files between two servers or any other commands that can take an unpredictable amount of time. 

`screen -d` would detach the current screen session.


If you have several screen sessions going on, you can provide the session id of the specific screen session that you'd like to reattach:

`screen -d session_id`

Here I detach the screen session by specifying the session id

```bash
(base) [username@CUBIC-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Attached)
1 Socket in /var/run/screen/S. 

(base) [username@CUBIC-sattertt ~]$ screen -d example # input
```

Again, you can use `screen -ls` to ensure that the screen session has been detached.

```bash
(base) [username@CUBIC-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Detached)
1 Socket in /var/run/screen/S. 


```

_Note: You can send commands to a screen session instead of the shell by pressing `Ctrl-a` (that is pressing the control key and the letter `a` at the same time)._

Now feel free to do other stuff!

## Reattach a session

How do we return to and check on the programs launched earlier in  a detached screen session? The magic wand we use is reattach the session.
`screen -r` would reattach the detached screen session.

If you have several screen sessions going on, you can provide the session id of the specific screen session that you'd like to reattach:

`screen -r session_id`

Here I detach the screen session by specifying the session name (which is also okay)

```bash

(base) [username@CUBIC-sattertt ~]$ screen -r example # input

```

Again, you can use `screen -ls` to ensure that the screen session has been reattached.

```bash
(base) [username@CUBIC-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Attached)
1 Socket in /var/run/screen/S. 


```

## Exit a session

Type `exit` on the screen terminal window to exit the session completely. 

```bash

(base) [username@CUBIC-sattertt ~]$ exit # input

```

You will be dropped back to your shell and see the message `[screen is terminating]`.



As an alternative, you can also press `Ctrl-a` and `k`. If you do so, you will be  asked `Ready kill this window [y/n]?`. 

## If you forgot to detach

If you lost the VPN connection or close the session terminal window or without detaching the session, you can run `screen -d -r` or `screen -dr` to return to the previously launched screen session.

## Summary of handy "screen" commands

- Start a named screen session - `screen -S [session_name]`
- Display all available screen sessions running in your system - `screen -ls`
- Detach a screen session - `screen -d [optional: screen_id]` or `Ctrl-a` and `d`
- Reattach a screen session - `screen -r [optional: session_id]` 


## Other resources

I've used the resources below in this tutorial. Feel free to check them out.

[How To Use Linux Screen - rackAID](https://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/)

[Why and How to use Linux Screen Tool](https://www.youtube.com/watch?v=TEehA8Q3D18)

[Using Screen - MIT SIPB](https://sipb.mit.edu/doc/screen/)

# Job submission on CUBIC

## Specifying CPUs on a node

In order to prevent your jobs from dying without the cluster giving errors or warnings, there are several steps that can be taken:

1. Include `-e` in the code to make sure that the environment is clean. It will also be important to check the `.e` log for the environment to spot potential warning that will specify whether or not the environment is corrupted.
2. Check for a core dump to identify whether there are certain jobs that did not go through:
	If there is a `core.XXX` file then the job definitely exited unusually.
3. Some jobs may be killed on CUBIC if the job is allocated to nodes where the number of CPUs specified in the code is less than the total available CPUs on that node. While it is not possible to select a particular node on CUBIC, it is possible to specify the requirement for submission so that it matches the nodes themselves. It is possible to specify the number of CPUs to be used during submission with the following code:

	a. `qsub -pe threaded N -l h_vmem=XG,s_vmem=YG`
	where `X` and `Y` represent numbers and `N` is the number of CPUs.
	`h_vmem` is the hard limit of the memory up to which the job can consume, and `s_vmem` is the soft virtual memory that is the minimum requested to run the job.

	b. 	`qsub -pe threaded N-M`
	where `N-M` speicify a range of CPUs and `M>N`

## Errors with Allocating Memory/Memory Overflow

Here is an example of a memory allocation error message:

`mmap cannot allocate memory failed (/gpfs/fs001/cbica/projects/RBC/Pipeline_Timing/cpac_1.7.1.simg), reading buffer sequentially…`

If you see this:

- Make sure in this case that everything is in the right directory.

- Make sure that the allocation of memory is specified. Example: `mem_gb 20`

- Make sure that the memory is being requested in the cluster itself and not just specified in the code:
`qsub -l h_vmem=22.5 , s_vmem=22G testrun.sh`

Note that the use of `h_vmem` adds 2.5 GBs to the original `mem_gb` specification. This is to remain on the safe side of memory specification to the cluster as the cluster will kill any job that uses more than the requested memory space when requesting hard memory (`h_vmem`). This function is used to save space on the cluster such that several jobs can be run simultaneously but is only advised to be used when the user is sure about the memory specification needed.

Note that `s_vmem` adds only 2 GBs to the original `mem_gb` specification. This is because soft memory has more flexibility than hard memory specifications. This is recommended to be used when the exact memory required by each subject is not concretely known so as to diminish the risk of the job being killed by accident.

## Useful tips and tricks

# Additional information about CUBIC
[This page](https://cbica-wiki.uphs.upenn.edu/wiki/index.php/Research_Projects) has tons of other useful information about using CUBIC. Anyone who plans on using CUBIC regularly should probably browse it. Also, when troubleshooting, make sure the answer to your question isn't on this page before asking others. Note that you will need to be within the UPenn infrastructure (i.e. on campus or using a VPN) to view this page.
