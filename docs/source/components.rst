.. _components:

Components
==========
The four constituent parts of a :ref:`Protocol <objects_protocol>`, and by extension of any :ref:`Deidentifier <objects_deidentifier>`.

.. uml:: diagrams/components.puml

:ref:`tags`, :ref:`filters`, :ref:`pixel` and :ref:`private` together define the complete
handling of any incoming :ref:`dataset`.

.. _tags:

Tags
----

.. uml:: diagrams/components_tags.puml

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


.. _filters:

Filters
-------

.. uml:: diagrams/components_filters.puml

Checks any dataset and either accepts it for further processing or rejects it.
Common reasons for rejection are unknown DICOM with :ref:`burnt in information <burnt_in_phi>`,
non-conformant DICOM or unknown `SOPClass <https://www.dicomlibrary.com/dicom/sop/>`_.

Filters can be applied at multiple times in a deidentification process. Particularly,
it can reject outright from the start, but can also be called after :ref:`pixel` is
called, as Pixel can change the tag 'PatientIdentityRemoved' which is a potential input
to Filters.

The Filters component is solely responsible for rejecting datasets. Not other component
can do this.

.. _filters_syntax:

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

For a :ref:`deidentifier <objects_deidentifier>`, Filters will be implemented to be
actually runnable. For a :ref:`protocol <objects_protocol>`, Filters can be written
down in any formal language that implements boolean logic.


.. _pixel:

Pixel
-----

.. uml:: diagrams/components_pixel.puml

Processes all :ref:`Image data elements <imagedata_element>`. So that :ref:`PHI` is removed from
the images. This includes burnt-in text, implant serial numbers and faces.

The tag `PatientIdentityRemoved <https://dicom.innolitics.com/ciods/parametric-map/patient/00120062>`_ can be
set by :ref:`pixel` and not touched by :ref:`tags` processing.


Syntax
......
The :ref:`protocol <objects_protocol>` Pixel processing definition differs for the two types
of pixel-based PHI :ref:`burnt_in_phi` and :ref:`dynamc_image_phi`.

.. _pixel_syntax_burnt_in:

For burnt in PHI
^^^^^^^^^^^^^^^^

For :ref:`burnt_in_phi`, pixel is processing is defined like a `boolean <https://en.wikipedia.org/wiki/Boolean_function>`_
function using only the tags from the :ref:`image_typ_id_subspace` followed by one or more square pixel regions to black out.
For example:

.. code-block:: text

        <Modality == "MR"> and <Manufacturer contains "Company A"> ->
        [0,0,512,30], [0,400,512,30]

The format for a black-out region is ``[top, left, size-x, size-y]`` where ``top``
and ``left`` are the pixel coordinates of the top left of the region, counting from
the top left of the image (top left of the image = (0,0)), and ``size-x`` and ``size-y``
are the size of the box in pixels.

.. note::

    In the future, pixel data processing will probably move to OCR-type techniques where
    text is recognized in any image regardless of its 'type'. This will make the
    currently described approach unneeded. Any list of type -> black out region can then
    still be useful for testing purposes.


For dynamic image PHI
^^^^^^^^^^^^^^^^^^^^^
For :ref:`dynamc_image_phi`, there is no set method or syntax. A
:ref:`protocol <objects_protocol>` should document whether any dynamic image PHI should
be removed. This should be a human-readable description. There is no set format for this.

For a :ref:`deidentifier <objects_deidentifier>` the description should include a
description of the methods used, if any. The evidence should make it


.. _private:

Private
-------

.. uml:: diagrams/components_private.puml

:ref:`private_tag` handling is boils down to maintaining a list of 'safe private' tags.
The DICOM standard allows indicating whether a deidentification method retains safe private
tags (option *'Rtn. Safe Priv. Opt'* in `table E.1-1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1>`_).
The standard does *not* define which private tags are considered safe. Several
lists are maintained by several organizations.

.. _safe_private_syntax:

Syntax
......
If a :ref:`protocol <objects_protocol>` retains safe private tags, these are defined as
a list of private tags deemed safe. For example:

.. code-block:: text

    0013,["Company_A"]01
    0013,["Company_A"]02

    0075,["Company_B"]01
    0075,["Company_B"]0e
    0075,["Company_B"]31

Looking at the first example ``0013,["Company_A"]01`` in detail:

    * ``0013`` is the element *group number*

    * ``Company_A`` is the value of the private creator tag

    * ``01`` is the last part of the *element number* (first part is dynamically set by private creator tag)

See :ref:`private_tag` for more information on private tag structure.



