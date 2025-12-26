import xml.etree.ElementTree as ET

def serialize_pattern_tree(patterns):
    root = ET.Element("patternTree")

    def build_node(p, parent):
        node = ET.SubElement(parent, "pattern")
        node.set("name", p.name)
        node.set("essence", p.essence)
        node.set("strength", str(p.strength))

        for child in p.children:
            build_node(child, node)

    for p in patterns:
        build_node(p, root)

    return ET.tostring(root, encoding="unicode")