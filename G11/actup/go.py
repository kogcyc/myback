
import os
import shutil

#path = './new/'

if os.path.exists("newbie"):
    shutil.rmtree("newbie")

os.mkdir("newbie")

f = open("newbie/finally.md", "w")
f.write("# zowie! #")
f.close()
