from midom.components import BooleanFunction, PixelArea, Protocol
from midom.constants import ActionCodes
from midom.identifiers import (
    PrivateBlockTagIdentifier,
    PrivateTags,
    RepeatingGroup,
    SingleTag,
)
from midom.serialization import ProtocolSerializer


def test_protocol_encoder():
    """Take a sample protocol, serialize it to json, then back to protocol.
    Did it work?
    """

    protocol = Protocol(
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

    serializer = ProtocolSerializer()
    encoded = serializer.to_json(protocol)
    decoded = serializer.from_json(encoded)

    def assert_elements(collection_a, collection_b):
        """Assert that each element in a is equal to the same element in b"""
        for a, b in zip(collection_a, collection_b):
            assert a == b, f"{a} is not {b}"

    assert_elements(protocol.tags, decoded.tags)
    assert_elements(protocol.filters, decoded.filters)
    assert_elements(protocol.pixel, decoded.pixel)
    assert_elements(protocol.private, decoded.private)
