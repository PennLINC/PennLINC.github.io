---
layout: default
title: Haufe Transforms
parent: Common Methods
---

When interpreting the regression weights of machine learning based models trained on multivariate neuroimaging data in the prediction of a variable of interest, if attempting to draw conclusions about the relationship between that variable and specific features, the covariance structure of the features must be taken into consideration. Indeed, an inversion of the linear models are needed to yield a correct interpretion, which is referred to as the Haufe transform.

Functionally, to perform the Haufe transform, we calculate the covariance between each feature and the model-predicted variable of interest (e.g. p-factor), and then normalize by the actual variable of interest. The resulting values are the Haufe transformed regression weights that account for feature covariance.

Example code can be found here: https://github.com/BGDlab/PFNs_ABCD/blob/main/ks_networks_7/Step_4/Weight_haufeAAB_All_cov.py.
