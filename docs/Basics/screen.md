---
layout: default
title: Using screen
parent: Computation Basics
has_children: false
nav_order: 6
has_toc: true
---

# Using `screen`


## Why `screen`

Have you ever faced the scenario where you are testing a script interactively on the login node of your remote machine, and suddenly the VPN connection drops and your work is lost? Luckily, there is a Linux utility called `screen` on the `sattertt` login node that allows us to resume sessions that otherwise would be lost. 


`screen` comes in handy when you want to let stuff run in the background without having to maintain a VPN or SSH connection. For example, let's say you want to submit many jobs to cubic at once. Since it can take a few minutes for each job to submit, you'd need to hold your VPN connection and your terminal window open for many hours if you're submitting several hundreds or even thousands of jobs. This is unrealistic for several reasons: your VPN connection is very likely to occassionally get dropped; your wifi connection might fail; you might accidentally close a terminal window; or maybe you just don't want to be biking down the Schuylkill river trail with your laptop open. In any case, you don't want to have to start all over or figure out where it left off if something interrupts your job submissions. 

The `screen` command will allow you to safely run whatever you need even without maintaining a connection and then return to check in on your process later. 


## What Is `screen`

`screen` is a terminal window manager. When you call the screen command, it creates a separate window where you can work as you would in a normal terminal window. `screen` is already installed in the `sattertt` node. 

## Start a Session
You can type `screen` to start a screen session. 

If you want to specify a meaningful name for the session in place of the default `cubic-sattertt` suffix, you can use the `-S` flag as in `screen -S [session_name]`. Type `man screen` for more information. If you are interested, you can also check out the [official GNU screen documentation](https://www.gnu.org/software/screen/manual/screen.html#Overview) for more customization tips.

Here I am creating a new screen session with the name `example`.

```bash
(base) [username@cubic-sattertt ~]$ screen -S example 
```


Note that it should say something like `[screen 0: username@cubic-sattertt:~]` on the terminal tab bar after creating the session.


You can use `screen -ls` to ensure that the screen session has been started.

```bash
(base) [username@cubic-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Attached)
1 Socket in /var/run/screen/S. 

```
## Detach a Session

As previously mentioned, programs launched in a screen session would continue to run when their window is closed or when the screen session is detached from the terminal. 

The reason is because `screen` makes it possible for you to leave a terminal window (detach) and return to it later (reattach). This can come in handy when you are `rsync`-ing files between two servers or any other commands that can take an unpredictable amount of time. 

`screen -d` would detach the current screen session.


If you have several screen sessions going on, you can provide the session id of the specific screen session that you'd like to reattach:

`screen -d session_id`

Here I detach the screen session by specifying the session id

```bash
(base) [username@cubic-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Attached)
1 Socket in /var/run/screen/S. 

(base) [username@cubic-sattertt ~]$ screen -d example # input
```

Again, you can use `screen -ls` to ensure that the screen session has been detached.

```bash
(base) [username@cubic-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Detached)
1 Socket in /var/run/screen/S. 


```

_Note: You can send commands to a screen session instead of the shell by pressing `Ctrl-a` (that is pressing the control key and the letter `a` at the same time)._

Now feel free to do other stuff!
## Reattach a Session

How do we return to and check on the programs launched earlier in  a detached screen session? The magic wand we use is reattach the session.
`screen -r` would reattach the detached screen session.

If you have several screen sessions going on, you can provide the session id of the specific screen session that you'd like to reattach:

`screen -r session_id`

Here I detach the screen session by specifying the session name (which is also okay)

```bash

(base) [username@cubic-sattertt ~]$ screen -r example # input

```

Again, you can use `screen -ls` to ensure that the screen session has been reattached.

```bash
(base) [username@cubic-sattertt ~]$ screen -ls # input

There is a screen on:               # output
	155085.example	(Attached)
1 Socket in /var/run/screen/S. 


```
## Exit a Session





Type `exit` on the screen terminal window to exit the session completely. 

```bash

(base) [username@cubic-sattertt ~]$ exit # input

```

You will be dropped back to your shell and see the message `[screen is terminating]`.



As an alternative, you can also press `Ctrl-a` and `k`. If you do so, you will be  asked `Ready kill this window [y/n]?`. 

## If You Forgot to Detach

If you lost the VPN connection or close the session terminal window or without detaching the session, you can run `screen -d -r` or `screen -dr` to return to the previously launched screen session.

## Summary of Handy `screen` Commands
- Start a named screen session - `screen -S [session_name]`
- Display all available screen sessions running in your system - `screen -ls`
- Detach a screen session - `screen -d [optional: screen_id]` or `Ctrl-a` and `d`
- Reattach a screen session - `screen -r [optional: session_id]` 


## Other Resources
I've used the resources below in this tutorial. Feel free to check them out.

[How To Use Linux Screen - rackAID](https://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/)

[Why and How to use Linux Screen Tool](https://www.youtube.com/watch?v=TEehA8Q3D18)

[Using Screen - MIT SIPB](https://sipb.mit.edu/doc/screen/)



  
  
