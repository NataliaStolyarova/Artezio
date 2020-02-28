"""Conversion an xml-string to a tree structure."""
import xml.etree.ElementTree as ElT


def my_tree(xml_str=str):
    """Fills the dictionary with the elements
    from an xml-string."""
    tree = ElT.fromstring(xml_str)

    def fill_tree(tree):
        my_dict = {'name': tree.tag, 'children': []}
        for element in tree:
            my_dict['children'].append(fill_tree(element))
        return my_dict
    return fill_tree(tree)


print(my_tree('<root><element1 /><element2 /><element3><element4 /></element3></root>'))
