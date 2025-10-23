"""
append mode -
1.if the file already exists then we add the contents into the file without disturbing the previous (existing) contents
2. if the file is not present it will create a new file and then add the contents to it
"""

FA = open("myfile.txt", "a")

data = input("Enter the contents of the file :")
FA.write(data + "\n")

FA.close()