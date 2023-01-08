import xml.etree.ElementTree as ET

tree = ET.parse('./annotations.xml')
root = tree.getroot()

#изменить порядок id
arr = []
for elem in root.iter('image'):
    arr.append(elem.attrib.get('id'))

arr.reverse()
num_id = 0

for elem in root.iter('image'):
    elem.set('id', arr[num_id])
    num_id += 1

#Изменение формата файлов
for elem in root.iter('image'):
    string = elem.attrib.get('name')
    edited = string.replace('.jpg', '.png')
    elem.set('name', edited)

#Удаление пути в названии файла
for elem in root.iter('image'):
    string = elem.attrib.get('name')
    n = string.rfind('/')
    edited = string[(n + 1):]
    elem.set('name', edited)

tree.write('newitems.xml', encoding="UTF-8")
