# CS382 Project 2
# Name: Sameer Sethuram and Samantha York
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

#assembles assembly program into image file

instructions = open("instructions.txt", "r")
imgFile = open("imageFile.txt", "w")
imgFile.write("v3.0 hex words addressed\n")

allLines = instructions.readlines()
allCodes = []
hexCodes = []


def binToHex(code):
    decimal = int(code, 2)
    if decimal < 10:
        return "0" + hex(decimal)[2:]
    return hex(decimal)[2:]
    

for line in allLines:
    code = ""
    print(line.strip())
    str = line[0:3]
    if str == "ADD":
        code += "00"
    elif str == "MUL":
        code += "01"
    elif str == "LDR":
        code += "10"
    elif str == "STR":
        code += "11"

    dest = line[5:6]
    destBin = bin(int(dest)).replace("0b","")
    if len(destBin) == 1:
        destBin = "0" + destBin
    code += destBin

    firstReg = line[9:10]
    firstBin = bin(int(firstReg)).replace("0b","")
    if len(firstBin) == 1:
        firstBin = "0" + firstBin
    code += firstBin
    
    secReg = line[13]
    secBin = bin(int(secReg)).replace("0b","")
    if len(secBin) == 1:
        secBin = "0" + secBin
    code += secBin

    allCodes.append(code)
    hexCodes.append(binToHex(code))
    
    print(code)
    print(int(code, 2))
    print(binToHex(code))
    print("\n")

print(allCodes)
print(hexCodes)
print("\n")
arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
instruction = 0
for i in range(16): #00 to f0
    line = ""
    line += arr[i] + "0:"
    n = 0
    while instruction < len(hexCodes) and n < 16:
        line += " " + hexCodes[instruction]
        instruction += 1
        n += 1

    while n < 16:
        line += " 00"
        n += 1
        
    print(line)
    imgFile.write(line)
    imgFile.write("\n")

instructions.close() 
imgFile.close() 
