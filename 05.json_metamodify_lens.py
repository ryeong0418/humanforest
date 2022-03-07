import os
import json

main_path="E:/hfvalidator/pngerror/json/json_final"

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                json_data=json.load(json_file)

                if file.split("_")[2][0]=="W":

                    json_data["Raw_Data_Info."]["Lens"]="W"
                    del json_data["Raw_Data_Info."]["File_Extension"]
                    json_data["Raw_Data_Info."]["File_Extension"]="mp4"

                if file.split("_")[2][0]=="T":
                    
                    json_data["Raw_Data_Info."]["Lens"]="T"
                    del json_data["Raw_Data_Info."]["File_Extension"]
                    json_data["Raw_Data_Info."]["File_Extension"]="mp4"



            with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
                print("{} meta 수정 완료".format(file))

            #print(json.dumps(json_data,indent="\t"))
