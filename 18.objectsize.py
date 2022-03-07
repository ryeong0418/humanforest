import sys
import math
import os
import json
import statistics


folder_path = "C:/Users/USER/Downloads/20220204152635220_NIA25/NIA.25 Denoising & Inpainting/mask_02/러닝머신"
json_path =""
ObjectArr = []
jsonCount = 0


coord_list = []





for(path,dir,files) in os.walk(folder_path):
    for file in files:
        if file.endswith(".json"):
            
            with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
                
                for j in range(len(json_data['Learning_Data_Info.']['Annotation'])):

                    
                    for i in range(int(len(json_data['Learning_Data_Info.']['Annotation'][j]['segmentation']))):
                        classid=json_data['Learning_Data_Info.']['Annotation'][j]['Class_ID']
                        #print(classid)

                    for i in range (int(len(json_data['Learning_Data_Info.']['Annotation'][j]['segmentation'])/2)) :
                        #print("number:",i)
                        x, y = json_data['Learning_Data_Info.']['Annotation'][j]['segmentation'][2*i], json_data['Learning_Data_Info.']['Annotation'][j]['segmentation'][2*i+1]
                        coord_list.append((x, y))
                    #print(coord_list)

                    plus = 0 
                    minus = 0 

                    coord_list.append(coord_list[0])
                    #print(coord_list)

                    # print("kkkkkkkkkkk")
                    # print(len(coord_list))
                    total_list=[]
                    for i in range(len(coord_list)-1):
                        #print(i)
                        
                        plus = (coord_list[i][0] * coord_list[i+1][1])
                        #print("plus:",plus)

                        minus = (coord_list[i+1][0] * coord_list[i][1])
                        #print("minus:",minus)

                        total=plus-minus
                        #print("total:",total)
                        
                        total_list.append(total)
                    #print(total_list)
                    total_sum=sum(total_list)
                    #print(total_sum)
                    area=math.fabs(0.5*total_sum)
                    #print(area)
                    print(str(classid))
                    #print(str(area))
                    json_data['Learning_Data_Info.']['Annotation'][j]['segmentation']=round(area)
                    print(json_data['Learning_Data_Info.']['Annotation'][j]['segmentation'])
                    
                    coord_list=[]
            with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                    json.dump(json_data,json_file,ensure_ascii=False,indent= 4 )
            


