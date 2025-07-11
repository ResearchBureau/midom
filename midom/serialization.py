"""Loading and saving protocol objects to disk"""
from json import JSONEncoder
from typing import DefaultDict, Dict, List, Tuple

from pydantic import BaseModel

from midom.components import BooleanFunction, Filter, PixelArea, PixelOperation, \
    Protocol
from midom.constants import ActionCode, ActionCodes
from midom.identifiers import (
    PrivateBlockTagIdentifier,
    TagIdentifier,
    tag_identifier_from_string,
)


class ProtocolEncoder(JSONEncoder):
    """Encodes all objects used in midom.components.Protocol to JSON"""

    def default(self, o):
        if isinstance(o, TagIdentifier):
            return o.key()
        elif isinstance(o, ActionCode):
            return o.var_name
        elif isinstance(o, BooleanFunction):
            return "BooleanFunctiong TODO"
        elif isinstance(o, PixelArea):
            return "PixelArea TODO"
        elif isinstance(o, Protocol):
            return o.__dict__
        else:
            return super().default(o)


class SerializedProtocol(BaseModel):
    """Intermediate data structure for saving and loading a protocol to JSON.

    Notes
    -----
    Why an extra data structure? Pydantic is good at serializing and deserializing
    objects. But the Protocol object contains elements that are not directly
    pydantic-serializable. Some of these objects can be serialized and deserialized if
    you have domain knowledge. For instance, the 'tags' attribute contains
    'TagIdentifier' objects that can be represented by a single string and re-created
    from this single string. I just don't want to load this very specific domain
    knowledge int the Protocol object itself. I want that to stay clean and re-usable
    for many other purposes other than serialization. I also don't want to mess
    with the more intricate pydantic decorators for field serialization. It's just
    too complex, too generic and hard to read for this purpose.
    An intermediate structure seems the cleanest here.

    tags: Dict[str, List[TagAction]]
    filters: List[Filter]
    pixel: List[PixelOperation]
    private: List[PrivateAllowGroup]

    """

    tags: Dict[str, Dict[str,tuple[str, str]]]
    filters: List[tuple[str,str]]
    pixel: List[tuple[str,str,list[tuple[int,int,int,int]]]]
    private: List[tuple[str, List[str]]]


class ProtocolSerializer:
    """Can translate a Protocol instance to a JSON string and back.

    Uses SerializedProtocol as intermediate step. See docstring there for reasons.
    """

    def to_json(self, protocol: Protocol) -> str:
        return self.to_serializable(protocol).model_dump_json(indent=2)

    @staticmethod
    def to_serializable(protocol: Protocol) -> SerializedProtocol:
        tags = DefaultDict(dict)
        for sopclass_id, tag_action_list in protocol.tags.items():
            for x in tag_action_list:
                tags[sopclass_id][x.identifier.key()] = (x.action.key, x.justification)


        return SerializedProtocol(
            tags=tags,
            filters=[(x.criterion.criterion, x.justification) for x in protocol.filters],
            pixel=[(x.description, x.criterion.criterion, list(y.area for y in x.areas) ) for x in protocol.pixel],
            private=[(x.justification, [y.key() for y in x.elements]) for x in protocol.private]
        )

    @staticmethod
    def from_deserialized(deserialized: SerializedProtocol) -> Protocol:
        """Transform SerializedProtocol to fit Protocol data signature:

        tags: Dict[str, List[TagAction]]
        filters: List[Filter]
        pixel: List[PixelOperation]
        private: List[PrivateAllowGroup]
        """

        tags = {}
        for sop_class_id, tag_list in deserialized.tags.items():
            tags[sop_class_id] = {
                (tag_identifier_from_string(x), ActionCodes.from_string(y[0]))
                for x, y in tag_list.items()
            }
        return Protocol(
            tags=tags,
            filters=deserialized.filters,
            pixel=deserialized.pixel,
            private=[
                PrivateBlockTagIdentifier(x) for x in deserialized.private
            ],
        )

    def from_json(self, json_str: str) -> Protocol:
        return self.from_deserialized(
            SerializedProtocol.model_validate_json(json_str)
        )
