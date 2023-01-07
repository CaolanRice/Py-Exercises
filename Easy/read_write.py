#functions to write and append to a file and then read from it and return a string

def writeToFile(filename, text):
    with open(filename, 'w') as fileObj:
        fileObj.write(text)
        

def appendToFile(filename, text):
    with open(filename, 'a') as fileObj:
        fileObj.write(text)

def readFromFile(filename):
    with open(filename, 'r') as fileObj:
        return fileObj.read()

#add user input to a file
def inputToFile(filename):
    input_string = input('Write here: ')
    with open(filename, 'w') as fileObj:
        fileObj.write(input_string)

#Allow user to name the created file and then write to it
def extraInput():
    txt_file = input('Write the name of the .txt file you would like to create')
    input_string = input('Write what you would like stored in the file: ')
    with open(txt_file, 'w') as fileObj:
        fileObj.write(input_string)


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
inputToFile('input.txt')
extraInput()
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

