import sys
import math
import os
import json
import statistics

main_path="C:/Users/USER/Desktop/pixelsize"


for(path,dir,files) in os.walk(main_path):
    
    for file in files:
        
        if file.endswith(".json"):

            with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)

                print(len(json_data["Learning_Data_Info."]["Annotation"]))

                i = 0
                while i < len(json_data["Learning_Data_Info."]["Annotation"]):
                    print(i)
                    
                    #print(file)
                    class_id=json_data["Learning_Data_Info."]["Annotation"][i]["Class_ID"]
                    segmen=json_data["Learning_Data_Info."]["Annotation"][i]["segmentation"]

                    #if segmen < 625:
                    #     #json_data['Learning_Data_Info.']['Annotation'][i]['segmentation']=segmen
                    #     #print(json_data['Learning_Data_Info.']['Annotation'][i]['segmentation'])

                    if segmen >= 625:
                        print("들어옴")
                        # print("kym : ", json_data['Learning_Data_Info.']['Annotation'][i], " i : ", i, "len: ", len(json_data["Learning_Data_Info."]["Annotation"]))
                        del json_data['Learning_Data_Info.']['Annotation'][i]
                        i -= 1
                    i += 1

            with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                json.dump(json_data,json_file,indent= 4)            
                print("{} meta 수정 완료".format(file))



