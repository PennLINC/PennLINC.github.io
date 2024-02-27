---
layout: default
title: Best practices for coding for scientific computing
parent: Lab Basics
nav_order: 3
has_toc: true
---

# Best practices for coding for scientific computing at PennLINC

This is a guide for coding for scientific computing at PennLINC. People may have different styles
in coding; however, there are a few guidelines we recommend here in order to enhance code's reproducibility, reusability, to make it less prone to mistakes, etc. In other words, your 
code achieves exactly what you wanted; after several months, when looking at your code, you 
can still quickly get what you coded; you or other lab members can also reuse your code for other projects in the future.

We will describe the guidelines in three stages: 

1. [Before you start coding for a project](#before-you-start-coding-for-a-project)
2. [During coding](#coding-itself)
3. [After you code a bit](#after-you-coded-a-bit)

We end here with some [final words](#final-words).

## Before you start coding for a project

* Create a GitHub repository for your project under the [PennLINC GitHub group](https://github.com/PennLINC). Use Git and GitHub from the beginning of your project, instead of waiting until the end stage of the project. You'll appreciate the version control when you need to look back at changes you made to your code throughout the project's lifespan. If you are worried about making your code fully public at the beginning of the project, that's okay - you can always choose to make the GitHub repository "Private".
* Organization:
  * You might organize your scripts in several different folders (e.g., for different purposes - image processing, hypothesis tests, etc). Add a `README.md` for each folder to describe the folder's purpose and what's included.
  * Do not mix code with your data; instead, make separate folders for code and data.
  * Avoid using GitHub to track image data or any data with large file size, or any data you will frequently change. Use `DataLad` to track your data.
  * Keep raw data in a separate folder. Save data derivatives in another folder.
* Tools: VS Code provides a great UI for coding (e.g., Python, bash), and it is also very helpful for git version control; R Studio provides a great UI for coding in R. Tips: use the "outline" in those tools to jump across sections in scripts.


## Coding itself

### Just before coding
Think about the purpose of the code you want to achieve.
What language will be efficient to achieve your goal here?
You can have more than one language of code in one project!
Python is good for image processing, data wrangling, and figure generation; R is good for data wrangling, statistical analysis, and figure generation; bash scripts are best for submitting jobs on clusters.

If the code involves a few steps, you might get lost when coding/focusing on one step. Consider writing down the list of the steps as comments before you start coding it.

### Reduce duplicated code
If you have duplicated code, it might be a good time to translate them into a function, so that in the future, you only need to edit the function once. Otherwise, if you want to edit one of the versions, you will also have to update the other one. In other words, it's easier for version control.

### Reduce duplicated list or table as input
Sometimes you hope to define a list of brain regions in your analysis, and you'll use it repeatedly in other scripts too. Define this list in a text file and save it in the Git repository if the file size is not big. For table (e.g., full names, abbreviations, color schemes, etc of brain regions), you can define it in a CSV file, and also save it in the Git repository if that's not big. When you want to use this, just `source` the text file or directly load the CSV file.


### Data wrangling
The data analysis part after (pre)processing often involve data wrangling.
We **strongly** recommend using R to handle the data wrangling part.
[Tidy data](https://r4ds.had.co.nz/tidy-data.html) is often very helpful here.
It is important to note that, although some columns seem redundant in the tidy data, 
it is very important to include them so that future data wrangling will be easy, 
and it'll be easy for sanity checks too 
(i.e., you'll know the exact information of the observation, 
e.g., from which subject, which session, which method, etc).

### Reduce manual work and additional brain work!!!
This is very important.
Manual work (e.g., manually counting or changing numbers) increases risk of mistakes and reduces the confidence of what you reported in the manuscript.
In addition, it will also increase the burden for the reproducibility buddy - they need to more carefully check it to make sure what you reported are consistent with the original output, especially if they are in a different format.

* Generate final tables and figures **directly** from the code as much as possible.
* Avoid additional manual work (e.g., round up, copy-paste, combination of figure panels) to generate the final table or figure you'll use in the paper. Instead:
  * Consider using R to export pdf versions of tables.
  * Consider writing code to directly generate the figure you want, instead of manually adjusting the fonts in Illustrator or Powerpoint later.
  * Consider writing code to directly combine figure panels and save the figure (rather than use Illustrator to do so).
  * Consider directly generating the final format of the values, e.g., let the code round up statistics; if you will report R-squared, let the code calculate the squared number for you; let the code count for you, instead of doing it by yourself.

## After you coded a bit

### Test out!

#### Use toy data to test your code
It's important to test out if your code really works as you thought.
Make some simple toy data, apply your code, and see if you can get what you want.

#### Include sanity checks
Are the shape (number of rows and columns) of the data frame you generated is consistent with expectations?
Use `testthat` from R (e.g., `expect_that()`), and `assert` from Python to assert that what you actually get is the same as what you expect.
Sanity checks are very helpful to rule out mistakes.

#### "Make incremental changes and test as you go."
This section is copied from [an OHBM blog](https://www.ohbmtrainees.com/blog-overview/2023/2/10/coding-best-practices-for-academia-bridging-the-gap-between-research-and-industry):

> "Instead of writing your entire code at once, make small changes and test each step as you go. This approach will make debugging much easier. This is especially important if you are using version control software, such as Git, where each incremental change should be its own commit."


### Document your code and make it readable
Sometimes we're too focused on writing runnable code and we forget to write notes for explanation.
You'll quickly forget the definition of arguments and the purpose of a function.
Document your code before you move on to another task.
You can also write docs before you write the function and use it to guide your coding.

We strongly recommend doing the following:

1. Add comments throughout the code to make sure readers can understand what's happening.
2. Add docstrings to any functions and scripts you write.
    - Stick with a popular convention for your docstrings. For example, you can use [numpydoc](https://numpydoc.readthedocs.io/en/latest/index.html) for Python code.
    - The docstring should include the following: 
        - the purpose of the script (or function)
        - explanation of arguments: name, data type expected, what it means
        - explanation of outputs: name, data type, what does it mean
3. Use informative variable names.
    - Single-letter variables (e.g., `i`) are generally not helpful for readers. Using interpretable variables will make it easier for readers (and future you) to make sense of the code.

For overview docs of scripts, you might consider including a `README.md` for each folder of your scripts.
This `README.md` should an overview of all your scripts, as well as the order in which those scripts should be run.


## Final words
If you feel like you're doing things in an ineffective way, Google it and see if there are better options. Neurostars + Stack Overflow are good platforms, and please make sure you check the number of votes before adopting it (more votes -> more likely to be trustable). You can also talk to other people in the lab or in the Slack channels (e.g., #informatics) for the issue you have.

