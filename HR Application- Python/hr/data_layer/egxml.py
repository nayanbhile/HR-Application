from xml.etree import ElementTree
f=open("dbconfig.xml","rt")
xmlTree=ElementTree.parse(f)
f.close()
rootNode=xmlTree.getroot()
print(rootNode.tag)
for node in rootNode:
    print(node.tag," --> ",node.text)