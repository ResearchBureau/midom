# MIDOM - Medical Image Deidentification Object Model

A set of concepts and relations to describe the process of DICOM deidentification


## Why?
For projects related to DICOM deidentification, I'm running into the problem of not 
having the right words. I keep inventing terms, coming up with long-winded descriptions
There is a lack of conceptual clarity. Lack of clarity causes:
* misunderstandings
* Ineffective communication
* misguided programming efforts
* wasted time generally.

The DICOM standard does not have enough detail. 
[DICOM PS3 E-E1](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#sect_E.1)  gives 
thorough information on _what_ to do to a single dataset, but not on how to reason or
talk about multiple deidentifying processess, their differences, their characteristics.

## For whom?
People developing or maintaining image deidentification pipelines. 
Niche, but existent nonetheless.

## What is it?
An information model first and foremost. Concept definitions with clear descriptions of
their relations.
There might be python code to define constants, transformations between objects maybe.

## What is it not?
Anything that does any actual image processing. No loading of DICOM files anywhere.

## Building locally
`make docs_html`