
import xml.etree.ElementTree as ET

tree1 = ET.parse('./annotations.xml')
tree2 = ET.parse('./annotations-2.xml')
tree3 = ET.parse('./annotations-3.xml')
root1 = tree1.getroot()
root2 = tree2.getroot()
root3 = tree3.getroot()

def figure_count(root):
    img = len(root.findall('image'))
    figure = 0
    img_mark = 0
    for i in range(len(root)):
        if root[i].tag == 'image':
            if len(root[i]):
                figure = figure + len(root[i])
                if root[i][0].tag == 'box' or root[i][0].tag == 'polygon':
                    img_mark = img_mark + 1
    return figure

def figure_mark_count(root):
    img = len(root.findall('image'))
    figure = 0
    img_mark = 0
    for i in range(len(root)):
        if root[i].tag == 'image':
            if len(root[i]):
                figure = figure + len(root[i])
                if root[i][0].tag == 'box' or root[i][0].tag == 'polygon':
                    img_mark = img_mark + 1
    return img_mark

figure_count = figure_count(root1)        #+ figure_count(root2) + figure_count(root3)

img_mark_count = figure_mark_count(root1)          #+ figure_mark_count(root2) + figure_mark_count(root3)

img_count = len(root1.findall('image'))           #+ len(root2.findall('image')) + len(root3.findall('image'))

print('изображений =', img_count)
print('размечено изображений =', img_mark_count)
print('не размечено изображений =', (img_count - img_mark_count))
print('количество фигур =', figure_count)

#extremum_S изображений
squares = []
count_min = 0
count_max = 0

for elem in root1.iter('image'):
    a = elem.attrib.get('width')
    h = elem.attrib.get('height')
    S = int(a) * int(h)
    squares.append(S)

for elem in root1.iter('image'):
    a = elem.attrib.get('width')
    h = elem.attrib.get('height')
    S = int(a) * int(h)
    if S == int(max(squares)):
        max_width = a
        max_height = h
        max_elem = elem.attrib.get('name')
        count_max += 1

for elem in root1.iter('image'):
    a = elem.attrib.get('width')
    h = elem.attrib.get('height')
    S = int(a) * int(h)
    if S == int(min(squares)):
        min_width = a
        min_height = h
        min_elem = elem.attrib.get('name')
        count_min += 1

if count_max > 1:
    print ('Самые большие изображения.', 'Одно из них: название -', max_elem, 'ширина =', max_width, 'высота =', max_height)
    print('количество самых больших изображений', count_max)
else: 
    print('Самое большое изображение: название -', max_elem, 'ширина =', max_width, 'высота =', max_height)

if count_min > 1:
    print ('Самые маленькие изображения.', 'Одно из них: название -', min_elem, 'ширина =', min_width,'высота =', min_height,)
    print('количество самых маленьких изображений', count_min)
else:
    print ('Самое маленькое изображение: название -', min_elem, 'ширина =', min_width,'высота =', min_height,)
