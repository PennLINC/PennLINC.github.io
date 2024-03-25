---
layout: default
title: Database Search
parent: Meta-analysis
nav_order: 2
---

## 2. Literature Search
After pre-registering the study on PROSPERO, begin the literature search. This stage of the process typically takes about 1-2 weeks.

### 2.1. Steps for proper literature search & documentation
First, set up the necessary documents and folders to ensure proper documentation. Hyperlinks contain examples of these items from the structural imaging pain meta-analysis.
* In the Google Drive project folder, create a folder named [Literature Search](https://drive.google.com/drive/folders/1n1YZ9BZtv2tSgcLJ7nxbPDot3edv32qR?usp=sharing).
* Set up a spreadsheet named [DatabaseSearch_[DATEHERE]](https://drive.google.com/open?id=1dZvsAdXGOQoFJGLC5N_EEsKJIXE4nNBB-dtgCeKqik8) to clearly document steps.
* Create a subfolder named [Database Search (RIS)](https://drive.google.com/open?id=1eRSWhYCCc6huxQre2lvTy99p5rRCmaZG) to save **.ris** files as backup.

Next, begin searching through recommended databases for full scope of the literature. For each database, make sure to do the following:
* Record, in the DatabaseSearch spreadsheet, number of records returned
* Get a **.ris** (or **PubMed XML**)  file from each source (steps outlined for databases below)
* Save the **.ris** files somewhere on your local computer and in the subfolder Database Search (RIS). *You will need this file to upload abstract records into Covidence.*

### 2.2. Recommended literature databases
For each database, you will type in your search strategy but also filter out irrelevant articles as much as possible (see below for what to filter and how to save record files). *If you have 10k+ records returned, you should maybe try a new search strategy.*

#### [PubMed/MEDLINE](https://pubmed.ncbi.nlm.nih.gov)
You can actually use a variant of this search strategy to filter your results:
```
{your search strategy here} AND ("loattrfull text"[sb] AND ("1990/01/01"[PDAT] : "2020/01/24"[PDAT]) AND "humans"[MeSH Terms] AND English[lang])
```

Replace `{your search strategy here}` with your actual search strategy. For example, the pain meta-analysis used the following search strategy:

```
("MRI"[All Fields] OR "magnetic resonance imaging"[All Fields]) AND ("T1"[All Fields] OR "brain mapping"[All Fields] OR "VBM"[All Fields] OR "voxel based morphometry"[All Fields] OR "cortical thickness"[All Fields] OR "cortical volume"[All Fields] OR "cortical surface area"[All Fields] OR "grey matter density"[All Fields] OR "gray matter density"[All Fields]) AND ("neuropathy"[All Fields] OR "pain"[All Fields] OR "hyperalgesia"[All Fields] OR "allodynia"[All Fields] OR "neuropathic"[All Fields]) AND ("brain"[All Fields])
```
This will filter out availability of text, sample subjects to be human, and language of article to be English.

##### Versions of PubMed

Note that there are two versions of PubMed now -- an old one accessible via incognito mode in Chrome or a new version that will replace it in May 2020. Here is how to save in both versions:

###### Old Version
* Click the **Save** button that’s right under the search bar.
* Change Selection to **All results** and Format to **PubMed**.

###### New Version
This is a workaround using [Zotero](https://zotero.org).
* First, click “Send to” and choose “Citation Manager”.
* Next, choose **All Results** and save the file.
* Open Zotero and import the new .nib file.
* Select **A file** when asked **Where do you want to import from?**. Choose the **.nib** file.
* In the next part, choose to **Place imported collections and items into new collection**, and choose **Link to files in original location.**
* The **.nib** file is now in Zotero and you can export it as a .ris file by double clicking on the collection name on the sidebar and “Export Collection…”.



#### [SCOPUS (proxy from UPenn library)](https://www-scopus-com.proxy.library.upenn.edu/)

Once you’re on the page, go to **Advanced** (it’s on the same line as Documents, Authors, Affiliations right above the search bar).
Filter using a variant of this string query:

```
{your search strategy here} AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "ch" ) OR LIMIT-TO ( DOCTYPE , "bk" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) ) AND ( LIMIT-TO ( SRCTYPE , "j" ) )
```

Replace `{your search strategy here}` with your search strategy. Here is an example from pain meta-analysis:

```
( "MRI" OR "magnetic resonance imaging" ) AND ( "VBM" OR "voxel based morphometry" OR "cortical thickness" OR "cortical volume" OR "cortical surface area" OR "grey matter density" OR "gray matter density" ) AND ( "pain" OR "neuropathy" OR "neuropathic" OR "hyperalgesia" OR "allodynia" ) AND "brain" AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) OR LIMIT-TO ( DOCTYPE , "ch" ) OR LIMIT-TO ( DOCTYPE , "bk" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) ) AND ( LIMIT-TO ( SRCTYPE , "j" ) )
```
This filters results to be from a peer-reviewed journal article, language to be English, document type to be either an article or review or chapter (useful in case there are systematic reviews).

##### Exporting from SCOPUS

Saving on this requires multiple steps because you can only export ~2000 records at a time.

1. To make sure you save all records, on the left hand bar, filter Year to the first half of the years of publication you’re searching for (e.g., 1990-2000).
2. Click the checkbox for All Results. Click **Export** and select **RIS Format**.
3. Now, filter for the rest of the years and repeat the steps. In Covidence, you will just upload both **.ris** files.


#### [EMBASE](https://www.embase.com)

Click on **Other institution login** to log in via UPenn.

Filter by using a variant of this search strategy:
```
{your search strategy here} AND [1990-2020]/py AND [embase]/lim AND ('article'/it OR 'article in press'/it OR 'chapter'/it OR 'editorial'/it OR 'letter'/it OR 'note'/it OR 'review'/it OR 'short survey'/it) AND [embase]/lim AND [english]/lim
```

This is the version used in pain:

```
('mri'/exp OR 'mri' OR 'magnetic resonance imaging'/exp OR 'magnetic resonance imaging') AND ('vbm' OR 'voxel based morphometry'/exp OR 'voxel based morphometry' OR 'cortical thickness'/exp OR 'cortical thickness' OR 'cortical volume'/exp OR 'cortical volume' OR 'cortical surface area'/exp OR 'cortical surface area' OR 'grey matter density' OR 'gray matter density'/exp OR 'gray matter density') AND ('pain'/exp OR 'pain' OR 'neuropathy'/exp OR 'neuropathy' OR 'neuropathic' OR 'hyperalgesia'/exp OR 'hyperalgesia' OR 'allodynia'/exp OR 'allodynia') AND ('brain'/exp OR 'brain') AND [1990-2020]/py AND [embase]/lim AND ('article'/it OR 'article in press'/it OR 'chapter'/it OR 'editorial'/it OR 'letter'/it OR 'note'/it OR 'review'/it OR 'short survey'/it) AND [embase]/lim AND [english]/lim
```
This will make sure you’re only searching for the years 1990 onwards, within the EMBASE database, and with articles that are only published.

##### Exporting from EMBASE

To export your results, do the following steps.

1. Click the checkbox next to **Results** and then click **Export**.
2. Select **RIS format (Mendeley, EndNote)** as your preferred format. If you have over 2000 results, you can apply a similar filtering strategy as SCOPUS and export articles every few years.


#### [Web of Science](https://www.webofknowledge.com)

Once you're on the website, do the following:
1. Type in the search strategy in the basic search bar.
2. Enter the year range to the bottom of the search bar.
3. You can further filter the studies based on language, document type and other restrictions using a bar to the right of the search results.
4. To export, select **Export** and then other file formats at the top of the page. You can download 500 per file and can easily adjust 1-500, then 501-1001, and so on.

#### [Cochrane](https://www.cochranelibrary.com)

To search through Cochrane, do the following steps:
1. Type in your search strategy in the search bar on the top right corner.
2. Click on the checkbox next to **Select all** in the search results and then **Export selected citation(s)**.
3. Choose **RIS (EndNote)** as your preferred format.
4. Click on the checkbox next to **Include abstract** and download.

#### [PsycINFO](https://www.proquest.com/products-services/psycinfo-set-c.html)

1. Log in through UPenn libraries and enter your search strategy.
2. Scroll down to change your view to 100 entries per page.
3. Go back to the top and click on the checkbox next to **Select 1-100** and then click on the **…** circle. Select **RIS** as your preferred format. Click **continue** and then you will have downloaded the first 100 abstracts. Go to the next page and repeat.

### 2.3. Upload onto Covidence
After you’re done with these steps, upload each **.ris** or **PubMed XML** file onto Covidence. Once you’re done, you can begin screening abstract records in Covidence.
