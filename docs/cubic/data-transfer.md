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

To mount a directory, (on Mac), open Finder and navigate to `Go` > `Connect to Server`.
When prompted to select a server address, use:

```
smb://cubic-share.uphs.upenn.edu/cbica/
```

Input your CUBIC credentials. This is the most seamless method and will likely have better long term support, but again is mostly useful for opening
your home directory, and moving a handful of files about. For more demanding file transfers, talk to Matt to see if its a good idea or not, and what the best approach is.

