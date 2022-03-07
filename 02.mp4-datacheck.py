
import os
import json
from openpyxl import load_workbook


excel_path="C:/Users/USER/Desktop/파일리스트/11월1주차/11월 1주차_인페인팅_원시데이터리스트_파일명_촬영계획표_211105.xlsx"
data_path="D:/링크플로우/원시데이터/(최종)/11월/11월1주"

load_excel=load_workbook(excel_path,data_only=True)
load_sheet=load_excel["11월 1주차 원시데이터"]
get_cell=load_sheet["C5":"C60"]



def ds_store():

    for path,dir,files in os.walk(data_path):
        for i in files:
            if i.endswith(".DS_Store"):
                print(i)
                os.remove(r""+path+"/"+i)

if __name__=="__main__":
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

def check():

    ex_list=[]
    mp_list=[]
    mp4_ng=[]
    ex_ng=[]
    ex_total=0
    mp4_total=0


    for row in get_cell:
        for i in row:
            ex_list.append(i.value)
            ex_total+=1

    print("엑셀 원시데이터 총 수량:{}".format(ex_total))
    #print("엑셀 원시데이터 리스트:{}".format(ex_list))
    print("----------------------------------------------------------")

    for path,dir,files in os.walk(data_path):
        for file in files:
            if file.endswith(".mp4"):
                mp4_total+=1
                a=file.split(".")
                mp_list.append(a[0])
    
    print("원시 데이터 총 수량:{}".format(mp4_total))
    #print("원시 데이터 리스트:{}".format(mp_list))


    for i in ex_list:
        if i not in mp_list:
            mp4_ng.append(i)

    print("원시데이터 없는 파일:{}".format(mp4_ng))


    for i in mp_list:
        if i not in ex_list:
            ex_ng.append(i)

    print("엑셀 데이터 없는 파일:{} ".format(ex_ng))



if __name__=="__main__":
    check()



    
