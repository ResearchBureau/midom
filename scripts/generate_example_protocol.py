"""Write a protocol to disk, serialized as json

Useful to generate a quick example when developing Protocol format and serialization.
"""
from midom.components import (
    CriterionString,
    Filter,
    PixelArea,
    PixelOperation,
    PrivateAllowGroup,
    Protocol,
    TagAction,
)
from midom.constants import ActionCodes
from midom.identifiers import (
    PrivateAttributes,
    PrivateBlockTagIdentifier,
    RepeatingGroup,
    SingleTag,
)


def a_protocol() -> Protocol:
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
                    identifier=PrivateAttributes(),
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
                    identifier=PrivateAttributes(),
                    action=ActionCodes.REMOVE,
                    justification="",
                ),
            ],
        },
        filters=[
            Filter(
                criterion=CriterionString(
                    content="Modality.equals('US') and BurntInAnnotation.equals('No')"
                ),
                justification="important",
            ),
            Filter(
                criterion=CriterionString(
                    content="SOPClassUID.equals('123456')"
                ),
                justification="this sopclass is bad",
            ),
        ],
        pixel=[
            PixelOperation(
                description="Model this and that",
                criterion=CriterionString(
                    content="Rows.equals(1024) and Columns.equals(720) and "
                    "Modelname.equals('Toshiba bla')"
                ),
                areas=[PixelArea(area=(0, 0, 720, 50))],
            ),
            PixelOperation(
                description="Another test operation",
                criterion=CriterionString(
                    content="Rows.equals(1024) and Columns.equals(740) and "
                    "Modelname.equals('Canon bla')"
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


if __name__ == "__main__":
    output_file = "/tmp/example_protocol.json"

    with open(output_file, "w") as f:

        protocol = a_protocol()
        protocol.sort_tags()
        f.write(protocol.model_dump_json(indent=2))
        print(f"written to {output_file}")
