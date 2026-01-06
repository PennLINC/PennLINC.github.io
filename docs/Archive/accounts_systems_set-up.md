---
layout: default
title: Accounts and systems set-up
parent: Onboarding
grand_parent: Lab Basics
nav_order: 4
---

# Accounts and systems set-up

## Accessing different accounts:

UPHS System Accounts Overview:

- PennKey = University accounts
    - Use this for anything Penn related/not through health system
    - Stace should set up your Penn Key account. Once he does, you should get an automated email with a 7-character Penn Key setup code and instructions on how to set up your Penn Key and enroll in two-step verification.
- UPHS = University of Pennsylvania Health Systems, i.e., hospital accounts
    - need to enroll in Duo Two-Factor Authentication as well
    - Stace should email you with your UPHS login information. This should include your Penn ID # and also a temporary password.
    - Reset your password from the temporary password according to the instructions in the email from Stace.
    - Access issues and password reset: Call the IS Service Desk at 215-662-7474
    - Use this for anything Penn Medicine related
    
- PMACS = IT accounts that services both University & UPHS sides
    - PMACS hosts “static” datasets – e.g., curated datasets as well as processed derivatives.
    - Stace will create your PMACS account.
    - Before attempting to log into any system you must complete the following 7 steps:
        
        1. Go to [this link](https://reset.pmacs.upenn.edu)
        
        2. On the right side of the page where it says "Sign In" for your username type in your PennKey username
        
        3. Use temporary password sent in email from Stace.
        
        4. Change/Reset your Password, "Old Password" is the temporary one you logged in with. Please make note of the Password Requirements Policies for new Passwords.
        
        5. To receive Email for when your Password will expire (important!) Click the *Enrollment* Tab.
        
        6. Complete the setup questions. Choose obvious answers that you will remember.
        
        7. You can continue to use this service in the future to Reset your Password if you forget it or to Unlock the account if you type in your password wrong too many times.
        
        If you are having any issues with the reset page, please close out of your browser and hit the refresh page button while on the reset website.
        
- VPN: Many websites as well as CUBIC and PMACS systems can only be accessed when on the PennMedicine network. When working from home, you will need to connect to VPN to access these resources.
When using VPN and / or when on PennMedicine network, some websites cannot be accessed. To enable access, download and install the [following certificates](https://cert-install.uphs.upenn.edu/) using your UPHS credentials (instructions provided with certificate download).
    - Big IP VPN client [Big IP VPN](http://www.uphs.upenn.edu/network/files/BIGIPMacEdgeClient2023.zip) will allow you to connect to all PMACS and UPHS systems. Use your UPHS credentials to connect.
    - Ivanti VPN client will allow you to connect to all PMACS systems. Use your PMACS credentials to connect.

Setting up email account:

- Stace will set up your Penn Medicine email account, with a temporary password. You will need to login and change your password.
- If you require help installing or configuring Outlook, please open a support ticket at [help desk](https://helpdesk.pmacs.upenn.edu/)

## Additional Systems to Set Up:

- [Slack](https://pennlinc.github.io/docs/LabHome/Onboarding/Onboarding/pennbbl.slack.com):
    - Ted can add you onto the slack channel(s) before you start.
    - *If you have a slack account tied to a different email, and want to change it so it is tied to your Penn email when you get it, Andrew can do this, or follow the instructions [here](https://slack.com/help/articles/207262907-Change-your-email-address).
- [Google Calendars](https://calendar.google.com/calendar/r):
    - Slack Ted with your gmail account to have him add you to the google calendar.
    - Ted posts meeting times each week on slack. In order to schedule an individual meeting, you can create an event on the google calendar on one of the times that says ‘open for meetings’.
- [Github](https://github.com/PennLINC/): all code belongs in our github code repository; our [github pages webpage](https://pennlinc.github.io/) associated with this organization also houses growing knowledge base of tutorials.
    - If you do not already have a Github account, follow the instructions to create one [here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
    - Ask Taylor to be added to the PennLINC Github.
    - In order to make a new project repository on Github under PennLINC, when you click ‘Create a new repository,’ under ‘Owner’ select PennLINC. There is also the option to use the PennLINC/paper-template.
- CUBIC:
    - used for large volumes of parallelizable subject-specific processing jobs
    - see [CUBIC](https://www.notion.so/Accounts-Systems-Set-up-13c2e9b4cd1980c794e9fd7eaf002b8d?pvs=21) documentation for specific cubic help
    - create a new project in CUBIC:
        - *Note: If you would be added to a specific project/not creating a new project, no need to fill out the project form, just submit the online ticket and screenshot.
        
        - Access the Project_data_use_template.doc document on CBICA Wiki: Main Page > Research projects > 3 Access/New Project Creation > Project Creation Request
        
        - Fill out the information in the Project_data_use_template.doc & save as a .txt file
        - Send an email to Ted (”Do you approve of this project folder request?”), and screenshot the conversation with data in frame of approval. Save that as an image.
        - Save the screenshot & **text file** of Project_data_use_template.doc
        - Submit ticket:
            - Go [here](https://pennmedaccess.uphs.upenn.edu/my.policy) —> CBICA Request Tracker —> Home —> Create ticket
            - ‘Cluster - New Project’ or ‘Cluster - Project Access’
            - Fill out request with EXACT SAME INFO as just filled in the Project_data_use_template.doc & attaching supporting docs (screenshot).
            - You should receive an email from CBICA confirming request, can return to Request Tracker to see the status of your ticket
