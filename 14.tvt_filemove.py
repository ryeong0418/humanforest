from openpyxl import load_workbook
import numpy
import os
import json
import glob
import shutil


excel_path="E:/tvt/testset.xlsx"
jpg_folder="E:/M(최종)"


load_excel=load_workbook(excel_path,data_only=True)
load_sheet=load_excel["eval"]
get_cell=load_sheet["A2":"A344"]
ex_list=[]
jpg_list=[]
final_list=[]
jpg_full_path=[]



for row in get_cell:
    for i in row:
        ex_list.append(i.value)

print("엑셀리스트",ex_list)


filename=os.listdir(jpg_folder)
jpg_list=filename
print("폴더경로",jpg_list)

for file in jpg_list:
    if file in ex_list:
        final_list.append(file)

print("공통폴더",final_list)

for i in final_list:
    print(i)
    print(jpg_folder+"/"+i)

    try:
        shutil.move(jpg_folder+"/"+i,"E:/tvt/masking(최종)/test")

    except Exception as e:
        print(e)
        print(file)




