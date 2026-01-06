---
layout: default
title: Data Transfer and Analysis
parent: CUBIC
nav_order: 5
---

# Interacting with CUBIC: data analysis and data transfer

You have two resources to interact with data.
You can use CUBIC or you can use your local computer to manipulate data.
Both of these have unique advantages.
CUBIC is a huge and largely non-interactive high performance computing cluster, and your laptop has beautiful graphics and is completely controlled by you.

You'll have to move data back and forth between these two resources.
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
> Why not just use VSCode Remote?
>
>[VSCode-Remote](https://code.visualstudio.com/docs/remote/remote-overview) is VSCode's built-in shipped method for
> working on remote servers. It's well documented, and works just fine as is, but our setup on CUBIC makes it challenging
> to use VSCode remote. The main issue is that the remote server it runs can only have access to the first user who logs in,
> which is not how CUBIC's project user setup works. You end up with a VSCode running from your personal user trying to modify and write files or submit jobs for a project user. We've tried setting up [jump hosts](https://www.doc.ic.ac.uk/~nuric/coding/how-to-setup-vs-code-remote-SSH-with-a-jump-host.html),
> [proxy commands](https://stackoverflow.com/questions/57289351/is-it-possible-to-create-a-proxy-in-remote-SSH-visual-studio-code), and brute forcing a user change with [RemoteCommand](https://github.com/microsoft/vscode-remote-release/issues/690) -- none of the methods worked on CUBIC. Code Server is our next best bet.

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

Let's confirm that you are a project user (instead of using your personal account):
Open a terminal (click icon at the corner of top left -> Terminal --> New Terminal), type `whoami`.
You should see the project user name, instead of your personal username.
This is very important - otherwise, you're editing the files using your personal account, and creating potential permission issues.

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

You can code in Jupyter Notebooks right in `code-server`. First, ensure that you have a [conda environment setup]({{ site.baseurl }}/docs/cubic/configuring-account#installing-miniforge-in-your-project).
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
##    52 pts/112  Sl+     0:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/out/bootstrap-fork --type=ptyHost
##   700 pts/112  Sl+     0:11 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/out/bootstrap-fork --type=extensionHost --uriTrans
##   711 pts/112  Sl+     0:00 /usr/lib/code-server/lib/node /usr/lib/code-server/lib/vscode/out/bootstrap-fork --type=fileWatcher
##   874 pts/112  Sl+     0:00 /cbica/home/taperat/miniconda3/envs/flywheel/bin/python /cbica/home/taperat/.local/share/code-server/extensions/
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

