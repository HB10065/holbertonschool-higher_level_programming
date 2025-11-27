'''Moduel Doc'''
import xml.etree.ElementTree as ET
import json


def serialize_to_xml(dictionary, filename):
    '''Serialize to XML'''
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    '''Deserialize from XML'''
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
