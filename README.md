# Deploy workflow

Checkout to the branch where the source code of the webpage is located: main

Upload new changes as usual

Remove all the content of the `_site` directory:

```
$ rm -r _site/*
```

Clone your repo's gh-pages branch into the _site directory:
```
git clone -b gh-pages git@github.com:mtailanian/mtailanian.github.io.git _site
```

Final steps: Just let jekyll build, do commit & push:
```
$ jekyll build 
cd into _site:
$ cd _site,
```

target all files for commit:
```
$ git add -A
```

commit them:

```
git commit -am 'Yeah. Built from subdir'
```

and push your site to GitHub-Pages:

```
git push.
```


# Gradfolio


```bash
cd assets/photography
cp img/* thumb/
mogrify -resize 20% thumb/*
``` 

`jekyll serve --incremental --trace`



responsive, dark-mode ready Jekyll theme designed for use as a personal website and portfolio. [Here's a live demo](https://jitinnair1.github.io/gradfolio/)

## Features
- Responsive
- Respects Dark Mode preference set by user
- Projects Page to showcase your work/side projects
- Easily link to your profiles on ResearchGate and ORCID

## Installation
* Click on `Use this template`
* Your new site should be ready at https://username.github.io/gradfolio/
* You can now modify the contents and personalise the template

Alternatively, you can [download the source files](https://github.com/jitinnair1/gradfolio/archive/master.zip) and make changes locally. 

To test these changes, open a terminal inside the source folder and use `jekyll serve --incremental --trace` to make it available on a local server (typically http://localhost:4000/)

The `--incremental` flag ensures that any changes you make are reflected in your browser in real time and the `--trace` option might be useful for debugging if things break while you are changing the source files.

Once you have personalised and tested the site, you can create a new repo, upload these files and host your website from the repo.

## Based on
- [hagura](https://github.com/sharu725/hagura)
- [al-folio](https://github.com/alshedivat/al-folio)
- [noir](https://github.com/essentialenemy/noir)
- [jekyll-TeXt-theme](https://github.com/kitian616/jekyll-TeXt-theme)

## License
MIT License

[![JekyllThemes](https://img.shields.io/badge/featured%20on-JekyllThemes-red.svg)](https://jekyll-themes.com)
