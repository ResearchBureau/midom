.. _glossary:

Glossary
========

Quick overview of all terms used throughout MIDOM

Protocol
........
    Deidentification Protocol. A full, abstract description of a deidentification
    procedure. Describes what to do with each :ref:`dicom_element`, voxel data, private
    elements. Also describes which datasets to reject completely. It consists
    of four elements :ref:`tags`, :ref:`filters`, :ref:`pixel`, :ref:`Private`.
    See :ref:`the objects page <objects_protocol>` as well.

Deidentifier
............
    The concrete implementation of a :ref:`objects_protocol`. Takes a :ref:`dataset` and then either
    aplies a transformation to it, or rejects it. Different deidentifiers can implement
    the same protocol.

.. _tag:

DICOM Tag
.........
    The name for a single type of data in a :ref:`dataset`. Like ``Modality``, ``PatientAge``, etc.
    All `4000+ official dicom tags are listed here <https://www.dicomlibrary.com/dicom/dicom-tags/>`_.
    There are also :ref:`private tags <private_tag>` which can be created by any DICOM producer.

    Each dicom tag has an associated :ref:`value_representation`.


.. _value_representation:

Value Representation (VR)
.........................
The 'data type' of a :ref:`DICOM element's<dicom_element>` value. For example an int,
a string, a date. Also contains more exotic datatypes like 'Unlimited Text'. All DICOM
VR's are `listed in the DICOM standard <https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html>`_


.. _dicom_element:

DICOM Element
.............
    A :ref:`tag` - Value pair. Like ``PatientName: A_Smith``

.. _dataset:

DICOM Dataset
.............
    A set of :ref:`DICOM elements <dicom_element>`. For extended description, see :ref:`the objects page <objects_dataset>`

.. _imagedata_element:

ImageData element
.................

    A :ref:`dicom_element` that contains image data. In most DICOM files this element is
    several times bigger than all other elements combined. The most common image data element
    is ``PixelData``

    .. code-block:: text

        (7FE0,0010) PixelData

    But there are several others:

    .. code-block:: text

        (7FE0,0008) FloatPixelData
        (7FE0,0009) DoubleFloatPixelData
        (0070,0022) GraphicData
        (5400,0110) WaveformData

    This list might not be complete. The criteria for what constitutes 'image data' are not
    completely set.

    ImageData elements can contain two types of :ref:`PHI`:
    :ref:`burnt_in_phi` and :ref:`dynamc_image_phi`


.. _burnt_in_phi:

Burnt-in image PHI
..................

    Burnt-in / Static image PHI is always in the same place in an image. Many DICOM-producing
    modalities, especially in Ultrasound, write PHI like patient name and date of birth into
    the image. For a specific vendor, model and dataset type, this information can always
    be found at the same X-Y coordinates.

.. _dynamc_image_phi:

Dynamic image PHI
.................

    Dynamic image PHI has no pre-determined place. It is not added to the image on purpose.
    Faces and implant serial numbers fall into this category.



.. _action:

Action
......
    An intended change to a single :ref:`dicom_element`. The change is expressed as an :ref:`Action code<action_codes>`.

.. _delta:

Delta
.....
    An observed change to a single :ref:`dicom_element`. The change is expressed as a :ref:`delta code<spaces_delta_codes>`.

.. _delta_set:

Delta set
.........
    A set of Deltas for a set of distinct :ref:`DICOM elements <dicom_element>`. See the :ref:`objects page<objects_deltaset>`.

.. _PHI:

PHI
...
    Personal Health Information. Also called **PII** *(Personally Identifiable information)* or **`PI`** *(Personal Information)*.
    MIDOM prefers the term PHI as this is more specifically `defined in the health domain <https://www.hipaajournal.com/phi-vs-pii/>`_.

    For medical imaging data, personal health information is found in many of the standard :ref:`DICOM elements <dicom_element>`.
    Obvious ones are patient name and date of birth. Next to that there are many more.
    The `DICOM standard lists more than 400 elements <https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1>`_
    for which some kind of processing is required to deidentify.

    In addition to elements, PHI can also be present in image data directly as
    :ref:`burnt_in_phi` or :ref:`dynamc_image_phi`


.. _pixel_data:

Pixel data
..........
    A special :ref:`dicom_element` that contains the bytes for the image component
    of a DICOM dataset. This element often take up many times more data than all other
    elements combined. Its processing is done by the specialized :ref:`pixel module <pixel>`


.. _private_tag:

Private tag
...........
    DICOM private tags are custom data elements that aren't part of the standard
    specification, allowing healthcare organizations to store proprietary or specialized
    information. Private tags enhance flexibility, but are a well known PII leak risk.
    They are handled by the specialized :ref:`private module <private>`.

    More information on private tag structure can be found in the `DICOM standard <https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_7.8.html>`_
    (very tough read), or in the `pydicom docs <https://pydicom.github.io/pydicom/stable/guides/user/private_data_elements.html>`_ (more understandable).