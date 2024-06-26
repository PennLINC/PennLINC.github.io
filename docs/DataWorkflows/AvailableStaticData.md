---
layout: default
title: Available Static Datasets
parent: Data Workflows
nav_order: 4
has_toc: false
---

# Available Static datasets
{: .no_toc }

## Available studies
1. [HCPD](https://www.humanconnectome.org/study/hcp-lifespan-development/data-releases) - The Human Connectome Project Developmental Sample; ages roughly 5-21 and N=~600. 
2. [PNC](https://www.med.upenn.edu/bbl/philadelphianeurodevelopmentalcohort.html) - The Philadelphia Neurodevelopmental cohort; ages roughly 8-23 and N=~1600. Also note that sometimes, PNC IDs will be labelled differently (as RBC IDs). The mapping between the two can be found here: `/cbica/projects/RBC/Curation/RBC_demo_pheno/data/bblid_renamed.csv`. 
3. [CCNP](https://www.sciencedirect.com/science/article/pii/S1878929321001109) - The Chinese Colornest Project (developmental); ages 6-18 and N=~200.
4. [HBN](https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/About.html)- The Healthy Brain Network; ages 5-21 and N~=2500.
5. [PACCT/ECAS](https://danlab.psychology.columbia.edu/research/studies) - Parents and Children Coming Together/Early Caregiving Adversities; ages 5-12 and N~=350
6. [NKI](https://www.nki.rfmh.org/study/rockland-sample/) - Nathan Kline Institute Rockland sample; ages 6-85 and N~=1300
7. [BHRC](https://osf.io/ktz5h/) - Brazilian High Risk Cohort; ages 5-14 and N~=600


## Available modalities

There are multiple different types of processed output available here, for the fMRI and DWI modalities. At the moment, no ASLPrep or perfusion data is available via PMACS. 

### BIDS
1. BIDS - These are curated in [BIDS](https://bids.neuroimaging.io/) format, but unprocessed. Typically these are put through the processing pipelines mentioned below before they can be used for any analyses.

### fMRI 
2. [fMRIPrep](https://fmriprep.org/en/stable/) - This data is preprocesed, but our lab typically does not use fMRIPrep derivatives directly, and runs them through XCP first. 
3. [XCP-D](https://xcp-d.readthedocs.io/en/latest/index.html) - These derivatives are commonly used for papers - particularly the ALFF, parcellated timeseries, and functional connectivity matrices. The in-lab developer is Taylor Salo. 

### DWI data
2. [QSIPrep](https://qsiprep.readthedocs.io/en/latest/) - This data is preprocesed, and typically the `preproc-dwi` files are used in further analyses/ put through QSIRecon workflows. The in-lab developer is Matt Cieslak. 
3. QSIRecon workflows - there are multiple different modes here, including `msmt`, `autotrack`,`gqi`,`sift`, `scalarfest` and `hsvs`. More information about the outputs of these can be found [here](https://qsiprep.readthedocs.io/en/latest/reconstruction.html). 



*Note that, when available, the QC files are also generated - EITHER in the parent bootstrap OR in a separate bootstrap - you will need to check the list below carefully.
In case these files are not generated, users will have to concatenate the individual subject files across the subjects themselves in order to generate a dataset-wide QC file.*

> Warning
>
> It is generally recommended to use the latest available version of each processed dataset.

Below, you can find a list of studies, modalities, and their clone IDs: 

| Study | Content                           | Clone URL                       | Format | Dataset ID                           |
| ----- | --------------------------------- | ------------------------------- | ------ | ------------------------------------ |
| PNC   | BIDS                              | LINC_PNC#~BIDS                  | Files  | f2cb6108-521b-4653-b492-003321e5f5e3 |
| PNC   | fMRIPrep v20.2.3                  | LINC_PNC#~FMRIPREP_zipped       | Zips   | 0e69e695-5219-4e32-9987-f4d795445c33 |
| PNC (select subjects)   | fMRIPrep v20.2.3                  | LINC_PNC#~FMRIPREP_ANAT_zipped  | Zips   | f9ef59de-be16-4987-a930-49f15bdee0b4 |
| PNC   | QSRecon - GQI+hsvs v0.16.0RC3     | LINC_PNC#~GQIHSVS               | Files  | f20c2eb1-c839-4404-8dad-63f0a20a4fff |
| PNC   | QSIRecon msmt sifthsvs v0.16.0RC3 | LINC_PNC#~SIFTHSVS              | Zips   | 2642a99d-de75-437a-b63f-7da4ed36f330 |
| PNC   | QSIPrep v0.14.2                   | LINC_PNC#~QSIPREP               | Zips   | 6af87a20-bfe5-458b-8773-cfe51e6200c6 |
| PNC   | XCP v0.3.2                        | LINC_PNC#~XCP_unzipped          | Files  | 4669d449-89fd-48ca-94a3-d8326f8ac98b |
| PNC   | XCP v0.3.2                        | LINC_PNC#~XCP_zipped            | Zips   | e75816f8-bc8f-479f-90db-a86dc35f4676 |
| PNC   | XCP v0.3.2                        | LINC_PNC#~XCP_QC                | Files  | 8ae2a9ed-e3ab-45d3-9072-e87f43511d0a |
| PNC   | XCP v0.6.rc6                      | LINC_PNC#~XCP_zipped_latest     | Zips   | b33b4478-a83e-4920-9015-b6b45d7e1411 |
| PNC   | XCP v0.6.rc6                      | LINC_PNC#~XCP_zipped_latest_cifti  | Zips   | d147a409-171d-489d-8fe8-8d5251c596e2 |
| PNC   | fstabulate                        | LINC_PNC#~fstabulate            | Files  | da925640-e6e2-4c4b-ba6a-60af03fb9014 |
| CCNP  | BIDS                              | LINC_CCNP#~BIDS                 | Files  | 30c9ce5c-b43e-45d5-8a82-4fb7561b51a6 |
| CCNP  | fMRIPrep v20.2.3                  | LINC_CCNP#~FMRIPREP_zipped      | Zips   | eee0d711-f800-4725-8097-4c7b79c7d87f |
| CCNP  | XCP v0.0.8                        | LINC_CCNP#~XCP_unzipped         | Files  | b464c213-ca15-4628-907e-f8c31a3d695e |
| CCNP  | XCP v0.0.8                        | LINC_CCNP#~XCP_zipped           | Zips   | 0b9140e7-cbeb-463b-88a9-7cddf3a22dfb |
| CCNP | XCP v0.0.8                         | LINC_CCNP#~XCP_QC               | Files  | 5bc52558-f00c-4855-b28e-a1eaff8474eb |
| HBN   | BIDS                              | LINC_HBN#~BIDS                  | Files  | f78d4b0a-50ba-4a59-9b84-4f90962eaba2 |
| HBN   | QSIRecon - SiftHSVS v0.16.0RC3    | LINC_HBN#~SIFTHSVS              | Zips+QC| d11e4667-98ad-4164-9f98-8f73a7be24cc |
| HBN   | fMRIPrep 20.2.3                   | LINC_HBN#~FMRIPREP-ANAT_zipped  | Zips   | c70d3696-54cf-425c-88c4-34abca40fc88 |
| HBN   | fMRIPrep v22.0.2                  | LINC_HBN#~FMRIPREP-FUNC_zipped  | Zips   | 6fc7c93a-9d31-4296-9c39-66f2ee6e12da |
| HBN   | fstabulate                        | LINC_HBN#~fstabulate            | Files  | d9b36d5e-5da1-422b-a747-72ad2b58495e |
| HBN   | QSIRecon - GQI+hsvs v0.16.0RC3    | LINC_HBN#~GQIHSVS               | Files+QC | 1da37bc2-7f6d-40c0-80d8-b07cbcdc7f15 |
| HBN   | QSIPrep 0.14.2                    | LINC_HBN#~QSIPREP               | Zips+QC| 4f42ad2d-4a25-470c-b8ca-c6ce71faf080 |
| HBN   | XCP v0.3.2                        | LINC_HBN#~XCP_zipped            | Zips   | 83e5caef-474d-43cf-a3ba-c01cf3e99d5f |
| HBN   | XCP v0.3.2                        | LINC_HBN#~XCP_QC                | Files  | 72669171-26b8-4f27-b6e6-db4ea33761d4 |
| HBN   | QSIRecon - dMRI Scalarfast        | LINC_HBN#~QSIRECON_SCALARFEST   | Zips   | Not yet transfered                   |
| PACCT | BIDS                              | LINC_PACCT#~BIDS                | Files  | dfb00c6e-8790-4308-8f6d-8835b9071575 |
| PACCT | fMRIPrep v20.2.3                  | LINC_PACCT#~FMRIPREP_zipped     | Zips   | 3564e335-4ab2-4873-bf87-1319edc45d82 |
| PACCT | XCP v0.0.8                        | LINC_PACCT#~XCP_unzipped        | Files  | c70a1420-3c64-4585-8d42-bf972576e5cc |
| PACCT | XCP v0.0.8                        | LINC_PACCT#~XCP_zipped          | Zips   | cfb0ef23-75d3-4f45-bd5f-307806e55b37 |
| PACCT | XCP v0.0.8                        | LINC_PACCT#~XCP_QC              | Files  | c7fa68cf-6dd5-4ed2-a0b3-f7d42abc11fb |
| NKI   | BIDS                              | LINC_NKI#~BIDS                  | Files  | abffebbd-c098-4d36-85da-b751dded7d07 |
| NKI   | fMRIPrep v20.2.3                  | LINC_NKI#~FMRIPREP_zipped       | Zips   | 3bfaa182-69ed-41ff-a29d-f5f4818fdfb6 |
| NKI   | XCP v0.0.8                        | LINC_NKI#~XCP_unzipped          | Files  | c15663d5-f5b0-4ff4-a2e3-6501917a8ac4 |
| NKI   | XCP v0.0.8                        | LINC_NKI#~XCP_zipped            | Zips   | 93da30fa-62b6-4434-80d3-bdc628a857cb |
| NKI   | XCP v0.0.8                        | LINC_NKI#~XCP_QC                | Files  | cf276b34-ae80-4826-b3f7-778df8097912 |
| HRC   | BIDS                              | LINC_HRC#~BIDS                  | Files  | 92a30924-4e29-48c6-a8f5-bbbe98c35297 |
| HRC   | fMRIPrep v20.2.3                  | LINC_HRC#~FMRIPREP_zipped       | Zips   | f0f2c3c1-0701-4a10-8975-7f70778adf5d |
| HRC   | XCP v0.0.8                        | LINC_HRC#~XCP_zipped            | Files  | a330511a-f40b-4206-8f9d-a72f18571746 |
| HRC   | XCP v0.0.8                        | LINC_HRC#~XCP_QC                | Files  | b497f7d6-1a80-43f1-a27b-2407f23577d8 |
| HCPD  | BIDS                              | LINC_HCPD#~BIDS                 | Files  | participant level subdatasets        |
| HCPD  | fMRIPrep v20.2.3                  | LINC_HCPD#~FMRIPREP-ANAT_zipped | Zips   | 4bae19b9-865b-4336-8452-6ea76ef0e720 |
| HCPD  | fMRIPrep v22.0.0                  | LINC_HCPD#~FMRIPREP-FUNC_zipped | Zips   | 580b2ea3-258f-4c28-a400-c053820453d7 |
| HCPD  | XCP v0.3.0                        | LINC_HCPD#~XCP_zipped           | Zips   | a7c428ec-b19a-44ef-9312-77e89bb19b0c | 
| HCPD  | XCP v0.3.0                        | LINC_HCPD#~XCP_QC               | Files  | 29dc283f-1075-4b7f-8ec1-0267ea729651 |
| HCPD   | XCP v0.6.rc6                      | LINC_HCPD#~XCP_zipped_latest   | Zips   | 9d62730e-46db-456c-a4e2-521e8a637f2b |
| HCPD  | QSIPrep v0.16.1                   | LINC_HCPD#~QSIPREP              | Zips   | 1dd9ad0a-e0df-4aa0-9ef5-657381292560 |
| HCPD  | QSIRecon - GQI+hsvs v0.16.0RC3    | LINC_HCPD#~GQIHSVS_unzipped     | Files  | c5e26695-e519-48bd-83ec-98568d541a09 |
| HCPD  | QSIRecon - sift+hsvs v0.16.0RC3   | LINC_HCPD#~SIFTHSVS_zipped      | Zips   | 83ae6014-561c-4767-a571-21348011888c |
| HCPD  | QSIRecon - autotrack v0.18.0      | LINC_HCPD#~AUTOTRACK_zipped     | Zips   | 3de13c00-7ea0-462e-8387-60444d7880e3 |
| HCPD  | fstabulate                        | LINC_HCPD#~fstabulate           | Files  | c70a6b74-7c11-4c85-9451-d6751836adea |
