.. _glossary:

Glossary
========

Quick overview of all terms used throughout MIDOM

Protocol
    Deidentification Protocol. A full, abstract description of a deidentification
    procedure. Describes what to do with each DICOM element, voxel data, private
    elements. Also describes which datasets to reject completely. It consists
    of four elements :ref:`tags`, :ref:`filter`, :ref:`pixel`, :ref:`Private`.

Deidentifier
    The concrete implementation of a protocol. Takes a DICOM dataset and then either
    aplies a transformation to it, or rejects it. Different deidentifiers can implement
    the same protocol.

.. _tag:

DICOM Tag
    The name for a single type of data in a DICOM dataset. Like ``Modality``, ``PatientAge``, etc.
    All 4000+ official dicom tags are listed `here <https://www.dicomlibrary.com/dicom/dicom-tags/>`_.

.. _dicom_element:

DICOM Element
    A tag - Value pair. Like ``PatientName: A_Smith``

.. _action:

Action
    An *intended* change to a single DICOM element. The change is expressed as an :ref:`Action code<action_codes>`.

.. _delta:

Delta
    An *observed* change to a single DICOM element. The change is expressed as a :ref:`change code<change_codes>`.

.. _delta_set:

Delta set
    A set of Deltas for a set of distinct DICOM elements.

.. _PII:

PII
    Personally Identifiable information. Also called `PI` (Personal Information) or `PHI`
    (Personal Health Information).

.. _pixel_data:

Pixel data
    A special :ref:`dicom_element` that contains the bytes for the image component
    of a DICOM dataset. This element often take up many times more data than all other
    elements combined. Its processing is done by the specialized :ref:`pixel module <pixel>`

Private tag
    DICOM private tags are custom data elements that aren't part of the standard
    specification, allowing healthcare organizations to store proprietary or specialized
    information. Private tags enhance flexibility, but are a well known PII leak risk.
    They are handled by the specialized :ref:`private module <private>`.
