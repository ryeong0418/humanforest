import os
from PIL import Image

main_path="D:/4개페어/Inpainting_v/Inpainting_v3/jpg"


def image_size():


    for path,dirs,files in os.walk(main_path):
        for file in files:
            if file.endswith(".jpg"):
                a=Image.open(path+"\\"+file)
                #print(a.size)
                if a.size == (1920,1080):
                    pass
            
                else:
                    print("사진크기 오류jpg:{}".format(file))

if __name__ == '__main__':
    image_size()
