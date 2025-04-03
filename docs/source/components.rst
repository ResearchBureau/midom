.. _components:

Components
==========
The four constituent parts of a :ref:`Protocol`, and by extension of any :ref:`deidentifier`.
These parts together define the complete handling of any incoming :ref:`dataset`.

<add image of parts here>

.. _tags:

Tags
----
Tags Processing. For :ref:`protocols <objects_protocol>`, defines what to do with each :ref:`tag`. The language for this is :ref:`action_codes`.

For :ref:`deidentifiers <deidentifier>`, tags defines *what is done* to each tag, expressed as a :ref:`objects_deltaset`.


.. _filter:

Filter
------
Checks any incoming dataset and either accepts it for further processing or rejects it.
Common reasons for rejection are unknown DICOM with burnt in information,

.. _pixel:

Pixel
-----

.. _private:
Private
-------
