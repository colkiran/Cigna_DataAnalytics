"""
Write mode -
1. if file is already present then deletes the content of the file and then writes new contents into the file
2. if the file is not present it will create a new file and then add the contents to it

functions
---------
1. write - to write one line at a time
2. writelines - to write more than one line into the file

"""
FW = open("myfile.txt", "w")

# data = input("Enter the contents of the file :")
# FW.write(data)

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"

FW.writelines([l1, l2, l3])

FW.close()