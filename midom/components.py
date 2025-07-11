"""Python definition of the parts"""
from typing import Dict, List, Tuple

from pydantic import BaseModel, ConfigDict

from midom.constants import ActionCode
from midom.identifiers import PrivateBlockTagIdentifier, TagIdentifier


class BooleanFunction(BaseModel):
    criterion: str


class PixelArea(BaseModel):
    area: tuple[int,int,int,int]

class TagAction(BaseModel):
    """Describes the action to take for a single identifier (tag or tag group) and the
    reason for this action.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)  # for TagIdentifier

    identifier: TagIdentifier
    action: ActionCode
    justification: str

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

class Protocol(BaseModel):

    tags: Dict[str, List[TagAction]]
    filters: List[Filter]
    pixel: List[PixelOperation]
    private: List[PrivateAllowGroup]
