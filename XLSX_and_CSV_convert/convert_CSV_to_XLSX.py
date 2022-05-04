from re import X
import pandas as pd
import os
import re


n = 0

# Get the list of all files and directories
Newpath = os.path.dirname(__file__)

print(Newpath)

pathlist =os.path.join(Newpath,'csv\\') 
dir_list = os.listdir(pathlist)

print(pathlist)

# Get all csv files of the path
for x in os.listdir(pathlist):
    if x.endswith(".csv"):

        name = x.split(".")
        stringname = x
        stringname = re.sub(".csv","",stringname)

        print(stringname)

        # Reading the csv file
        df_new = pd.read_csv(pathlist+ x, sep=";", on_bad_lines='skip', encoding='latin-1')
        
        
        mid = str(n)
        end = '.xlsx'
        if not os.path.exists(pathlist + '/ConvertDONE'):
            os.makedirs(pathlist + '/ConvertDONE')
        pathlist2 =os.path.join(Newpath,'csv\\ConvertDONE\\')
        print(pathlist2)
        # saving xlsx file
        GFG = pd.ExcelWriter(pathlist2 + 'Converted_'+stringname+end )
        df_new.to_excel(GFG, index=False)
        GFG.save()
        n += 1
