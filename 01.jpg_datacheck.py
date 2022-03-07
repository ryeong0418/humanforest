import os
from PIL import Image

main_path="C:/Users/USER/Downloads/9월 4주차 (1차 전달 건)/9월 4주차 (1차 전달 건)"


#ds store 삭제
def ds_store():

    for (path, dir, files) in os.walk(main_path):
        for i in files:
            if i.endswith(".DS_Store"):
                print(i)
                os.remove(r""+path+"/"+i)
                #os.remove(r""+path+"\\.DS_Store")

if __name__ == '__main__':
    ds_store()


#데이터 통계
def sta():

    in_count=0
    out_count=0
    total_count=0
    w_count=0
    t_count=0
    gt_count=0
    f_count=0
    error_count=0


    for path, dirs, files in os.walk(main_path):
        for i in files:
            if i.endswith('.jpg'):
                total_count+=1
                if i.split("_")[1][0] == "I":
                    in_count+=1
                if i.split("_")[1][0] == "O":
                    out_count+=1
                if i.split("_")[2][0] =="W":
                    w_count+=1
                if i.split("_")[2][0] == "T":
                    t_count+=1
                if i.split("_")[3][0] =="G":
                    gt_count+=1
                if i.split("_")[3][0] == "F":
                    f_count+=1
            else:
                print(i)



    print("------------------------------------------------------------------------")
    print("파일 총수량:{}개".format(total_count))
    print("------------------------------------------------------------------------")
    print("실내 총수량:{}개".format(in_count))
    print("실외 총수량:{}개".format(out_count))
    print("실내+실외 총수량:{}개".format(in_count+out_count))
    print("------------------------------------------------------------------------")
    print("T망원 총수량:{}개".format(t_count))
    print("W광각 총수량:{}개".format(w_count))
    print("T망원 + W광각 총수량:{}개".format(t_count+w_count))
    print("------------------------------------------------------------------------")
    print("GT 총수량:{}개".format(gt_count))
    print("전경 총수량:{}개".format(f_count))
    print("GT+전경 총수량:{}개".format(gt_count+f_count))
    print("------------------------------------------------------------------------")

if __name__ == '__main__':
    sta()

#중복 파일명 체크

def samename():

    name_Arr=[]
    errorname_Arr=[]
    errorname_count=0

    for path,dirs,files in os.walk(main_path):
        for i in files:
            s=os.path.splitext(i)
            #print(s)
           
            if s[0] not in name_Arr:
                name_Arr.append(s[0])
                #print(name_Arr)
            
            else:
                errorname_Arr.append(s[0])
                errorname_count+=1

    print("중복파일명:{}개".format(errorname_count))            
    print("중복파일명:{}".format(errorname_Arr))

if __name__ == '__main__':
    samename()

    
# #사진 크기 확인

def image_size():


    for path,dirs,files in os.walk(main_path):
        for file in files:
            if file.endswith(".jpg"):
                a=Image.open(path+"\\"+file)
                #print(a.size)
                if a.size == (1920,1080):
                    pass
            
                else:
                    print("사진크기 오류jpg:{}".format(file))
    print("사진크기 확인")

if __name__ == '__main__':
    image_size()


# #folder-file 일치확인

def ffcheck():


    for path,dirs,files in os.walk(main_path):
        for file in files:
            folder=path.split("\\")
            #print(folder)            

            filename=os.path.splitext(file)
            #print(filename)
            folder_name=folder[-1]
            #print(folder_name)
            file_name=filename[0][:19]
            #print(file_name)
            if folder_name!=file_name:
            
                print(folder_name)
    print("finish")


if __name__ == '__main__':
    ffcheck()





