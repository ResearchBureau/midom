.. _spaces_and_codes:

Spaces and codes
================
For several MIDOM objects, it is useful to describe the space they inhabit. Inside this
space, all possible objects of a certain type are represented. By defining the space,
it becomes easier to reason about relationships and operations.

.. _dataset_space:

Dataset Space
-------------
All possible :ref:`DICOM datasets <Dataset>`. Each :ref:`DICOM tag <tag>` is a
dimension, the possible values of the tag are the value of the dimension. Each unique
dataset is a unique point in dataset space.

.. uml:: diagrams/dataset_space.puml
   :caption: Dataset Space contains all possible values for all non-private DICOM tags.
    Each point is a unique :ref:`data set <dataset>`.

:ref:`Private tags <private_tag>` are *not* part of dataset space.

Size
....
This space has one dimension for each :ref:`tag`, which comes to slightly over 4000.
The size of each dimension is bounded by each tag's :ref:`value_representation`. Some
value representations, like 'Other Byte String' are potentially infinite. Tags like ``PixelData``,
``WaveformData``, ``SpectroscopyData`` and ``EncapsulatedDocument`` are all potentially
infinite in size, only constrained by practical implementation.

The number of permutations is so large as to be practically infinite.


.. _delta_space:

Delta Space
-----------
All possible :ref:`delta sets <delta_set>`.

.. uml:: diagrams/delta_space.puml
   :caption: Delta Space contains all possible perceived changes to all non-private DICOM tags.
    Each point is a unique :ref:`delta set <delta_set>`.

Size
....
Delta space is smaller than :ref:`dataset_space`. Most importantly it is not infinite.
It compresses all variability down to 5 :ref:`delta_codes`. Which means the total
number of delta sets is :math:`5^n` with :math:`n` the number of possible elements.
For 4000+ elements this is still astronomical but *bounded* nonetheless. For the
611-dimensional :ref:`e1_1_subspace` the size is roughly :math:`e^{427}`.




.. _action_space:

Action Space
------------
All possible :ref:`action sets <action_set>`.

.. uml:: diagrams/action_space.puml
   :caption: Action Space contains all possible changes all non-private DICOM tags.
    Each point is a unique :ref:`action set <action_set>`.



Subspaces
---------
The space created by a subset of all dicom tags.

.. _image_typ_id_subspace:

Image Type ID subspace
......................
Sixteen tags that contain information about the system that produced this DICOM image. Mainly
used for mapping :ref:`PHI` regions. In code it looks like this


.. literalinclude:: ../../midom/subspaces.py
   :language: python
   :pyobject: ImageTypeIDSubspace


.. _e1_1_subspace:

E1-1 subspace
.............
All non-private tags mentioned in `DICOM PS3.15 table E.1-1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1>`_
If a tag is in this list, it means the official DICOM deidentification rules have something to
say about how to handle that tag. These 640 tags are the only ones to have an :ref:`action code <action_codes>`
associated with them.

`Code (python) for the E1-1 subspace is in github <https://github.com/ResearchBureau/midom/blob/main/midom/subspaces.py#L28>`_

This subspace can be applied to both :ref:`delta_space` and :ref:`dataset_space`.

.. _action_codes:

Action Codes
------------
The codes used in the DICOM standard Attribute and Confidentiality Profiles to denote
per :ref:`tag` the action that should be taken to deidentify it.

Main action codes:

+---------------+------------------------------+
| Code          | Description                  |
+===============+==============================+
| D             | Replace with dummy           |
+---------------+------------------------------+
| Z             | Replace with empty or dummy  |
+---------------+------------------------------+
| X             | Remove                       |
+---------------+------------------------------+
| K             | Keep                         |
+---------------+------------------------------+
| C             | Clean                        |
+---------------+------------------------------+
| U             | Replace with UID             |
+---------------+------------------------------+

There are 5 more action codes that are combinations of the 6 main ones above.
All 11 action codes are listed in `PS3.15 table E.1-1a <https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1a>`_.

Action codes are used to describe what *should* happen to a tag. In contrast,
:ref:`delta codes <spaces_delta_codes>` are used to describe an observable change in a tag value.

.. _spaces_delta_codes:


.. _action_set:

Action Set
----------
A set of :ref:`action_codes`. All possible codes are contained in :ref:`action_space`.
Example action set:

+----------------------------------+--------+
| DICOM Tag Name                   | Action |
+==================================+========+
| Patient's Name                   | REMOVE |
+----------------------------------+--------+
| Study Date                       | KEEP   |
+----------------------------------+--------+
| Series Instance UID              | UID    |
+----------------------------------+--------+
| Accession Number                 | EMPTY  |
+----------------------------------+--------+
| Referring Physician's Name       | REMOVE |
+----------------------------------+--------+
| Modality                         | KEEP   |
+----------------------------------+--------+

When characterizing the :ref:`tags` component of a :ref:`objects_protocol` or
:ref:`objects_deidentifier`, an action set is often called an ``action profile``


Delta Codes
------------
A Delta Code or describes an observable change in a DICOM element, typically
before and after processing

+---------------+----------------------+
| Change Code   | Description          |
+===============+======================+
| UNCHANGED     | No modification      |
+---------------+----------------------+
| CHANGED       | Modified             |
+---------------+----------------------+
| REMOVED       | Deleted              |
+---------------+----------------------+
| EMPTIED       | Cleared/Set to empty |
+---------------+----------------------+
| CREATED       | Newly added          |
+---------------+----------------------+

Note that multiple :ref:`action codes<action_codes>` can cause the same change code
to be observed.
