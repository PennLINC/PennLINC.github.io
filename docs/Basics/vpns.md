---
layout: default
title: VPNs
parent: Computation Basics
nav_order: 5
has_toc: true
---

# VPNs

We have two main VPN security measures at PennLINC. One is called Big IP f5 VPN, and is used to connect to any UPHS & Penn Medicine service, including the CUBIC cluster and CBICA wiki. To download this VPN, follow [these instructions](https://www.cbica.upenn.edu/sbia/bergman/Remote_Access.html) and use [this guide](https://www.uphs.upenn.edu/network/docs/Duo_PennVPN.pdf) to connect.

The other is Pulse Secure VPN, which is mainly used for connecting to the PMACS cluster. To download this VPN, follow [this guide](https://www.med.upenn.edu/dart/assets/user-content/documents/manually-install-and-setup-vpn-on-mac.pdf), followed by [this one](https://www.med.upenn.edu/dart/pulse-vpn-duo-instructions.html) for logging in.

To reset your PennMedicine password for the VPN (which expires every half year), simply go to [reset.uphs.upenn.edu](reset.uphs.upenn.edu), enter your username + last four digits of SSN. If this does not work, you may need to call UPHS service desk at 215-662-7474, and they will expire your password so that you can reset it manually. In addition, you may also try using `passwd` on a CUBIC login node to change the password.
