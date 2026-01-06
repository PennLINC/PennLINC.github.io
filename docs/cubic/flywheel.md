---
layout: default
title: Getting data from flywheel
parent: CUBIC
nav_order: 9
---

# Getting data from flywheel
The source data for some projects may exist on flywheel.
After you've made a flywheel account (go to [upenn.flywheel.io/](https://upenn.flywheel.io/) in Google Chrome) and have been added to the project, navigate to your profile.

### Download the flywheel CLI
Under your profile near the top you should see a section titled 'Flywheel CLI'.
Download the classic CLI for Linux. Unzip the file and follow instructions elswhere on this page to transfer the `fw` executable to your cubic project directory's `~/bin/` path.
At the very bottom of the flywheel profile page, you will see a section titled 'Flywheel Access' and in it a button 'Generate API Key'. Click that button, give your key a name and an expiration date.
Copy the key and save it somewhere safe.

### Building your own glibc on cubic
At the time of these instructions, cubic's `glibc` library version is incompatible with the flywheel CLI.
To circumvent this problem, you will need to download a build your own glibc library to use with flywheel.

#### Load updated make and devtoolset
```bash
module avail make
module load make/<latest_version> ## was 4.3 at the writing of these instructions

module load devtoolset/9
```

#### Create a directory to store glibc source code
```bash
mkdir -p $HOME/bin/glibc
cd $HOME/bin/glibc
```

#### Download and extract glibc
```bash
wget http://ftp.gnu.org/gnu/libc/glibc-2.34.tar.gz
tar -xvzf glibc-2.34.tar.gz
cd glibc-2.34
```

#### Configure and build glibc
```bash
export CFLAGS="-O2"
export CXXFLAGS="-O2"
mkdir build
cd build
../configure --prefix=$HOME/bin/glibc-2.34
make -j$(nproc)
make install
```

The configure and build should take some time.

### Calling fw
Now you should be ready to login to flywheel.
First you'll need to unset your `LD_LIBRARY_PATH` to avoid calling cubic's default glibc.
Now is when you'll need your API key as well.

```bash
unset LD_LIBRARY_PATH # Do not use old GLIBC
~/bin/glibc-2.34/lib/ld-linux-x86-64.so.2 \ # Use new GLIBC
~/bin/fw login YOUR-API-KEY
```

Now you're logged in!
From here you may download specific files or sync the full project.
See flywheel's [documentation](https://docs.flywheel.io/CLI/) for more details.

Note: it's recommended that you use `fw sync` if you want the full project (or even most of it).
The `-m` flag is also advised if you want to get all of the subject/session level metadata.

#### Setting up an alias (optional)
It may be worth it to create an alias if you plan to use `fw` regularly. For example, in .bashrc, you can have:
```bash
alias fww="unset LD_LIBRARY_PATH;~/bin/glibc-2.34/lib/ld-linux-x86-64.so.2 ~/bin/fw"
```

