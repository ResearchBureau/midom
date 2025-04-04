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

    1. The special tag `PixelData <https://dicom.innolitics.com/ciods/ct-image/image-pixel/7fe00010>`_
       is excluded as it has its own dedicated component :ref:`pixel`

    2. Similarly, all :ref:`private tags <private_tag>` are excluded from tags processing and handled in
       :ref:`private`.


Definition
..........

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

Definition
..........
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
actually runnable. For a :ref:`protocol <objects_protocol>`, Filter can just be written
down in any formal language


.. _pixel:

Pixel
-----

The tag `PatientIdentityRemoved <https://dicom.innolitics.com/ciods/parametric-map/patient/00120062>`_ can be
set by :ref:`pixel` and not touched by Tags processing.


.. _private:
Private
-------
