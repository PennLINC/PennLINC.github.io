---
layout: default
title: Project Documentation
parent: Project Workflow
has_children: false
has_toc: true
nav_order: 4
---

# Project Documentation with GitHub Pages

Part of the project lifespan for any large project (e.g., something that results in a paper) with PennLINC is creating documentation.
We recommend creating a website associated with your project's GitHub repository, using GitHub Pages.

The [`PennLINC/paper-template`](https://github.com/PennLINC/paper-template) repository can be used as a template for your project's GitHub repository.

The branch that controls the repository's documentation is `gh-pages`. 

At minimum, you should update the files `index.md` and `_config.yml`,
filling in everything with details from your project.
You can add more pages, subfolders, etc. if you'd like to customize the documentation more.
Some recent `gh-pages` you can peruse as examples:
- [https://pennlinc.github.io/luo_wm_dev](https://pennlinc.github.io/luo_wm_dev)
- [https://pennlinc.github.io/thalamocortical_development/](https://pennlinc.github.io/thalamocortical_development/)
- [https://pennlinc.github.io/network_replication/](https://pennlinc.github.io/network_replication/)
- [https://pennlinc.github.io/spatiotemp_dev_plasticity/](https://pennlinc.github.io/spatiotemp_dev_plasticity/)

For the GitHub Page to build properly, you need to first make sure that your repo is public. Second, go to your project repo's "Settings" page and navigate to the "Pages" subsection (under Code and Automation). Make sure that under "Build and deployment" you have selected "Deploy from a branch". Under branch, select "gh-pages". Once you have made these changes to your repo, modified these files, and pushed your repository's `gh-pages` branch,
your project's documentation should build on GitHub Pages and should be available at **https://pennlinc.github.io/YOUR_PROJECT_NAME**
(replace **YOUR_PROJECT_NAME_HERE** with your GitHub repo name)!

{: .note-title }
> Important
>
> Just remember not to mix up your `main` and `gh-pages` branches!
> You don't want to add code to `gh-pages` or unnecessary documentation to `main`.

## Customizing GitHub Pages

If you ever want to see what's going on with your GitHub Pages branch on GitHub,
you can simply go to **https://github.com/PennLINC/YOUR_PROJECT_NAME_HERE/branches** to look at your `main` and `gh-pages` branch.

## Themes

Now, if you want a nice theme, do the following:

1. Go to **Settings** in your GitHub repository.
2. Go all the way down to the section **GitHub Pages**.
3. Click `Change theme` and choose a theme.


### Table of Contents Example

Note that if you'd like to include a table of contents in your project page, doing so is simple!
Just include the lines ```1. TOC
{:toc}``` at the level you'd like your table to be.
Every title and subtitle after those lines should be reflected in your table of contents.
You can now jump to each section by clicking on it's respective title in the table!

Here is an example:
1. TOC
{:toc}

### Title 1
Foo
#### Subtitle 1
Foo2
### Title 2
Bar
#### Subtitle 2
Bar2
##### Sub-sub-title 2
Foobar
