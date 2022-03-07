import os
import json

main_path="C:/Users/USER/Downloads/20220204152635220_NIA25/NIA.25 Denoising & Inpainting/mask_02/러닝머신"

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".json"):


            with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                json_data=json.load(json_file)

                
                #json_data["Learning_Data_Info."]=json_data.pop("Learning_Data_Info")


                json_data["Learning_Data_Info."]["Json_Data_ID"]=file.split(".")[0]


                with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                    json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
                    print("{} meta 수정 완료".format(file))



