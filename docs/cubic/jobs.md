---
layout: default
title: Job Submission
parent: CUBIC
nav_order: 5
---

# Job submission on CUBIC
CUBIC now uses SLURM as its job scheduler (previously CUBIC used SGE). The basic syntax for submitting jobs on SLURM is the following:

```bash
sbatch my_script.sh
```

`my_script.sh` must have the following directives in its header:
```bash
#!/bin/bash
#SBATCH --nodes=1               # number of nodes should be 1 (>1 requires use of a library such as MPI (Message-Passing Interface) which CUBIC doesn't have as of now...)
#SBATCH --ntasks=1              # number of tasks
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00         # Set expected wall time it takes for your job

# code for your job
```

It can also have additional directives such as:
```bash
#SBATCH --job-name="job_name"
#SBATCH --output="output.out"
#SBATCH --error="error.err"
```

Alternatively, your sbatch directives can be included in the command line instead. For example:
```bash
sbatch --nodes=1 --ntasks=1 --cpus-per-task=1 --time=00:30:00 --job-name="job_name" --output="output.out" --error="error.err" my_script.sh
```
(In this alternative, the directives would not be in `my_script.sh`.)

You can read CBICA's documentation on basic job submission here:
https://cbica-wiki.uphs.upenn.edu/docs/List_of_Slurm_Articles/

### Checking SLURM job status
If you need to cancel your job:
```bash
scancel $jobid # cancel your job!
```

Other commands for checking your job status and looking at job history:
```bash
# check the status of all your jobs
squeue -u username

# another way to do it
squeue --me

# check the status of specific job
squeue $jobid

# this is just a nice shortcut to expand the headings of squeue :)
squeue --o "%.18i %.9P %.60j %.8u %.8T %.10M %.9l %.6D %R" --me

# display history of jobs starting at a specific time
sacct -u username --starttime=yyyy-mm-dd -o JobID,JobName,Elapsed,State,MaxRSS,ReqMem,Timelimit
```

### Figuring out how much memory to request

```bash
# check how much time your job took,
# how much memory you had requested and how much was actually used.
# Adjust your future jobs from this information
seff $jobid

# same thing but for job arrays
seff_array $jobid
```

### Job arrays

Job arrays in SLURM are useful for running a series of similar or repetitive tasks, like processing multiple participants.
By submitting a job array, you create a single job submission with multiple sub-jobs (or array tasks).
This reduces SLURM’s workload in scheduling compared to submitting each job individually.
Furthermore, instead of manually creating and tracking many separate jobs, you use a single job script that SLURM handles as an array.
You can access each task's unique identifier within the script (using the environment variable `$SLURM_ARRAY_TASK_ID`).

You can refer to the excellent CUBIC wiki documentation on simple job arrays:
https://cbica-wiki.uphs.upenn.edu/docs/Slurm_Example_05_-_Array_Jobs/


### Job dependencies

Job dependencies allow you to control the order in which jobs run, setting conditions so that a job only starts once another job has completed a specific action.
This is helpful if you have a series of tasks where one needs to finish before the next can start.

CUBIC wiki examples for simple and intermediate job dependencies:

https://cbica-wiki.uphs.upenn.edu/docs/Slurm_Example_06_-_Job_Dependencies_%28Simple%29/

https://cbica-wiki.uphs.upenn.edu/docs/Slurm_Example_07_-_Job_Dependencies_%28Intermediate%29/

### Job arrays with job dependencies!
Say you have an analysis pipeline with multiple steps that can't be consolidated into a single script.
And you want to run one job array after the other.
You can run job arrays with job dependencies, and dynamically update your output and error log files!
Here is a [repo of a current project](https://github.com/audreycluo/cubic_luowmdev/tree/main/tract_to_cortex) with an example of job arrays with job dependencies.
See scripts `c**` for a clean example.
This repo will be updated once the project is completed.


# Mapping of the commands in SGE to Slurm

This webpage is a helpful resource: [https://github.com/aws/aws-parallelcluster/wiki/Transition-from-SGE-to-SLURM](https://github.com/aws/aws-parallelcluster/wiki/Transition-from-SGE-to-SLURM).
