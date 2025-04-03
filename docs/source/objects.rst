.. _objects:

Objects
=======

Objects at different levels of deidentifying a DICOM dataset. Deidentification comes down to
changing the right parts of a :ref:`DICOM dataset <objects_dataset>`. The change to each :ref:`DICOM element <dicom_element>`
in a single :ref:`dataset <objects_dataset>` can be characterized as a :ref:`delta set <objects_deltaset>`.
A DeltaSet is applied by a :ref:`deidentifier <objects_deidentifier>`. A deidentifier is a
concrete implementation of a :ref:`Protocol <objects_protocol>`.

.. uml:: diagrams/system_context.puml
   :caption: Deidentification objects from abstract (top) to concrete (bottom)

.. _objects_dataset:

Dataset
-------

A standardized container that stores a medical image along with associated metadata.
Each dataset contains both pixel data (the actual medical image) and a comprehensive set
of information tags that describe patient details, acquisition parameters, and clinical
context. Each element in a dataset consists of a tag, tag description and value.
For example:

+------------------+-------------------------------+-----------------------+
| Tag              | Description                   | Example Value         |
+==================+===============================+=======================+
| (0010,0010)      | Patient's Name                | SMITH^JOHN            |
+------------------+-------------------------------+-----------------------+
| (0010,0020)      | Patient ID                    | MRN12345678           |
+------------------+-------------------------------+-----------------------+
| (0010,0030)      | Patient's Birth Date          | 19700101              |
+------------------+-------------------------------+-----------------------+
| (0008,0020)      | Study Date                    | 20240315              |
+------------------+-------------------------------+-----------------------+
| (0008,0060)      | Modality                      | MR                    |
+------------------+-------------------------------+-----------------------+
| (0008,0070)      | Manufacturer                  | Medical systems LTD   |
+------------------+-------------------------------+-----------------------+
| (0008,0090)      | Referring Physician's Name    | JONES^SARAH^M.D.      |
+------------------+-------------------------------+-----------------------+
| (0020,000D)      | Study Instance UID            | 1.2.840.10008.1.2.3.4 |
+------------------+-------------------------------+-----------------------+

DICOM datasets can be stored as files, in databases or in memory.


.. _objects_deltaset:

Deltaset
--------
A set of observed changes to dataset elements. See :ref:`the Spaces and Codes page <spaces_delta_codes>` for a full description

Like this:

+---------------------------+-----------------+-----------------+-------------+
| Tag Name                  | Value Before    | Value After     | Delta       |
+===========================+=================+=================+=============+
| PatientName               | SMITH^JOHN      | Patient01       | CHANGED     |
+---------------------------+-----------------+-----------------+-------------+
| Modality                  | CT              | CT              | UNCHANGED   |
+---------------------------+-----------------+-----------------+-------------+
| Study Date                | 20240315        | <tag not found> | REMOVED     |
+---------------------------+-----------------+-----------------+-------------+
| Manufacturer              | Company A       | <empty>         | EMPTIED     |
+---------------------------+-----------------+-----------------+-------------+
| De-identification Method  | <tag not found> | deidentifier B  | CREATED     |
+---------------------------+-----------------+-----------------+-------------+


.. _objects_deidentifier:

Deidentifier
------------
A piece of software that takes a :ref:`dataset` and removes :ref:`PHI` from it. It does this
via four :ref:`components`: :ref:`filter`, :ref:`tags`, :ref:`pixel` and :ref:`private`.

A deidentifier can only do one of two things with an incoming dataset:

    1. It rejects the dataset trough triggering one of the :ref:`filters <filter>`
    2. It applies a transformation to the dataset. The transformation is defined in the
       :ref:`tags`, :ref:`pixel` and :ref:`private` components. The observed changes
       in the tags form a :ref:`objects_deltaset`

A deidentifier implements a :ref:`deidentification protocol <objects_protocol>`. Multiple
deidentifiers can implement the same protocol.

Contrary to a :ref:`Protocol`, a deidentifier is a concrete implementation. meaning it
will have to actually implement a protocol's abstract :ref:`action_codes`. For action
codes like ``REMOVE`` this is trivial, just remove the dicom element. But for ``CLEAN``
many different operations might be said to implement 'cleaning'. It is up to the creators
of a deidentifier to defend the choice for an implementation in a given context.


.. _objects_protocol:

Protocol
--------
Defines what to do with an incoming dataset using four :ref:`components`:
:ref:`filter`, :ref:`tags`, :ref:`pixel` and :ref:`private`.

The main difference with a :ref:`deidentifier` is


