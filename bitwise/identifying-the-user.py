import os
import pwd

print(os.getlogin())

print(os.getuid()) # NOT FOR WINDOWS

for id in pwd.getpwall(): # NOT FOR WINDOWS
    print(id[0])

