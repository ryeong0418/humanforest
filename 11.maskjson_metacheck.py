import os
import json

main_path="C:/Users/USER/Desktop/integratedmasking"

jsonArr = []
jsonCount = 0 

def data():

    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                    json_data=json.load(json_file)
                    #print(json_data["Learning_Data_Info."])
                    error_json={}
                    error_json[os.path.join(path,file)]=""

                    if "Path" not in json_data["Learning_Data_Info."]:
                        error_json=error_json[os.path.join(path,file)]+"path 없음"

                    if "File_Extension" not in json_data["Learning_Data_Info."]:
                        error_json=error_json[os.path.join(path,file)]+"file_extension 없음"

                    if "Json_Data_ID" not in json_data["Learning_Data_Info."]:
                        error_json=error_json[os.path.join(path,file)]+"json_data_id 없음"
                
                    if  error_json[os.path.join(path, file)] == "":
                        pass

                    else:
                        print(error_json)

if __name__ == '__main__':
    data()


def data_type():

    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                #print(file.split(".")[0])
                with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                    json_data=json.load(json_file)
                    error_json={}
                    error_json[os.path.join(path,file)]=""

                    annot=json_data["Learning_Data_Info."]["Annotation"]

                    if json_data["Learning_Data_Info."]["File_Extension"] not in "json":
                        error_json[os.path.join(path,file)]=error_json[os.path.join(path,file)]+"json파일 오류"
                    if json_data["Learning_Data_Info."]["Json_Data_ID"] != file.split(".")[0]:
                        error_json[os.path.join(path,file)]=error_json[os.path.join(path,file)]+"json_data_id오류"

                    for i in range(len(annot)):
                        class_id=annot[i]["Class_ID"]
                        seg=annot[i]["segmentation"]
                        ty=annot[i]["type"]

                        if class_id not in "M42":
                            error_json[os.path.join(path,file)]=error_json[os.path.join(path,file)]+"class_id 오류"

                        if ty!= "segmentation":
                            error_json[os.path.join(path,file)]=error_json[os.path.join(path,file)]+"segmentatino 오류"


                    if  error_json[os.path.join(path, file)] == "":
                        pass

                    else:
                        print(error_json)

if __name__=='__main__':
    data_type()

def duplicate():
    global jsonCount

    for path, dir, files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                if file not in jsonArr:
                    jsonArr.append(file)
                    jsonCount += 1
                else:
                    print("json중복 파일 : {}".format(file))
    print("총 json 수량 : {}".format(jsonCount))

if __name__ == '__main__':
    duplicate()





