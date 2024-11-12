---
layout: default
title: NeuroMaps
parent: Common Methods
---

# Neuromaps

Neuromaps is a wonderful Python package that is both a data resource and an analytical toolbox.
Here’s an overview of what it can be used for: 

1. **Data resource**: neuromaps includes a host of different cortical surface properties, such as maps of cortical thickness, functional networks, gene expression, myelin content, and many more.
2. You could for instance use these maps to understand how your own dataset relates to known brain features.
3. **Transformations and Resampling**: neuromaps includes tools to bring brain maps into a common space (like the MNI, fsaverage fslr).
4. It also provides functions to align and resample maps across different parcellations and resolutions, whether they are in volume (3D) or surface (cortical surface) form.
5. **Assessing relationships between maps**: It provides metrics for comparing maps, such as spatial correlation, which helps in quantifying the similarity between different brain maps.
6. This includes various implementations of the spin test (see corresponding section for more details on that). 

Here’s a link to neuromaps: [https://netneurolab.github.io/neuromaps/usage.html](https://netneurolab.github.io/neuromaps/usage.html)
