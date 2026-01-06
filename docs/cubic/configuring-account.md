---
layout: default
title: Configuring a CUBIC account
parent: CUBIC
nav_order: 4
---

# Configuring a CUBIC account

Note that individual user accounts typically have very little hard drive space allotted to them.
You will likely be doing all your heavy computing while logged in as a project user.
This means that you will want to configure your *project user* account with any software you need.
This example we will use the `xcpdev` account as an example. First, log in as the project user:

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

Additionally, there is something that was recently added that changes your prompt to something unhelpful.
Consider adding:

```bash
export PS1="\[\e[0;32m\]\u@\h\[\e[0m\]:\[\e[0;34m\]\w\[\e[0m\]\$ "
unset LC_ALL
```

to get rid of the locale warnings coming from git/git annex.


# Installing miniforge in your project

You will want a python installation that you have full control over. After logging in as your project user and changing permission on your `.bashrc` file, you can install miniforge using

```bash
$ cd ~
$ wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
$ chmod +x Miniforge3-Linux-x86_64.sh
$ ./Miniforge3-Linux-x86_64
```

You will need to hit Enter to continue and type `yes` to accept the license terms.
The default installation location is fine (it will be `$HOME/miniforge3`).
Sometimes you will run into a memory error at this step.
If this happens, just log out and log back in and the issue should be remediated.
This can be avoided in the first place by, when SSHing into CUBIC, logging into `*login4`.

When prompted if you want to initialize miniforge3, respond again with `yes`

```bash
Do you wish the installer to initialize Miniforge3
by running conda init? [yes|no]
[no] >>> yes
```

For the changes to take place, log out of your sudo bash session and your second bash session, then log back in:

```bash
$ exit
$ sudo -u [PROJECTNAME] sudosh
(base) $ which conda
~/miniforge3/bin/conda
```

You will notice that your shell prompt now begins with `(base)`, indicating that you are in conda's base environment.

There will be a permission issue with your conda installation. You will need to change ownership of your miniconda installation. To fix this run

```bash
$ chown -R $(whoami) ~/miniforge3
```

When you launch jobs on CUBIC, they will autmoatically use CUBIC's base conda environment instead of your project user's miniconda installation. To fix this, you will need to initialize miniconda for a bash script submitted to qsub by running

 ```bash
source ~/miniconda3/etc/profile.d/conda.sh
```

Let's create an environment for this project.

```bash
conda create -n myproject python=3.11
conda activate myproject
```

{: .note-title }
> Note
>
> An important benefit of using Miniforge is that it gives you access to `mamba`!
> This can be used in place of most `conda` commands
> (e.g., `mamba install ...` or `mamba update...`)
> and uses a C-based implementation of `conda` that tends to run noticeably faster.

{: .note-title }
> Tip
>
> For simple use of a Python interpreter managed by `conda`,
> you can use the installed module(s) like `module load python/anaconda/3`.
> But it is **highly recommended** to install miniforge as described above.


# Configuring git in your project

Project users provide a unique situation,
where multiple users will have access to any credentials stored for the project,
but it's easiest to only manage a single set of credentials.
This means that anyone who has access to the project user can also use these credentials.
In order to ensure that other project contributors can't accidentally abuse these credentials
(e.g., by pushing to a GitHub repository that is unrelated to the project),
there are two configurations that we recommend.

For larger projects, where many people will have access to the project user and there will be a lot of GitHub activity,
you may wish to create a GitHub account specifically for the project (e.g., `rbcuser` for the RBC project).
This way, any GitHub activity on the project user will be linked to this project-specific GitHub username,
making it clear that activity is not driven by a single lab member.

For smaller projects, where most GitHub activity will be by a single individual,
we recommend using that individual's GitHub username and setting up a fine-grained personal access token (PAT) on GitHub so that the project user can only commit to repositories linked to the project.
The steps to do this are as follows:

1.  `git config --global user.name <username>`
2.  `git config --global user.email <email>`
3.  `git config --global credential.helper store`
    -   This will store the PAT in ~/.git-credentials.
        It's plain text, but not an issue since we only have one repo.
4.  `git clone https://github.com/PennLINC/<repo>.git code`
    - This will clone the repository into a new folder named "code".
    -   Must be HTTPS
5.  Create fine-grained PAT on GitHub.
    -   Resource owner is PennLINC.
    -   Choose the repositories that are relevant for the project.
    -   Longest expiration time allowed (366 days).
    -   Read access to metadata.
    -   Read and Write access to contents, commit statuses, and pull requests.
    -   Copy the newly generated key to your clipboard.
    -   Ping someone with PennLINC admin priveledges (Matt, Taylor, or Parker) to approve your PAT request.
6.  Now if you commit a change and run `git push` you will be asked to provide credentials:
    -   Put in the username.
    -   Paste the PAT.
7.  Going forward, you can push commits without needing to enter your credentials! (until that PAT expires)

