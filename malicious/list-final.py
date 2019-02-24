import xml.etree.ElementTree as ET
permission = []
for i in range(1,743):
	file = "AndroidManifest" + str(i) + ".xml";
	tree = ET.parse(file)
	root = tree.getroot()
	temp = []

	for item in root.iter('uses-permission'):
		x = item.get("{http://schemas.android.com/apk/res/android}name")
		temp.append(x)

	if len(temp) != 0 : permission.append(temp)

