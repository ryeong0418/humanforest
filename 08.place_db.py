import os
import json

main_path="E:/final/json최종/11"

os.chdir(main_path)

def count_place(main_path):

    json_count=0
    count_kp=""
    gt_kp=""

    for(path,dir,files) in os.walk(main_path):
        for fileName in files:
            if fileName.endswith('.json'):
                json_count+=1

                with open(os.path.join(path, fileName), encoding='utf-8-sig') as json_file:
                    
                    try:
                        jsonData=json.load(json_file)
                        location=jsonData['Raw_Data_Info.']['Location']
                        gt_check = jsonData["Learning_Data_Info."]["Json_Data_ID"]
                        gtDict ={}

                        gt_Type = {'O01001':0,'O01002':0,'O01003':0,'O01004':0,'O01005':0 ,'O01006':0 ,'O01007':0 ,'O01008':0,
                        'O01009':0,'O02010':0 ,'O02011':0,'O02012':0,'O02013':0,'O03014':0, 'O03015':0,'O03016':0,'O03017':0,
                        'O04018':0,'O04019':0,'O04020':0,'O04021':0,'O05022':0,'O05023':0,'O05024':0,'O05025':0,'O05026':0,
                        'O06027':0,'O06028':0,'O06029':0,'O06030':0,'O07031':0,'O07032':0,'O07033':0,'O07034':0,'O07035':0,
                        'O08036':0,'O08037':0,'O08038':0,'O09039':0,'O09040':0,'O09041':0,'O09042':0,'O10043':0,'O10044':0,
                        'O10045':0,'O11046':0,'O11047':0,'O11048':0,'O12049':0,'O12050':0,'O12051':0,'O12052':0,'O12053':0
                        ,'O12054':0,'O12055':0,'I01001':0,'I01002':0,'I01003':0,'I01004':0,'I01005':0,'I01006':0,'I01007':0,
                        'I02008':0,'I02009':0,'I02010':0,'I03011':0,'I03012':0,'I03013':0,'I04014':0,'I04015':0,'I05016':0,'I05017':0,'I05018':0
                        ,'I06019':0,'I06020':0,'I07021':0,'I08022':0,'I08023':0,'I08024':0,'I09025':0,'I09026':0,'I09027':0,'I09028':0,'I09029':0,'I09030':0
                        ,'I09031':0,'I09032':0}


                        if gt_check.split("_")[3][0]=="F":
                            gtDict[fileName]=gt_Type
                            gtDict[fileName][location]+=1

                            #print(gtDict)

                            gt_line = "" #class별 순서대로 B00,B01,,,
                            for val in gtDict[fileName].values():
                                gt_line = gt_line +", " + str(val)
                            gt_kp = gt_kp + "(" + "\'" + fileName + "\'" + gt_line +  "),"

                    
                    except Exception as ex:
                            
                        print(ex)
                        print("오류파일:",fileName)
   

    gtplace_kp= gt_kp[:-1]

    #print(gtplace_kp)

    return  gtplace_kp

if __name__ == '__main__':
     count_place(main_path)

