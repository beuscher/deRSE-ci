# A short Git primer

A more complete guide to Git can be fount here:

- [SoftwareCarpentry Git Intro](https://swcarpentry.github.io/git-novice/index.html)

## Installation

On Linux `git` should already be installed, on MacOs or Windows, refer to [git downloads](https://git-scm.com/downloads)

### Setting up the credentials

```sh
git config --global user.name "Maximilian Beuscher"
git config --global user.email "max@beuscher.dev"
```

### SSH key setup

```sh
cd ~/.ssh
```

```sh
ssh-keygen -t ed25519 -C "max@beuscher.dev"
```

When prompted for a file name just accept with `enter` to get the default naming, then `cat` the public key and copy it to the clipboard.

```sh
cat ~/.ssh/id_ed25519.pub
```

Go to [Account > Keys](https://github.com/settings/keys) and create a new SSH Key.

Check if ssh is configured correctly:

```sh
ssh -T git@github.com
```

### Adding a Remote

When cloning the repository from GitHub the remote should be already configured correctly, this can be verified with

```sh
git remote -v
```

if not, modify the following command with your user and repository:

```sh
git remote add origin git@github.com:beuscher/repo.git
```

git also allows to use https, requiring a slightly different "syntax" for the remote origin.

## Git Command Cheat Sheet

Add a file to the git repository:

```sh
git add *
```

Check the current status of the repository, it will list for example uncommitted changes

```sh
git status
```

Commit changes

```sh
git commit -m [commit message]
```

Push changes to remote

```sh
git push origin main
```

Pull changes fro remote

```sh
git pull origin main
```
