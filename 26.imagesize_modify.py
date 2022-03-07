import sys
import cv2
from PIL import Image
import os,glob
import shutil


main_path="E:/Inpainting_v/Inpainting_v28/jpg"

for path,dirs,files in os.walk(main_path):
    for file in files:
        if file.endswith(".jpg"):
            a=Image.open(path+"\\"+file)
            #print(a.size)
            if a.size == (1920,1080):
                pass
            
            if a.size!=(1920,1080):
                print("사진크기오류:{}".format(file))
                img_name=os.path.splitext(file)
                print(img_name[0])
                b=a.resize((1920,1080))
                os.chdir("C:/Users/USER/Desktop/namecheck/aa")
                b.save(img_name[0]+".jpg")
 







            