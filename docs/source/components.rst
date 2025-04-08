.. _components:

Components
==========
The four constituent parts of a :ref:`Protocol`, and by extension of any :ref:`deidentifier`.
These parts together define the complete handling of any incoming :ref:`dataset`.

<add image of parts here>

.. _tags:

Tags
----
Tags Processing. Processes all :ref:`DICOM elements <dicom_element>` in a :ref:`dataset`
except for PixelData and Private tags (see 'excluded elements' below). Tags has a
different form for protocols and deidentifiers:

    * For :ref:`protocols <objects_protocol>`, tags defines what *should be done* with each
      :ref:`tag`. The language for this is :ref:`action_codes`. Per tag, a protocol
      defines whether to ``clean``, ``remove``, ``keep`` etc. each value.


    * For :ref:`deidentifiers <objects_deidentifier>`, tags defines *what is actually done*
      to each tag. For each tag, a deidentifier implements a procedure that maps to one
      of the :ref:`action codes <action_codes>`. For example, an operation ``clean``
      might be implemented as writing a dummy value, or obtaining a pseudonym from a
      secure source, or writing an aggregated value.


Excluded elements
.................

Two types of DICOM elements are specifically excluded from tags prococessing:

    1. :ref:`Image data elements <imagedata_element>` are excluded, as
       their structure requires specialized treatment. They have their own dedicated
       component :ref:`pixel`.

    2. Similarly, all :ref:`private tags <private_tag>` are excluded from tags
       processing and handled in :ref:`private`.


Syntax
......

How to define tags processing

    For :ref:`protocols <objects_protocol>`, tags is easily defined by a list
    of :ref:`tag <tag>` -> :ref:`action code<action_codes>`.


    For :ref:`deidentifiers <objects_deidentifier>`, the definition is more involved.
    It should be a list of :ref:`tag <tag>` -> Implemented function with an additional
    mapping and explanation of how each implemented function maps to an
    :ref:`action code<action_codes>`.


.. _filter:

Filter
------
Checks any dataset and either accepts it for further processing or rejects it.
Common reasons for rejection are unknown DICOM with burnt in information, non-conformant
DICOM, unknown SOPClass.

Filter can be applied at multiple times in a deidentification process. Particularly,
it can reject outright from the start, but can also be called after :ref:`pixel` is
called, as Pixel can change an

The Filter component is solely responsible for rejecting datasets. Not other component
can do this.

Syntax
......
A filter is defined in the form of a `boolean <https://en.wikipedia.org/wiki/Boolean_function>`_ or
`propositional <https://en.wikipedia.org/wiki/Boolean_function>`_ truth function. For example:

.. code-block:: text

        <Modality == "MR"> and <Manufacturer contains "Company A"> -> Reject


*   Relationships between propositions are purely standard logical connectives
    ``and`` ``or`` ``not`` and parenthesis ``( )`` for grouping.

*   Each proposition in the formula is a boolean function over a :ref:`tag <tag>` value.
    The test performed inside a preposition can be of any form, as long as the outcome is
    boolean (yes/no).
*   The outcome the formula is always ``Reject yes/no``

For a :ref:`deidentifier <objects_deidentifier>`, Filter will be implemented to be
actually runnable. For a :ref:`protocol <objects_protocol>`, Filter can be written
down in any formal language that implements boolean logic.


.. _pixel:

Pixel
-----

Processes all :ref:`Image data elements <imagedata_element>`. So that :ref:`PHI` is removed from
the images. This includes burnt-in text, implant serial numbers and faces.

The tag `PatientIdentityRemoved <https://dicom.innolitics.com/ciods/parametric-map/patient/00120062>`_ can be
set by :ref:`pixel` and not touched by :ref:`tags` processing.

Burnt-in vs Dynamic
...................

.. _burnt_in_info:

**Burnt-in / Static information** is always in the same place in an image. Many DICOM-producing
modalities, especially in Ultrasound, write PHI like patient name and date of birth into
the image. For a specific vendor, model and dataset type, this information can always
be found at the same X-Y coordinates.

.. _
**Dynamic image PHI** has no pre-determined place. It is not added to the image on purpose.
Faces and implant serial numbers fall into this category.


Syntax
......


The means by which :ref:`PHI` is removed from image data is out of scope for MIDOM. A
common approach is to

:ref:`deidentifier <objects_deidentifier>`, Filter will be implemented to be
actually runnable. For a :ref:`protocol <objects_protocol>`




.. _private:
Private
-------

Syntax
......
