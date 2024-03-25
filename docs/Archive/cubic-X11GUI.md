---
layout: default
title: CUBIC-X11GUI
parent: Archive
nav_order: 2
has_toc: true
---

## Running X11 Sessions
Sometimes you'll want to run an application on CUBIC that requires a GUI. In order to be able to view and interact with GUIs from remote applications, you can use X11 to provide a display window.

To get started, you'll probably need to download [XQuartz](https://www.xquartz.org/) (if your local machine is a Mac) or [Xming](http://www.straightrunning.com/XmingNotes/) (for Windows). More information on setting up - as well as detailed instructions for configuring/using Xming - can be found [here](https://cets.seas.upenn.edu/answers/x11-forwarding.html). If you're running Linux, congratulations, should already be good to go. 

To start a X session on CUBIC project user:
1. If you're on a Mac, make sure XQuartz is installed and running. From the terminal, ssh to your account: 
```bash
$ ssh -Y yourusername@CUBIC-sattertt
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
