"""Python definition of the parts

"""
from typing import List, Tuple

from pydantic import BaseModel, ConfigDict

from midom.constants import ActionCode
from midom.identifiers import PrivateBlockTagIdentifier, TagIdentifier


class BooleanFunction(BaseModel):
    criteria: str

class PixelArea(BaseModel):
    area: str


class Protocol(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    tags: List[Tuple[TagIdentifier, ActionCode]]
    filters: List[BooleanFunction]
    pixel: List[Tuple[BooleanFunction, PixelArea]]
    private: List[PrivateBlockTagIdentifier]
