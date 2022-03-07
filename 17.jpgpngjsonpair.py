import os
import json
import glob
import csv


json_dir = "D:\\Sample\\라벨링데이터\\json"
jpg_dir="D:\\Sample\\원천데이터\\jpg"
png_dir="D:\\Sample\\라벨링데이터\\png"

json_count = 0
jpg_count = 0
png_count =0

json_Arr = [] 
jpg_Arr = [] 
png_Arr = []

json_NG = [] 
jpg_NG = [] 
png_NG = []

json_NG_count=0
jpg_NG_count=0
png_NG_count=0


for (path, dirs, files) in os.walk(jpg_dir):
    for i in files:
        if i.endswith(".jpg"): 
            jpg_Arr.append(i.split(".")[0]) 
            jpg_count += 1 


print("수령된 jpg 파일 : {}개".format(jpg_count))


for (path, dirs, files) in os.walk(png_dir):
    for i in files:
        if i.endswith(".png"): 
            png_Arr.append(i.split(".")[0]) 
            png_count += 1 


print("수령된 png 파일 : {}개".format(png_count))


for (path, dirs, files) in os.walk(json_dir):
    for i in files:
        if i.endswith(".json"): 
            json_Arr.append(i.split(".")[0]) 
            json_count += 1

print("수령된 json 파일 : {}개".format(json_count))



for i in jpg_Arr:
    if i not in json_Arr:
        jpg_NG.append(i+'.json')
        jpg_NG_count+=1 

    if i not in png_Arr:
        jpg_NG.append(i+'.png')
        jpg_NG_count+=1 

print("json,png와 pair가 안되는 jpg:{}개".format(jpg_NG_count))
print(jpg_NG)



for i in json_Arr:
    if i not in jpg_Arr:
        json_NG.append(i+'.jpg')
        json_NG_count+=1

    if i not in png_Arr:
        json_NG.append(i+'.png')
        json_NG_count+=1
     
 
print("jpg,png와 pair가 안되는 json:{}개".format(json_NG_count))
print(json_NG)


for i in png_Arr:
    if i not in jpg_Arr:
        png_NG.append(i+'.jpg')
        png_NG_count+=1

    if i not in json_Arr:
        png_NG.append(i+'.json')
        png_NG_count+=1
     
 
print("jpg,json와 pair가 안되는 png:{}개".format(png_NG_count))
print(png_NG)
