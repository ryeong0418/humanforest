import os
import json

json_dir="E:\\10%\\masking"


path_list  = []
filenum_list = []
fordername_list = []

def Numfile(p) :
      jpg_count= 0
      for currentdir, dirs, files in os.walk(p):
            for file in files :
                  if file.endswith(".json") :
                            jpg_count+= 1
                  
      return jpg_count 
            
      

for path, dirs, files in os.walk(json_dir):
      path_list.append(path)
      #print(path)
      #filenum_list= len(next(os.walk(path))[2])


for i in range(0, len(path_list))  :
      file_name = str (path_list[i]).split('\\')
      #print(str(file_name[-1]))
      #print(str(Numfile(path_list[i])))
      
      print(("   "*len(file_name))+' ㄴ' + str(file_name[-1]) + '     ' + str(Numfile(path_list[i])))
      #print((""*len(file_name))+ str(file_name[-1]))
     
    
