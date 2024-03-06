# Running containers in an Action

There is the possibility that a lot of environments needed cannot or only be created in a time consuming manner in one of the provided runners. While one possibility is to use a selfhosted runner a far more straight forward solution could be to use containerization. Containers can provide an easy way to setup consistent environments and there is already a long list of pre build containers available (eg. on [docker.hub](https://docker.hub).

It is also possitble to use a `dockerfile` to define a custom container environment, but in most cases it is sufficient to use a prebuild one.

## Practical Example: A LaTeX Container 

In this example we will use the `texlive/texlive:latest` container to compile a simple latex document.  

The sample document can be downloaded through

```sh
curl -L https://derse-ci.beuscher.dev/main.tex -o main.tex
```

Continuing our previous examples, we create a new job `texlive:`. 

GitHub provides already a straight forward way of creating a docker environment on the `ubuntu-latest` image by adding a `container` key and specify the container.

```yml
{{#include .github/workflows/container-ci.yml:32:39}}
```

After checking out the repository we need to download the previously saved artifact using an action provided by GitHub>

```yml
{{#include .github/workflows/container-ci.yml:40:44}}
```

Finally we invoke `latexmk`, starting the compilation and create an Artifact for the `main.pdf`:

```yml
{{#include .github/workflows/container-ci.yml:45:47}}
```

The container part of the final workflow should be similar to:

```yml
{{#include .github/workflows/container-ci.yml:48:}}
```

Note that since the - in terms of file size - large container needs to be downloaded from [docker.hub](https://docker.hub) this workflow will run for some time.
