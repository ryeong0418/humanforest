import os
import json


folder_path ="E:/final/json최종/2"
jsonArr = []
json_path =""
jsonArr = []
jsonCount = 0   



def meta():

    for (path, dir, files) in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                error_json = {}
                try:
                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)

                        error_json[os.path.join(path, file)] = ""

                        fps = json_data['Raw_Data_Info.']['FPS'] 
                        fstop = json_data['Raw_Data_Info.']['F-Stop']
                        e_time = json_data['Raw_Data_Info.']['Exposure_Time']
                        lens = json_data['Raw_Data_Info.']['Lens']
                        annot=json_data["Learning_Data_Info."]["Annotation"]
                        json_id=json_data["Learning_Data_Info."]["Json_Data_ID"]
                    
                        json_place_id=json_id.split("_")[1]
                        #print(json_place_id)


                        if json_data["Raw_Data_Info."]["Raw_Data_ID"] != list(file.split("_"))[0] + "_" + list(file.split("_"))[1] + "_" + list(file.split("_"))[2]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Raw data ID 에러, "

                        if json_data["Raw_Data_Info."]["Location"] != file.split("_")[1][0:6] :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Location 에러, "

                        if json_data["Raw_Data_Info."]["Location"] not in ['O01001','O01002','O01003','O01004','O01005' ,'O01006' ,'O01007','O01008','O01009','O02010' ,'O02011','O02012','O02013','O03014', 'O03015','O03016','O03017','O04018','O04019','O04020','O04021','O05022','O05023','O05024','O05025','O05026','O06027','O06028','O06029','O06030','O07031','O07032','O07033','O07034','O07035','O08036','O08037','O08038','O09039','O09040','O09041','O09042','O10043','O10044','O10045','O11046','O11047','O11048','O12049','O12050','O12051','O12052','O12053','O12054','O12055','I01001','I01002','I01003','I01004','I01005','I01006','I01007','I02008','I02009','I02010','I03011','I03012','I03013','I04014','I04015','I05016','I05017','I05018','I06019','I06020','I07021','I08022','I08023','I08024','I09025','I09026','I09027','I09028','I09029','I09030','I09031','I09032']:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "raw_Location 에러, "
                        
                        if json_data["Raw_Data_Info."]["Copyrighter"] != "㈜미디어그룹사람과숲" :
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Copyrighter 에러, "
                 
                        if json_data["Raw_Data_Info."]["Resolution"] not in "1920, 1080":
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Resolution 에러, "


                        if len(json_data["Raw_Data_Info."]["Start_Time"]) != 8:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Start time 길이 에러, "

                        if json_data["Raw_Data_Info."]["Start_Time"] != "00:00:00":
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Start time 에러, "

                        if len(json_data["Raw_Data_Info."]["End_Time"]) != 8:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "End time 에러, "
                        

                        if "." not in json_data["Raw_Data_Info."]["GPS"].split(",")[0] or "." not in json_data["Raw_Data_Info."]["GPS"].split(",")[1]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "GPS 에러, "

                        if int(fps) not in [30, 60]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "FPS 에러, "

                  
                        if str(lens) not in ['T', 'W']:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Lens 에러, "
                    
                        if json_data["Raw_Data_Info."]["File_Extension"] not in ["mp4"]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "File_Extension, "                      

                        if json_data["Raw_Data_Info."]["Date"].replace("-","")[2:] != file.split("_")[0].replace("I-", ""):
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Date 에러, "                             

                    
                        if json_data["Source_Data_Info."]["Source_Data_ID"] != file.split(".")[0]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Source data ID 에러, "

                        if json_data["Source_Data_Info."]["Classification_ID"] != file.split("_")[1][0:6]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Classification_ID 에러, "

                        if json_data["Source_Data_Info."]["File_Extension"] != "jpg":
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "source_file_extension 에러, "  

                        if json_data["Learning_Data_Info."]["Json_Data_ID"] != file.split(".")[0]:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "json data ID 에러, "

                        if json_data["Learning_Data_Info."]["File_Extension"] != "json":
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "json_File_extension 에러, " 

                        if json_place_id not in ('O01001','O01002','O01003','O01004','O01005' ,'O01006' ,'O01007','O01008','O01009','O02010' ,'O02011','O02012','O02013','O03014', 'O03015','O03016','O03017','O04018','O04019','O04020','O04021','O05022','O05023','O05024','O05025','O05026','O06027','O06028','O06029','O06030','O07031','O07032','O07033','O07034','O07035','O08036','O08037','O08038','O09039','O09040','O09041','O09042','O10043','O10044','O10045','O11046','O11047','O11048','O12049','O12050','O12051','O12052','O12053','O12054','O12055','I01001','I01002','I01003','I01004','I01005','I01006','I01007','I02008','I02009','I02010','I03011','I03012','I03013','I04014','I04015','I05016','I05017','I05018','I06019','I06020','I07021','I08022','I08023','I08024','I09025','I09026','I09027','I09028','I09029','I09030','I09031','I09032'):
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "json_place 에러, " 


                        for i in range(len(annot)):

                            class_id=annot[i]['Class_ID']
                            seg=annot[i]["segmentation"]
                            type_seg=annot[i]["type"]                                    

                            if class_id not in("B000","BO01","BO02","BO03","BO04","BO05","BO06","BO07","BO08","BO09","BO10","BO11","BO12","BO13","BO14","BO15","BI16","BI17","BI18","BI19","BI20","BI21","BI22","BI23","BI24","BI25","BI26","BI27","BI28","BI29","BI30","BI31","BI32","BI33","BI34","BI35","BI36","BI37","F38","F39","F40","F41"):
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "class_id 에러, "

                            if type_seg != "segmentation":
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "type_segmantation 에러, "
                                                
                            for d in seg:
                                if d >2000:
                                    error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "seg 에러, "
                                    break


                    if error_json[os.path.join(path, file)] == "":
                        pass

                    else :
                        print(error_json)

                    

                except:
                    error_json[os.path.join(path, file)] = "json 형식 에러"


if __name__ == '__main__':
    meta()




def gt_check():

    for path,dirs,files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                s=os.path.splitext(file)
                filename =s[0].split("_")[3]
                if filename[0]=="G":
                    #print(s)
                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        #print(file)
                        json_data = json.load(json_file)
                        annot = json_data['Learning_Data_Info.']['Annotation']
                        #print(annot)
                        s1=annot[:len(annot)//2]
                        s2=annot[len(annot)//2:]

                        if s1==s2:
                            del annot[:len(annot)//2]
                        else:
                            pass

                    with open(os.path.join(path, file), "w", encoding="utf-8") as json_file:                    
                    
                        json.dump(json_data, json_file, ensure_ascii=False, indent= 4)

if __name__ == '__main__':
    gt_check()



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
