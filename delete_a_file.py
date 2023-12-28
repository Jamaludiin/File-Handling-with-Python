import os

# os.remove("/Users/jamalabdullahi/Python Tutorial/File Handling with Python/created_file.txt")

# good practice is to check if such file exist or not
file_path = "/Users/jamalabdullahi/Python Tutorial/File Handling with Python/created_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("the file is removed")
else:
    print("the file does not exist any more")


#--------------------------------------------------------------------------------------------------
# if you want to remove directory ot folder use this style
#  os.rmdir("path")