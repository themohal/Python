import json
#writing list to json file
alphabet=["a","b","c","d"]
with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myjsonfile.json","w") as filewrite:
    json.dump(alphabet,filewrite)
#reading from json
with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myjsonfile.json","r") as filereader:
    content = json.load(filereader)
    print(content)

customer_29876={
    "first_name":"David",
    "last_name":"Elliot",
    "address":"4803 Wellesly St."
}
with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myjsonfile2.json","w") as filewrite:
    json.dump(customer_29876,filewrite)

with open("G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Part3\myjsonfile2.json","r") as filereader:
    content = json.load(filereader)
    print(content)