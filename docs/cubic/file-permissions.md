---
layout: default
title: File permissions on CUBIC
parent: CUBIC
nav_order: 3
---

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

