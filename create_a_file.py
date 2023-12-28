import os


#--------------------------------------------------------------------------------------------------
"""

# use the open() method and specify the path and name of the file to be created and "x" as create file parameter
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/created_file.txt","x")# make sure you pass the "create parameter "x" at the end"
# the file must not be existed other wise it will return error

# now write in to it
is_written = var_file.write("I am free for the weekend")

var_file.close()

"""

#--------------------------------------------------------------------------------------------------
# Followed this procedure as well to make sure the error will not happen if exist

file_path = "/Users/jamalabdullahi/Python Tutorial/File Handling with Python/created_file.txt"

# Check if the file exists
if os.path.exists(file_path):
    print("File already exists")
else:
    # If the file doesn't exist, create a new one
    var_file = open(file_path, "w") 
    print("File created")
    var_file.close()




#--------------------------------------------------------------------------------------------------
"""
# you can also use with statement

file_path = "/Users/jamalabdullahi/Python Tutorial/File Handling with Python/created_file.txt"

# Check if the file exists
if os.path.exists(file_path):
    print("File already exists")
else:
    # If the file doesn't exist, create a new one
    with open(file_path, "w") as file:
        print("File created")


"""