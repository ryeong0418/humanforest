import zipfile
import os

# from matplotlib.cbook import to_filehandle

# def zip_dir(directory, zipname):
    
#     if os.path.exists(directory):
#         print(directory)

#         outZipFile=zipfile.ZipFile(zipname+".zip","w",zipfile.ZIP_DEFLATED)
        
#         rootdir=os.path.basename(directory)
#         print(rootdir)

#         for dirpath,dirnames,filenames in os.walk(directory):
#             for filename in filenames:
#                 print("kkkkk",filename)
#                 filepath=os.path.join(dirpath,filename)
#                 parentpath=os.path.relpath(filepath,directory)
#                 arcname=os.path.join(rootdir,parentpath)
#                 outZipFile.write(filepath,arcname)

#     outZipFile.close()

# if __name__=="__main__":
#     zip_dir("D:/tvt/test/TeS1.실외-운동", "D:/zipresult/TeS1.실외-운동.zip")

zipresult_path="D:/zipresult/TS1.실외-운동.zip"
zipf = zipfile.ZipFile(zipresult_path,'w',zipfile.ZIP_DEFLATED)

file_path="E:/tvt_최종/jpg/training/1.실외/TS1.실외-운동"

if os.path.exists(file_path):
    rootdir=os.path.basename(file_path)
    for dirpath,dirnames,filenames in os.walk(file_path):
       
        for filename in filenames:
            filepath=os.path.join(dirpath,filename)
            parentpath=os.path.relpath(filepath,file_path)
            print(parentpath)
            zipf.write(filepath,parentpath)
    zipf.close()
