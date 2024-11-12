---
layout: default
title: Personalized Functional Networks (PFNs)
parent: Common Methods
---

# Personalized Functional Networks (PFNs)

Personalized Functional Networks, or PFNs, capture inter-individual variability in the spatial layout of functional brain networks, derived from fMRI data.
Although there are multiple ways of deriving PFNs (these methods are usually referred to as precision brain mapping, or PFM), in our lab, we use a machine-learning based method called spatially regularized non-negative matrix factorization (NMF), which defines networks based on individual BOLD timeseries data while preserving interpretability by using a group consensus as a prior.

This results in a PFN loading matrix for each participant, composed of k network columns and s cortical vertex rows, in which the loading value quantifies the extent to which each vertex belongs to each network—a probabilistic network definition.

To derive PFNs, our lab uses a toolbox named pNET, developed by our collaborators at CBICA, which can take fMRI inputs and outputs PFNs, as well as QC reports and network visualizations: https://github.com/MLDataAnalytics/pNet.
