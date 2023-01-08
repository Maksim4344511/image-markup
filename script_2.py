
import xml.etree.ElementTree as ET

tree1 = ET.parse('./annotations.xml')
tree2 = ET.parse('./annotations-2.xml')
tree3 = ET.parse('./annotations-3.xml')
root1 = tree1.getroot()
root2 = tree2.getroot()
root3 = tree3.getroot()

obj = {}
def count_class_box(root):
    for elem in root.iter('box'):
        key_obj = elem.attrib.get('label')
        if key_obj in obj:
            obj[key_obj]+=1
        else:
            obj[key_obj] = 1
    return obj

def count_class_polygon(root):
    for elem in root.iter('polygon'):
        key_obj = elem.attrib.get('label')
        if key_obj in obj:
            obj[key_obj]+=1
        else:
            obj[key_obj] = 1
    return obj



count_class_box(root1)
#count_class_box(root2)
#count_class_box(root3)
count_class_polygon(root1)
#count_class_polygon(root2)
#count_class_polygon(root3)

for i in obj:
    print(i, '=', obj[i])


