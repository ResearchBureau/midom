.. _spaces_and_codes:

Spaces and codes
================
For several MIDOM objects, it is useful to describe the space they inhabit. Inside this
space, all possible objects of a certain type are represented. By defining the space,
it becomes easier to reason about relationships and operations.

Dataset Space
-------------
All DICOM datasets


Delta Space
-----------
All possible :ref:`deltas<delta>`.

.. _action_codes:

Action Codes
------------
The codes used in the DICOM standard Attribute and Confidentiality Profiles to denote
per :ref:`tag` the action that should be taken to deidentify it. All action codes are
listed in `PS3.15 table E.1-1a <https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1a>`_

Example action codes:

+---------------+----------------------+
| Code          | Description          |
+===============+======================+
| D             | Replace with dummy   |
+---------------+----------------------+
| Z             | Replace with empty   |
+---------------+----------------------+
| X             | Remove               |
+---------------+----------------------+
| K             | Keep                 |
+---------------+----------------------+
| C             | Clean                |
+---------------+----------------------+

Action codes are used to describe what _should_ happen to a tag. In contrast,
:ref:`change_codes` are used to describe an observable change in a tag value.

.. _change_codes:

Change Codes
------------
A change code or *Delta Code* describe an observable change in a DICOM element, typically
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