from PIL import Image
import io

inputFile = "Example Files\CoelaToot.png"
outputFile = "Output\CoelaToot.h"
pictureOutput = "Output\CoelaToot.png"
name = "CoelaToot"
numColors = 16 

def GetData(className, file):
    image = Image.open(file).convert("P", palette = Image.ADAPTIVE, colors = numColors)
    image.save(pictureOutput)
    w, h = image.size
    
    image.seek(0)
    pal = image.getpalette()

    data = "#pragma once\n\n"
    data += "#include \"..\..\Materials\Image.h\"\n\n"
    data += "class " + className + " : public Image{\n"
    data += "private:\n"
    data += "\tstatic const uint8_t rgbMemory[];\n"
    data += "\tstatic const uint8_t rgbColors[];\n\n"
    data += "public:\n"
    data += "\t" + className + "(Vector2D size, Vector2D offset) : Image(rgbMemory, rgbColors, " + str(w) + ", " + str(h) + ", " + str(numColors) + ") {\n"
    data += "\t\tSetSize(size);\n"
    data += "\t\tSetPosition(offset);\n"
    data += "\t}\n};\n\n"

    data += "const uint8_t " + className + "::rgbMemory[] PROGMEM = {"
    
    for i in range(h):
        for j in range(w):
            index = image.getpixel((j, i))

            data += str(index)
            
            if i == h - 1 and j == w - 1:
                data += "};\n\n"
            else:
                data += ","

    data += "const uint8_t " + className + "::rgbColors[] PROGMEM = {"
    
    pal = image.getpalette()

    for i in range(numColors):
        r = pal[i * 3]
        g = pal[i * 3 + 1]
        b = pal[i * 3 + 2]

        data += str(r) + "," + str(g) + "," + str(b)
        
        if i == numColors - 1:
            data += "};\n"
        else:
            data += ","

    return data


output = GetData(name, inputFile)

print(output)
f = open(outputFile, "w")
f.write(output)
f.close()