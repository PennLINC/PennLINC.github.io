---
layout: default
title: Spin Tests
parent: Common Methods
---

# Spin tests

If there is one statistical method that the lab pretty much always uses at one point or another, it’s `spin tests`!! 

What’s a spin test, you might ask? Briefly, it’s a test that allows to determine whether say two brain maps are significantly associated.
The trick here is that this type of test accounts for the fact that brain regions that are close together tend to share similar brain features (i.e., there is spatial autocorrelation in brain data).
The spin test assesses significance by transforming the brain into a little sphere and rotating one of the two original brain maps a bunch (let’s say, 10,000) times.
You then recompute your test statistic (e.g., a correlation between the two maps), except that this time it’s a correlation between a spun map and the second (unchanged) brain map.
This generates a “null distribution” of your test statistic, which represents results that you could have obtained just due to simple autocorrelation in the brain data.

## Spin tests using Python

Our go-to spin test when working in Python is from `neuromaps` .
[Here](https://netneurolab.github.io/neuromaps/auto_examples/plot_spatial_nulls.html) is a nice walkthrough for it.

This particular example uses the [Alexander-Bloch et al., 2018 *NeuroImage*](https://doi.org/10.1016/j.neuroimage.2018.05.070) implementation of the null model.
There are a number different implementations of spatial autocorrelation-preserving null models.
Broadly, there are two types: generative nulls and randomization nulls.
This paper by [Ross Markello and Bratislav Misic, 2021., *Neuroimage*,](https://doi.org/10.1016/j.neuroimage.2021.118052) is great if you want to learn more about null models and figure out which type of null is most appropriate for your project.

## Spin tests using R

František Váša also has R and a Matlab implementations based on the [Alexander-Bloch et al., 2018 *NeuroImage*](https://doi.org/10.1016/j.neuroimage.2018.05.070) spin-test:

[`frantisekvasa/rotate_parcellation`](https://github.com/frantisekvasa/rotate_parcellation/tree/master)

Briefly, it’s a two step process.
Here’s an example of how Val Sydnor used the R version in her [thalamocortical development project](https://github.com/PennLINC/thalamocortical_development/tree/main): 

**Step 1 - generate null data:**

```r
perms <- rotate.parcellation(coord.l, coord.r, nrot = 10000, method = 'vasa')
```

**Step 2 - do the significance testing:**

```r
perm.sphere.p(x = brainmap_1,y = brainmap_2,perm.id = perms,corr.type='spearman')  
```
