try:
    file = open("sample.txt","r")
except FileNotFoundError:
    print("This file is not on the disk. Do you wish to create one this name?")
except IOError:
    print("Seems like file has been corrupted.")
else:
    print("Opening the file in a second")
finally:
    print("Transation completed")
