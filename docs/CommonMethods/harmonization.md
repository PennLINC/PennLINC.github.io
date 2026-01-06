---
layout: default
title: Harmonization
parent: Common Methods
---

# Harmonization
While multisite collaboration is essential for modern neuroscience, it introduces substantial site-related variability that can obscure true biological effects, inflate false positives, and reduce reproducibility. Differences in scanner manufacturer, field strength, pulse sequences, hardware upgrades, and preprocessing pipelines can all induce systematic biases in imaging-derived measures that are unrelated to the underlying neurobiology of interest.

Multisite harmonization methods aim to mitigate these unwanted sources of technical variability while **preserving meaningful biological signal** (e.g., age, sex, diagnosis). Although consortia often attempt to control for acquisition protocol differences prospectively, such strategies are frequently insufficient to eliminate all site effects, particularly in large or retrospective studies. Statistical harmonization methods have therefore become a critical component of multisite neuroimaging analysis pipelines.

ComBat [Johnson, Li, and Rabinovic, 2007](10.1093/biostatistics/kxj037), originally developed for genomics and later adapted for neuroimaging, has emerged as a widely used harmonization technique. By estimating and removing systematic site-related differences in the overall level and variability of imaging measurements, ComBat places data from different scanners on a common scale while retaining associations with covariates of interest. This approach has been shown to substantially reduce scanner-related variability across a wide range of neuroimaging modalities.

Importantly, simple approaches such as demeaning or standardizing data within site are not sufficient for harmonization. These methods assume that scanner effects are limited to constant shifts in the mean, and they do not account for differences in measurement variability or interactions between site and biological covariates. As a result, naïve centering approaches can either fail to remove site effects or inadvertently remove meaningful biological signal, leading to biased estimates and reduced reproducibility.

## Advances in Harmonization
### CovBat
Standard ComBat is effective at reducing site-related differences in the overall level and variability of individual imaging measurements. This makes it well suited for many univariate analyses that examine brain regions independently. However, many neuroimaging analyses do not treat regions in isolation. Instead, they rely on patterns across multiple regions, such as multivariate models, machine learning approaches, and network-based analyses.

In these settings, it is important to consider not only the values of individual imaging features, but also how features relate to one another. Brain regions often vary together in systematic ways, reflecting shared development, anatomy, or disease processes. Scanner-related effects can alter these relationships, changing how regions appear to co-vary across subjects even when average values and variances are well matched across sites. When such effects are present, harmonizing only individual features may leave behind site-driven differences that influence downstream analyses.

CovBat extends the ComBat framework by addressing scanner-related differences in the relationships among imaging features, in addition to differences in their individual values [Chen et al., 2022](onlinelibrary.wiley.com/doi/10.1002/hbm.25688). Rather than focusing solely on aligning the mean and variability of each region, CovBat also harmonizes patterns of co-variation across regions, ensuring that multivariate relationships are more comparable across sites.

This extension is particularly important for neuroimaging analyses that depend on distributed patterns of brain measures rather than single regions. Scanner-induced differences in inter-regional relationships can cause subjects to cluster by site in multivariate space, affect the performance and generalizability of machine learning models, and bias network-level measures. By reducing these effects, CovBat helps ensure that multivariate signals reflect biological differences rather than technical artifacts.

CovBat does not assume that all relationships among features should be identical across sites. Instead, it aims to remove systematic scanner-driven distortions while preserving biologically meaningful patterns of co-variation. This leads to more stable statistical interpretations and improved reproducibility in studies that rely on multivariate neuroimaging data.

### Longitudinal ComBat
Longitudinal neuroimaging studies introduce additional challenges because the same individuals are scanned repeatedly over time. In these studies, the primary scientific interest often lies in subtle within-subject changes, such as development, aging, or disease progression. Scanner-related variability can interfere with the accurate estimation of these changes, particularly when scanners differ across sites or change over time.

Applying cross-sectional harmonization methods to longitudinal data without accounting for repeated measurements can distort individual trajectories, potentially removing meaningful biological change or introducing artificial trends. Longitudinal ComBat extends the original ComBat framework by explicitly accounting for the fact that measurements are nested within individuals [Beer et al., 2020](sciencedirect.com/science/article/pii/S1053811920306157?via%3Dihub). This allows scanner-related effects to be reduced while preserving true within-subject patterns over time.

Importantly, this can change statistical interpretations by preventing scanner-related variability from being mistaken for within-subject change, which is critical when estimating developmental trajectories, rates of decline, or treatment effects. By respecting the structure of longitudinal data, Longitudinal ComBat provides harmonization that is better aligned with the goals of developmental and clinical neuroimaging studies. It enables more accurate modeling of change over time and supports reliable inference in multisite longitudinal analyses.

### ComBatLS
Scanner-related effects can interact with biological factors such as age, diagnosis, or disease severity, leading to site effects that differ across subgroups of participants.

ComBat-LS (Location–Scale ComBat) was developed to address this limitation by allowing scanner-related effects to vary as a function of covariates. Rather than applying a single correction per site, ComBat-LS adapts the harmonization to account for how scanner effects may change across the range of biological variables in the data. This is particularly important in heterogeneous datasets, where the distribution of covariates differs across sites.

For example, if one site primarily scans younger participants and another scans older participants, scanner effects may become entangled with age-related differences. Standard harmonization approaches may either under-correct site effects or inadvertently remove true biological signal. ComBat-LS helps disentangle these effects by modeling scanner-related differences in a way that respects covariate-dependent variation.

**If you care about centiles of data besides the median, use ComBatLS**. E.g., if you want to plot or analyze the 25th and 75th percentiles of the data, the preservation of location and scale is important.

> [!CAUTION]
> Unfortunately, a Longitudinal CovBatLS GAM/GAMM implementation is not feasible at this time, so pick the appropriate method based on your needs and data type.

## Example with ComBat Family
To run ComBat family while taking advantage of all the advances of CovBat and Longitudinal ComBat, we can use the [`ComBatFamily` R package](https://github.com/andy1764/ComBatFamily).

The following examples presume the following variables are available (which you can adapt for your purposes):
`X_complete`: R dataframe, with dimensions num sessions X num features to harmonize.
`bat_complete`: Vector, Num sessions x 1, site labels. *Ensure that the order of sites is the same as the order of rows in X_complete*.
`cov_complete`: R dataframe, with dimensions num sessions X num covariates (age, sex, and subject ID if using longitudinal harmonization). The column names should be consistent with what is used in the formulas below.

In all of these cases, the harmonized data frame can be accessed by `fit$dat.combat`.

### Simple ComBat
This simple ComBat approach is okay when you have one/few features (cannot use CovBat), not longitudinal data (cannot use Longitudinal ComBat), and a small age range (no need for GAMs/GAMMs)

```{R}
lm_formula <- as.formula(
"y ~ age + sex" # Linear age and fixed effects for sex
)

fit <- comfam(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates
  model   = "lm",
  formula = lm_formula
)
```

### Longitudinal ComBat

```{R}
lm_formula <- as.formula(
"y ~ age + sex + (1 + age | subject_id)" # Linear age and fixed effects for sex, with random effects for intercept and slope
)

fit <- comfam(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates (age, sex, subject_id)
  model   = "lmer",
  formula = lm_formula
)
```

### ComBat GAM
This is suitable when you have a wide age range and expect nonlinear effects, but do not have longitudinal data.

```{R}
gam_formula <- as.formula(
"y ~ s(age, k=4) + sex" # Smooth age with 4 knots, fixed effects for sex
)

fit <- combat_gam(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates (age, sex)
  formula = gam_formula
)
```

### Longitudinal ComBat GAMM

```{R}
gamm_formula <- as.formula(
"y ~ s(age, k=4) + sex" # Same formula as ComBat GAM, the longitudinal-ness comes from the random effects
)

fit <- comfam(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates (age, sex, subject_id)
  model   = "gamm4",
  formula = gamm_formula,
  random  = ~(1 + age | subject_id) # random effects for intercept and slope
)
```

### ComBat-LS
This in theory works with GAMM to, but in implementation has not been working. It also works with linear models.

```{R}
gam_formula <- as.formula(
"y ~ s(age, k=4) + sex" # Same formula as ComBat GAM, also works with linear models
)

fit <- combatls(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates (age, sex, subject_id)
  formula = gam_formula,
  sigma.formula = ~ age + sex,
  control = gamlss.control(trace = FALSE)
)
```

### CovBat Linear

```{R}
lm_formula <- as.formula(
"y ~ age + sex"
)

fit <- covfam(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates (age, sex)
  model   = lm,
  formula = lm_formula
)
```

### CovBat GAM

```{R}
gam_formula <- as.formula(
"y ~ s(age, k=4) + sex"
)

fit <- covfam(
  data    = X_complete, # Num sessions X num features
  bat     = bat_complete, # Num sessions x 1, site labels
  covar   = cov_complete, # Num sessions x num covariates(age, sex)
  model   = gam,
  formula = gam_formula
)
```

### Train Test splitting
If you are performing a training/testing procedure, you should learn the harmonization parameters only from the training set.
```{R}
fit <- covfam(
  data    = X_in_sample, # Num sessions X num features
  bat     = bat_in_sample, # Num sessions x 1, site labels
  covar   = cov_in_sample, # Num sessions x num covariates (age, sex)
  model   = gam,
  formula = gam_formula
)
```

To apply the harmonization parameters to the test set, we can do the following:
```{R}
out_of_sample_prediction <- predict(
  fit, # or whatever you called your ComBat family model
  newdata  = X_out_of_sample, 
  newbat   = bat_out_of_sample,
  newcovar = cov_out_of_sample
)
```

### Choosing a Harmonization Method

- **ComBat**: Simple univariate analyses; legacy workflows; only have one (or few) feature(s). Linear or GAM.
- **CovBat**: Multivariate analyses, preserve covariance of features, does not work with longitudinal data right now. Linear or GAM.
- **Longitudinal ComBat**: Repeated-measures. Linear, GAM, and GAMM.
- **ComBat-LS**: Heterogeneous datasets with covariate imbalance or interest in distributional effects. Linear and GAM.

## Tips

- When feasible, model as many features as you can, as appropriate. For example, if you have one diffusion metric summarized in several bundles, try to harmonize all bundles at once for each feature. This allows you to take advantage of the empirical Bayes correction.
- By default, ComBat-based methods estimate scanner effects relative to a pooled reference across all sites, which is appropriate for most analyses. However, in some situations it may be useful to specify a reference site explicitly. This is most appropriate when one site is known to be of particularly high quality, has the largest sample size, or closely matches the acquisition protocol of an external dataset to which results will be compared. In such cases, specifying a reference site anchors the harmonized data to a concrete and interpretable scale. Caution is warranted when choosing a reference site, as doing so implicitly treats that site as the standard. If the reference site is atypical or has a narrow range of covariates, this can introduce bias or distort biological effects. As a general rule, a reference site should be well-sampled, representative of the target population, and stable across time.
- For ABCD, we have used site 16 as the reference site, as it is the largest site and uses a Siemens (high quality) scanner.