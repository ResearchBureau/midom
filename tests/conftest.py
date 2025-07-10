from typing import Tuple, Union

import factory
from pydicom import DataElement


class DatasetFactory(factory.Factory):
    class Meta:
        model = DataElement

    tag: Union[int, str, Tuple[int, int]] = "PatientID"
    VR = "SH"  # short string
    value = factory.Sequence(lambda n: "value%d" % n)
