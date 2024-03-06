# Hello CI

## Setup a git repository and add a remote

First we start on GitHub.com and create a new repository by selecting on the top right **New** > **Repository** and choose a suitable name. Next we select **SSH** instead of **HTTPS** and copy the address to the clipboard.

We then switch to our local command line and start by creating a new folder and `cd` into it:

```sh
mkdir first-ci
cd first-ci
```

then we locally initialize a new git repository, ensure we are on branch `main` and add the remote "origin":

```sh
git init
git checkout -b main
git remote add origin git@github.com:beuscher/repo.git
```

one can verify this by running

```sh
git remote -v
```

then we push our sample files to remote using

```sh
git push origin main
```

Now we can start setting up our first CI pipeline.

## A first workflow file

Work flows are defined using `.yml` files located in the  `.github/workflows/` directory, where each workflow is defined in its own file. Thus we create a new workflow `hello-ci` by creating a file named `hello-ci.yml`.

```sh
mkdir .github/workflows/
touch .github/workflows/hello-ci.yml
```

For each workflow some basic parameters are required, while `name` and `run-name` are technically optional (name would default to the file name of that action) they still should be set.
The `run-name` parameter specifies the name of a workflow run. When triggered by a pull or push event it will default to the commit message.
Here we will directly make use of a feature named Contexts, which allows us to access information about the repository, the current workflow run itself, the triggering event, etc. In this case we will use it to define the `run-name` in such a way that it will include who and which event triggered the run.

One of the most important key:value pairs to be set is the `on: []` which defines which events will triggers this workflow, which we will set to `push, pull_request`.
To allow for a manually triggered workflow the `workflow_dispatch` event must be set. It is also possible to define more complex events like the creation of an issue or to restrict the tigger conditions by depending on changes to a subdirectory, but this is out of scope for this tutorial.

The final top level key we need to set is `jobs:`. It groups all jobs of the workflow together. For our workflow to actually do something we will need to add a job.

```yml
{{#include .github/workflows/hello-ci.yml::4}}
```

## The Hello CI job

We start by creating our first job with the name `hello` and the job id `hello_job`.

```yml
{{#include .github/workflows/hello-ci.yml:5:6}}
```

Further jobs (dependent or independent of other) can be defined by adding further named keys under `jobs:`.
 
When then have to choose a runner for our job or in other words: We need to choose a platform and OS. In most cases this will be `ubuntu-latest`.

```yml
{{#include .github/workflows/hello-ci.yml:5:7}}
```

GitHub also provides default runners for windows and mac (`windows-latest` and `macos-latest`) but one should note here, that those are billed with a factor x2, x10 on minutes.
Further there is also the option of self hosted runners.

### Steps

Each job is split up in multiple steps. In each step one can directly specify a command to run or run a script. Each step can also have a name. For a lot of common tasks like to checkout/clone the repository into virtual machine GitHub provides default actions. In our case we specify `actions/checkout@v4` which will allow us to access the contents of this repository.
We also `ls` to check that the checkout worked as expected.

```yml
{{#include .github/workflows/hello-ci.yml:8:}}
```

these actions are essentially GitHub repositories containing robust scripts performing these tasks.

Now one could use `actionlint` to check for syntax errors.

## a first pipeline run

The contents of `hello_ci.yml` should now be something like:

```yml
{{#include .github/workflows/hello-ci.yml}}
```

Finally Sync with GitHub:

```sh
git add .github/workflows/hello-ci.yml
git commit -m "hello-ci.yml"
git push origin main
```

### view run on GitHub

In our repository (on [github.com](github.com)) when go check the Actions tab and select a workflow run to view details.
