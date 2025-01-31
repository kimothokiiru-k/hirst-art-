import colorgram



colours = colorgram.extract('hirst.jpg', 20)
colourList = []

print(colours)

def listcolor():
    r = colours.rgb.r
    g = colours.rgb.g
    b = colours.rgb.b
    rangi = (r, g, b)
    colourList.append(rangi)
for _ in colourList:
    listcolor()

