---
layout: default
title: Fetching Your Data
parent: The Way
nav_order: 1
has_toc: true
---

# Fetching Your Data
{: .no_toc}

There are a number of places you may have to fetch data from to get them onto a cluster filesystem. We will briefly cover best practices for the methods we've used before. Additions will be made as we gain more experience.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Between Clusters Or Local Disks

The best option for moving a large amount of data between clusters is to use the `scp` command. Remember that this process must remain open and running in your terminal, so it might be useful to do this in a fresh terminal window or use `&` at the end of your command. You could also use [`screen`](https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/) to set up a non-terminating terminal.

As mentioned in our general [PMACS documentation](/docs/pmacs), you should scp *into* a node called `transfer`, for PMACS projects. That would look like this:

```
## my username is <username>
scp -r path/to/your/data <username>@transfer:/path/on/pmacs
```

An alternative to `scp` is `rsync`, but that tends to have [more happening under the hood](https://stackoverflow.com/questions/20244585/how-does-scp-differ-from-rsync).

# Flywheel

On Flywheel, your data may already be in BIDS. In this case we recommend using Flywheel's export function `fw export bids`, or the export function provided by [`fw-heudiconv`](https://fw-heudiconv.readthedocs.io/en/latest/). We built the export function into `fw-heudiconv` because we wanted to have more flexibility in what BIDS data we could grab, including data that's not yet supported in the official BIDS spec. Admittedly though, downloading all of `fw-heudiconv` a lot of overhead for just the export function.

```
# with fw export bids
fw export bids <DESTINATION_DIRECTORY> --project <PROJECT_NAME> --subject <SUBJECT_FILTER>

# with fw-heudiconv
fw-heudiconv-export --project <PROJECT_NAME> --subject <SUBJECTS_FILTER> --session <SESSION_FILTER> --folders <LIST_OF_BIDS_FOLDERS>
```

Try `fw-heudiconv-export -h` for more info.

# Globus

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

# Datalad addurls from AWS S3
Now that AWS S3 has become increasingly popular for public data storage, you might want to fetch data from a set of S3 links. `datalad addurls` is a useful command that can retrieve files from web sources and register their location automatically.

For any dataset that comes with a manifest file, the steps are as below:

## Step 0: Data Preparation
{: .no_toc }

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



## Step 1: Download a copy of the NDA download manager 
{: .no_toc }

The command line downdownload manager is written in Java and allows for the automatic download of files. We can use `wget` to retrieve the program from the NIH web server.
  ```
  wget https://ndar.nih.gov/jnlps/download_manager_client/downloadmanager.zip
  ```

## Step 2: Unzip the download manager
 {: .no_toc }

 Since the downloaded program is a zipped file, we would need to unzip the program to use the download manager. 

  ```
  unzip downloadmanager.zip
  ```

## Step 3: Use the command-line download manager to generate temporary Amazon S3 security credentials
 {: .no_toc }

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


## Step 4: Export the AWS S3 credentials to your working directory
{: .no_toc }

For instance, navigate to `~/.aws/credentials` and paste in the `awskeys.txt` according to the format below:


```
[NDAR]
aws_access_key_id = xxxxx[copy and paste the value of accessKey in `awskeys.txt`]
aws_secret_access_key = xxxxx[copy and paste the value of secretKey in `awskeys.txt`]
aws_session_token = xxxxx[copy and paste the value of sessionToken in `awskeys.txt`]
```


## Step 5: Check whether you have the datalad special remote enabled
{: .no_toc }

```

git annex info | grep datalad
```

If not enabled (that is, no string returned), run the `git annex initremote` command. 
Don't forget to give the remote a name (it is `datalad` here). The following command will configure datalad as a special remote for the annexed contents in the dataset.

```
git annex initremote datalad type=external externaltype=datalad encryption=none

```

## Step 6: Create your datalad dataset in the desired directory
{: .no_toc }

```

datalad create mydataset
cd mydataset
```

Take HCP-D as an example, you will run:

```
datalad create HCP-D
cd HCP-D
```

## Step 7: Run datalad addurls command
{: .no_toc }

It would be helpful to first go over the [documentation](http://docs.datalad.org/en/stable/generated/man/datalad-addurls.html) to have the command tailored to your needs. 
Take HCP-D as an example, you will run:

```
datalad addurls FILE_PREPARED_IN_STEP_0 '{associated_file}' '{filename}'
```

where `{associated_file}` refers to the `associated_file` column in `FILE_PREPARED_IN_STEP_0` and `{filename}` refers to the `filename` column in `FILE_PREPARED_IN_STEP_0`. 

# rclone

[rclone](https://rclone.org/) is a command line program to manage files on cloud storage. It is a feature rich alternative to cloud vendors' web storage interfaces. Over 40 cloud storage products support rclone including S3 object stores, business & consumer file storage services, as well as standard transfer protocols.

Rclone has powerful cloud equivalents to the unix commands rsync, cp, mv, mount, ls, ncdu, tree, rm, and cat. Rclone's familiar syntax includes shell pipeline support, and --dry-run protection. It is used at the command line, in scripts or via its API.

Rclone has been specifically useful for accessing data within the University of Minnesota's Supercomputing Institute's [2nd tier storgage](https://www.msi.umn.edu/content/second-tier-storage). This is the primary use case for which we recommend rclone for data transfer.

Rclone has only been tested for transfer to PMACS. To start, you might want to make a project directory on PMACS as a landing zone for your data. Please see [PMACS documentation](/docs/pmacs#making-a-project-directory) for further detail.

On the other end of the transfer, you will need filesystem access to the directory for which you wish to transfer data from. In the tested use case (UMN's MSI second tier storage -> PMACS), an MSI username and password is a prequisite to performing this file transfer. Additionally, your MSI username will need permissions to your directory of interest. For now, we are dependent on our collaborators for facilitating this step.

Once you have a PMACS directory, MSI user, and permissions for that MSI user, you may proceed through the following steps to transfer data from MSI's second tier/s3 storage to PMACS:

1. Install rclone. Download the appropriate version of rclone from [this link](https://rclone.org/downloads/), Intel/AMD 64 bit for linux works for PMACS. If you are on PennMed internet, you might be told that "this page is dangerous" and might have to click a "proceed anyways" link. You can use `scp` to bring it to your PMACS home or project directory, and `unzip` to unzip the file. From here, you can either proceed with the full installation instructions and add rclone commands to your path, or you can just call directly from the unzipped folder (i.e., `./rclone-v1.56.2-linux-amd64/rclone`).

2. Obtain your AWS secret keys from MSI. Use [this link](https://www.msi.umn.edu/content/s3-credentials) to get an access key and secret key for your MSI username. You'll need to log in to obtain them.

3. Configure rclone. Use the command `rclone config` (or `./rclone-v1.56.2-linux-amd64/rclone config`) to configure rclone for use. Here's how you should respond to the subsequent configuration prompts:

        a. `n` for new remote

        b. name your remote. `3bassigned_name` in the example below (step 4).

        c. select `4` for "type" to select Amazon S3 compliant storage

        d. select `3` for the type of S3 provider, corresponding to Ceph Object Storage

        e. hit enter to select default for `env_auth`

        f. enter your AWS access key from step 2 for the `AWS Access Key ID` prompt

        g. enter your AWS secret access key from step 2 for the `AWS Secret Access Key` prompt

        h. hit enter to select the default for Region to connect to (`region`)

        i. enter `s3.msi.umn.edu` for Endpoint for S3 API (`endpoint`)

        j. hit enter to select the default for `location constraint`

        k. enter `1` for owner full control (`acl`). You'll be able to change local permissions once the data is in.

        l. hit enter to select the default for `server_side_encryption`

        m. hit enter to select the default for `sse_kms_key_id`

        n. hit `n` or enter to NOT edit advanced configuration of the remote

        o. Check the outputted config file, hit `y` when ready to approve and move ahead with accessing the remote

4. Test rclone. Using the name you assigned for the remote in 3b, you should be able to list the contents of the directory you wish to transfer with `rclone ls 3bassigned_name:name_of_directory`. Note that for globbing/wild card usage works slightly differently for rclone than for your standard linux `ls`'ing. `--include` and `--exclude` flags can be applied in tandem with wildcards to alter which files you return for `rclone ls`, `rclone copy`, and `rclone sync`. See [this page](https://rclone.org/filtering/) for more detail.

6. Transfer data. Finally, to transfer data from `name_of_directory` to your PMACS directory, use `rclone copy 3bassigned_name:name_of_directory/name_of_desired_file /path_of_desired_output_directory` or `rclone sync`. Details on both are available [here](https://rclone.org/commands/rclone_copy/) and [here](https://rclone.org/commands/rclone_sync/), respectively. If using an include or exclude flag, insert it between the remote and local directory, as detailed in rclone's documentation.