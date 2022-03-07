import os
import json
from openpyxl import Workbook
from openpyxl import load_workbook

folder_path ="C:/Users/USER/Desktop/integratedmasking"
con = 0
jsonArr = []
jsonCount = 0   


def data():


    for (path, dir, files) in os.walk(folder_path):

        for file in files:

            if file.endswith(".json"):

                error_json = {}

                try:

                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)
                        #print(json_data["Raw_Data_Info."])
                        json_id=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        json_place_id=json_id.split("_")[1]


                        error_json[os.path.join(path, file)] = ""


                        if 'Raw_Data_ID' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Raw data ID 형식 에러, "
                        
                        if 'Location' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Location 형식 에러, "

                        if 'Copyrighter' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Copyrighter 형식 에러, "

                        if 'Resolution' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Resolution 형식 에러, "

                        if 'Date' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Date 형식 에러, "

                        if 'Start_Time' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Start_Time 형식 에러, "

                        if 'End_Time' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "End_Time 형식 에러, "

                        if 'Length' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Length 형식 에러, "
                        
                        if 'GPS' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "GPS 형식 에러, "

                        if 'FPS' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "FPS 형식 에러, "

                        if 'F-Stop' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "F-Stop형식 에러, "

                        if 'Exposure_Time' not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Exposure_Time 형식 에러, "

                        if 'Lens' not in json_data["Raw_Data_Info."]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Lens 형식 에러, "

                        if "File_Extension" not in json_data["Raw_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "mp4_File_Extension 형식 에러, "

                        if "Source_Data_ID" not in json_data["Source_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + " Source_Data_ID 형식 에러, "

                        if "Classification_ID" not in json_data["Source_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + " Classification_ID 형식 에러, "

                        if "File_Extension" not in json_data["Source_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "jpg_File_Extension 형식 에러, "


                        if "Path" not in json_data["Learning_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Path 형식 에러, "


                        if "File_Extension" not in json_data["Learning_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "json_File_Extension 형식 에러, "


                        if "Json_Data_ID" not in json_data["Learning_Data_Info."]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Json_Data_ID 형식 에러, "  
                        
                        if "Annotation" not in json_data["Learning_Data_Info."] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Annotation 형식 에러, " 


                        for i in range(len(json_data["Learning_Data_Info."]["Annotation"])):

                            if "Class_ID" not in json_data["Learning_Data_Info."]["Annotation"][i]: 
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Class_ID 형식 에러, " 
                            
       
                            if "segmentation" not in json_data["Learning_Data_Info."]["Annotation"][i]: 
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "segmentation 형식 에러, " 
              

                            if "type" not in json_data["Learning_Data_Info."]["Annotation"][i]: 
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "type 형식 에러, " 
                          
                        
                        
                        if error_json[os.path.join(path, file)] == "":
                            pass

                        else :
                            print(error_json)


                except:
                    error_json[os.path.join(path, file)] = "json 존재 에러"

if __name__ == '__main__':
    data()


def data_type():

    for (path, dirs, files) in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                error_json = {}
                try:

                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)
                        error_json[os.path.join(path, file)] =""

                        if 'Raw_Data_ID' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Raw_Data_ID"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Raw_Data_ID 타입 에러, "

                        if 'Location' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Location"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Location 타입 에러, "

                        if 'Copyrighter' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Copyrighter"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Copyrighter 타입 에러, "

                        if 'Resolution' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Resolution"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Resolution 타입 에러, "

                        if 'Date' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Date"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Date 타입 에러, "

                        if 'Start_Time' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Start_Time"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Start_Time 타입 에러, "

                        if 'End_Time' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["End_Time"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "End_Time 타입 에러, "

                        if 'Length' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Length"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Length 타입 에러, "

                        if 'GPS' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["GPS"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "GPS 타입 에러, "

                        if 'FPS' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["FPS"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "FPS 타입 에러, "
                        
                        if 'F-Stop' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["F-Stop"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "F-Stop 타입 에러, "

                        if 'Exposure_Time' in json_data["Raw_Data_Info."] and type(json_data["Raw_Data_Info."]["Exposure_Time"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Exposure_Time 타입 에러, "

                        if 'Source_Data_ID' in json_data["Raw_Data_Info."] and type(json_data["Source_Data_Info."]["Source_Data_ID"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Source_Data_ID타입 에러, "

                        if 'Classification_ID' in json_data["Raw_Data_Info."] and type(json_data["Source_Data_Info."]["Classification_ID"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Classification_ID 타입 에러, "

                        if 'File_Extension' in json_data["Raw_Data_Info."] and type(json_data["Source_Data_Info."]["File_Extension"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "File_Extension 타입 에러, "

                        if 'Path' in json_data["Raw_Data_Info."] and type(json_data["Learning_Data_Info."]["Path"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Path 타입 에러, "
                        
                        if 'File_Extension' in json_data["Raw_Data_Info."] and type(json_data["Learning_Data_Info."]["File_Extension"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "File_Extension 타입 에러, "

                        if 'Json_Data_ID' in json_data["Raw_Data_Info."] and type(json_data["Learning_Data_Info."]["Json_Data_ID"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Json_Data_ID 타입 에러, "

                        if 'Annotation' in json_data["Raw_Data_Info."] and type(json_data["Learning_Data_Info."]["Annotation"]) != list:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Annotation타입 에러, "

                    if error_json[os.path.join(path, file)] == "":
                        pass

                    else :
                        print(error_json)

                except:
                    error_json[os.path.join(path, file)] = "json 타입 에러"


if __name__ == '__main__':
    data_type()

def duplicate():
    global jsonCount

    for path, dir, files in os.walk(folder_path):
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
