---
layout: default
title: Creating BIDS Events TSVs from ITC EPrime Files
parent: Tutorials
nav_order: 4
---

| Title                                           | Author         | Replicator | Goal                          | Input Data   | Output                 |
|-------------------------------------------------|----------------|------------|-------------------------------|--------------|------------------------|
| Creating BIDS Events TSVs from ITC EPrime Files | Tinashe Tapera | TBD        | Convert EPrime data into BIDS | EPrime files | BIDS Valid Events TSVs |

# Introduction

Alongside your imaging data, BIDS also allows for the storage and
sharing of events data. Here, we demonstrate how to transform a common
event file known as EPrime into a BIDS valid events file.

# EPrime

EPrime is a software suite for experimental psychology. Without saying
too much, EPrime software can be linked to an fMRI scanner and be used
to record responses to questionnaires, run experiments with
participants, and so on. The output of these experiments is an EPrime
file:

``` r
ff <- read.delim("RTG1_1ITCscanner1LLA-04888-1.txt", fileEncoding="UCS-2LE")
# eprime files are already so esoteric that we have to use specific file encoding
# in R for them to work
```

This is one EPrime file from a scan session for one subject:

``` r
ff$X....Header.Start....[1:50]
```
```
 [1] "VersionPersist: 1"                "LevelName: Session"              
 [3] "LevelName: Block"                 "LevelName: Trial"                
 [5] "LevelName: SubTrial"              "LevelName: LogLevel5"            
 [7] "LevelName: LogLevel6"             "LevelName: LogLevel7"            
 [9] "LevelName: LogLevel8"             "LevelName: LogLevel9"            
[11] "LevelName: LogLevel10"            "Experiment: RTG1_1ITCscanner1LLA"
[13] "SessionDate: 04-26-2011"          "SessionTime: 14:30:53"           
[15] "SessionTimeUtc: 6:30:53 PM"       "Subject: 04888"                  
[17] "Session: 1"                       "RandomSeed: 711119607"           
[19] "Group: 1"                         "Display.RefreshRate: 60.052"     
[21] "*** Header End ***"               ""                                
[23] ""                                 "Level: 3"                        
[25] ""                                 ""                                
[27] "*** LogFrame Start ***"           ""                                
[29] ""                                 "Procedure: TrialProc"            
[31] ""                                 ""                                
[33] "TrialList: 1"                     ""                                
[35] ""                                 "Offer: 23"                       
[37] ""                                 ""                                
[39] "delay: 21"                        ""                                
[41] ""                                 "NullDuration: 5000"              
[43] ""                                 ""                                
[45] "LeftRight: 0"                     ""                                
[47] ""                                 "FeedbackDur: 0"                  
[49] ""                                 ""
```
This is not a very useful representation of data. Fortunately, the
`rprime` package exists for parsing this file.

# `rprime` Package

``` r
# install.packages("rprime")
library(rprime)
library(tidyverse) # it pairs well with the tidyverse
```

```
── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──

✓ ggplot2 3.3.5     ✓ purrr   0.3.4
✓ tibble  3.1.6     ✓ dplyr   1.0.8
✓ tidyr   1.2.0     ✓ stringr 1.4.0
✓ readr   2.0.0     ✓ forcats 0.5.1

Warning: package 'tidyr' was built under R version 4.1.2

Warning: package 'dplyr' was built under R version 4.1.2

── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
x dplyr::filter() masks stats::filter()
x dplyr::lag()    masks stats::lag()
```

It’s straightforward to read in an EPrime file, using the following:

``` r
dat <- rprime::read_eprime("RTG1_1ITCscanner1LLA-04888-1.txt")
dat <- dat %>%
  rprime::FrameList()

preview_frames(dat)
```

```
 Eprime.Level Running Procedure
            1  Header    Header
List of 17
 $ Eprime.Level       : num 1
 $ Eprime.LevelName   : chr "Header_"
 $ Eprime.Basename    : chr "RTG1_1ITCscanner1LLA-04888-1"
 $ Eprime.FrameNumber : chr "1"
 $ Procedure          : chr "Header"
 $ Running            : chr "Header"
 $ VersionPersist     : chr "1"
 $ LevelName          : chr "LogLevel10"
 $ Experiment         : chr "RTG1_1ITCscanner1LLA"
 $ SessionDate        : chr "04-26-2011"
 $ SessionTime        : chr "14:30:53"
 $ SessionTimeUtc     : chr "6:30:53 PM"
 $ Subject            : chr "04888"
 $ Session            : chr "1"
 $ RandomSeed         : chr "711119607"
 $ Group              : chr "1"
 $ Display.RefreshRate: chr "60.052"
 - attr(*, "class")= chr [1:2] "EprimeFrame" "list"

 Eprime.Level   Running Procedure
            3 TrialList TrialProc
List of 66
 $ Eprime.Level                     : num 3
 $ Eprime.LevelName                 : chr "TrialList_1"
 $ Eprime.Basename                  : chr "RTG1_1ITCscanner1LLA-04888-1"
 $ Eprime.FrameNumber               : chr "2"
 $ Procedure                        : chr "TrialProc"
 $ Running                          : chr "TrialList"
 $ Offer                            : chr "23"
 $ delay                            : chr "21"
 $ NullDuration                     : chr "5000"
 $ LeftRight                        : chr "0"
 $ FeedbackDur                      : chr "0"
 $ Cycle                            : chr "1"
 $ Sample                           : chr "1"
 $ nullscreen.OnsetDelay            : chr "71"
 $ nullscreen.OnsetTime             : chr "102383"
 $ nullscreen.DurationError         : chr "-71"
 $ nullscreen.StartTime             : chr "102314"
 $ nullscreen.OffsetTime            : chr "107112"
 $ nullscreen.FinishTime            : chr "107112"
 $ nullscreen.ActionDelay           : chr "0"
 $ nullscreen.ActionTime            : chr "102383"
 $ nullscreen.OffsetDelay           : chr "0"
 $ Choice1.OnsetDelay               : chr "0"
 $ Choice1.OnsetTime                : chr "107312"
 $ Choice1.DurationError            : chr "0"
 $ Choice1.Duration                 : chr "4000"
 $ Choice1.StartTime                : chr "107113"
 $ Choice1.OffsetTime               : chr "111112"
 $ Choice1.FinishTime               : chr "111112"
 $ Choice1.OffsetDelay              : chr "0"
 $ Choice1.RTTime                   : chr "111192"
 $ Choice1.RT                       : chr "3880"
 $ Choice1.RESP                     : chr "y"
 $ Choice1.CRESP                    : chr "r"
 $ FeedbackDisplay6.OnsetDelay      : chr "0"
 $ FeedbackDisplay6.OnsetTime       : chr "0"
 $ FeedbackDisplay6.DurationError   : chr "-999999"
 $ FeedbackDisplay6.Duration        : chr "0"
 $ FeedbackDisplay6.StartTime       : chr "111182"
 $ FeedbackDisplay6.OffsetTime      : chr "0"
 $ FeedbackDisplay6.FinishTime      : chr "111192"
 $ FeedbackDisplay6.OffsetDelay     : chr "-999999"
 $ Choice.OnsetDelay                : chr "0"
 $ Choice.OnsetTime                 : chr "0"
 $ Choice.DurationError             : chr "0"
 $ Choice.Duration                  : chr "4000"
 $ Choice.StartTime                 : chr "0"
 $ Choice.OffsetTime                : chr "0"
 $ Choice.FinishTime                : chr "0"
 $ Choice.TargetOffsetTime          : chr "0"
 $ Choice.TargetOnsetTime           : chr "0"
 $ Choice.OffsetDelay               : chr "0"
 $ Choice.RTTime                    : chr "0"
 $ Choice.RT                        : chr "0"
 $ Choice.RESP                      : chr ""
 $ Choice.CRESP                     : chr ""
 $ FeedbackDisplay3.OnsetDelay      : chr "0"
 $ FeedbackDisplay3.OnsetTime       : chr "0"
 $ FeedbackDisplay3.DurationError   : chr "0"
 $ FeedbackDisplay3.Duration        : chr "0"
 $ FeedbackDisplay3.StartTime       : chr "0"
 $ FeedbackDisplay3.OffsetTime      : chr "0"
 $ FeedbackDisplay3.FinishTime      : chr "0"
 $ FeedbackDisplay3.TargetOffsetTime: chr "0"
 $ FeedbackDisplay3.TargetOnsetTime : chr "0"
 $ FeedbackDisplay3.OffsetDelay     : chr "0"
 - attr(*, "class")= chr [1:2] "EprimeFrame" "list"

 Eprime.Level   Running Procedure
            2 BlockList BlockProc
List of 9
 $ Eprime.Level      : num 2
 $ Eprime.LevelName  : chr "BlockList_1"
 $ Eprime.Basename   : chr "RTG1_1ITCscanner1LLA-04888-1"
 $ Eprime.FrameNumber: chr "52"
 $ Procedure         : chr "BlockProc"
 $ Running           : chr "BlockList"
 $ PracticeMode      : chr "?"
 $ Cycle             : chr "1"
 $ Sample            : chr "1"
 - attr(*, "class")= chr [1:2] "EprimeFrame" "list"

 Eprime.Level Running Procedure
            1    <NA>      <NA>
List of 65
 $ Eprime.Level            : num 1
 $ Eprime.LevelName        : logi NA
 $ Eprime.Basename         : chr "RTG1_1ITCscanner1LLA-04888-1"
 $ Eprime.FrameNumber      : chr "53"
 $ Procedure               : logi NA
 $ Running                 : logi NA
 $ Experiment              : chr "RTG1_1ITCscanner1LLA"
 $ SessionDate             : chr "04-26-2011"
 $ SessionTime             : chr "14:30:53"
 $ SessionTimeUtc          : chr "6:30:53 PM"
 $ Subject                 : chr "04888"
 $ Session                 : chr "1"
 $ RandomSeed              : chr "711119607"
 $ Group                   : chr "1"
 $ Display.RefreshRate     : chr "60.052"
 $ Slide2.OnsetDelay       : chr "5"
 $ Slide2.OnsetTime        : chr "16024"
 $ Slide2.DurationError    : chr "-999999"
 $ Slide2.PreRelease       : chr "0"
 $ Slide2.Duration         : chr "-1"
 $ Slide2.StartTime        : chr "16019"
 $ Slide2.OffsetTime       : chr "80941"
 $ Slide2.FinishTime       : chr "80941"
 $ Slide2.TimingMode       : chr "0"
 $ Slide2.CustomOnsetTime  : chr "0"
 $ Slide2.CustomOffsetTime : chr "0"
 $ Slide2.ActionDelay      : chr "0"
 $ Slide2.ActionTime       : chr "16024"
 $ Slide2.TargetOffsetTime : chr "-1"
 $ Slide2.TargetOnsetTime  : chr "16019"
 $ Slide2.OffsetDelay      : chr "-999999"
 $ Slide2.RTTime           : chr "80940"
 $ Slide2.ACC              : chr "0"
 $ Slide2.RT               : chr "64916"
 $ Slide2.RESP             : chr "n"
 $ Slide2.CRESP            : chr ""
 $ Slide1.OnsetTime        : chr "80945"
 $ Slide1.DurationError    : chr "-999999"
 $ Slide1.Duration         : chr "-1"
 $ Slide1.StartTime        : chr "80943"
 $ Slide1.OffsetTime       : chr "102312"
 $ Slide1.FinishTime       : chr "102312"
 $ Slide1.RT               : chr "21367"
 $ Goodbye.OnsetDelay      : chr "1"
 $ Goodbye.OnsetTime       : chr "605961"
 $ Goodbye.DurationError   : chr "0"
 $ Goodbye.PreRelease      : chr "0"
 $ Goodbye.Duration        : chr "6000"
 $ Goodbye.StartTime       : chr "605770"
 $ Goodbye.OffsetTime      : chr "611961"
 $ Goodbye.FinishTime      : chr "611961"
 $ Goodbye.TimingMode      : chr "0"
 $ Goodbye.CustomOnsetTime : chr "0"
 $ Goodbye.CustomOffsetTime: chr "0"
 $ Goodbye.ActionDelay     : chr "1"
 $ Goodbye.ActionTime      : chr "605962"
 $ Goodbye.TargetOffsetTime: chr "611961"
 $ Goodbye.TargetOnsetTime : chr "605960"
 $ Goodbye.OffsetDelay     : chr "0"
 $ Goodbye.RTTime          : chr "0"
 $ Goodbye.ACC             : chr "0"
 $ Goodbye.RT              : chr "0"
 $ Goodbye.RESP            : chr ""
 $ Goodbye.CRESP           : chr ""
 $ Clock.StartTimeOfDay    : chr "4/26/2011 2:30:53 PM"
 - attr(*, "class")= chr [1:2] "EprimeFrame" "list"

```

This creates a more workable data structure. The section with the
expriment is called the `trial` frame.`rprime` allows you to filter
these with built-ins:

``` r
trial <- filter_in(dat, "Running", "TrialList")
block <- filter_in(dat, "Running", "BlockList")
slides <- filter_in(dat, "Eprime.Level", 1)

slides_df <- to_data_frame(slides) %>%
  readr::type_convert()
trial_df <- to_data_frame(trial) %>%
  readr::type_convert()

head(trial_df)
```


| Eprime.Level | Eprime.LevelName | Eprime.Basename               | Eprime.FrameNumber | Procedure | Running   | Offer | delay | NullDuration | LeftRight | FeedbackDur | Cycle | Sample | nullscreen.OnsetDelay | nullscreen.OnsetTime | nullscreen.DurationError | nullscreen.StartTime | nullscreen.OffsetTime | nullscreen.FinishTime | nullscreen.ActionDelay | nullscreen.ActionTime | nullscreen.OffsetDelay | Choice1.OnsetDelay | Choice1.OnsetTime | Choice1.DurationError | Choice1.Duration | Choice1.StartTime | Choice1.OffsetTime | Choice1.FinishTime | Choice1.OffsetDelay | Choice1.RTTime | Choice1.RT | Choice1.RESP | Choice1.CRESP | FeedbackDisplay6.OnsetDelay | FeedbackDisplay6.OnsetTime | FeedbackDisplay6.DurationError | FeedbackDisplay6.Duration | FeedbackDisplay6.StartTime | FeedbackDisplay6.OffsetTime | FeedbackDisplay6.FinishTime | FeedbackDisplay6.OffsetDelay | Choice.OnsetDelay | Choice.OnsetTime | Choice.DurationError | Choice.Duration | Choice.StartTime | Choice.OffsetTime | Choice.FinishTime | Choice.TargetOffsetTime | Choice.TargetOnsetTime | Choice.OffsetDelay | Choice.RTTime | Choice.RT | Choice.RESP | Choice.CRESP | FeedbackDisplay3.OnsetDelay | FeedbackDisplay3.OnsetTime | FeedbackDisplay3.DurationError | FeedbackDisplay3.Duration | FeedbackDisplay3.StartTime | FeedbackDisplay3.OffsetTime | FeedbackDisplay3.FinishTime | FeedbackDisplay3.TargetOffsetTime | FeedbackDisplay3.TargetOnsetTime | FeedbackDisplay3.OffsetDelay |
|-------------:|:-----------------|:------------------------------|-------------------:|:----------|:----------|------:|------:|-------------:|----------:|------------:|------:|-------:|----------------------:|---------------------:|-------------------------:|---------------------:|----------------------:|----------------------:|-----------------------:|----------------------:|-----------------------:|-------------------:|------------------:|----------------------:|-----------------:|------------------:|-------------------:|-------------------:|--------------------:|---------------:|-----------:|:-------------|:--------------|----------------------------:|---------------------------:|-------------------------------:|--------------------------:|---------------------------:|----------------------------:|----------------------------:|-----------------------------:|------------------:|-----------------:|---------------------:|----------------:|-----------------:|------------------:|------------------:|------------------------:|-----------------------:|-------------------:|--------------:|----------:|:------------|:-------------|----------------------------:|---------------------------:|-------------------------------:|--------------------------:|---------------------------:|----------------------------:|----------------------------:|----------------------------------:|---------------------------------:|-----------------------------:|
|            3 | TrialList\_1     | RTG1\_1ITCscanner1LLA-04888-1 |                  2 | TrialProc | TrialList |  23.0 |    21 |         5000 |         0 |           0 |     1 |      1 |                    71 |               102383 |                      -71 |               102314 |                107112 |                107112 |                      0 |                102383 |                      0 |                  0 |            107312 |                     0 |             4000 |            107113 |             111112 |             111112 |                   0 |         111192 |       3880 | y            | r             |                           0 |                          0 |                        -999999 |                         0 |                     111182 |                           0 |                      111192 |                      -999999 |                 0 |                0 |                    0 |            4000 |                0 |                 0 |                 0 |                       0 |                      0 |                  0 |             0 |         0 | NA          | NA           |                           0 |                          0 |                              0 |                         0 |                          0 |                           0 |                           0 |                                 0 |                                0 |                            0 |
|            3 | TrialList\_2     | RTG1\_1ITCscanner1LLA-04888-1 |                  3 | TrialProc | TrialList |  28.0 |     5 |         5000 |         1 |         760 |     1 |      2 |                     8 |               111200 |                       -8 |               111199 |                115992 |                115992 |                      0 |                111200 |                      0 |                  0 |            107312 |                     0 |             4000 |            107113 |             111112 |             111112 |                   0 |         111192 |       3880 | y            | r             |                           0 |                          0 |                        -999999 |                         0 |                     111182 |                           0 |                      111192 |                      -999999 |                 0 |           116192 |              -999999 |            4000 |           115993 |            119432 |            119432 |                  119992 |                 116192 |            -999999 |        119432 |      3240 | y           | r            |                           3 |                     119435 |                             -3 |                       760 |                     119434 |                      119992 |                      119992 |                            119992 |                           119432 |                            0 |
|            3 | TrialList\_3     | RTG1\_1ITCscanner1LLA-04888-1 |                  4 | TrialProc | TrialList |  30.5 |    55 |         5000 |         1 |        1361 |     1 |      3 |                     0 |               120192 |                        0 |               119999 |                124992 |                124992 |                      0 |                120192 |                      0 |                  0 |            107312 |                     0 |             4000 |            107113 |             111112 |             111112 |                   0 |         111192 |       3880 | y            | r             |                           0 |                          0 |                        -999999 |                         0 |                     111182 |                           0 |                      111192 |                      -999999 |                 0 |           125192 |              -999999 |            4000 |           124993 |            127832 |            127832 |                  128992 |                 125192 |            -999999 |        127831 |      2639 | r           | r            |                           3 |                     127835 |                             -3 |                      1361 |                     127834 |                      128993 |                      128993 |                            128993 |                           127832 |                            0 |
|            3 | TrialList\_4     | RTG1\_1ITCscanner1LLA-04888-1 |                  5 | TrialProc | TrialList |  39.0 |    34 |        17000 |         1 |           0 |     1 |      4 |                     0 |               129193 |                        0 |               129000 |                145993 |                145993 |                      0 |                129193 |                      0 |                  0 |            107312 |                     0 |             4000 |            107113 |             111112 |             111112 |                   0 |         111192 |       3880 | y            | r             |                           0 |                          0 |                        -999999 |                         0 |                     111182 |                           0 |                      111192 |                      -999999 |                 0 |           146193 |                    0 |            4000 |           145994 |            149993 |            149993 |                  149993 |                 146193 |                  0 |             0 |         0 | NA          | r            |                           0 |                     150193 |                            200 |                         0 |                     149995 |                      150193 |                      150193 |                            149993 |                           150193 |                          200 |
|            3 | TrialList\_5     | RTG1\_1ITCscanner1LLA-04888-1 |                  6 | TrialProc | TrialList |  25.0 |     7 |         8000 |         0 |         993 |     1 |      5 |                     9 |               150202 |                       -9 |               150201 |                157993 |                157993 |                      0 |                150202 |                      0 |                  0 |            158193 |               -999999 |             4000 |            157994 |             161200 |             161200 |             -999999 |         161200 |       3007 | r            | r             |                           3 |                     161203 |                             -3 |                       993 |                     161202 |                      161993 |                      161993 |                            0 |                 0 |           146193 |                    0 |            4000 |           145994 |            149993 |            149993 |                  149993 |                 146193 |                  0 |             0 |         0 | NA          | r            |                           0 |                     150193 |                            200 |                         0 |                     149995 |                      150193 |                      150193 |                            149993 |                           150193 |                          200 |
|            3 | TrialList\_6     | RTG1\_1ITCscanner1LLA-04888-1 |                  7 | TrialProc | TrialList |  22.5 |    45 |         2000 |         1 |        1329 |     1 |      6 |                     0 |               162193 |                        0 |               162000 |                163993 |                163993 |                      0 |                162193 |                      0 |                  0 |            158193 |               -999999 |             4000 |            157994 |             161200 |             161200 |             -999999 |         161200 |       3007 | r            | r             |                           3 |                     161203 |                             -3 |                       993 |                     161202 |                      161993 |                      161993 |                            0 |                 0 |           164193 |              -999999 |            4000 |           163994 |            166864 |            166864 |                  167993 |                 164193 |            -999999 |        166864 |      2671 | r           | r            |                           3 |                     166867 |                             -3 |                      1329 |                     166866 |                      167993 |                      167993 |                            167993 |                           166864 |                            0 |


This is far more useful, as we can see some of the encoded experimental
variables like `offer`, `delay`, and `choice`.

You can generally expect this method to be useful for parsing any EPrime
file. To export this to BIDS, one could simply write this dataframe to a
[BIDS-valid events
file](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/05-task-events.html):

``` r
trial_df %>%
  write_delim("sub-X/ses-1/func/sub-X_ses-1_task-ITC_events.tsv")
```

In this case, we have to do some more data wrangling for the ITC
experimental design.

# ITC Experimental Design

Each line of this table indicates an event (trial) happening in the
experiment. In an ITC task, participants are shown a value of money and
a delay. They’re asked, “would you rather receive $20 now, or wait X
number of days to receive $Y later?” Hence, each line is an offer in
this paradigm. To convert this to BIDS, we expect an output

### Mandatory in BIDS:

`onset`: time that the trial happened from the start of the scan

`duration`: how long that event happened for

### Required for ITC

`choice`: did they choose the delayed offer or not

`button_press`: did they go left or right

`amount`: how much they were offered

`delay`: what was the delay on the offer

`reaction_time`: how long did they take to make their decision

# Data Wrangling

The first thing we need to define is what choice they made. The column
`LeftRight` indicates whether the instant $20 option is on the left or
right of the screen. If `LeftRight == 1`, the delayed option was
presented on the left.

We’ll code this as a factor `delay_position` with two levels, 1 to
indicate it was on the right, and 0 to indicate it was on the left:

``` r
trial_df_proc <- trial_df %>%
  select(-contains("null"), -contains("Eprime"), -contains("Feedback")) %>%
  mutate(delay_position = ifelse(LeftRight == 0, 1, 0))
```

Next, we define which button they pressed, left (0) or right (1):

We’ll also define the motor response they made, `button_press`, as
either 1 (right) or 0 (left). We use `CHOICE.RESP` and `CHOICE1.RESP` as
the indicator of which side they picked. If the delayed option was on
the left, use `CHOICE.RESP`; `r` is right, `y` is left.

Then, we encode the `choice` as either `1=delayed` (the delayed position
and the chosen button press where the same) or `0=now` (the delayed
position and the chosen button press where different):

``` r
trial_df_proc <- trial_df_proc %>%
  mutate(
    button_press = case_when(
      
      LeftRight == 1 & Choice.RESP == "y" ~ 0,
      LeftRight == 1 & Choice.RESP == "r" ~ 1,
      LeftRight == 0 & Choice1.RESP == "y" ~ 0,
      LeftRight == 0 & Choice1.RESP == "r" ~ 1
      
    ),
    choice = case_when(
      
      LeftRight == 1 & Choice.RESP == "y" ~ 1,
      LeftRight == 1 & Choice.RESP == "r" ~ 0,
      LeftRight == 0 & Choice1.RESP == "y" ~ 0,
      LeftRight == 0 & Choice1.RESP == "r" ~ 1
      
      )
    )
```

We also include the amount and delay:

``` r
trial_df_proc <- trial_df_proc %>%
  rename(offer = Offer) %>%
  select(offer, delay, choice, button_press, delay_position, everything())
```

The duration of the trial is uniform at 4000ms. There are two columns
for event timings: `Choice1.OnsetTime` and `Choice.OnsetTime`. If
`LeftRight==1` the task proceeds to Choice.\*. If they clicked right,
the time for this gets recorded in `Choice.OnsetTime`, and the value in
`Choice1.OnsetTime` is duplicated from the previous row:

    10            216687           222699  left
    11            228727           222699  left
    12            246744           222699  right
    13            246744           264762  right
    14            246744           270774  right

Here we use the `duplicated` function to tell us if a value in a vector
is a duplicate of itself. If there’s a duplicate, take the value from
the opposite column:

``` r
trial_df_proc <- trial_df_proc %>%
  mutate(
    onset = case_when(
       
      # the first row should both not be duplicates
      !duplicated(Choice.OnsetTime) & !duplicated(Choice1.OnsetTime) ~ 0,
      
      # if any value in Choice is a duplicate, choose the value from Choice1
      duplicated(Choice.OnsetTime) ~ Choice1.OnsetTime,
      
      # vice versa
      duplicated(Choice1.OnsetTime) ~ Choice.OnsetTime
    ),
    
    duration = 4000,
    
  ) %>%
  select(onset, duration, everything())
```

We can do the same for response time:

``` r
trial_df_proc <- trial_df_proc %>%
  mutate(
    row_num = row_number(),
    response_time = case_when(
       
      # the first row should be the one that's not zero
      row_num == 1 & Choice.RT == 0 ~ Choice1.RT,
      row_num == 1 & Choice1.RT == 0 ~ Choice.RT,
      
      # if any value in Choice is a duplicate, choose the value from Choice1
      duplicated(Choice.RT) ~ Choice1.RT,
      
      # vice versa
      duplicated(Choice1.RT) ~ Choice.RT
    )
  ) %>%
  select(onset, duration, response_time, everything(), -row_num)
```

Lastly, we have to account for the timepoint that the task began (as
opposed to when the participant is reading instructions). This is given
in the `slides_df`:

``` r
trial_df_proc <- trial_df_proc %>%
  mutate(onset = ifelse(onset == 0, onset, onset - slides_df$Slide1.OffsetTime[2]))
```

Here’s the data head so far:

``` r
trial_df_sv <- trial_df_proc %>%
  select(onset:delay_position) %>%
  mutate(IA = 20)
trial_df_sv %>%
  head()
```

| onset | duration | response\_time | offer | delay | choice | button\_press | delay\_position |  IA |
|------:|---------:|---------------:|------:|------:|-------:|--------------:|----------------:|----:|
|     0 |     4000 |           3880 |  23.0 |    21 |      0 |             0 |               1 |  20 |
| 13880 |     4000 |           3240 |  28.0 |     5 |      1 |             0 |               0 |  20 |
| 22880 |     4000 |           2639 |  30.5 |    55 |      0 |             1 |               0 |  20 |
| 43881 |     4000 |           3880 |  39.0 |    34 |     NA |            NA |               0 |  20 |
| 55881 |     4000 |           3007 |  25.0 |     7 |      1 |             1 |               1 |  20 |
| 61881 |     4000 |           2671 |  22.5 |    45 |      0 |             1 |               0 |  20 |

# K Parameter Estimation

The penultimate step is to estimate each participant’s `k` parameter.
This is estimated from a discount function that you can read about in
[this paper](https://www.nature.com/articles/nn2007). For our purposes,
the code is in matlab and exists as a precompiled binary on CUBIC at
`/cbica/projects/wolf_satterthwaite_reward/Curation/code/itc_eprime/matlab_code/kable_itc_wrapper`.
It was run with
`/cbica/projects/wolf_satterthwaite_reward/Curation/code/itc_eprime/loop_processed_eprimes.sh`,
which outputs the `k` parameter value to
`/cbica/projects/wolf_satterthwaite_reward/Curation/code/itc_eprime/matlab_code/data/processed/*.txt`

# Output

After estimating the `k` parameter, we can then calculate the
*subjective value* (the participant’s evaluation of each offer of money
now or later as the experiment continues) by doing
$\\frac{\\text{offer}} {1 + k \\times \\text{delay}}$:

``` r
# a fake k value
k_param <- 0.07106205
final_df <- trial_df_sv %>%
  mutate(subjective_value = offer / (1 + k_param * delay)) %>%
  mutate_if(~ is.numeric(.) && all(unique(.) %in% c(0, 1, NA)), factor) %>%
  select(-IA) 
```

And here’s the output for this example subject:

``` r
final_df %>%
  head(10)
```


|  onset | duration | response\_time | offer | delay | choice | button\_press | delay\_position | subjective\_value |
|-------:|---------:|---------------:|------:|------:|:-------|:--------------|:----------------|------------------:|
|      0 |     4000 |           3880 |  23.0 |    21 | 0      | 0             | 1               |          9.228412 |
|  13880 |     4000 |           3240 |  28.0 |     5 | 1      | 0             | 0               |         20.659476 |
|  22880 |     4000 |           2639 |  30.5 |    55 | 0      | 1             | 0               |          6.213821 |
|  43881 |     4000 |           3880 |  39.0 |    34 | NA     | NA            | 0               |         11.416495 |
|  55881 |     4000 |           3007 |  25.0 |     7 | 1      | 1             | 1               |         16.695223 |
|  61881 |     4000 |           2671 |  22.5 |    45 | 0      | 1             | 0               |          5.359960 |
|  67881 |     4000 |           2471 |  37.5 |   149 | 0      | 1             | 0               |          3.236038 |
|  82881 |     4000 |           3959 |  40.5 |    97 | 1      | 0             | 0               |          5.131117 |
|  94840 |     4000 |           2896 |  31.5 |    68 | 0      | 0             | 1               |          5.401031 |
| 100840 |     4000 |           3000 |  46.5 |    48 | 1      | 0             | 0               |         10.541879 |


This procedure is reproduced for the full dataset in
`/cbica/projects/wolf_satterthwaite_reward/Curation/code/itc_eprime/parse_eprime.Rmd`.
