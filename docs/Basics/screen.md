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

Have you ever faced the scenario where you are testing a script interactively on the login node of your remote machine, and suddenly the VPN connection drops and your work is lost?

Luckily, there is a Linux utility called `screen` on the `sattertt` login node that allows us to resume sessions that otherwise would be lost. Programs launched in a screen session would continue to run when their window is closed or when the screen session is detached from the terminal.

## What Is `screen`

`screen` is a terminal window manager. When you call the screen command, it creates a separate window where you can work as you would in a normal terminal window. `screen` is already installed in the `sattertt` node. 

## Start a Session
You can type `screen` to start a screen session. 

If you want to specify a meaningful name for the session in place of the default `cubic-sattertt` suffix, you can use the `-S` flag as in `screen -S [session_name]`. Type `man screen` for more information. If you are interested, you can also check out the [official GNU screen documentation](https://www.gnu.org/software/screen/manual/screen.html#Overview) for more customization tips.

Here I am creating a new screen session with the name `example`.
<img width="670" alt="Screen Shot 2022-01-13 at 2 12 16 PM" src="https://user-images.githubusercontent.com/53891017/149397837-80de4b37-d93a-4b61-acec-f542193ff69c.png">


Note that it says `screen 0` on the terminal tab bar after creating the session.
<img width="670" alt="Screen Shot 2022-01-13 at 2 12 23 PM" src="https://user-images.githubusercontent.com/53891017/149397934-31c903b1-51cc-4800-aa76-16a27f2d4583.png">

You can use `screen -ls` to ensure that the screen session has been started.

<img width="670" alt="Screen Shot 2022-01-13 at 2 12 37 PM" src="https://user-images.githubusercontent.com/53891017/149398185-f3fda35a-293e-40e9-ad4b-f8c062096a4a.png">

## Detach a Session

As previously mentioned, programs launched in a screen session would continue to run when their window is closed or when the screen session is detached from the terminal. 

The reason is because `screen` makes it possible for you to leave a terminal window (detach) and return to it later (reattach). This can come in handy when you are `rsync`-ing files between two servers or any other commands that can take an unpredictable amount of time. 

`screen -d` would detach the current screen session.


If you have several screen sessions going on, you can provide the session id of the specific screen session that you'd like to reattach:

`screen -d session_id`

Here I detach the screen session by specifying the session id
<img width="670" alt="Screen Shot 2022-01-13 at 2 13 17 PM" src="https://user-images.githubusercontent.com/53891017/149398279-e295bf4b-4e52-470d-be6e-de0ac6a92cbe.png">


Again, you can use `screen -ls` to ensure that the screen session has been detached.

<img width="670" alt="Screen Shot 2022-01-13 at 2 13 32 PM" src="https://user-images.githubusercontent.com/53891017/149398630-a28a4230-16ed-4a93-86ea-84ecb129689a.png">


_Note: You can send commands to a screen session instead of the shell by pressing `Ctrl-a` (that is pressing the control key and the letter `a` at the same time)._

Now feel free to do other stuff!
## Reattach a Session

How do we return to and check on the programs launched earlier in  a detached screen session? The magic wand we use is reattach the session.
`screen -r` would reattach the detached screen session.

If you have several screen sessions going on, you can provide the session id of the specific screen session that you'd like to reattach:

`screen -r session_id`

Here I detach the screen session by specifying the session name (which is also okay)

<img width="670" alt="Screen Shot 2022-01-13 at 2 15 02 PM" src="https://user-images.githubusercontent.com/53891017/149398725-50067a1e-192d-48f8-92d8-0fa1b9f51b59.png">


Again, you can use `screen -ls` to ensure that the screen session has been reattached.

<img width="670" alt="Screen Shot 2022-01-13 at 2 15 20 PM" src="https://user-images.githubusercontent.com/53891017/149398847-f464964c-b6e0-47bf-8bfa-3b28e5d29462.png">

## Exit a Session


<img width="670" alt="Screen Shot 2022-01-13 at 2 15 48 PM" src="https://user-images.githubusercontent.com/53891017/149398949-681b75c5-76f8-4342-ad1c-6832eb734b40.png">

Type `exit` on the screen terminal window to exit the session completely. You will be returned to your shell and see the `[screen is terminating]` message.
<img width="227" alt="Screen Shot 2022-01-13 at 2 16 32 PM" src="https://user-images.githubusercontent.com/53891017/149398979-c2b24617-871b-4b16-8e78-ded3e0fb3db3.png">


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



  
  
