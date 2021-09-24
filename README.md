# PROTECTSQL

# Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Inspiration](#inspiration)
- [What it does](#what-it-does)
- [How we built it](#how-we-built-it)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Challenges we ran into](#challenges-we-ran-into)
- [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
- [What's next for Protectsql](#whats-next-for-envprotecc)
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
     protectsql init 
```

### Analyze command
Runs the static analysis.

```bash
     protectsql analyze
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


## Challenges we ran into
- Understanding `pysa` documentation
- Coming up with target frameworks vulnerable to sqli injections and how can we use `pysa` for them

## What we learned
- Using `pysa` for static analysis
- Usage of `click`, the python CLI tool

## What's next for Protectsql
Protectsql is published on [PyPi](https://pypi.org/project/protectsql/) and is ready for use. Anyone can contribute following our contribution [rules and guidelines](CONTRIBUTING.md).

## Demo
