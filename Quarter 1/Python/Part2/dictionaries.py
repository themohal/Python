#my_dict ={key:value,key:value}
my_dict ={"name":"Farjad","age":30,"gender":"Male"}
print(len(my_dict))
print(my_dict.keys())
print(my_dict.get("name"))
print(my_dict.values())
print(my_dict.items())
my_dict["email"]= "farjad@gmail.com"
print(my_dict["email"])
my_dict["email"]= "ali@gmail.com"
print(my_dict["email"])
# finding key
print("email" in my_dict)
#delting
del my_dict["email"]
print(my_dict)

#iterating keys

for keys in my_dict.keys():
    print(keys)

#iterating values
for value in my_dict.values():
    print(value)