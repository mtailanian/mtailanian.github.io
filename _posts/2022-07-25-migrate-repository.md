---
layout: post
title: Migrate repository origin
---

# Migrate repository origin

Sometimes you need to move your existing git repository to a new remote repository (/new remote origin).

Here are a simple and quick steps that does exactly this.

Let's assume we call `old repo` the repository you wish to move, and `new repo` the one you wish to move to.

## Step 1. 

Make sure you have a local copy of all `old repo` branches and tags.

### Fetch all of the remote branches and tags

```bash
git fetch origin
```

### Make a local copy of all remote brances

View all `old repo` local and remote branches

```bash
git branch -a
```

If some of the remotes/ branches doesn't have a local copy, checkout to create a local copy of the missing ones:

```bash
git checkout -b <branch> origin/<branch>
```

Now we have to have all remote branches locally.


## Step 2. Add a `new repo` as a new remote origin:

```bash
git remote add new-origin git@github.com:user/repo.git
```

## Step 3. Push all local branches and tags to a `new repo`.

### Push all local branches (note we're pushing to new-origin):

```bash
git push --all new-origin
```

### Push all tags:

```bash
git push --tags new-origin
```

## Step 4. Remove `old repo` origin and its dependencies.

### View existing remotes (you'll see 2 remotes for both fetch and push)

```bash
git remote -v
```

### Remove `old repo` remote

```bash
git remote rm origin
```

### Rename `new repo` remote into just `origin`

```bash
git remote rename new-origin origin
```


Done! Now your local git repo is connected to "new repo" remote which has all the branches, tags and commits history.


[Taken from here](https://gist.github.com/niksumeiko/8972566?permalink_comment_id=3037855)