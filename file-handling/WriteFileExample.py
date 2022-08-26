"""
    Write file:
    "a" - Append - will append to the end of the file

    "w" - Write - will overwrite any existing content
"""

from ReadFileExample import ReadFile
import os


class WriteFile:

    def __init__(self, file=''):
        self.file = file

    def openFileAndAppendContent(self):
        print('1. Updating file by writing file :-')
        file = open(self.file, 'a')
        file.write("Appending new line to existing file\n")
        file.close()

        readFile = ReadFile(self.file)
        readFile.readCompleteContent()

    def openFileAndOverwrite(self):
        print('2. Updating file by deleting old content of the file and adding new content :-')
        file = open(self.file, "w")
        file.write("Overwrite file content and adding the new content\n")
        file.close()

        readFile = ReadFile(self.file)
        readFile.readCompleteContent()

    """
        To create a new file in Python, use the open() method, with one of the following parameters:

            "x" - Create - will create a file, returns an error if the file exist

            "a" - Append - will create a file if the specified file does not exist

            "w" - Write - will create a file if the specified file does not exist
    """
    def createNewFile(self):
        print(f'3. Creating new File.\n')
        newFileName = 'myNewFile1.txt'
        if os.path.exists(newFileName):
            print(f'{newFileName} already exists!\n')
        else:
            open(newFileName, 'x')
            print(f'New File created {newFileName}\n')


    def CreateNewFileIfNotExists(self):
        print(f'4. Creating new File if does not exists\n')
        newFileName = 'myNewFile5.txt'
        open(newFileName, 'w')


if __name__ == '__main__':
    writeFile = WriteFile(file='demoFile.txt')
    writeFile.openFileAndAppendContent()
    writeFile.openFileAndOverwrite()
    writeFile.createNewFile()
    writeFile.CreateNewFileIfNotExists()
