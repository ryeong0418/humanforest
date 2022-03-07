import os
import json

#json_dir = os.getcwd() + '/test'
json_dir="E:/final/json최종"


def check (a):
        temp = a.split("_")
       
        if( (len(temp[0]) == 8 and list(temp[0])[0] != 'I') or (len(temp[0]) != 8 and list(temp[0])[0] == 'I') )or ( (len(temp[1]) != 6 and (list(temp[1])[0] == 'I'or 'O')) and (len(temp[1]) == 6 and list(temp[1])[0] != 'I'or 'O') )or ( (len(temp[2]) != 3 and (list(temp[2])[0] == 'W'or 'T')) and (len(temp[2]) == 3 and list(temp[2])[0] != 'W'or 'T') ) or ( (len(temp[3]) != 5 and (list(temp[3])[0] == 'G'or 'F')) and (len(temp[3]) == 5 and list(temp[3])[0] != 'G'or 'F') ):
        
                
        #if( (len(temp[1]) != 6 and (list(temp[1])[0] == 'I'or 'O')) and (len(temp[1]) == 6 and list(temp[1])[0] != 'I'or 'O') ) :        
        
                return  a
        



for path, dirs, files in os.walk(json_dir):
  if (len(files) > 0):
    for filename in files:
      s = os.path.splitext(filename)
      if s[1] != '.json' :
          not_pass_name = s[0]
          print("확장자오류"" ""파일명"" "+not_pass_name+s[1])
       
      else :
              
          pass_name = s[0]
          check_name = check(pass_name)
          if check_name != None:
                  
                  
           print('파일명오류 파일명: ' + str(check_name))
          
        
        
         
