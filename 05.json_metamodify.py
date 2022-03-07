import os
import json

file_path ="E:/final/json최종/1"
con = 0

#rawdata수정

for path, dir, files in os.walk(file_path):
    for file in files:
        if file.endswith(".json"):
            try:
                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)
                        a=file.split(".")[0]
                        filename=a.split("_")[0]+"_"+a.split("_")[1]+"_"+a.split("_")[2]
                        print(filename)

                        json_data["Raw_Data_Info."]["Raw_Data_ID"] = filename
                    
                    with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                        json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
                        print("{} meta 수정 완료".format(file))

            except Exception as e:
                print(e)
                print(file)

# # #start_time 수정

# for path, dir, files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):
#             try:
#                     with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                         json_data = json.load(json_file)

#                         json_data["Raw_Data_Info."]["Start_Time"]="00:00:00"
#                         print(json_data["Raw_Data_Info."]["Start_Time"]) 


#                     with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                         json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                         print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)


# # # # JSON_DATA_ID 수정

# for path, dir, files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):
#             try:
#                     with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                         json_data = json.load(json_file)
#                         print(file.split(".")[0])
#                         json_data["Learning_Data_Info."]["Json_Data_ID"] = file.split(".")[0]
#                         #json_data["Source_Data_Info."]["Source_Data_ID"] = file.split(".")[0]
                    
#                     with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                         json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                         print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)


# # # # # Source_DATA_ID 수정

# for path, dir, files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):
#             try:
#                     with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                         json_data = json.load(json_file)
#                         print(file.split(".")[0])
#                         #json_data["Learning_Data_Info."]["Json_Data_ID"] = file.split(".")[0]
#                         json_data["Source_Data_Info."]["Source_Data_ID"] = file.split(".")[0]
                    
#                     with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                         json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                         print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)



# #date 수정

# for path, dir, files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):
#             try:
#                     with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                         json_data = json.load(json_file)
#                         #print(file.split("_")[0])
#                         a=file.split("_")[0]
#                         print(a.split("-")[1])
#                         b=a.split("-")[1]
#                         print(str(20)+str(b[0:2])+"-"+str(b[2:4])+"-"+str(b[4:6]))
#                         json_data["Raw_Data_Info."]["Date"] = str(20)+str(b[0:2])+"-"+str(b[2:4])+"-"+str(b[4:6])
                    
#                     with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                         json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                         print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)

# #location 수정

for path, dir, files in os.walk(file_path):
    for file in files:
        if file.endswith(".json"):
            try:
                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)
                        #print(file.split("_")[0])
                        a=file.split("_")[1]
                        #print(a)
            #             print(str(20)+str(b[0:2])+"-"+str(b[2:4])+"-"+str(b[4:6]))
                        json_data["Raw_Data_Info."]["Location"] = a
                        #print(json_data["Raw_Data_Info."]["Location"])
                    
                    with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
                        json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
                        print("{} meta 수정 완료".format(file))

            except Exception as e:
                print(e)
                print(file)

# #Learning_Data_Info. 수정

# # for path,dir,files in os.walk(file_path):
# #     for file in files:
# #         if file.endswith(".json"):

# #             try:
# #                 with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
# #                     json_data = json.load(json_file)

# #                     json_data["Learning_Data_Info."]=json_data.pop("Learning_Data_Info")

# #                 with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
# #                     json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
# #                     print("{} meta 수정 완료".format(file))

# #             except Exception as e:
# #                 print(e)
# #                 print(file)


# #Classification_ID 수정

# for path,dir,files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):

#             try:
#                 with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                     json_data = json.load(json_file)

#                     a=file.split("_")[1]

#                     json_data["Source_Data_Info."]["Classification_ID"] = a
#                         #print(json_data["Raw_Data_Info."]["Location"])

#                 with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                     json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                     print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)


#segmentation 수정

# for path, dir, files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):
#             try:
#                     with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                         json_data = json.load(json_file)

#                         for i in range(len(json_data["Learning_Data_Info."]["Annotation"])):
#                             print(json_data["Learning_Data_Info."]["Annotation"][i]["type"])
#                             json_data["Learning_Data_Info."]["Annotation"][i]["type"]="segmentation"

                    
#                     with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                         json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                         print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)



#segmentation 수정

# 

#mp4 수정

# for path, dir, files in os.walk(file_path):
#     for file in files:
#         if file.endswith(".json"):
#             try:
#                     with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
#                         json_data = json.load(json_file)



#                         json_data["Raw_Data_Info."]["File_Extension"]="mp4"

                    
#                     with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:
#                         json.dump(json_data, json_file, ensure_ascii=False,indent="\t")
#                         print("{} meta 수정 완료".format(file))

#             except Exception as e:
#                 print(e)
#                 print(file)