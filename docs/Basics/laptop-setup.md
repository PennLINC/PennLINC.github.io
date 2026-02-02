---
layout: default
title: Setting up your lab computer
parent: Computation Basics
nav_order: 1
has_toc: true
---

# Setting up your lab computer

This page outlines how to set up your lab computer for day-to-day science.

## Software

Almost everyone in the lab will be using a Mac for lab-related work.
The laptop should be configured by UPenn IT (PMACS, then Andrew Zitelli) to have the basic
software installed and configured.
This should include, at a minimum, the VPN client needed to access CUBIC.

Most lab members will also install additional software on this machine,
so that they can use it for their own projects.

Common tasks that we do entirely on our laptops (rather than using the laptop to interace with CUBIC) include:

- Creating figures for papers, presentations, etc.
- Interacting with imaging data, such as by loading it into a viewer like FSLEyes or ITKSnap.
- Running analyses on tabular/summary data generated on CUBIC,
  such as by using R or Python.
- Writing up a manuscript, or other documents.
- Interacting with the lab on Slack, Zoom, Notion, etc.
- Email, calendar, other admin tasks.

### Installing software

1. Install Homebrew (https://docs.brew.sh/Installation) so you can use it to install other packages.
2. Save the following to a file (`brewfile.rb`):
    ```ruby
    tap "homebrew/cask"
    tap "homebrew/cask-versions"    # only if you need alt versions

    cask "cursor"  # Cursor code editor
    cask "github"  # GitHub Desktop
    cask "slack"  # Slack messaging app
    cask "zotero"  # Zotero reference manager
    cask "inkscape"  # Inkscape vector graphics editor
    cask "docker"  # Docker Desktop
    cask "rstudio"  # RStudio integrated development environment
    cask "itk-snap"  # ITK-SNAP image segmentation tool
    cask "xquartz"  # XQuartz X11 server

    brew "r"   # base R (not a cask)
    ```
3. Install the software using Homebrew:
   ```bash
   brew bundle install --file=brewfile.rb
   ```
4. Install Connectome Workbench (https://humanconnectome.org/software/get-connectome-workbench) for working with CIFTI data.
5. Install MiniForge/Mamba (https://conda-forge.org/download/) for managing Python environments.
6. Install fsleyes with mamba (`mamba install fsleyes`) for visualizing MRI data.
7. Install MRtrix3 (https://www.mrtrix.org/download/) for working with diffusion MRI data.

Once all of these applications have been installed, you should be able to open them and use them.
Your Mac will almost certainly tell you that the applications cannot be opened, so we suggest opening your
Settings->Privacy & Security and explicitly allowing the applications to be opened.

When you open RStudio, you will likely see a popup about RStudio requiring Rosetta.
Click the button to install Rosetta.
