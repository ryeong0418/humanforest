import os
import json

main_path="C:/Users/USER/Desktop/7m2w00/meta_data"

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                json_data=json.load(json_file)


                
                length=json_data["Raw_Data_Info."]["Length"]
                print(length)
                new_length=str(length)
                print(type(new_length))
                json_data["Raw_Data_Info."]["Length"]=new_length
                print("_--------------------")
                print(type(json_data["Raw_Data_Info."]["Length"]))

            with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
                print("{} meta 수정 완료".format(file))


