import json
import os

filename=r"C:\Users\USER\Documents\Python\Week1\Student_management_system\data.json"
def read_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename,'r') as f:
                records=json.load(f)
                return records
        except json.JSONDecodeError:
            return []
    else:
        return []
    
def store_data(filename,records):
        with open(filename,'w') as f:
            json.dump(records,f,indent=4)
