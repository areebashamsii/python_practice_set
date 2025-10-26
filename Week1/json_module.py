## JSON stands for JavaScript Object Notation.
# JSON is a file format which can be easily read,write and share , you can't use data of python stored variable so you first covert 
# it into a JSON String for APIS.
## Creating a python dictionary and convertig it into a JSON string. ##
#import JSON module
import json
product_info={  # python dictionary
 
"headphone":{"Name":"Zero","price":3000},
"Cable":{"Name":"Ronin","price":500},
"Mobile Cover":{"Name":"Layer","price":700},
}

#coverting and storing it into a JSON file
with open("data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=2) 
    
      ## Explaination ##
# "with" close the file after storing the data , 
#"Open()" open the given file ,
# open(file_name,"W" means write mode) as f where f is the varible name to store python dict into json str
#json.dump() to convert python dict into a json str
#json.dump(dict_name,jason_file_name, indent=value) # indent=4 will give 4 space after every level for the readabilty
 
 # Adding value in python dic:
  
product_info["Mouse"]={"Name":"Lenovo","Price":4000}

with open("data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=2) 
    
# We cant direclty add value in json str so we do the above step.

## delete a key value pair from the JSON file

with open("data.json","r") as product_info_json: # to read an existing jason file
    product_info = json.load(product_info_json) #to load a jason file or to convert it into a python dic for updation or deletion
product_info.pop("Cable",None) #dict_name.pop("key",None) is to delete a value from an existing dict

#save the updated dict into json
with open("data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=3)