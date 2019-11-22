# ------------------------------------------------- #
# Title: Pickling & Structured Error Handling
# Description: Examples of pickling a file and using error handling
# ChangeLog: (Who, When, What)
# <PShoup>,<11.20.2019>,Created Script
# ------------------------------------------------- #
import pickle

strFileName = 'PetData.dat'
lstPet = []


def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()


def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data


strType = str(input("Enter pet type (cat, dog, etc.): "))
strName = str(input("Enter pet name: "))
intAge = int(input("Enter pet age: "))
lstPet = [strType, strName, intAge]

save_data_to_file(strFileName, lstPet)

print(read_data_from_file(strFileName))
