"""Write a protocol to disk, serialized as json

Useful to generate a quick example when developing Protocol format and serialization.
"""
from midom.components import BooleanFunction, PixelArea, Protocol
from midom.constants import ActionCodes
from midom.identifiers import (
    PrivateBlockTagIdentifier,
    PrivateTags,
    RepeatingGroup,
    SingleTag,
)
from midom.serialization import ProtocolSerializer


def a_protocol():
    return Protocol(
        tags={
            "1.2.840.10008.5.1.4.1.1.2": [
                (SingleTag("PatientID"), ActionCodes.REMOVE),
                (SingleTag("Modality"), ActionCodes.KEEP),
                (PrivateTags(), ActionCodes.REMOVE),
                (
                    PrivateBlockTagIdentifier("112d['company']3f"),
                    ActionCodes.KEEP,
                ),
                (RepeatingGroup("50xx,xxxx"), ActionCodes.DUMMY),
                (SingleTag(0x3313001D), ActionCodes.KEEP),  # unknown tag
            ],
            "1.2.840.10008*": [
                (SingleTag("PatientID"), ActionCodes.REMOVE),
                (SingleTag("Modality"), ActionCodes.REMOVE),
                (PrivateTags(), ActionCodes.REMOVE),
            ],
        },
        filters=[
            BooleanFunction(criteria="SOPClassUID=123456"),
            BooleanFunction(
                criteria="Modality='US' and BurntInAnnotation=EMPTY"
            ),
        ],
        pixel=[
            (
                BooleanFunction(
                    criteria="Rows=1024 and Columns=720 and Modelname='Toshiba bla'"
                ),
                PixelArea(area="(0,0,720,50)"),
            )
        ],
        private=[
            PrivateBlockTagIdentifier('0075["company"]01'),
            PrivateBlockTagIdentifier('0013["companyB"]ff'),
        ],
    )


if __name__ == "__main__":
    output_file = "/tmp/example_protocol.json"

    with open(output_file, "w") as f:
        f.write(ProtocolSerializer().to_json(a_protocol()))
        print(f"written to {output_file}")
