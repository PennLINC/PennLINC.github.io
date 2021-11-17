---
layout: default
title: Current Studies
has_children: false
has_toc: false
nav_order: 11
---

# Current Studies in the Lab

Below is a list of the current studies in the lab:

| Study Title |    Lead Name(s)    |               Link                |
| ------------- | --------------- | --------------------------------- |
| Reward    | Tinashe Tapera, Margaret Gardner | [https://pennlinc.github.io/Reward/index](https://pennlinc.github.io/Reward/index){:target="_blank"} |
| GRMPY | Kristin Murtha, Diego Davila | [https://pennlinc.github.io/grmpyproject/](https://pennlinc.github.io/grmpyproject/){:target="_blank"} |
| cros-map | Jacob Vogel | [https://pennlinc.github.io/cros-map/](https://pennlinc.github.io/cros-map/){:target="_blank"} |
| EF | Kristin Murtha, Sophia Linguiti | [https://pennlinc.github.io/executivefunction/](https://pennlinc.github.io/executivefunction/){:target="_blank"} |
| Mobile Phenomics | Kahini Mehta, Kristin Murtha | [https://pennlinc.github.io/mobilephenomics/](https://pennlinc.github.io/mobilephenomics/){:target="_blank"} |

---------------------------------------------------------------------------------

# How to Add Your Study

If you'd like to add your study to this list, read on! Successful/complete documentation of your study requires two things:

1. A Github Pages site, and
2. An entry on this page

## Github Pages Documentation

We use Github Pages to reproducibly document how we arrived at a scientific finding, usually for a paper or poster. A Github Pages site is a static website linked directly to a Github repository -- for example, this website is a Github Pages site for the Github repository [PennLINC/pennlinc.github.io](https://github.com/PennLINC/PennLINC.github.io). The underlying code is markdown and is rendered (converted) automatically into a website by Github. You'll want to create one of these sites for your project and its code repository. To learn how to do this, see [this tutorial](/docs/Contributing/project-documentation/).

## Study Page Entry

Lastly, you'll need to add your study to the list below.
To add a study to this list, please first read the [documentation guide](/docs/Contributing/documentation_guidelines) to familiarize yourself with the process of adding content to this website. When it comes time to add your study, simply add a Pull Request with your entry in the raw text of table:

```
| Study Title   |    Lead Name(s)    |               Link                |
| ------------- | ------------------ | --------------------------------- |
| Study 1       | Joe Bloggs         | [My study 1](mystudy.github.io)   |
| Study 2       | Jane Doe           | [My study 2](study2.github.io)    |
```

Simply add a new line, using the pipes `|` to delineate columns, and a newline to delineate rows — don't forget to use correct markdown formatting for links: `[title](url)`.

For additional information see the [Project Setup Page](/docs/LabHome/ProjectSetup/).

----------------------------------------

