import os
import json

json_dir = "E:/hfvalidator/pngremake/json_final-7,8" #파일 경로




def check (a):  # 오류판단 함수
        temp = a.split("_")
       
        if( (len(temp[0]) == 8 and list(temp[0])[0] != 'I') or (len(temp[0]) != 8 and list(temp[0])[0] == 'I') )or ( (len(temp[1]) != 6 and (list(temp[1])[0] == 'I'or 'O')) and (len(temp[1]) == 6 and list(temp[1])[0] != 'I'or 'O') )or ( (len(temp[2]) != 3 and (list(temp[2])[0] == 'W'or 'T')) and (len(temp[2]) == 3 and list(temp[2])[0] != 'W'or 'T') )  :
                return  a


for path, dirs, files in os.walk(json_dir):
  if (len(files) > 0):
    for filename in files:
      s = os.path.splitext(filename)
      
      if s[0] == '.DS_Store' :
          pass
          
      elif s[1] != '.json' :        #확장자체크
              
          not_pass_name = s[0]
          print("확장자오류"" ""파일명"" "+not_pass_name+s[1])
       
      else :
                                                                  #파일명오류 체크
          pass_name = s[0]
          check_name = check(pass_name)
          if check_name != None:
                  
                  
           print('파일명오류 파일명: ' + str(check_name))
          
        
        
         

