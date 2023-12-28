# lets first add data to an existing file
"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""
#--------------------------------------------------------------------------------------------------
# Open file before you add data into a file using write() method
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt","a")# make sure you pass the "append parameter a at the end"

# now write it
is_written = var_file.write("I am free for the weekend")

print("File is written",is_written)# this return the number of charecters inserted in the file
# close the file
var_file.close()

# NOTE EVEYTIME YOU EXECUTE THE ABOVE LINE WILL BE WRITTEN AGAIN AGAIN, SO MAKE SURE THE NUMBER OF TIME YOU RUN
#--------------------------------------------------------------------------------------------------
var_file = open("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/file1.txt","r")# make sure you CHANGE TO "r" NOT "a" now

# read to check if it is sucess 
for i in var_file:
    print(i)

# close the file
var_file.close()

#--------------------------------------------------------------------------------------------------
