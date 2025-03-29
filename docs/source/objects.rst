.. _objects:

Objects
=======

The different levels of deidentifying a DICOM dataset. Deidentification comes down to
changing the right parts of a dataset. If leave out the special cases of :ref:`pixel data<pixel>`
and private tags, The change to each :ref:`DICOM element <dicom_element>`
in a single :ref:`dataset <dataset>` can be characterized as a :ref:`delta set <deltaset>`.
A DeltaSet

.. uml:: diagrams/system_context.puml



.. _protocol:

Protocol
--------

.. _deidentifier:

Deidentifier
------------

.. _deltaset:

Deltaset
--------

.. _dataset:

Dataset
-------

