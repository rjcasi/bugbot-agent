# core/patterns/deserializer.py

import xml.etree.ElementTree as ET
from core.patterns.registry import Pattern

def deserialize_pattern_tree(xml_string):
    root = ET.fromstring(xml_string)
    patterns = []

    for p in root.findall("pattern"):
        patterns.append(
            Pattern(
                id=int(p.findtext("id")),
                name=p.findtext("name"),
                mantra=p.findtext("mantra"),
                essence=p.findtext("essence"),
                structure=p.findtext("structure"),
                slots=p.findtext("slots").split(", "),
                examples=p.findtext("examples").split(", ")
            )
        )

    return patterns