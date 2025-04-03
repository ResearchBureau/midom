.. _glossary:

Glossary
========

Quick overview of all terms used throughout MIDOM

protocol
........
    Deidentification Protocol. A full, abstract description of a deidentification
    procedure. Describes what to do with each :ref:`dicom_element`, voxel data, private
    elements. Also describes which datasets to reject completely. It consists
    of four elements :ref:`tags`, :ref:`filter`, :ref:`pixel`, :ref:`Private`.
    See :ref:`the objects page <objects_protocol>` as well.

deidentifier
............
    The concrete implementation of a :ref:`objects_protocol`. Takes a :ref:`dataset` and then either
    aplies a transformation to it, or rejects it. Different deidentifiers can implement
    the same protocol.

.. _tag:

DICOM Tag
.........
    The name for a single type of data in a :ref:`dataset`. Like ``Modality``, ``PatientAge``, etc.
    All `4000+ official dicom tags are listed here <https://www.dicomlibrary.com/dicom/dicom-tags/>`_.

.. _dicom_element:

DICOM Element
.............
    A tag - Value pair. Like ``PatientName: A_Smith``

.. _dataset:

DICOM Dataset
.............
    A set of :ref:`DICOM elements <dicom_element>`. For extended description, see :ref:`the objects page <objects_dataset>`

.. _action:

action
......
    An intended change to a single :ref:`dicom_element`. The change is expressed as an :ref:`Action code<action_codes>`.

.. _delta:

delta
.....
    An observed change to a single :ref:`dicom_element`. The change is expressed as a :ref:`delta code<spaces_delta_codes>`.

.. _delta_set:

delta set
........
    A set of Deltas for a set of distinct :ref:`DICOM elements <dicom_element>`. See the :ref:`objects page<objects_deltaset>`.

.. _PHI:

PHI
...
    Personal Health Information. Also called **PII** *(Personally Identifiable information)* or **`PI`** *(Personal Information)*.
    MIDOM prefers the term PHI as this is more specifically `defined in the health domain <https://www.hipaajournal.com/phi-vs-pii/>`_.

.. _pixel_data:

pixel data
..........
    A special :ref:`dicom_element` that contains the bytes for the image component
    of a DICOM dataset. This element often take up many times more data than all other
    elements combined. Its processing is done by the specialized :ref:`pixel module <pixel>`

private tag
...........
    DICOM private tags are custom data elements that aren't part of the standard
    specification, allowing healthcare organizations to store proprietary or specialized
    information. Private tags enhance flexibility, but are a well known PII leak risk.
    They are handled by the specialized :ref:`private module <private>`.