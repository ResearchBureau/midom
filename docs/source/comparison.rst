.. _comparison:

Comparison
==========

How to compare and evaluate MIDOM objects

    - Deidentifier implementing a protocol
    - Determining delta space point from examples
    - Mapping delta space to action space
    - Stricter vs identical vs less-strict for each component, in delta and action space

Comparing:
    - Comparing two deidentifiers without knowing protocol (from examples)
    - Comparing a protocol to a deidentifier (from examples on one side?)
    - Determining deidentification profile options from examples
    - Comparing two protocols

Discussion
----------

What is a protocol's task?
    - apply a transformation so for each dataset d P(d) does not contain PI
    - Protocol should always define a context, as this determines what is PI
    - Filters does two things: indicate limits in dataset space (transformation can't
      handle this part) and codify domain knowledge (black list this producer)



Dual goals of developing a protocol
    - Finetuning the transformation
    - Exploring the dataset space from context/domain that protocol is used in


Why is deidentification so hard?
    - tasks looks like a technical one but is actually operational (exploring local dataset space)
    - several ambiguities (clean action, safe private)
    - dicom standard only covers part of it
    - Exploring the dataset space is inherently slow and always incomplete



Evaluating
----------
A protocol. Checking performance
    - which space?
    - which examples?
    - sensitivity/specificity (based on examples you always want this to be sensitivity
      1, but you have incomplete dataset space knowledge)
