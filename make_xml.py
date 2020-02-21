import os
import xml.etree.ElementTree as ET

dir_path = "/Users/watanabekai/Documents/research/program/gui_pra/images"
xml_save_path = '/Users/watanabekai/Documents/research/program/gui_pra/images_xml'

class_names = os.listdir(dir_path)
for class_name in class_names:
    images_names = os.listdir(dir_path + '/' + class_name)
    for image_name in images_names:
        split_name = os.path.splitext(image_name)[0]
        roots = ET.Element('root', {'title': split_name})
        category = ET.SubElement(roots, {'class_name': class_name})
        # xml_file = open(split_name + '.xml', 'w')
        ET.dump(roots)
        # xml_file.close()

        tree = ET.ElementTree(roots)
        xml_filename = split_name + '.xml'
        tree.write(xml_filename)