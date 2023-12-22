import os
import sys
import pandas as pd 
from docx import Document
path = os.getcwd()
try:
    df = pd.read_excel("comand_list.xlsx")
except FileNotFoundError:
    print("File not found")  
    sys.exit()
columns = list(df.columns) 
for index,item in df.iterrows(): 
    try:
        document = Document("手順書.docx")
    except FileNotFoundError: 
        print("File not found") 
        sys.exit()
    for par in document.paragraphs: 
        for column in columns: 
            if str(column) in par.text: 
                if str(column) == "$start-day-time":
                    item[column] = str(item[column]) 
                if str(column) == "$end-day-time":
                    item[column] = str(item[column]) 
                if str(column) == "$users":
                    item[column] = str(item[column]) 
                if str(column) == "$operation_file":
                    item[column] = str(item[column])
                if str(column) == "$cluster-1":
                    item[column] = str(item[column])  
                if str(column) == "$cluster-2":
                    item[column] = str(item[column])  
                par.text = par.text.replace(str(column),str (item[column]))
    outfile = os.path.join(path,"old",item["$file_name"]+".docx")
    try:
        document.save(outfile) 
    except FileNotFoundError:
        print("No destination folder")
        sys.exit()