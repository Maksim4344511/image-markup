
import xml.etree.ElementTree as ET

tree1 = ET.parse('./annotations.xml')
tree2 = ET.parse('./annotations-2.xml')
tree3 = ET.parse('./annotations-3.xml')
root1 = tree1.getroot()
root2 = tree2.getroot()
root3 = tree3.getroot()

box = 0
polygon = 0

for i in range(len(root1)):
    if root1[i].tag == 'image':
        if len(root1[i]):
            for j in range(len(root1[i])):
                if root1[i][0].tag == 'box':
                    box += 1
                elif root1[i][0].tag == 'polygon':
                    polygon += 1

print('боксы: =', box)
print('полигоны =', polygon)

