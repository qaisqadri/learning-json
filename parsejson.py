import json
import sys

if len(sys.argv) != 2:
	print("Pass correct no. of arguments")
	sys.exit()
with open(str(sys.argv[1]),'r') as f:
	data=json.load(f)
	
	for d in data:
		print(d['S.No']," Name : ",d['Name'], " Age : ",d['Age']," Salary : ",d['Salary']," City : ",d['City'])
	

