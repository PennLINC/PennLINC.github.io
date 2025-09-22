---
layout: default
title: CUBIC
has_children: true
has_toc: true
nav_order: 7
---

# Using the CUBIC Cluster

{: .note-title }
> Important
>
> Our documentation on CUBIC reflects the PennLINC team's experience with CUBIC.
> It is not necessarily the most up-to-date information,
> so please refer to the [official CUBIC wiki](https://cbica-portal.uphs.upenn.edu/docs/)
> for the most current documentation.

The CUBIC cluster is a very powerful set of servers that we can use for computing.
Although they are running Linux, familiarity with Linux does not mean that you will be able to effectively use CUBIC.
This section details how to get up and running on the CUBIC cluster.
In general we recommend using CUBIC as a high-performance computing cluster.


# File permissions on CUBIC

Unlike many shared computing environments, read and write permissions are *not* configured using groups.
Instead, individual users are granted access to data on a project-by-project basis.
For example, if you are a member of the project `pnc_fixel_cs` you will not be able to read or write directly to that project's directory (which will be something like `/cbica/projects/pnc_fixel_cs`).

To access a project's files you have to log in as a *project user*.
This is done using the `sudo` command after you have logged in as your individual user.
In this example you would need to use `sudo` to log in as the `pncfixelcs` user and run a shell.
Note that underscores in the project directory are removed when logging in as the project user.
By running

```bash
$ sudo -u pncfixelcs sudosh
```

and entering the same UPHS password you used to log in to your individual user account.
You can see that the project user has their own environment:

```bash
$ echo $HOME
/cbica/projects/pnc_fixel_cs
```

This means that the user will have their own startup scripts like `.bashrc` and `.bash_profile` in their `$HOME` directory.


# Additional information about CUBIC

[The official CUBIC wiki](https://cbica-portal.uphs.upenn.edu/docs/) has tons of other useful information about using CUBIC.
Anyone who plans on using CUBIC regularly should probably browse it.
Also, when troubleshooting, make sure the answer to your question isn't on this page before asking others.
Note that you will need to be within the UPenn infrastructure (i.e. on campus or using a VPN) to view this page,
and using Firefox is recommended.
Other browsers may warn that the page is unsafe.
