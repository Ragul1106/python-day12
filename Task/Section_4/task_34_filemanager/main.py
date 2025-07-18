# Create test.txt 
with open("test.txt", "w") as f:
    f.write("This is a test file.\n")

from Python_learning_module.Day12.Task.Section_4.task_34_filemanager.copy import copy_file
from Python_learning_module.Day12.Task.Section_4.task_34_filemanager.move import move_file
from Python_learning_module.Day12.Task.Section_4.task_34_filemanager.delete import delete_file

# File operations
copy_file("test.txt", "copy_test.txt")
move_file("copy_test.txt", "moved_test.txt")
delete_file("moved_test.txt")

print("All file operations completed.")
