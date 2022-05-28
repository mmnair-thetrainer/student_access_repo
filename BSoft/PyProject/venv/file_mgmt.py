import os

fileHandle = open("sample_text.txt","w")
str = "Hello Neethu, This is our first file operation text"
fileHandle.write(str)
print("FileName is: ", fileHandle.name)
print("FileMode is: ", fileHandle.mode)
print("FileClosed is: ", fileHandle.closed)
fileHandle.close()
print("FileClosed is: ", fileHandle.closed)

try:
    fileRHandle = open("second_text.txt","r")
    print(fileRHandle.read(10))
    print(fileRHandle.tell())
    print(fileRHandle.read(10))
    print(fileRHandle.tell())
    print(fileRHandle.read(10))
    print(fileRHandle.tell())
except IOError:
    print("Error: The file can't be opened.")
else:
    print("File reading completed.")
fileHandle.close()

#os.rename("this_text.txt","deletable_text.txt")
#os.remove("deletable_text.txt")