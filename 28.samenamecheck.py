import os
import json

json_dir = "D:/링크플로우/정제데이터(최종)"  #파일 경로

        
name_stack = []
error_name_stack = []

for path, dirs, files in os.walk(json_dir):
  if (len(files) > 0):
    for filename in files:
      s = os.path.splitext(filename)
      
       
      if s[0] not in name_stack :
        name_stack.append(s[0])
       
      else :  
        error_name_stack.append(s[0])


print('중복파일명:' + str(error_name_stack))
#print('중복아닌 파일명:'+str(name_stack))

