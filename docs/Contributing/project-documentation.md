---
layout: default
title: Project Documentation with GitHub Pages
parent: Documentation
has_children: false
has_toc: true
nav_order: 2
---

# Project Documentation with GitHub Pages

In the event that you've completed and/or published a large project with PennLINC, you may want to write documentation for replication and easy sharing. The recommended way of doing this is to create a website for the Github repository of the project, using Github Pages.

To write documentation for a finished project using GitHub Pages, begin by going to this tutorial [here](https://www.thinkful.com/learn/a-guide-to-using-github-pages/). The steps outlined below will guide you through the same steps as in the link.

Each project page should be organized according to the [Project Template](https://github.com/PennLINC/PennLINC.github.io/blob/master/docs/Contributing/ProjectTemplate.md).


## GitHub Pages tutorial

1. For projects with a repo already, begin tutorial by choosing the option `Already wrote code`.

2. When prompted on what type of pages to create, choose `Project Pages`.

3. When asked if your code is already on GitHub, click `Yes` if it is. This creates a new branch where you can create the GitHub Page; this will be separate from your GitHub repo containing your code.

4. You will now be shown how to create a branch to your existing repository! The steps are essentially the following:
  * On your terminal, `cd` to your repository.
  * Create a branch in your repo for your GitHub Page by typing in `git checkout -b gh-pages` in your terminal.
  * Create a markdown file called **index.md**. This is your documentation, so edit this with documentation on your project. [Here's](https://www.markdownguide.org/basic-syntax/) a great guide for getting started with Markdown if you haven't used it before.
  * Push it to GitHub by using `git push origin gh-pages`

Your page is now set and can be found by typing via the url **pennlinc.github.io/YOUR_PROJECT_NAME_HERE** (replace **YOUR_PROJECT_NAME_HERE** with your GitHub repo name)!

Now, if you want to go back to the branch of your original repository, you can use the command `git checkout master` (and if you ever want to go back to the branch of the GitHub Page, you can use `git checkout gh`). You can always check which branch you're in by using the command `git branch -al`.

## Customizing GitHub Page

If you ever want to see what's going on with your GitHub Pages branch on GitHub, you can simply go to **github.com/PennLINC/YOUR_PROJECT_NAME_HERE/branches** to look at your **master** and **gh-pages** branch.

## Themes

Now, if you want a nice theme, do the following:
1. Go to **Settings** in your GitHub repository.
2. Go all the way down to the section **GitHub Pages**.
3. Click `Change theme` and choose a theme.


### Table of Contents Example

Note that if you'd like to include a table of contents in your project page, doing so is simple!
Just include the lines ```1. TOC
{:toc}``` at the level you'd like your table to be. Every title and subtitle after those lines should be reflected in your table of contents. You can now jump to each section by clicking on it's respective title in the table! 

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


