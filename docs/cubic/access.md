---
layout: default
title: Access and Configuration
parent: CUBIC
nav_order: 1
---

# Getting + setting up your CUBIC account

To get login credentials for CUBIC, you must have already a Penn Medicine account (i.e. an @pennmedicine.upenn.edu email) as well as UPHS VPN.
This is handled in onboarding; if you do not have these ask Ted + post to the #it_issues channel on slack and flag Andrew Zitelli.

Once you do, you can ask for a CUBIC account.
The current procedure is to email Jessica Incmikoski -- the AI2D/CBICA admin -- for an account and CC Ted; who will approve.
She will work with the CUBIC team to initiate account creation.

Once the account is made, you will receive an email with your login credentials and other instructions.
Once you are granted login credentials for CUBIC, you will be able to connect from inside the Penn Medicine network using SSH.
To access the network remotely, follow [instructions to install the client](http://www.uphs.upenn.edu/network/index_vpn.html).
If you can successfully authenticate but are blocked from access, you may need to contact someone to put you on an exceptions list.

Once inside the Penn network, the login to CUBIC looks like this:

```bash
ssh username@cubic-sattertt
```
You use your UPHS password to login. If you don't have access to cubic-sattertt, but do have access to cubic-login then you need to open another ticket to get access.

Note that `cubic-sattertt` is different from the suggested urls in the email you will get from the CUBIC admins after onboarding.
This is a private login node used only by our lab.

# Project Directory Creation Request

Once you have access to CUBIC, you may need to start a project in a new directory.
The direct link to the relevant sections on CUBIC project direction creation is [here](https://cbica-wiki.uphs.upenn.edu/docs/).
This is best viewed in Firefox.
Note again that one must be on the VPN to access this page.

First you need to fill out the data management document available [here](https://cbica-wiki.uphs.upenn.edu/wiki/images/Project_data_use_template.doc).
If this link doesn't work for you, you can find this document on the CBICA Wiki: `Main Page > Research projects > 3 Access/New Project Creation > Project Creation Request`.
This document will ask you for a number of details about your project, including the data's source and estimates about how much disk space you will need over a 6 month, 12 month, and 24 month period, and the estimated lifespan of the data ( 🤷).
PennLINC is only charged for the amount of disk space _actually used_ on a project, not the amount you request at this stage. It is reasonable to be liberal in your disk space estimate at this stage, as it is a pain to upgrade later.
You will also need to provide the CUBIC usernames for everyone you want to have read and/or write access to the project — getting this done ahead of time is strongly recommended because, as you can imagine, requesting changes after-the-fact can be a bother.

Additionally, you will need to be familiar with:

- Whether or not the data has an IRB associated with it and who has approval
- Whether or not the data is the *definitive* source
- Whether or not you have a data use agreement
- What will happen to the data at the end of its expected lifespan on the cluster

This document must be saved as a `.txt` file and before being submitted with your request.

Finally, you will need approval from your PI.
This involves sending an email to the PI with a written blurb to the effect of "Do you approve of this project folder request", to which the PI only needs to respond "Yes, approved".
Once you've got this you can screenshot the conversation (include the date in frame) and save that as an image.

With these two documents, you can now submit the request via the the CBICA Request Tracker.
Similar to the CBICA Wiki, you need to access the Request Tracker through the [PennMedicine Remote Access Portal](https://cbica-portal.uphs.upenn.edu/rt/), then click CBICA Request Tracker.
You'll need your CBICA/cubic login credentials for this (same as UPHS credentials)!

<img src="/assets/images/request-tracker.png" alt="">

Open a new ticket and, fill out the project or user name (the name of your project dicrectory), your username, select your PI from the dropdown, and upload the plain text version of the project request form under 'Data Management', and lastly upload a pdf of your PR's email approvale of the project creation.

<img src="/assets/images/new-project-request2.png" alt="">


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

Additionally, you will want to add the following line to the end of `.bashrc`:

```bash
unset PYTHONPATH
```
