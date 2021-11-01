import json
from PIL import Image

img = Image.open('example.jpg')
imgWidth, imgHeight = img.size
img = img.convert("RGBA")
imgdata = img.getdata()

x_pos = 0
y_pos = 1

pixel_value = []
x = []
y = []
data = {}
counter = 1

for item in imgdata:
    if (x_pos) == imgWidth:
        x_pos = 1
        y_pos += 1
    else:
        x_pos += 1
    if item[3] != 0:
        data[f'CASE={counter}'] = item[2]
        x.append(x_pos)
        y.append(y_pos)
        counter += 1

json_object = json.dumps(data, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)