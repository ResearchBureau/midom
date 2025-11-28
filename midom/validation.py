"""Classes and functions having to do with checking deidentifiers against a
reference
"""
from typing import Iterator, List, Tuple, Union

from pydantic import BaseModel
from pydicom import Dataset


class DatasetRejectedError(Exception):
    """The input dataset was rejected by the deidentifier"""

    pass


class Domain(BaseModel):
    """The context in which a protocol is considered to be usable"""

    description: str


class RegionSampleSet(BaseModel):
    """A collection of DICOM datasets from a common region in dataset space.
    For example 'datasets from hospital A' or 'Ultrasound datasets'
    """

    description: str

    def all_samples(self) -> Iterator[Dataset]:
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
    reference should ideally contain a valid result for each sample.
    """

    samples: List[RegionSampleSet]
    reference: DeidentificationReference

    def get_reference(self, ds: Dataset):
        try:
            self.reference.get_reference(ds)
        except DatasetRejectedError:
            return DatasetRejected

    def validation_items(
        self,
    ) -> Iterator[Tuple[Dataset, Union[DatasetRejected, Dataset]]]:
        for sample in zip(x.all_samples() for x in self.samples):
            yield sample, self.get_reference(sample)
