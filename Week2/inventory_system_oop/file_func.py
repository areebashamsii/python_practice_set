import json
import os

filename=r"C:\Users\USER\Documents\Python\Week2\inventory_system_oop\data.json"


def read_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename,'r') as f:
                records=json.loads(f)
                return records
        except:
            json.JSONDecodeError
            return
    else:
        return []
    
def add_data(filename,records):
    with open(filename,'w') as f:
        json.dump(records,f,indent=4) 
          