"""
read mode -  is the default mode. we can only read the contents of the file when we open it in read mode

functions
---------
read() - will read the entire contents of the file
read(bytes) - will read the specified number of bytes from the file

readline() - will read one line at a time
readline(bytes) - reads the specified number of bytes from the line

readlines() - it will read all the lines from the file and stores it in a list. each line is one element of the list
readlines(bytes) - it will print the entire line where the byte falls

"""
FL = open('C:/Training/PycharmProjects/Cigna_DataAnalytics/Day03/data.txt', "r")

# st = FL.read(500)
# print(st)

# st = FL.readline(850)
# print(st)

st = FL.readlines(900)
print(st)

# for line in FL.readlines():
#     print(line)

FL.close()
