"""Loading and saving protocol objects to disk"""
import json
from json import JSONEncoder
from typing import Dict, List, Tuple

from midom.components import BooleanFunction, PixelArea, Protocol
from midom.constants import ActionCode, ActionCodes
from midom.identifiers import PrivateBlockTagIdentifier, SingleTag, TagIdentifier, \
    tag_identifier_from_string
from pydantic import BaseModel

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
    """
    tags: Dict[str, str]
    filters: List[BooleanFunction]
    pixel: List[Tuple[BooleanFunction, PixelArea]]
    private: List[str]


class ProtocolSerializer:
    """Can translate a Protocol instance to a JSON string and back.

    Uses SerializedProtocol as intermediate step. See docstring there for reasons.
    """

    def to_json(self, protocol: Protocol) -> str:
        return self.to_serializable(protocol).model_dump_json(indent=2)

    @staticmethod
    def to_serializable(protocol: Protocol) -> SerializedProtocol:
        return SerializedProtocol(
            tags={identifier.key(): action.var_name for (identifier, action) in protocol.tags},
            filters=protocol.filters,
            pixel=protocol.pixel,
            private=[identifier.key() for identifier in protocol.private])

    def from_deserialized(self, deserialized: SerializedProtocol) -> Protocol:
        """Transform SerializedProtocol to fit Protocol data signature:

        tags: List[Tuple[TagIdentifier, ActionCode]]
        filters: List[BooleanFunction]
        pixel: List[Tuple[BooleanFunction, PixelArea]]
        private: List[PrivateBlockTagIdentifier]
        """
        # TODO: do not cast to SingleTag but cast to any Identifier subtype
        return Protocol(tags=[(tag_identifier_from_string(x),
                               ActionCodes.from_string(y)) for x,y in deserialized.tags.items()],
                        filters=deserialized.filters,
                        pixel=deserialized.pixel,
                        private=[PrivateBlockTagIdentifier(x) for x in deserialized.private])


    def from_json(self, json_str: str) -> Protocol:
        return self.from_deserialized(SerializedProtocol.model_validate_json(json_str))


class ProtocolDecoder:
    """Parses the output of ProtocolEncoder"""

    def decode(self, string_in):
        """Decode json string into a Protocol"""
        object_in = json.loads(string_in)


        test = 1




