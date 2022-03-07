import os
from os import path
import shutil
import glob
import stat

def copytree(src, dst, symlinks=False, ignore=None):
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for item in os.listdir(src):
        print("item:",item)
        s=os.path.join(src,item)
        print("s:",s)
        d=os.path.join(dst,item)
        print("d:",d)

        if os.path.isdir(s):
            copytree(s,d,symlinks,ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)


copytree("C:/Users/USER/Desktop/aaa","C:/Users/USER/Desktop/result")