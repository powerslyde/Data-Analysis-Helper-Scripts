import pandas as pd
import pymssql as pym
import xlsxwriter
from fileDataLoad import fileDataLoad

filename = r'c:\Users/jpuryear1/Downloads/NA_APPS.xlsx'
sheetname = 'Sheet1'
df = fileDataLoad(filename, sheetname)

df['EAI Code'] = df['EAI Code'].apply(str)
eai_list = df['EAI Code'].tolist()
#converts the eai_list to string and then remove the brackets by selecting the range within the brackets
sql_append = f"and RTRIM(LEFT(ci_item,5)) in ({str(eai_list)[1:-1]})"
print (sql_append)