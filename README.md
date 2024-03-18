# Lisys Recognizes

This repository contains code for the Lisys Recognizes project, a facial recognition system developed by LisysTL.

## Setup

Follow these steps to set up the Lisys Recognizes project:

```bash
# Create a New Anaconda Environment
conda create -n lisys-env python=3.7

# Activate the Anaconda Environment
conda activate lisys-env

# Install Dependencies
conda install -c conda-forge dlib

# Install Python Dependencies
pip install -r requirements.txt

```
## GitHub Setup 🚀

### Clone the Repository
Follow these steps to set up your local environment for collaborating on Lisys Recognizes:

#### Github Steps

```bash
git clone -b dev https://github.com/LisysTL/lisys-recognizes.git
```

Make Your Own Respective Branches
Create your own respective branches to work on:

```bash
git checkout -b yourname-branch
```

For example:
```bash
git checkout -b divesh-branch

```
Always Push on This Below Branch
Follow these steps to ensure smooth collaboration:

1. Switch to your branch:
```bash
git checkout yourname-branch

```

2. Add your changes:

```bash
git add .

```
3. Commit your changes with a descriptive comment:
```bash
git commit -m "Your commit comment"

```
4. Switch back to the dev branch:

```bash
git checkout dev

```
5. Merge your branch into dev:

```bash
git merge yourname-branch

```
6. Push your changes to the dev branch on the remote repository:

```bash
git push -u origin dev
```

## Useful Git Commands : 
Always work on your branch.

```bash
git checkout yourname-branch
```
Merge your branch with the dev branch.

```bash
git merge yourname-branch
```
git pull origin dev: Pull changes from the dev branch when others have made changes.
```bash
git pull origin dev
```
