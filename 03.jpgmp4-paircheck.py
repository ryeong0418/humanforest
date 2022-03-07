import os
import json
import glob


mp4_path="E:/final_mp4/7월"
jpg_path="E:/final_jpg/7월/*/*"

mp4_arr=[]
jpg_arr=[]

mp4_count=0
jpg_count=0

mp4_NG=[]
jpg_NG=[]

mp4_NG_count=0
jpg_NG_count=0




#mp4 배열

for path,dir,files in os.walk(mp4_path):
    for file in files:
        mp4_name=os.path.splitext(file)[0]
        mp4_arr.append(mp4_name)
        mp4_count+=1

#print("MP4배열:",mp4_arr)
print("mp4개수: ",mp4_count)
#jpg 배열

filename=glob.glob(jpg_path)
#print(filename)
for i in filename:
    #print(i)
    jpg_name=i.split("\\")[2]
    jpg_arr.append(jpg_name)
    jpg_count+=1

print("jpg개수: ",jpg_count)

for v in mp4_arr:
    if v not in jpg_arr:
        jpg_NG.append(v)
        jpg_NG_count+=1

print("jpg누락:",jpg_NG)
print("jpg누락 개수: ",jpg_NG_count)


for v in jpg_arr:
    if v not in mp4_arr:
        mp4_NG.append(v)
        mp4_NG_count+=1

print("mp4누락:",mp4_NG)
print("mp4누락 개수: ",mp4_NG_count)




