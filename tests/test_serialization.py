import pytest

from midom.components import (
    BooleanFunction,
    Filter,
    PixelArea,
    PixelOperation,
    PrivateAllowGroup,
    Protocol,
    TagAction,
)
from midom.constants import ActionCodes
from midom.identifiers import (
    PrivateBlockTagIdentifier,
    PrivateTags,
    RepeatingGroup,
    SingleTag,
)


@pytest.fixture()
def a_protocol():
    return Protocol(
        tags={
            "1.2.840.10008.5.1.4.1.1.2": [
                TagAction(
                    identifier=SingleTag("PatientID"),
                    action=ActionCodes.REMOVE,
                    justification="",
                ),
                TagAction(
                    identifier=SingleTag("Modality"),
                    action=ActionCodes.KEEP,
                    justification="",
                ),
                TagAction(
                    identifier=PrivateTags(),
                    action=ActionCodes.REMOVE,
                    justification="",
                ),
                TagAction(
                    identifier=PrivateBlockTagIdentifier("112d['company']3f"),
                    action=ActionCodes.KEEP,
                    justification="",
                ),
                TagAction(
                    identifier=RepeatingGroup("50xx,xxxx"),
                    action=ActionCodes.DUMMY,
                    justification="",
                ),
                TagAction(
                    identifier=SingleTag(0x3313001D),
                    action=ActionCodes.KEEP,
                    justification="",
                ),  # unknown tag
            ],
            "1.2.840.10008*": [
                TagAction(
                    identifier=SingleTag("PatientID"),
                    action=ActionCodes.REMOVE,
                    justification="",
                ),
                TagAction(
                    identifier=SingleTag("Modality"),
                    action=ActionCodes.REMOVE,
                    justification="",
                ),
                TagAction(
                    identifier=PrivateTags(),
                    action=ActionCodes.REMOVE,
                    justification="",
                ),
            ],
        },
        filters=[
            Filter(
                criterion=BooleanFunction(
                    criterion="Modality='US' and BurntInAnnotation=EMPTY"
                ),
                justification="important",
            ),
            Filter(
                criterion=BooleanFunction(criterion="SOPClassUID=123456"),
                justification="this sopclass is bad",
            ),
        ],
        pixel=[
            PixelOperation(
                description="Model this and that",
                criterion=BooleanFunction(
                    criterion="Rows=1024 and Columns=720 and Modelname='Toshiba bla'"
                ),
                areas=[PixelArea(area=(0, 0, 720, 50))],
            ),
            PixelOperation(
                description="Another test operation",
                criterion=BooleanFunction(
                    criterion="Rows=1024 and Columns=720 and Modelname='canon bla'"
                ),
                areas=[PixelArea(area=(0, 0, 720, 150))],
            ),
        ],
        private=[
            PrivateAllowGroup(
                justification="Is really safe. See https://a_link_to_dicom_"
                "conformance_statement",
                elements=[
                    PrivateBlockTagIdentifier('0075["company"]01'),
                    PrivateBlockTagIdentifier('0075["company"]02'),
                ],
            )
        ],
    )


def test_pydantic_serialiazation():
    action = TagAction(
        identifier=SingleTag("PatientID"),
        action=ActionCodes.REMOVE,
        justification="",
    )
    serialized = action.model_dump()
    reserialized = TagAction.model_validate(serialized)
    assert reserialized


def test_protocol_serialization(a_protocol):
    serialized = a_protocol.model_dump_json(indent=2)
    reserialized = Protocol.model_validate_json(serialized)
    assert reserialized  # No exceptions is enough for now
