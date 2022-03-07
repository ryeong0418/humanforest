from genericpath import exists
from openpyxl import load_workbook
import os
import json


excel_path="C:/Users/USER/Desktop/파일리스트/7월5주차/7월 5주차_인페인팅_원시데이터리스트_파일명_촬영계획표_210730.xlsx"
data_path="D:/링크플로우/원시데이터/(최종)/7월5주차"

load_excel= load_workbook(excel_path, data_only=True)
load_sheet= load_excel["7월 5주차 원시데이터 파일리스트"]
get_cell=load_sheet["C5":"C193"]
ex_list=[]
mp_list=[]
mp4_ng=[]
total =0

def ds_store():

    for (path, dir, files) in os.walk(data_path):
        for i in files:
            if i.endswith(".DS_Store"):
                print(i)
                os.remove(r""+path+"/"+i)
                #os.remove(r""+path+"\\.DS_Store")

if __name__ == '__main__':
    ds_store()



def count():
    mp4_Arr = []
    mp4_count= 0
    mov_count=0
    mov_Arr=[]



    for (path, dir, files) in os.walk(data_path):

        for file in files:
            if file.endswith(".mp4") :
            #print(file)
                mp4_Arr.append(file)
                mp4_count+=1

            if file.endswith(".MP4"):
                #print(file)
                mov_Arr.append(file)
                mov_count+=1

    print("mp4 원시데이터 총 수량:{}개".format(mp4_count))
    print("MP4 원시데이터 수량:{}개".format(mov_count))
    print("--------------------------------------------------------------------------------------")
    print("원시데이터 총 수량:{}".format(mp4_count+mov_count))
    print("--------------------------------------------------------------------------------------")


if __name__ == '__main__':
    count()



for row in get_cell:
    for i in row:
        ex_list.append(i.value)
        total+=1
print("엑셀 원시데이터 총 수량:{}개".format(total))
#print(ex_list)
print("---------------------------------------------------------------------------------------")


    
def check():

    total= 0
    ex_check = 0
    non_check = 0
    exists_list= []
    non_exists_list= []



    for(path,dir,files) in os.walk(data_path):
        for fileName in files:
            #print(fileName)
            s = os.path.splitext(fileName)
            mp_list.append(s[0])
            #print(s[0])
            if s[0] in ex_list:
                #total+=1
                ex_check+=1
                exists_list.append(s[0])

            else:
                non_check+=1
                non_exists_list.append(s[0])

    print("존재하는 파일리스트 수량:{}".format(ex_check))
    print("존재하지 않는 파일리스트 수량:{}".format(non_check))
    print("존재하지 않는 파일리스트:{}".format(non_exists_list))

    for i in ex_list:
        if i not in mp_list:
            mp4_ng.append(i)
            
    print("존재하지 않는 mp4파일:{}".format(mp4_ng))
            
    
    #print("존재하지 않은 mp4파일:{}".format(i))


check()




