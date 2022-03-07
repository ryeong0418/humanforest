import os
import json
#from openpyxl import Workbook

# 1. json 파일별로 클래스의 개수를 카운트 함.
# 2. json 파일별로 카운트된 클래스 개수를 sql문으로 인서트 할 수 있는 형식으로 변환.
# 3. annotation이 하나도 안되어 있는 json 파일은 삭제하고, 삭제 리스트를 엑셀에 출력해줌.


main_path = "E:/final/json최종/11"

os.chdir(main_path)

def count_annot(main_path):

    json_count=0
    count_kp =""

    for (path, dir, files) in os.walk(main_path):

        for fileName in files:

            if fileName.endswith('.json'):

                json_count+=1

                with open(os.path.join(path, fileName), encoding='utf-8-sig') as json_file:
                   
                    try:

                        jsonData = json.load(json_file)

                        annot = jsonData['Learning_Data_Info.']['Annotation'] 

                        jsonDict= {}

#                         is_bb = False
                         # anntation type 별로 클래스를 분류해서 Dictionary로 저장.
               
                        annotType = {'B000':0,'BO01':0,'BO02':0,'BO03':0,'BO04':0 ,'BO05':0 ,'BO06':0 ,'BO07':0,
                        'BO08':0,'BO09':0 ,'BO10':0,'BO11':0,'BO12':0,'BO13':0, 'BO14':0,'BO15':0,'BI16':0,
                        'BI17':0,'BI18':0,'BI19':0,'BI20':0,'BI21':0,'BI22':0,'BI23':0,'BI24':0,'BI25':0,
                        'BI26':0,'BI27':0,'BI28':0,'BI29':0,'BI30':0,'BI31':0,'BI32':0,'BI33':0,'BI34':0,
                        'BI35':0,'BI36':0,'BI37':0,'F38':0,'F39':0,'F40':0,'F41':0}
                        #print(annotType)

                        for i in range(len(annot)):
                           
                            #print("I got in")
                            jsonDict[fileName]=annotType
                            #print(jsonDict)
                            jsonDict[fileName][annot[i]['Class_ID']] += 1
                            
                            # is_count=True
                        #print(jsonDict)
                            # for key in annotType:
                            #  print(jsonDict)


                        # if is_count:

                        #result="("+annot[fileName]+")"
                        
                        kp_line = "" #class별 순서대로 B00,B01,,,
                        #total_kp=0 
                        for val in jsonDict[fileName].values():
                             kp_line = kp_line +", " + str(val)
                             #total_kp += val #업데이트
                        #count_kp = count_kp + "(" + "\'" + fileName + "\'" + kp_line + ", " +str(total_kp) + "),"
                        count_kp = count_kp + "(" + "\'" + fileName + "\'" + kp_line +  "),"
                        
                    
                    except Exception as ex:
                        print(ex)
                        pass

    result_kp = count_kp[:-1]+";"
    #print(result_kp)

    return  result_kp

if __name__ == '__main__':
     count_annot(main_path)



# def annot_miss(main_path):
#     write_xl = Workbook()
#     write_ws = write_xl.active
#     write_ws.append(['폴더명', 'JSON'])
#     for error in remove_list:
#         write_ws.append(error)
#     write_xl.save(os.path.join(main_path, '누락\\{}.xlsx'.format(main_path.split('\\')[-1])))

# if __name__ == '__main__':
#     annot_miss()


# def remove_non_annot():
#     remove_filename=[]
#     row_num=0
#     for i in remove_list:
#         remove_filename.append([os.path.join(remove_list[row_num][0],remove_list[row_num][1])])
#         row_num+=1

#     row_num2=0
#     for remove in remove_filename:
#         os.remove(remove[row_num2])
#         row_num2+=1

# if __name__ == '__main__':
#     remove_non_annot()
