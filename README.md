# PROTECTSQL

# Table of Contents

- [PROTECTSQL](#protectsql)
- [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Installing the repository for contribution purposes](#installing-the-repository-for-contribution-purposes)
    - [Installing the package](#installing-the-package)
  - [Usage](#usage)
    - [Init command](#init-command)
    - [Analyze command](#analyze-command)
  - [Inspiration](#inspiration)
  - [What it does](#what-it-does)
  - [How we built it](#how-we-built-it)
  - [Tech Stack](#tech-stack)
  - [Screenshots](#screenshots)
  - [Challenges we ran into](#challenges-we-ran-into)
  - [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
  - [What's next for Protectsql](#whats-next-for-protectsql)
  - [Demo](#demo)
## Installation

### Installing the repository for contribution purposes
Please refer to [our CONTRIBUTING.md file](CONTRIBUTING.md) to setup protectsql locally

### Installing the package

Our package is publicly available on [PyPi](https://pypi.org/project/protectsql/).
To install using `pip`, run the command:

```bash
pip install protectsql
```

## Usage

### Init command

```bash
protectsql init # initialise the pysa configurations
```

### Analyze command
Runs the static analysis.

```bash
protectsql analyze # analyze your app
```

## Inspiration
We wanted to make a package to check for SQLi vulnerabilities for generic frameworks/specific to Flask as there are quite a few python applications that don't use ORM and are vulnerable to SQLi vulnerabilities.

## What it does
A CLI tool which will help you analyze your python/flask app, using [Pysa](https://github.com/facebook/pyre-check) (a static analysis tool by facebook), In case sqli are found, they're displayed at runtime after running the `analyze` command.

## How we built it
Protectsql is build on top of `pysa`, a part of the `pyre-check` project package (see more about `pysa` [here](https://pyre-check.org/docs/pysa-running)).
Additionally, since it's a CLI tool, we also make use of `click` (see more [here](https://click.palletsprojects.com/en/7.x/)).

## Tech Stack
- `python`
- `pysa`
- `click`
- `flask`

## Screenshots
![Step 1](screenshots/step-1.png)
![Step 2](screenshots/step-2.png)
![Step 3](screenshots/step-3.png)
![Step 4](screenshots/step-4.png)


## Challenges we ran into
- Understanding `pysa` documentation
- Coming up with target frameworks vulnerable to sqli injections and how can we use `pysa` for them

## Accomplishments that we're proud of
- Using `pysa` for static analysis
- Usage of `click`, the python CLI tool
- Uploading our own package to [PyPi](https://pypi.org/project/protectsql/)

## What's next for Protectsql
We plan to add support to more lightweight framework which does not rely on ORM!

As of now, Protectsql is published on [PyPi](https://pypi.org/project/protectsql/) and is ready for use. Anyone can contribute following our contribution [rules and guidelines](CONTRIBUTING.md).

## Demo
