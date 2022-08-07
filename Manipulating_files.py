####open the text file
# with open("cool_doc.txt") as cool_doc :
#     read_file = cool_doc.read()

# print(read_file)

####open the text file using with traditional approach
# cool_doc = open('cool_doc.text', 'r')

# read_file = cool_doc.read()

# cool_doc.close()

# print(read_file)

###read lines of a text file
# with open("cool_doc.txt", "r") as cool_doc:
#      read_file = cool_doc.readlines()
     
# for list in read_file:
#     print(type(list))

# print(type(read_file))

###open file in other mode (write mode)
# with open("cool_doc.txt", "w") as cool_doc:
#      write_file = cool_doc.write('i have overwritten everthing, because i am a write method!')

# print(write_file)
     
###open file in other mode (append mode)
with open("cool_doc.txt", "a") as cool_doc:
     cool_doc.write('i have appended this line, because i am an append method!')

# print(write_file)

