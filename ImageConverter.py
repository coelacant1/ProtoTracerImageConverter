from PIL import Image
import io

inputFile = "Example Files\CoelaToot.png"
outputFile = "Output\CoelaToot.h"
name = "CoelaToot"

def GetData():
    image = Image.open(inputFile).convert('RGB')
    w, h = image.size

    data = "#pragma once\n\n"
    data += "#include \"..\..\Materials\Image.h\"\n\n"
    data += "class " + name + " : public Image{\n"
    data += "private:\n"
    data += "\tstatic const uint8_t rgbMemory[];\n\n"
    data += "public:\n"
    data += "\t" + name + "(Vector2D size, Vector2D offset) : Image(rgbMemory, " + str(w) + ", " + str(h) +") {\n"
    data += "\t\tSetSize(size);\n"
    data += "\t\tSetPosition(offset);\n"
    data += "\t}\n};\n\n"

    data += "const uint8_t " + name + "::rgbMemory[] PROGMEM = {"
    
    for i in range(h):
        for j in range(w):
            r, g, b = image.getpixel((j, i))

            data += str(r) + "," + str(g) + "," + str(b)
            
            if i == h - 1 and j == w - 1:
                data += "};\n"
            else:
                data += ","

    return data


output = GetData()

print(output)
f = open(outputFile, "w")
f.write(output)
f.close()