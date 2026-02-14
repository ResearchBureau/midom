"""Classes and functions having to do with checking deidentifiers against a
reference
"""
from copy import deepcopy
from itertools import chain
from typing import ClassVar, Iterable, Iterator, List, Tuple, Union

from pydantic import BaseModel
from pydicom import Dataset


class DatasetRejectedError(Exception):
    """The input dataset was rejected by the deidentifier"""

    pass


class ValidationFailedError(Exception):
    """A Deidentifiers result does not conform to a reference"""

    pass


class Domain(BaseModel):
    """The context in which a protocol is considered to be effective for protecting
    confidentiality
    """

    description: str


class RegionSampleSet(BaseModel):
    """A collection of DICOM datasets from a common region in dataset space.
    For example, 'datasets from hospital A' or 'Ultrasound datasets'.
    """

    description: str

    def all_samples(self) -> Iterable[Dataset]:
        """All DICOM samples contained in this Region Sample Set"""
        raise NotImplementedError("Implemented in child classes")


class DeidentificationReference(BaseModel):
    """Holds a deidentification result for one or more datasets."""

    description: str

    def get_reference(self, ds: Dataset) -> Dataset:
        """Get the deidentification result for the given dataset

        Raises
        ------
        DatasetRejectedError
            When the deidentification result for this dataset is to reject the dataset
            outright.
        KeyError
            When there is no reference for this dataset.
        """
        raise NotImplementedError("Implemented in child classes")


class DatasetRejected:
    """Class used as return value to indicate rejection of the input dataset"""

    pass


class ValidationSet(BaseModel):
    """An example of 'correct' deidentification of a set of DICOM samples
    reference should contain a valid result for each sample.
    """

    sample_sets: List[RegionSampleSet]
    reference: DeidentificationReference

    def get_reference(self, ds: Dataset) -> Union[DatasetRejected, Dataset]:
        """Find the correct deidentification result for the given dataset."""
        try:
            return self.reference.get_reference(ds)
        except DatasetRejectedError:
            return DatasetRejected()

    def items(
        self,
    ) -> Iterator[Tuple[Dataset, Union[DatasetRejected, Dataset]]]:
        """All tuples dataset -> correct deidentification result

        Translates errors
        """
        for sample_set in chain(self.sample_sets):
            for sample in sample_set.all_samples():
                yield sample, self.get_reference(sample)


def deepcopy_fix(dataset):
    """Works around a pydicom 3.0.1 bug https://github.com/pydicom/pydicom/issues/2294
    Fixed in pydicom main but not released. Remove this method and use regular
    deepcopy when a release is available
    """
    dataset_copy = deepcopy(dataset)
    for key in dataset_copy._private_blocks.keys():
        dataset_copy._private_blocks[key].dataset = dataset_copy
    return dataset_copy


class Deidentifier:
    """Something that has a deidentify() method that processes pydicom datasets"""

    def deidentify(self, dataset: Dataset) -> Dataset:
        raise NotImplementedError()


class Check:
    """Checks whether a deidentifier results corresponds to a reference

    Base class for child classes that can fill in what 'corresponds to a reference'
    means. Some examples:
    * Result is as strict or stricter
    * Result transformation seems identical
    * Private tags that should be kept are kept
    * Burnt-in image data was correctly removed

    A better name for this would possibly be 'Criterion' but that name is taken.
    """

    description: ClassVar[str] = ""  # What does this check do? Human-readable

    def run(self, original: Dataset, reference: Dataset, result: Dataset):
        """Check whether result conforms to the reference result

        Raises
        ------
        ValidationFailedError
            If result does not conform.
        """
        raise NotImplementedError


class Validator:
    def __init__(self, checks: List[Check]):
        """Can check whether a deidentifier's operation corresponds to a reference.

        Parameters
        ----------
        checks:
            All check to perform on each deidentification result
        """
        self.checks = checks

    def validate(
        self, deidentifier: Deidentifier, validation_set: ValidationSet
    ):
        """Check whether a deidentifier conforms to each example in a ValidationSet

        Raises
        ------
        ValidationFailedError
            If any deidentifier result does not conform to the reference
        """

        for original, reference in validation_set.items():
            for check in self.checks:
                check.run(
                    original,
                    reference,
                    deidentifier.deidentify(deepcopy_fix(original)),
                )
