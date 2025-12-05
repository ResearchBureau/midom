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

.. _context_of_use_is_essential:

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

The basic approach is to collect DICOM dataset examples from the :ref:`validation_domain`.
Each example is then connected to a desired output which together are a :ref:`validation_set`.
Each example in a :ref:`validation_set` can then be compared to the output of the :ref:`deidentifier <objects_deidentifier>`.

.. _validation_set:

Validation Set
..............

A collection of medical image examples with reference output.

The DICOM dataset examples are collected together in a :ref:`region_sample_set`. For each of
the DICOM datasets in the region sample set, the desired output is registered in a :ref:`deidentification_reference`.
Multiple region sample sets can be included in this way. All the sample sets and references together
form a :ref:`validation_set`.

A validation set describes what is considered 'correct' deidentification for a certain :ref:`validation_domain`. Defining
a validation set is as much a policy decision as it is a technical one.

.. uml:: diagrams/validation_set.puml
   :caption: A :ref:`validation_set` consists of multiple :ref:`region sample sets <region_sample_set>` and their desired
        output. Desired output is always defined in the context of a :ref:`validation_domain`.


Overview
........

To protect patient confidentiality in certain :ref:`validation_domain`, A :ref:`protocol <objects_protocol>`
is defined. A :ref:`deidentifier <objects_deidentifier>` is then created that implements this protocol.

To validate the deidentifier, examples and reference output are collected in a :ref:`validation_set`. Reference
output can only be considered correct in the context of a certain :ref:`validation_domain`


.. uml:: diagrams/validation_objects.puml
   :caption: Objects used in the validation of a :ref:`deidentifier <objects_deidentifier>`.

A deidentification process

Use this link:
https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en
:ref:`deidentifier <validation_objects>`


.. _validation_domain:

Domain
......

The context in which a :ref:`deidentifier <objects_deidentifier>` or :ref:`protocol <objects_protocol>` is meant
to help protect patient confidentiality. See :ref:`context_of_use_is_essential`

In MIDOM, the concept domain is used in two related by separate ways:

Domain in a broad sense
  A Domain in a broader sense refers to "The entire context in which a deidentifier functions". This includes
  policy and organizational aspects, contracts, training, cyber security. This sense of 'domain' is the one used in
  the `GDPR <https://gdpr.eu/what-is-gdpr/>`_. It is the sense used in the sentence "A protocol is suitable for this domain".

Domain in a narrow sense
  When talking about :ref:`region sample sets <region_sample_set>`, 'domain' means "All possible DICOM datasets" that
  a deidentifier is expected to handle". Technically, it is a region in :ref:`dataset_space` and does not include
  any organizational elements.


.. _region_sample_set:

Region Sample Set
.................

A distinct region of :ref:`dataset_space` that the deidentifier is expected to work in.
The grouping is not strictly defined, but described in free text. For example "Standard DICOM datasets",
"Complicated Ultrasound images", "Images used in hospital X" or "Samples of studies encountered in project Y"


.. _deidentification_reference:

Deidentification Reference
..........................

The desired output for the examples in a :ref:`region sample sets <region_sample_set>`. Valid only
int he context of a :ref:`validation_domain`.

Desired output for a single example can be one of two types:

1) **A (transformed) dataset** - This indicates the 'correct' deidentification of this dataset in the context of the domain

2) **Reject** - The input dataset is supposed to be rejected by the deidentifier. Processing it is considered too risky.
