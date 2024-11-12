---
layout: default
title: Non-negative Matrix Factorization (NMF)
parent: Common Methods
---

# opNMF

In a nutshell, orthogonal projective non-negative matrix factorization (opNMF) is a great tool for discovering hidden patterns in large datasets by dividing them into interpretable, non-overlapping subcomponents.
In neuroimaging, opNMF can for instance be used to identify areas in the brain that show similar structure (i.e., covary together).
It’s a little bit like finding the “building blocks” that make up the (way more more complex) brain data. Unlike principal component analysis (PCA), values can only be positive (whereas PCA can have negative loadings), which makes the components much easier to interpret.

Aristeidis Sotiras has a github repo with Matlab code for running opNMF: [https://github.com/asotiras/brainparts](https://github.com/asotiras/brainparts)

[Sotiras et al., 2015, NeuroImage](https://doi.org/10.1016/j.neuroimage.2014.11.045) provides a great description of how this method can be used in the context of neuroimaging research.
[Sotiras et al., 2017, PNAS](https://doi.org/10.1073/pnas.1620928114), shows an application of NMF that identifies structural (cortical thickness) brain networks.
Here’s another example [paper](https://doi.org/10.1016/j.celrep.2023.113487) by the lab that used opNMF to find data-driven patterns of covarying white matter structure in fixel data.
