import json
import csv
import pandas as pd
file = open("raw_data2021.txt", mode = "r", encoding ="utf8")
datas = file.read().split("\n")
for i in datas:
	try:
		res = json.loads(i)

		df = pd.Series(res).to_frame()
		df.T.to_csv("datas.csv", mode ="a+")
	except:
		res = {'schoolYear': '2021', 'stt': '', 'studentCode': '', 'TOAN': '', 'VAN': '', 'LY': '', 'HOA': '', 'SINH': '', 'SU': '', 'DIA': '', 'GDCD': '', 'NGOAINGU': '', 'CODE_NGOAINGU': '', 'groupCode': '', 'groupName': '', 'HKTN': '', 'HKXH': '', 'A00': '', 'B00': '', 'C00': '', 'D01': '', 'A01': ''}
		df = pd.Series(res).to_frame()
		df.T.to_csv("datas2021.csv", mode ="a+")
