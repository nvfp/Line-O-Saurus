# Lineosaurus🦕

(under development)

[![Run tests](https://github.com/nvfp/Line-O-Saurus/actions/workflows/run-tests.yml/badge.svg)](https://github.com/nvfp/Line-O-Saurus/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/github/license/nvfp/Line-O-Saurus)](https://github.com/nvfp/Line-O-Saurus/blob/main/LICENSE)

![lineosaurus](https://github.com/nvfp/Line-O-Saurus/blob/main/assets/lineosaurus_h200.jpg?raw=true)



## Usage

Copy this file `.github/workflows/lineosaurus.yml` to your repository.

```yaml
name: Lineosaurus

on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily
  workflow_dispatch:  # Update manually via 'Actions' tab

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # For committing
    steps:
      - uses: nvfp/Line-O-Saurus@v1
        with:
          git-name: your name
          git-email: your@email
          only-type: null
          ignore-type: null
          header: null
          footer: null
          custom-title: |-
            ### ~ Updated on _DATE_ ~

            ### _LINE_ lines of code stretch through _OWNER_'s repositories.
          num-shown: 3
          show-approx: true
          card-titles: |
            - line: #### Lines of code
            - type: #### Languages
            - star: #### Stargazers
            - stat: #### _OWNER_'s statistics
          card-order: |
            - line
            - type
            - star
            - stat
          prefer-extension: true
          show-credit: false
        env:
          GH_TOKEN: ${{ github.token }}  # For GitHub CLI
```

> Note: both `git-name` and `git-email` must be specified for committing the update.

### Options

option             | description | default
---                | ---         | ---
`only-type`        | foo | `null`
`ignore-type`      | ignored if only-type is specified | 
`header`           | header file (relative to repo root) | 
`footer`           | footer file (relative to repo root) | 
`custom-title`     | you can use `_OWNER_`,  | 
`num-shown`        | number of  | 
`show-approx`      | `13K` instead of `13,241` | 
`card-titles`      |  | 
`card-order`       |  | 
`prefer-extension` | `.py` over `Python` | 
`show-credit`      | show the credit at the end of the file | 

### Variables

variable | description
---      | ---
`_OWNER_` | your GitHub username
`_DATE_` | todays date in format 'Jan 1, 2023'
`_LINES_` | total lines (regardless only-type/ignore-type)
`_LINE_` | total lines (excluding only-type/ignore-type)
`_NUM_PUB_REPOS_` | number of public repo
`_NUM_STARS_` | total stargazers

### Variations

```yml
with:
  git-name: your name
  git-email: your@email
  only-type: '[".txt", ".md", ".json"]'  # don't forget to use double instead of single quotes for JSON list
  ignore-type: |
    - .py
    - .md
  header: assets/header.md
  custom-title: "_LINE_ lines of code stretch through _OWNER_'s repositories - last update: _DATE_."
  show-approx: true
  card-titles: '{"line": "foo", "star": "bar"}'
  card-order: '["line", "star"]'
```

```yml
with:
  git-name: your name
  git-email: your@email
  only-type: '[".txt", ".md", ".json"]'  # don't forget to use double instead of single quotes for JSON list
  ignore-type: |
    - .py
    - .md
  header: assets/header.md
  custom-title: "_LINE_ lines of code stretch through _OWNER_'s repositories - last update: _DATE_."
  show-approx: true
  card-titles: |
    - type: #### Top languages
    - stat: #### _OWNER_'s statistics
    - line: #### Lines of code
    - size: #### Repo sizes
    - char: #### Number of characters
    - star: #### Stargazers
    - cmit: #### Total commits
    - file: #### Total files
  card-order: |
    type
    stat
    line
    size
    char
    star
    cmit
    file
```


## License

The scripts and documentation in this project are released under the [MIT License](https://github.com/nvfp/Line-O-Saurus/blob/main/LICENSE)