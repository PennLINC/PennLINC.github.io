---
layout: default
title: SSH Keys
parent: Computation Basics
has_children: false
nav_order: 2
has_toc: true
---

### Introduction

The Secure Shell Protocol (or SSH) is a cryptographic network protocol that allows users to securely access a remote computer over an unsecured network.

Though SSH supports password-based authentication, it is generally recommended that you use *SSH keys* instead. SSH keys are a more secure method of logging into an SSH server, because they are not vulnerable to common brute-force password hacking attacks.

Generating an SSH key pair creates two long strings of characters: a public and a private key. You can place the public key on any server, and then connect to the server using an SSH client that has access to the private key.

When the public and private keys match up, the SSH server grants access without the need for a password. You can increase the security of your key pair even more by protecting the private key with an optional (but highly encouraged) passphrase.

Step 1 --- Creating the Key Pair
------------------------------

The first step is to create a key pair on the client machine. This will likely be your local computer. Type the following command into your local command line:

```bash
ssh-keygen -t ed25519
```

You should see

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/max/.ssh/id_ed25519):
```

You will see a confirmation that the key generation process has begun, and you will be prompted for some information, which we will discuss in the next step.

Step 2 --- Specifying Where to Save the Keys
------------------------------------------

The first prompt from the `ssh-keygen` command will ask you where to save the keys:

```
Enter file in which to save the key (/Users/<username>/.ssh/id_ed25519):
```

Press `ENTER` here to save the files to the default location in the `.ssh` directory of your home directory.

Alternately, you can choose another file name or location by typing it after the prompt and hitting `ENTER`.

Step 3 --- Creating a Passphrase
------------------------------

The second and final prompt from `ssh-keygen` will ask you to enter a passphrase. Hit `ENTER` twice.

```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/<username>/.ssh/id_ed25519.
```

Finally, it will give you some pretty art under this:
```
The key fingerprint is:
```

The public key is now located in `/Users/<username>/.ssh/id_ed25519.pub`. The private key is now located in `/Users/<username>/.ssh/id_ed25519`.

Step 4 --- Copying the Public Key to Your Server
----------------------------------------------

Once the key pair is generated, it's time to place the public key on the server that you want to connect to.

You can copy the public key into the server's `authorized_keys` file with the `ssh-copy-id`command. Make sure to replace the example username and address (which are mine!)

```
ssh-copy-id USER@SERVER
```

You will be prompted for your password, type it in:

```
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/<username>/.ssh/id_ed25519.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
USER@SERVER's password: 

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'USER@SERVER'"
and check to make sure that only the key(s) you wanted were added.
```
For me, this hangs upon login, so you don't really get confirmation it works. After a minute or so, open a new terminal and ssh in. It should not prompt you for a password if it worked (also try typing in the ssh command with single quotes as above).

Important limitations!!! 
----------
Never run `chmod -R` type commands on your home directory, as the key will no longer work.

Conclusion
----------

In this tutorial we created an SSH key pair, copied our public key to a server, and (optionally) disabled password-based authentication completely. You can now use Visual Code Studio to handle your remote connections to CUBIC or PMACS.
