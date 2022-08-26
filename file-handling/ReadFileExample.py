"""
 Read file in python

 You should always close your files, in some cases,
 due to buffering, changes made to a file may not show until you close the file.
"""


class ReadFile:
    def __init__(self, file=''):
        self.file = file

    def readCompleteContent(self):
        inputFile = open(self.file, 'r')
        print('------------Execute Python read() method----------')
        print(inputFile.read())
        print('\n')
        inputFile.close()  # It is a good practice to always close the file when you are done with it.


    def readSpecificChar(self):
        inputFile = open(self.file, 'r')
        print('------------Execute Python read(7) sequence of char method----------')
        print(inputFile.read(7))
        print('\n')
        inputFile.close()  # It is a good practice to always close the file when you are done with it.


    def readLines(self):
        inputFile = open(self.file, 'r')
        print('------------Execute Python readline() method----------')
        print(inputFile.readline())  # By calling readline() two times, you can read the two first lines:
        print('\n')
        inputFile.close()  # It is a good practice to always close the file when you are done with it.


    def readLineByLine(self):
        inputFile = open(self.file, 'r')
        print('------------Execute Python: looping the file and read line by line----------')
        for line in inputFile:
            print(line)
        print('\n')
        inputFile.close()  # It is a good practice to always close the file when you are done with it.


if __name__ == '__main__':
    readFile = ReadFile(file='demoFile.txt')
    readFile.readCompleteContent()
    readFile.readSpecificChar()
    readFile.readLines()
    readFile.readLineByLine()
