## JSON stands for JavaScript Object Notation.
# JSON is a file format which can be easily read,write and share , you can't use data of python stored variable so you first covert 
# it into a JSON String for APIS.
## Creating a python dictionary and convertig it into a JSON string. ##
#import JSON module
import json

product_info={  # python dictionary
 
"headphone":{"Name":"Zero","price":3000},
"Cable":{"Name":"Ronin","price":500},
"Mobile Cover":{"Name":"Layer","price":700}
}

#coverting and storing it into a JSON file
with open(r"C:\Users\USER\Documents\Python\Week1\JSON_MODULE\data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=2) 
    
      ## Explaination ##
# "with" close the file after storing the data , 
#"Open()" open the given file ,
# open(file_name,"W" means write mode) as f where f is the varible name to store python dict into json str
#json.dump() to convert python dict into a json str
#json.dump(dict_name,jason_file_name, indent=value) # indent=4 will give 4 space after every level for the readabilty
 
 #updating key

with open(r"C:\Users\USER\Documents\Python\Week1\JSON_MODULE\data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=2) 
product_info["Headphone"]=product_info["headphone"]


 # Adding value in python dic:
  

with open(r"C:\Users\USER\Documents\Python\Week1\JSON_MODULE\data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=2) 
    
# We cant direclty add value in json str so we do the above step.

## delete a key value pair from the JSON file

with open(r"C:\Users\USER\Documents\Python\Week1\JSON_MODULE\data.json","r") as product_info_json: # to read an existing jason file
    product_info = json.load(product_info_json) #to load a jason file or to convert it into a python dic for updation or deletion
product_info.pop("Cable",None) #dict_name.pop("key",None) is to delete a value from an existing dict

#save the updated dict into json
with open("c:/Users/USER/Documents/Python/Week1/JSON_MODULE/data.json","w") as product_info_json:
    json.dump(product_info,product_info_json,indent=3,sort_keys=True) # sort_keys=True will sort the keys alphabatically
print(product_info)

## Converting 3 different i.e nested JSON str into separate python dict:


#load file

with open(r"C:\Users\USER\Documents\Python\Week1\JSON_MODULE\uni_infor.json", "r") as info:
    uni_info=json.load(info)

student_info=uni_info["stu_info"]
visiting_faculty=uni_info["staff_info"]["visiting_faculty"]
uni_faculty=uni_info["staff_info"]["uni_faculty"]

print("Studnet Info:",student_info)
print("visiting faculty:",visiting_faculty)
print("University faculty",uni_faculty)

## dumps over dump use: ( dump store the json str in file where as dumps only convert 
# the dict into json str but donot store in a seperate file) ##

items={
    "Car":{"name":"Nissan GTR"},
    "Bike":{"name":"Yamaha"},
    "SUV":{"name":"Fortuner"},

} 
print(items)
print(type(items))
# convert into json str
item_json=json.dumps(items) #convert the python dic into json str but won't store in file ,is shareable and good for API
print(item_json)
print(type(item_json))

## loads over load
# loads is used to read json str which is store in the code as python dict and not in the separate json file

item_dict=json.loads(item_json)
print(item_dict)
print(type(item_dict)) #converted again into a python dict

## .get , it sets the default value of the key so that if value doesn't exist the keyError not appear insted the defualt value will print

#print(items("Bicycle"))                     #will through an error
print(items.get("Bicycle", "Not Found!")) #.gets only work in python dict so first convert json into py dict.
