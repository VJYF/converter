from re import X
import pandas as pd 
import os

n = 1
# Get the list of all files and directories
pathlist = "Desktop\\XLSX_and_CSV_convert\\xlsx"
dir_list = os.listdir(pathlist)
# Get all csv files of the path
for x in os.listdir(pathlist):
    if x.endswith(".xlsx"):
        
        # Reading the xlsx file
        read_file = pd.read_excel ('Desktop\\XLSX_and_CSV_convert\\xlsx\\' +x) 

        mid = str(n)
        end = '.csv'

        # saving csv file
        read_file.to_csv ('Desktop\\XLSX_and_CSV_convert\\csvDONE\\'+x+mid+end, index = None, header=True, sep=";") 
        n += 1
    
