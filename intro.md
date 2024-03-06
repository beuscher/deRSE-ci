# Getting up and running with your First CI/CD pipeline

[GitHub rpository](https://github.com/beuscher/deRSE-ci)

## Prerequisites:

- GitHub Account
- git
- local shell (preferably UNIX)
- text editor

## What is CI/CD and why should you use it

Continuous Integration/Deployment CI/CD refers to the automation of a large portion of human interaction usually necessary to propagate (small) code changes from the development stage into production. Using CI/CD pipelines can usually streamline the development and release usually also increasing productivity and reliability. This includes some of the following tasks:

- testing and validation
  - unit test
  - code validation and formatting
- building of
  - application
  - website
  - documentation
- deployment to
  - package repositories
  - infrastructure

### Continuous Integration

Continuous Integration is the practice of integrating source code changes frequently while utilizing automated testing and code validation to minimize code conflicts and help in the identification of error/bugs.

### Continuous Deployment/Delivery

Continuous Deployment/Delivery refers to the automated packaging (and building) of an application, website or project release - previously tested and validated by CI - with following deployment to infrastructure or repositories.

## CI/CD integration

There are several different choices for running CI/CD pipelines. While most are tied to a remote version control host some solutions are independent of those:

- Travis CI
- GitHub Actions
- GitLab CI/CD
- containerization using self developed scripts (docker, podman, ...)
- ...

### GitHub Actions

GitHub Actions is the CI/CD Pipeline system provided by GitHub. For this tutorial we choose GitHub Actions for several reasons:

- (Most) popular remote Git host
- Free Plan includes substantial amount of container minutes
- similar concepts compared to other implementations like GitLab CI

#### Spending Limits and Billing

Depending on the account type there is a free quota for GitHub Actions. Here minutes refer to the available processing time (in case of a Linux container) and Storage refers to the space available for storing "Artifacts".

| Account type | Storage   | Minutes    |
|--------------|-----------|------------|
| GitHub Free  | 500 MB    | 2000       |
| GitHub Pro   | 1 GB      | 3000       |

More details can be found under [Billing of GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).

You can view the current usage in **Settings** > **Billing and plans** > **Plans and usage** then under "Usage this Month" > "Actions".

#### YAML Syntax

GitHub Actions are written in [YAML](https://yaml.org/spec/1.2.2/). It is a dataserialization language commonly used for configuration files. It uses python style indentation to indicate nesting of data. 

- `Key: value` pairs use intendation and newlines or are encapsuled by curly braces `{key1: 1, key2: 2}`
- Items in a list are prependen with `-` or can be inlined enclosed by `[Item1 ,Item2 ]`.
- Strings do not **need** to be encapsuled by `" "`.
- Multiline strings preserving the newline (usefull eg for chaining multiple commands) can be written using `|`:
  ```yml
    commands: |
      echo "Hello,"
      echo "Wold"
  ```

Example from the official website:

```yml
YAML Resources:
  YAML Specifications:
  - YAML 1.2:
    - Revision 1.2.2      # Oct 1, 2021 *New*
    - Revision 1.2.1      # Oct 1, 2009
    - Revision 1.2.0      # Jul 21, 2009
  - YAML 1.1
  - YAML 1.0
```
