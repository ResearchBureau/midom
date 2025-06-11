.. _documentation:

Documentation
=============
How to write down a :ref:`objects_protocol` so that it can be shared and versioned.


Protocol definition
-------------------
A protocol definition defines each of the four parts of a
:ref:`protocol<objects_protocol>`:


+-------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Part                          | Syntax                                                                                          | Example                                       |
+===============================+=================================================================================================+===============================================+
| :ref:`Tags`                   | :ref:`tag <tag>` -> :ref:`action code<action_codes>` list                                       | *PatientID -> REMOVE*                         |
+-------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+
| :ref:`Filters`                | Boolean functions (:ref:`more info <filters_syntax>`)                                           | *<Modality == 'US'> -> Reject*                |
+-------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+
| :ref:`Pixel`                  | Boolean functions + pixel location (:ref:`more info <pixel_syntax_burnt_in>`)                   | *<Manufacturer == 'A'> -> [0,0,100,500]*      |
+-------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+
| :ref:`private`                | List of safe private tags (:ref:`more info <safe_private_syntax>`)                              | *0013,["Company_A"]01*                        |
+-------------------------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------+



Write a `protocol definition`.

Should contain:
* name

* version

* tags

* Filter

* Pixel

* Private

Anything else?

Which syntax? -> Does not matter much, can be multiple. As long as there is a reader
to a uniform syntax.

That uniform syntax is probably python (define in midom). Then there can be different
ways to serialize this

A protocol document will have a persisted version of the protocol definition plus
reasoning, explanation etc. whatever you want.


```
some code?

```