import json
import csv
import sys

if len(sys.argv) != 2:
	print("Pass correct no. of arguments")
	sys.exit()


with open(str(sys.argv[1]),'r') as f:
	csv_data=csv.DictReader(f)
	
	out = json.dumps( [ row for row in csv_data] ,indent=2)
	
	with open ('resultjson.json','w') as f:
		f.write(out)
	
