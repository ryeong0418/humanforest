import os

main_path="E:/masking_newexport/1월1주차"

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".json"):
            if file.split("-")[0] == "AI":
                print("I"+"-"+file.split("-")[1])
                os.rename(path+"/"+file,path+"/"+"I"+"-"+file.split("-")[1])

