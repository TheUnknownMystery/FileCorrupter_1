import random

FileInput = str(input())


def CorrouptFile(File): 
    FilePath = File.strip()

    # Storing the file_OBJ in a file and reading every line
    File_OBJ = open(FilePath, 'r')

    # Reading the Files lines
    File_OBJ_Lines = File_OBJ.readline()

    # Ready to use variable for stoaring the lines
    Final_Text_Lines = ''

    # Running throughh each file and storing the lines
    for words in File_OBJ_Lines:
        Final_Text_Lines = words

    # Writing all the message
    RandomMessage = ['Sorry text encoder is not found', 'Error: ob system auto fail 1111',
                     'System TERMINATED' 'ERROR: nothing found please reinstall system cannot find error please install error error please close file cannot recive text please find data binary search entre']

    RandomChoice = random.choice(RandomMessage)

    File_OBJ_Read = open(FilePath, 'w')
    File_OBJ_Read.write(str(RandomChoice))

CorrouptFile(FileInput)