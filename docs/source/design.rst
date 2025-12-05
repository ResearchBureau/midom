.. _design:

Design
======

How to design a :ref:`deidentifier <objects_deidentifier>`? And how to verify that it
does what you designed it to do?

.. _design_aims:

Aims
....

Why do we need medical image deidentification? Deidentification is *one* of the available
methods to achieve two goals:

1. To make the data inside a medical image available

2. To Protect patient confidentiality

Other methods can be used instead of or in addition to deidentification. Restricting access,
contracts, aggregating data are all valid approaches. For a full discussion of methods,
reasoning and legal underpinning, see the `European Data Protection Board guidelines on Pseudonymization <https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en>`_.

.. Note:: MIDOM focuses on deidentification of medical image data in the european context.
    Firstly, "patient confidentiality" is understood to be based on the EU's
    `GDPR regulation <https://gdpr.eu/what-is-gdpr/>`_. Secondly, alternative methods of
    protecting patient confidentiality, though important, are kept out of scope here.

Split actions from implementation
.................................

How to create a script or program to remove patient information from medical
image files? The most direct way is to find code to modify the image file, set
rules to modify the elements you want, and done.

This approach runs into problems. The crux of the problem is that image deidentification
contains both technical and policy elements. Implementation can be complex and highly technical
At the same time, the general approach should be based on policy decisions and reviewable.

The solution proposed by MIDOM is to separate the definition into two concepts.
A :ref:`protocol <objects_protocol>` describes deidentification approach in terms of
:ref:`actions <action_codes>`. A :ref:`deidentifier <objects_deidentifier>` is a specific
implementation of the rules set out in a protocol.

.. uml:: diagrams/protocol_deidentifier.puml
    :caption: Deidentification definition is split between general rules (Protocol) and concrete implementation (Deidentifier)

One Protocol can be implemented in multiple ways, on different platforms.

Context of use is essential
...........................

One of the most important elements of `EU pseudonymization guidelines <https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf>`_
is the concept of the *pseudonymization domain*, defined as

   *the context in which pseudonymisation is to preclude attribution of data to*
   *specific data subjects*

In MIDOM, any :ref:`protocol <objects_protocol>` is *only considered appropriate for a given :ref:`domain <validation_domain>`.

.. uml:: diagrams/domain_protocol.puml
   :caption: A Protocol is only appropriate for a given domain


.. _validation:

Validation
==========

Once you have decided on a protocol, and implemented a :ref:`deidentifier <objects_deidentifier>` based on it,
how do you make sure it does what you want?

The basic approach is to take a DICOM dataset


And how do
you make sure that after a change it still conforms to all the policy decision that underpin it?

How to make sure a :ref:`deidentifier <objects_deidentifier>` does what you want it to do?

We will talk about the following components:

.. uml:: diagrams/validation_objects.puml
   :caption: Objects used in the validation of a :ref:`deidentifier <objects_deidentifier>`.

A deidentification process

Use this link:
https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en
:ref:`deidentifier <validation_objects>`

.. _validation_objects:

Validation Objects
------------------


.. _validation_domain:

Domain
......

.. _validation_set:

Validation Set
..............

.. _region_sample_set:

Region Sample Set
.................

.. _deidentifier_reference:

Deidentifier Reference
......................

.. _validation_protocol:

Protocol
........

.. _validation_deidentifier:

Deidenfifier
............






