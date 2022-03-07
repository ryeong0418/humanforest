import os
import json
import copy



main_path ="E:/maskingjsonmerge2"

os.chdir(main_path)

def count_annot(main_path):

    json_count=0
    count_kp =""
    F_sum=[]
    total_F_sum=[]
    small_size=0
    middle_size=0
    big_size=0


    for (path, dir, files) in os.walk(main_path):

        for fileName in files:

            if fileName.endswith('.json'):
                if fileName.split("_")[3][0]=="F":
                    with open(os.path.join(path, fileName), encoding='utf-8-sig') as json_file:
                        try:
                            jsonData = json.load(json_file)
                            annot = jsonData['Learning_Data_Info.']['Annotation']               
                            annotType = {'M42':0}

                            for i in range(len(annot)):
                                class_id=annot[i]["Class_ID"]
                                segmen=annot[i]["segmentation"]

                                jsonDict= {}
                                jsonDict[fileName] = annotType                                                                                                        
                                jsonDict[fileName][annot[i]['Class_ID']] += segmen
                            #print(jsonDict[fileName])



                            kp_line = "" #class별 순서대로 B00,B01,,,
                        #total_kp=0 
                            for val in jsonDict[fileName].values():
                                kp_line = kp_line +", " + str(val)
                             #total_kp += val #업데이트
                        #count_kp = count_kp + "(" + "\'" + fileName + "\'" + kp_line + ", " +str(total_kp) + "),"
                            count_kp = count_kp + "(" + "\'" + fileName + "\'" + kp_line +  "),"
                        
                    
                        except Exception as ex:
                            print(ex)
                            print(fileName)
                            pass

    result_kp = count_kp[:-1]+";"
    #print(result_kp)

    return  result_kp
                                                              


if __name__ == '__main__':
     count_annot(main_path)