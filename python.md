# Hello Python

Next we introduce some Python code into our workflow. First we will run `pylint` to check our code for possible syntax errors, then we run some python code to produce an output which we will save as an artifact.
As a test case i prepared a small python programm generating Mandelbrot Sets. It generates an ASCII version by default, printing to `stdout`, but also a higher resolution `.pdf` when `--pdf` is specified as an argument..

In many production cases one would run for example some sort of unit test or build a python package and deploy it to pip.

To get the sample python script run

```sh
curl -L https://derse-ci.beuscher.dev/mandelbrot.py -o mandelbrot.py
```

or [download](https://deRSE-ci.beuscher.dev/mandelbrot.py) it manually.

## Setup Python and pylint

Starting with a copy of the `hello-ci.yml` workflow, we choose suitable names the workflow(-run) and name the job `plot`

```yml
{{#include .github/workflows/python-ci.yml:1:10}}  
```

To setup our python environment we use an action provided by GitHub and specify a python version, in this case `3.10`

```yml
{{#include .github/workflows/python-ci.yml:11:14}}
```

To install the `numpy` and `matplotlib` dependency used by this programm as well as pylint we provide `pip` (the python package manager) with a `requirements.txt` file which will be located in the top level directory of our repository.
 
Our `requirements.txt`:

```txt
{{#include requirements.txt}}
```

In the workflow file we add the following two commands:

```yml
{{#include .github/workflows/python-ci.yml:15:18}}
```

Next, we run `pylint` on `mandelbrot.py` to check for syntax error and if it obeys code conventions.

```yml
{{#include .github/workflows/python-ci.yml:19:21}}
```

Note: Here we need the argument `--disable=import-outside-toplevel` since the `matplotlib` dependency is only imported when `--pdf` is specified.

When a syntax error is detected `pylint` will return an error and the job will be marked as *failed*.

Finally we execute the python program with the `--pdf` argument:

```yml
{{#include .github/workflows/python-ci.yml:22:24}}
```

## Save an Artifact

By default we do not retain any build artifacts or other files generated during our workflow run. When files should be made available outside a job one needs to upload an artifact explicitly. This Artifact is then available in another job to "download" or can be viewed and downloaded from GitHub. If no retention days are specified GitHub will use the account default (initially set to 30 Days)

```yml
{{#include .github/workflows/python-ci.yml:25:}}
```

The full action should now be similar to

```yml
{{#include .github/workflows/python-ci.yml}}
```

Again one could check the worklfow using `actionlint`.

## Commit and view the Artifacts

We again commit our changes to the remote repository.

After the run is finished we can access the generated artifacts when selecting a specific workflow run.
