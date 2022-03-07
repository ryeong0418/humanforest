import csv
import os
import glob

jpg_full_path=[]
json_full_path=[]

jpg_arr=[]
json_arr=[]

jpg_NG=[]
json_NG=[]

json_NG_count=0

for file in glob.glob("E:/jpg최종/8월/*/*.jpg"):
    json_full_path.append(file)
#print(json_full_path)

    
for file in glob.glob("E:/jpg최종/json/*/*.json"):
    jpg_full_path.append(file)
#print(jpg_full_path)

for file in jpg_full_path:
    a=file.split(".")[0]
    b=a.split("\\")
    #print(b[2])
    jpg_arr.append(b[2])

#print(jpg_arr)

for file in json_full_path:
    #print(file)
    a=file.split("\\")
    #print(a[2])
    b=a[2].split(".")[0]
    json_arr.append(b)


# for v in jpg_arr:
#     if v not in json_arr:
#         jpg_NG.append(v+".jpg")

for v in json_arr:
    if v not in jpg_arr:
        json_NG.append(v+".jpg")
        json_NG_count+=1


for i in json_full_path:
    #print("kkk",i)
    a=i.split("\\")[2]
    if a in json_NG:
        os.remove(i)