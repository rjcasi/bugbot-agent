import xml.etree.ElementTree as ET

# ---------------------------------------------------------
# Convert your in‑memory pattern registry → XML
# ---------------------------------------------------------

def serialize_pattern_tree(patterns):
    """
    Convert a list of Pattern objects into an XML tree.
    """
    root = ET.Element("patterns")

    for pattern in patterns:
        p = ET.SubElement(root, "pattern")
        ET.SubElement(p, "id").text = str(getattr(pattern, "id", ""))
        ET.SubElement(p, "name").text = getattr(pattern, "name", "")
        ET.SubElement(p, "mantra").text = getattr(pattern, "mantra", "")
        ET.SubElement(p, "essence").text = getattr(pattern, "essence", "")
        ET.SubElement(p, "structure").text = getattr(pattern, "structure", "")
        ET.SubElement(p, "slots").text = str(getattr(pattern, "slots", ""))
        ET.SubElement(p, "examples").text = str(getattr(pattern, "examples", ""))

    return ET.tostring(root, encoding="unicode")


# ---------------------------------------------------------
# Convert XML → JSON‑friendly dict for WebSocket streaming
# ---------------------------------------------------------

def pattern_tree_to_json(xml_string):
    """
    Convert the XML output of serialize_pattern_tree() into a JSON‑friendly dict.
    """
    root = ET.fromstring(xml_string)

    patterns_json = []

    for p in root.findall("pattern"):
        patterns_json.append({
            "id": p.findtext("id"),
            "name": p.findtext("name"),
            "mantra": p.findtext("mantra"),
            "essence": p.findtext("essence"),
            "structure": p.findtext("structure"),
            "slots": p.findtext("slots"),
            "examples": p.findtext("examples"),
        })

    return {"patterns": patterns_json}