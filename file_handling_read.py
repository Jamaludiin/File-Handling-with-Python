# In python we can create,read, update and delete data from file

#--------------------------------------------------------------------------------------------------
# Open file before you Read data from a file using read() method
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt")

print(var_file) # displays something like this: <_io.TextIOWrapper name='/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt' mode='r' encoding='UTF-8'>

#--------------------------------------------------------------------------------------------------
# Then read now from them
print()
print(var_file.read()) # display all data from the txtfile 

# Note: after you read() data a file you must close and reopen at the next time
var_file.close()

#--------------------------------------------------------------------------------------------------
# lets read only few text by specifying the number of charecters needed the index starts 1 to n
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt", "r") # open is must again since you closed before
print("\nAfter reading 10 Lines and result is as follow:")
print(var_file.read(10)) # it reads the first 10 charecters, Note: space will be counted as well
print("Lengs of the text extracted is:", len(var_file.read(10)))

var_file.close()

#--------------------------------------------------------------------------------------------------
# Read and return one line by using the readline() method:
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt") # open is must again since you closed before
print("\nAfter reading first Line, result is as follow:")
print(var_file.readline()) # reads only one line

# if you repeat the readline() method again before you close the file, it will read the second line
print("\nAfter reading second Line, result is as follow:")
print(var_file.readline()) # reads only one line

var_file.close()


#--------------------------------------------------------------------------------------------------
# looping the file lines
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt") 
count = 1
for i in var_file:
    print("Line",count, ":",i)
    count += 1