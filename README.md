# MIDOM - Medical Image Deidentification Object Model

[![CI](https://github.com/ResearchBureau/midom/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/ResearchBureau/midom/actions/workflows/build.yml?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/midom)](https://pypi.org/project/midom/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/midom)](https://pypi.org/project/midom)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

A set of concepts and relations to describe the process of DICOM deidentification
and a structured format for a deidentification protocol.


## Why?
To use with projects related to DICOM deidentification. I'm running into the problem of not 
having the right words. I keep inventing terms, coming up with long-winded descriptions.
There is a lack of conceptual clarity. Lack of clarity causes:
* misunderstandings
* Ineffective communication
* misguided programming efforts
* wasted time generally.

The DICOM standard is not sufficient. 
[DICOM PS3 E-E1](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#sect_E.1)  gives 
thorough information on _what_ to do to a single dataset, but not on how to reason or
talk about multiple deidentifying processess, their differences, their characteristics.

## For whom?
People developing or maintaining image deidentification software. Either full pipelines 
or separate parts.

## What is it?
An information model first and foremost. Concept definitions with clear descriptions of
their relations. To clearly express these, a structured language is required. Python 
has been chosen for this, but it should be possible to express MIDOM concepts in 
any structured language.

## What is it not?
* No image processing. Anything that does any actual image processing. No loading of DICOM files anywhere.
* Not married to python. MIDOM uses pydantic for clean, serializable object definitions, pydicom for clean dicom file access and dicomcriterion to encode boolean expressions for DICOM datasets. Beyond that I will try to keep the dependencies to a minimum. This is the ambition. Time will tell whether this is realistic.


## For docs editors
### Render html docs
Go to 
(in docs/build): `make docs_html`

### Fancy auto-updating 
Auto-reload a html view as you change the docs source.
Requirements:
* Linux or WSL (this uses some subshell and piping tricks)
* [entr](https://github.com/eradman/entr) - Run a command when files change. Apt install this
* [livereload](https://livereload.readthedocs.io/en/latest/index.html) - Serve local files and auto-reload on change. Python lib found as dev dependency in midom.
* Possibly firefox to make livereload work properly

Steps:
* Start a shell in this midom base dir (where Makefile is) 
* run `uv run make launch_source_listener`
* Open the livereload url printed in the script output. By default this is http://127.0.0.1:35729/

You might have to reload the page once to link livereload to the browser. After that, any
save to a `.rst` or `.puml` file will trigger rebuild of docs/build, which will in turn
trigger a page reload