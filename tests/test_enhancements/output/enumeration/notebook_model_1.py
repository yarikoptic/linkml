# Auto generated from notebook_model_1.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-01-27T02:54:10
# Schema: simple
#
# id: http://example.org/test/simple
# description: Very simple enumeration
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
import sys
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional, Union

from jsonasobj2 import JsonObj, as_dict
from linkml_runtime.linkml_model.meta import (EnumDefinition, PermissibleValue,
                                              PvFormulaOptions)
from linkml_runtime.linkml_model.types import String
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import \
    dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import camelcase, sfx, underscore
from linkml_runtime.utils.metamodelcore import bnode, empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (YAMLRoot, extended_float,
                                            extended_int, extended_str)
from rdflib import Namespace, URIRef

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PLAY = CurieNamespace('play', 'http://example.org/test/play/')
DEFAULT_ = PLAY


# Types

# Class references
class PositionalRecordId(extended_str):
    pass


@dataclass
class PositionalRecord(YAMLRoot):
    id: Union[str, PositionalRecordId] = None
    position: Union[str, "OpenEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PositionalRecordId):
            self.id = PositionalRecordId(self.id)

        if self._is_empty(self.position):
            self.MissingRequiredField("position")
        if not isinstance(self.position, OpenEnum):
            self.position = OpenEnum(self.position)

        super().__post_init__(**kwargs)


# Enumerations
class OpenEnum(EnumDefinitionImpl):
    """
    Baseline enumeration -- simple code/value pairs, where the value (description) is optional
    """
    a = PermissibleValue(text="a",
                         description="top")
    b = PermissibleValue(text="b",
                         description="middle")
    c = PermissibleValue(text="c",
                         description="bottom")
    d = PermissibleValue(text="d")

    _defn = EnumDefinition(
        name="OpenEnum",
        description="Baseline enumeration -- simple code/value pairs, where the value (description) is optional",
    )

# Slots
