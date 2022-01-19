---
layout: default
title: Fetching Your Data
parent: The Way
nav_order: 1
has_toc: true
---

# Fetching Your Data
{: .no_toc }

There are a number of places you may have to fetch data from to get them onto a cluster filesystem. We will briefly cover best practices for the methods we've used before. Additions will be made as we gain more experience.


## Between Clusters Or Local Disks

The best option for moving a large amount of data between clusters is to use the `scp` command. Remember that this process must remain open and running in your terminal, so it might be useful to do this in a fresh terminal window or use `&` at the end of your command. You could also use [`screen`](https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/) to set up a non-terminating terminal.

As mentioned in our general [PMACS documentation](/docs/pmacs), you should scp *into* a node called `transfer`, for PMACS projects. That would look like this:

```
## my username is <username>
scp -r path/to/your/data <username>@transfer:/path/on/pmacs
```

An alternative to `scp` is `rsync`, but that tends to have [more happening under the hood](https://stackoverflow.com/questions/20244585/how-does-scp-differ-from-rsync).

## Flywheel

On Flywheel, your data may already be in BIDS. In this case we recommend using Flywheel's export function `fw export bids`, or the export function provided by [`fw-heudiconv`](https://fw-heudiconv.readthedocs.io/en/latest/). We built the export function into `fw-heudiconv` because we wanted to have more flexibility in what BIDS data we could grab, including data that's not yet supported in the official BIDS spec. Admittedly though, downloading all of `fw-heudiconv` a lot of overhead for just the export function.

```
# with fw export bids
fw export bids <DESTINATION_DIRECTORY> --project <PROJECT_NAME> --subject <SUBJECT_FILTER>

# with fw-heudiconv
fw-heudiconv-export --project <PROJECT_NAME> --subject <SUBJECTS_FILTER> --session <SESSION_FILTER> --folders <LIST_OF_BIDS_FOLDERS>
```

Try `fw-heudiconv-export -h` for more info.

## Globus

[Globus](https://www.globus.org/) is a research data management platform whose best feature is data transfer and sharing. It's surprisingly easy to use and gets the job done with minimal setup. The data sharing concept revolves around setting virtual *endpoints* that data can be shared to and from. Endpoints can be thought of conceptually as mounts, where you can give outbound network access to a certain directory on your machine or cluster, and by sharing the URL of your endpoint, someone can access your directory through the internet or network cluster.

Currently, the best way to use Globus is either through your local disk or on PMACs (recommended). We're still awaiting CUBIC authorization. The general docs for globus are located [here](https://docs.globus.org/how-to/), but for posterity, here are the best instructions:

On a local disk:

1. Log in to Globus with your UPenn organization account -- [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/) -- and try out the tutorial for sharing between two test endpoints on Globus' system
2. Download and install [Globus Connect Personal](https://www.globus.org/globus-connect-personal); this service will manage the endpoint on your local machine
3. Download and install the [CLI](https://docs.globus.org/cli/) with pip -- remember to use conda environments! This service will allow you to manage the Globus session when it's running
4. [Login with the CLI](https://docs.globus.org/cli/quickstart/) and transfer your data either through the CLI commands or by visiting the file manager (which you saw in step 1). If someone has shared a Globus endpoint with your account, you'll have access to it in "Endpoints".

On PMACs:

0. Make sure you have access to the PULSE Secure VPN -- [remote.pmacs.upenn.edu](remote.pmacs.upenn.edu)

1. Log in to PMACs' dedicated node for Globus functionality:

```
# first ssh into sciget for network access
ssh -y <username>@sciget

# then from sciget, log onto the globus node
ssh -y <username>@sciglobus
```

2. Globus Connect Personal should be available. As above, use it to initialize an endpoint on a directory of your choice on PMACs. Specifically, you should run it as below so that it opens a GUI for logging in with an auto-generated token:

```
# this command will return a URL you can open in any browser and a token you can use to sign in
globusconnect -start &
```

3. Using a new or existing conda environment (see [here](https://pennlinc.github.io/docs/pmacs#logging-in-to-pmacs-lpc) for how to activate conda on PMACs), install the [CLI](https://docs.globus.org/cli/) using `pip` and login with `globus login`.

4. Visit [https://docs.globus.org/how-to/get-started/](https://docs.globus.org/how-to/get-started/) to access the File Manager, as in the Local Disk instructions, to start transferring data.

## Datalad addurls from AWS S3
Now that AWS S3 has become increasingly popular for public data storage, you might want to fetch data from a set of S3 links. `datalad addurls` is a useful command that can retrieve files from web sources and register their location automatically.

For any dataset that comes with a manifest file, the steps are as below:

### Step 0: Data Preparation

Prepare a well-organized CSV or TSV or JSON file from the given manifest file
The file should contain columns that specifies, for each entry, the URL and the relative path of the destination file to which the URL’s content will be downloaded. 
The first few rows of an example file is shown below. For security purposes, the information shown in the shaded block below is not real and is only intended for educational purposes.

```
submission_id,associated_file,filename
sub1,s3://NDAR_BUCKET/SUBMISSION_ID/.../a.json, a.json
sub2,s3://NDAR_BUCKET/SUBMISSION_ID/.../b.json, b.json
sub3,s3://NDAR_BUCKET/SUBMISSION_ID/.../c.nii.gz, c.nii.gz
```
In this case,  `submission_id` column holds the subject ID, `associated_file` column holds the s3 links/URL and `filename` column holds the relative path of the destination file to which the URL’s content will be downloaded. 

  
Next we would need to obtain relevant AWS S3 credentials, which are needed to access S3 Objects. For datasets held in [NDA](https://nda.nih.gov/), the web service provides temporary credentials in three parts:

   + an access key, 
   + a secret key, 
   + and a session token

All three parts are needed in order to authenticate properly with S3 and retrieve data. AWS credentials for [NDA](https://nda.nih.gov/) can be obtained according to the following steps:

Note 1: For security purposes, the AWS access key ID, AWS secret access key and AWS session token referenced below are all FAKE values. Please replace them with your real ID/key.

Note 2: This tutorial is partially adapted from the NDA's tutorial [How to Access S3 Objects](https://github.com/NDAR/ndar_toolkit/blob/master/how_to_access_s3_objets.md).



### Step 1: Download a copy of the NDA download manager 

The command line downdownload manager is written in Java and allows for the automatic download of files. We can use `wget` to retrieve the program from the NIH web server.
  ```
  wget https://ndar.nih.gov/jnlps/download_manager_client/downloadmanager.zip
  ```

### Step 2: Unzip the download manager
 
 Since the downloaded program is a zipped file, we would need to unzip the program to use the download manager. 

  ```
  unzip downloadmanager.zip
  ```

### Step 3: Use the command-line download manager to generate temporary Amazon S3 security credentials
 
 We specify the name of the output file `awskeys.txt` with the `-g` flag.
  ```
  java -jar downloadmanager.jar -g awskeys.txt
  ```

You will be prompted for your ndar username and password, after which you will be able to find your keys in the file `awskeys.txt`
  ```
  cat awskeys.txt
  ```
You will see something like below from your `awskeys.txt` file.
  ```
  accessKey=xxxxx
secretKey=xxxxx
sessionToken=xxxxx
expirationDate=xxxxx
  ```


### Step 4: Export the AWS S3 credentials to your working directory


For instance, navigate to `~/.aws/credentials` and paste in the `awskeys.txt` according to the format below:


```
[NDAR]
aws_access_key_id = xxxxx[copy and paste the value of accessKey in `awskeys.txt`]
aws_secret_access_key = xxxxx[copy and paste the value of secretKey in `awskeys.txt`]
aws_session_token = xxxxx[copy and paste the value of sessionToken in `awskeys.txt`]
```


### Step 5: Check whether you have the datalad special remote enabled

```

git annex info | grep datalad
```

If not enabled (that is, no string returned), run the `git annex initremote` command. 
Don't forget to give the remote a name (it is `datalad` here). The following command will configure datalad as a special remote for the annexed contents in the dataset.

```
git annex initremote datalad type=external externaltype=datalad encryption=none

```

### Step 6: Create your datalad dataset in the desired directory


```

datalad create mydataset
cd mydataset
```

Take HCP-D as an example, you will run:

```
datalad create HCP-D
cd HCP-D
```

### Step 7: Run datalad addurls command
It would be helpful to first go over the [documentation](http://docs.datalad.org/en/stable/generated/man/datalad-addurls.html) to have the command tailored to your needs. 
Take HCP-D as an example, you will run:

```
datalad addurls FILE_PREPARED_IN_STEP_0 '{associated_file}' '{filename}'
```

where `{associated_file}` refers to the `associated_file` column in `FILE_PREPARED_IN_STEP_0` and `{filename}` refers to the `filename` column in `FILE_PREPARED_IN_STEP_0`. 
