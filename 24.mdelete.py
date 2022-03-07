import os

jpg_full_path=[]
jpg_list=[]
path_list=[]

jpg_folder="C:/Users/USER/Downloads/20220222164602896_NIA25/NIA.25 Denoising & Inpainting/infiniq_mask/22년 1월 4주차"


for path,dirs,files in os.walk(jpg_folder):
    if path.split("\\")[-1].split("-")[0]=="I":
        path_list.append(path)


for i in path_list:
    a=i.split("\\")[0:-1]
    b='/'.join(a)
    m_filename=i.split("\\")[-1]
    m_delete_filename=m_filename.split("_")[0]+"_"+m_filename.split("_")[1]+"_"+m_filename.split("_")[2]   
    os.rename(b+"/"+ m_filename,b+"/"+m_delete_filename)


