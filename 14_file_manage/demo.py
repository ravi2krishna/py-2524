# Working With Files & Folders(Directories)
# Use Persistent Storage 

# syntax - 1
file = open("14_file_manage/file.txt","r")
print(file)
print(file.closed)
file.close() # explicitly closing
print(file.closed)

# syntax - 2
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file_data.closed)

# Reading Data From File - whole file  
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())

# Reading Data From File - whole character wise   
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read():
        print(char)
        
# Reading Data From File - whole word wise    
with open("14_file_manage/file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)

# Reading Data From File - whole line wise (one line)   
with open("14_file_manage/file.txt","r") as file_data:
        print(file_data.readline())
        
# Reading Data From File - whole line wise (multiple lines)   
with open("14_file_manage/file.txt","r") as file_data:
        print(file_data.readlines())
        
# Reading Data From File - whole lines from list
with open("14_file_manage/file.txt","r") as file_data:
        list_data = file_data.readlines()
        for line in list_data:
            print(line.strip())
            
# Write Mode 
# Writing Data To File 
# Using write mode, we can create files 

# write mode, to create file
with open("14_file_manage/write.txt","w") as file_data:
    print(file_data)
    
# write mode, write content to file 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("hello")
    
# write mode, write content to file with multiple lines
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['Hello there how are you\n', 'are you coming to class today'])

# Overrides Data    
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['Line 3\n', 'Line 4'])    

# append mode, write content to file with multiple lines
with open("14_file_manage/new.txt","w") as file_data:
    file_data.writelines(['Hello there how are you\n', 'are you coming to class today\n'])
    
# append Data    
with open("14_file_manage/new.txt","a") as file_data:
    file_data.writelines(['Line 3\n', 'Line 4']) 
    
# Working Folder / Directory 

# Create Folder / Directory 
import os 
directory_name = "14_file_manage/students_data"     
if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Create file
with open("14_file_manage/students_data/student.txt","w") as file_data:
    print(file_data)

# Delete File 
os.remove("14_file_manage/new.txt")

# Delete Empty Folder 
directory_name = "14_file_manage/test"
os.rmdir(directory_name)

# Delete Non-Empty Folder 
import shutil
directory_name = "14_file_manage/students_data"    
shutil.rmtree(directory_name)