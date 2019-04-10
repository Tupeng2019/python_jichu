import xml.etree.ElementTree as et

stu = et.Element("Student1")  # 生成一个新的元素

name = et.SubElement(stu, 'Name') # 生成一个子元素1
name.attrib = {'lang','en'}    # 生成的属性1
name.text = 'maozedong'


age = et.SubElement(stu, 'Age') # 生成子元素 2
age.text = 18

et.dump(stu)