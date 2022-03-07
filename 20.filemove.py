import os
from os import path
import shutil
from distutils.dir_util import copy_tree


origin="C:/Users/USER/Desktop/txt/jpg"

files=os.listdir(origin)
for file in files:
    print(file)
    #print(origin+"/"+file)
    try:

            place=file[9:15]

            if place in ["O01001","O01002","O01003","O01004","O01005","O01006","O01007","O01008","O01009"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/1.운동")
                continue

            if place in ["O02010","O02011","O02012","O02013"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/2.업무")
                continue

            if place in ["O03014","O03015","O03016","O03017"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/3.여행")
                continue

            if place in ["O04018","O04019","O04020","O04021"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/4.여가")
                continue

            if place in ["O05022","O05023","O05024","O05025","O05026"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/5.애완용")
                continue

            if place in["O06027","O06028","O06029","O06030"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/6.야생")
                continue

            if place in ["O07031","O07032","O07033","O07034","O07035"]:
                shutil.move(origin+"/"+file, "E:/final_jpg_최종/1.실외/7.자동차")
                continue

            if place in ["O08036","O08037","O08038"]:      
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/8.비행기")
                continue

            if place in ["O09039","O09040","O09041","O09042"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/9.배")
                continue

            if place in ["O10043","O10044","O10045"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/10.이륜차")
                continue

            if place in ["O11046","O11047","O11048"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/11.기타")
                continue
            
            if place in ["O12049","O12050","O12051","O12052","O12053","O12054","O12055"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/1.실외/12.사물")
                continue

            if place in ["I01001","I01002","I01003","I01004","I01005","I01006","I01007"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/1.운동")
                continue
        
            if place in ["I02008","I02009","I02010"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/2.업무")
                continue

            if place in ["I03011","I03012","I03013"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/3.여행")
                continue

            if place in ["I04014","I04015"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/4.여가")
                continue

            if place in ["I05016","I05017","I05018"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/5.애완동물")
                continue

            if place in ["I06019","I06020"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/6.자동차")
                continue

            if place in ["I07021"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/7.비행기")
                continue

            if place in ["I08022","I08023","I08024"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/8.기타")
                continue

            if place in ["I09025","I09026","I09027","I09028","I09029","I09030","I09031","I09032"]:
                shutil.move(origin+"/"+file,"E:/final_jpg_최종/2.실내/9.사물")
                continue


    except Exception as e:
        print(e)
        print("오류파일:".format(file))