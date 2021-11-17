---
layout: default
title: Flywheel SDK Theory
parent: Flywheel
nav_order: 3
---

# Using the SDK: Theory


## Client objects

Whenever you use the Flywheel SDK, you communicate with Flywheel using a *client*. All actions that use the SDK begin with creating a client, which looks like this

```python
>>> import flywheel
>>> fw = flywheel.Client()
```

where the `fw` object is the client. In order to connect to flywheel using the `Client()` function, you need to have [logged in](https://docs.flywheel.io/hc/en-us/articles/360008162214) to flywheel using the commandline tool.

Under the hood, the client object translates your interactions with it into http requests that are sent back and forth with the Flywheel server. In this way, you are able to tell the Flywheel server to change metadata, add or delete files, or run gears.

## Data containers

Data on a Flywheel data gets stored in *containers*. This terminology can be confusing, because gears are [containerized](https://en.wikipedia.org/wiki/OS-level_virtualization) pipelines. To disambiguate between software containers and the entities Flywheel uses to store data, we will refer to these as *data containers*. A data container could be an Acquisition, Analysis, Subject, Session or Project. Files stored in Flywheel all exist inside a container. When [downloading data](/docs/flywheel/sdk_getting) or [uploading data](https://docs.flywheel.io/hc/en-us/articles/360019252953-CLI-reference-guide-fw-upload), you will need to specify which container will house the file(s).

You can find the container ids using the SDK by accessing an object's `.id` property. Alternatively, you can browse to the subject, session or project in on the website and get the container IDs from the URL. For example,

<img src="/assets/images/url.png" alt="">

shows that we browsed from project ID `5c8937fddf93e3002e025e2b` to session `5e3d92d76dea31062c2a7448`. In the sdk we could easily access either of these containers by doing

```python
>>> this_project = fw.get("5c8937fddf93e3002e025e2b")
>>> this_session = fw.get("5e3d92d76dea31062c2a7448")
```
