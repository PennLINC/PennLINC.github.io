---
layout: default
title: Ridge Regression
parent: Common Methods
---

Ridge regression is a linear regression model that is useful when dealing with highly dimensional data which will be prone to overfitting. Ridge regression applies a regularization term that penalizes the coefficient of colinear parameters, shrinking them towards zero. The strength of regularization is based on an alpha term, which can be modified based on how aggressive you want your feature selection and how many parameters you're starting with.

In recent projects, we have used ridge regression to relate the multivariate data of personalized function network topography loadings (59,412 x 17 values) to our variables of interest (cognition, p-factor, polygenic risk, etc.). For example code: https://github.com/PennLINC/keller-networks/tree/main/Step2_RidgeRegression.
