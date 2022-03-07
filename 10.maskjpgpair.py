import os
import json
import glob
import csv


json_dir = "E:\\Inpainting_v\\Inpainting_v30\\M"
jpg_dir="E:\\Inpainting_v\\Inpainting_v30\\jpg"
json_count = 0
jpg_count = 0
json_Arr = [] # json 파일명 리스트
jpg_Arr = [] # jpg 파일명 리스트
json_NG = [] # NG된 json파일 리스트
jpg_NG = [] # NG된 jpg파일 리스트
json_NG_count=0
jpg_NG_count=0


for (path, dirs, files) in os.walk(jpg_dir):
    for i in files:
        if i.endswith(".jpg"):
            if i.split("_")[3][0]=="F": # 현재 폴더와 최하위 폴더까지 탐색해 json파일 탐색
                jpg_Arr.append(i.split(".")[0]) # 탐색된 json파일명 json_Arr에 리스트로 할당
                jpg_count += 1 # 탐색된 json파일 갯수 확인


print("수령된 jpg 파일 : {}개".format(jpg_count))
#print(jpg_Arr)
#print("---------------------------------------------------")      

for (path, dirs, files) in os.walk(json_dir):
    for i in files:
        if i.endswith(".json"): 
            if i.split("_")[3][0]=="F":
                m=i.split(".")[0]
                json_Arr.append(m.split("_")[0]+"_"+m.split("_")[1]+"_"+m.split("_")[2]+"_"+m.split("_")[3])
                json_count += 1

print("수령된 json 파일 : {}개".format(json_count))
#print(json_Arr)
#print("---------------------------------------------------")

for i in jpg_Arr:
    if i not in json_Arr:
        jpg_NG.append(i+".jpg")
        jpg_NG_count+=1


print("json과 pair가 안되는 jpg:{}개".format(jpg_NG_count))
print(jpg_NG)
#print("---------------------------------------------------")


for i in json_Arr:
    if i not in jpg_Arr:
            json_NG.append(i+"_"+"M"+'.json')
            json_NG_count+=1

 
print("json와 pair가 안되는 json:{}개".format(json_NG_count))
print(json_NG)
# #print("---------------------------------------------------")