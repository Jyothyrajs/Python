
## List directory
#  List all python files 
import os
import re
import subprocess

c_root = os.path.join('..','python')
print(c_root)
for directory, subdir_list, file_list in os.walk(c_root):
    print('Files in Directory:', directory)
    print("Subdir list")
    for s_dir in subdir_list:
        print( s_dir)

    regex = re.compile("[a-z0-9_]*.py", re.IGNORECASE)
    for name in file_list:
        if( re.match(regex,name)):
            print(name)