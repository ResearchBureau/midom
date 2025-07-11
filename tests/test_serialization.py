from midom.components import BooleanFunction, Filter, PixelArea, PixelOperation, \
    PrivateAllowGroup, Protocol, TagAction
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

    protocol = Protocol(tags={"1.2.840.10008.5.1.4.1.1.2": [
        TagAction(identifier=SingleTag("PatientID"), action=ActionCodes.REMOVE,
                  justification=""),
        TagAction(identifier=SingleTag("Modality"), action=ActionCodes.KEEP,
                  justification=""),
        TagAction(identifier=PrivateTags(), action=ActionCodes.REMOVE,
                  justification=""),
        TagAction(identifier=PrivateBlockTagIdentifier("112d['company']3f"),
                  action=ActionCodes.KEEP, justification=""),
        TagAction(identifier=RepeatingGroup("50xx,xxxx"), action=ActionCodes.DUMMY,
                  justification=""),
        TagAction(identifier=SingleTag(0x3313001D), action=ActionCodes.KEEP,
                  justification="")  # unknown tag
    ], "1.2.840.10008*": [
        TagAction(identifier=SingleTag("PatientID"), action=ActionCodes.REMOVE,
                  justification=""),
        TagAction(identifier=SingleTag("Modality"), action=ActionCodes.REMOVE,
                  justification=""),
        TagAction(identifier=PrivateTags(), action=ActionCodes.REMOVE,
                  justification="")], }, filters=[Filter(criterion=BooleanFunction(
        criterion="Modality='US' and BurntInAnnotation=EMPTY"),
                                                         justification="important"),
        Filter(criterion=BooleanFunction(criterion="SOPClassUID=123456"),
               justification="this sopclass is bad")

    ], pixel=[PixelOperation(description="Model this and that",
                             criterion=BooleanFunction(
                                 criterion="Rows=1024 and Columns=720 and Modelname='Toshiba bla'"),
                             areas=[PixelArea(area=(0, 0, 720, 50))]),
        PixelOperation(description="Another test operation", criterion=BooleanFunction(
            criterion="Rows=1024 and Columns=720 and Modelname='canon bla'"),
                       areas=[PixelArea(area=(0, 0, 720, 150))])

    ], private=[PrivateAllowGroup(
        justification="Is really safe. See https://a_link_to_dicom_conformance_statement",
        elements=[PrivateBlockTagIdentifier('0075["company"]01'),
                  PrivateBlockTagIdentifier('0075["company"]02')])], )


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
