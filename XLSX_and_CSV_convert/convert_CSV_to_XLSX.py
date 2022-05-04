from re import X
import pandas as pd
import os
import re

# Get the list of all files and directories
Newpath = os.path.dirname(__file__)
pathlist =os.path.join(Newpath,'csv\\') 
dir_list = os.listdir(pathlist)

# Get all csv files of the path
for x in os.listdir(pathlist):
    if x.endswith(".csv"):

        # delete the .csv
        stringname = re.sub("\\..*","",x)

        # Reading the csv file
        df_new = pd.read_csv(pathlist+ x, sep=";", on_bad_lines='skip', encoding='latin-1')
        
        # It will remplace the .csv
        end = '.xlsx'
        
        # Create a new directorie on our path
        if not os.path.exists(pathlist + '/ConvertDONE'):
            os.makedirs(pathlist + '/ConvertDONE')

        # Get the path of ConvertDone's directories
        pathlist2 =os.path.join(Newpath,'csv\\ConvertDONE\\')
        print(pathlist2)

        # saving xlsx file
        GFG = pd.ExcelWriter(pathlist2 + 'Converted_'+stringname+end )
        df_new.to_excel(GFG, index=False)
        GFG.save()
        
