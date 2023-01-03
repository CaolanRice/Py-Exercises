#function to print out ASCII numbers alongside their corresponding character

def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))

printASCIITable()