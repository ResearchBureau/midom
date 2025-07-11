"""Python definition of the parts"""
from typing import Dict, List

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.functional_serializers import field_serializer

from midom.constants import ActionCode, ActionCodes
from midom.identifiers import (
    PrivateBlockTagIdentifier,
    TagIdentifier,
    tag_identifier_from_string,
)


class BooleanFunction(BaseModel):
    criterion: str


class PixelArea(BaseModel):
    area: tuple[int, int, int, int]


class TagAction(BaseModel):
    """Describes the action to take for a single identifier (tag or tag group) and the
    reason for this action.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )  # for TagIdentifier

    identifier: TagIdentifier
    action: ActionCode
    justification: str

    @field_serializer("identifier")
    def serialize_identifier(self, value, _info):
        return value.key()

    @field_validator("identifier", mode="before")
    @classmethod
    def deserialize_identifier(cls, value):
        if isinstance(value, TagIdentifier):
            return value
        elif isinstance(value, str):
            return tag_identifier_from_string(value)
        else:
            raise ValueError(
                f'Invalid input data for TagAction.identifier: "{value}"'
            )

    @field_serializer("action")
    def serialize_action(self, value, _info):
        return value.key

    @field_validator("action", mode="before")
    @classmethod
    def deserialize_action(cls, value):
        if isinstance(value, ActionCode):
            return value
        elif isinstance(value, str):
            return ActionCodes.from_string(value)
        else:
            raise ValueError(
                f'Invalid input data for TagAction.identifier: "{value}"'
            )


class Filter(BaseModel):
    criterion: BooleanFunction
    justification: str


class PixelOperation(BaseModel):
    description: str
    criterion: BooleanFunction
    areas: List[PixelArea]


class PrivateAllowGroup(BaseModel):
    # Allow arbitrary for PrivateBlockTagIdentifier
    model_config = ConfigDict(arbitrary_types_allowed=True)

    elements: List[PrivateBlockTagIdentifier]
    justification: str

    @field_serializer("elements")
    def serialize_identifier(self, value, _info):
        return [x.key() for x in value]

    @field_validator("elements", mode="before")
    @classmethod
    def deserialize_tag(cls, values):
        if not isinstance(values, list):
            ValueError(f"elements should be a list, got {values}")
        deserialized = []
        for x in values:
            if isinstance(x, TagIdentifier):
                deserialized.append(x)
            elif isinstance(x, str):
                deserialized.append(tag_identifier_from_string(x))
            else:
                raise ValueError(
                    f'Invalid input data for TagAction.identifier: "{x}"'
                )
        return deserialized


class Protocol(BaseModel):
    """Defines how to handle the deidentification of any incoming dataset. It does
    not say anything about implementation, it only prescribes what should be done
    to each part of a dataset and under which circumstances to reject it outright.
    """

    tags: Dict[str, List[TagAction]]
    filters: List[Filter]
    pixel: List[PixelOperation]
    private: List[PrivateAllowGroup]
