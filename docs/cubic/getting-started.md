---
layout: default
title: Getting + setting up your CUBIC account
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

