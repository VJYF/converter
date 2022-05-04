from re import X
import pandas as pd 
import os
import re

# Get the list of all files and directories
Newpath = os.path.dirname(__file__)
pathlist =os.path.join(Newpath,'xlsx\\') 
dir_list = os.listdir(pathlist)

# Get all xlsx files of the path
for x in os.listdir(pathlist):
    if x.endswith(".xlsx"):
        
        # delete the .xlsx
        stringname = re.sub("\\..*","",x)

        # Reading the xlsx file
        read_file = pd.read_excel (pathlist+ x) 

        # It will remplace the .xlsx
        end = '.csv'

        # Create a new directorie on our path
        if not os.path.exists(pathlist + '/ConvertDONE'):
            os.makedirs(pathlist + '/ConvertDONE')

        # Get the path of ConvertDone's directories
        pathlist2 =os.path.join(Newpath,'xlsx\\ConvertDONE\\')
        print(pathlist2)

        # saving csv file
        read_file.to_csv (pathlist2 + 'Converted_'+stringname+end, index = None, header=True, sep=";") 
    
