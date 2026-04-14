from typing import Iterable, List

from dicomgenerator.generators import quick_dataset
from dicomgenerator.pixeldata import draw_noise
from pydantic import ConfigDict
from pydicom import Dataset

from midom.components import PixelArea
from midom.validation import (
    DatasetRejected,
    DatasetRejectedError,
    DeidentificationReference,
    Domain,
    RegionSampleSet,
    RegionValidationSet,
    SampleDataset,
)


class InMemorySampleSet(RegionSampleSet):
    """Dummy implementation of RegionSampleSet"""

    model_config = ConfigDict(arbitrary_types_allowed=True)  # for Dataset

    datasets: List[Dataset]

    def all_samples(self) -> Iterable[Dataset]:
        return self.datasets


class InMemoryDeidentificationReference(DeidentificationReference):
    """Dummy implementation"""

    iteration: int = 0

    def get_reference(self, ds: Dataset) -> Dataset:
        """Will just alternate between returning a dataset and raising rejected"""
        self.iteration += 1
        if self.iteration % 2 == 1:
            return ds
        else:
            raise DatasetRejectedError("I don't want to!")


def test_validation():
    """Just build and combine some objects, see whether they make sense"""

    _ = Domain(description="Images used in tests")
    sample_set = InMemorySampleSet(
        description="Some test images",
        datasets=[
            quick_dataset(PatientName="Patient1"),
            quick_dataset(PatientName="Patient2"),
            quick_dataset(PatientName="Patient3"),
        ],
    )
    reference = InMemoryDeidentificationReference(
        description="A test reference"
    )
    validation_set = RegionValidationSet(
        sample_sets=[sample_set], reference=reference
    )

    items = [x for x in validation_set.items()]

    assert len(items) == 3
    assert type(items[1][1]) == DatasetRejected  # item should be


def test_sample_dataset_serialization():
    """A SampleDataset should be writable and loadable as JSON"""
    sample = SampleDataset(
        uid="vna/1234/554/234",
        dataset=quick_dataset(Modality="CT", AccessionNumber="1234"),
        pi_regions=[PixelArea(x=10, y=8, width=100, height=40)],
    )

    serialized = sample.model_dump_json(indent=2)
    reserialized = SampleDataset.model_validate_json(serialized)
    assert reserialized.dataset.Modality == sample.dataset.Modality
    assert (
        reserialized.dataset.AccessionNumber == sample.dataset.AccessionNumber
    )
    assert reserialized.pi_regions == sample.pi_regions


def test_sample_dataset_pixeldata_serialization():
    """Pixeldata can be serialized but will easily be huge. Offer guide rails"""
    sample = SampleDataset(
        uid="vna/1234/554/234",
        dataset=quick_dataset(
            Modality="CT",
            AccessionNumber="1234",
            PixelData=draw_noise(201, 301, "uint8"),
        ),
        pi_regions=[PixelArea(x=10, y=8, width=100, height=40)],
    )

    serialized = sample.model_dump_json(indent=2)
    reserialized = SampleDataset.model_validate_json(serialized)
    assert reserialized.dataset.Modality == sample.dataset.Modality
    assert (
        reserialized.dataset.AccessionNumber == sample.dataset.AccessionNumber
    )
    assert reserialized.pi_regions == sample.pi_regions
