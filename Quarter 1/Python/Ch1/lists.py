#list a datastructure that is mutable
listInt = [1,2,3,4,5,6,7,8,9,10]
listString =["Hamza","Fatima","Farjad","Ali","Imran"]
listFloat =[21.2,43.21,67.3,75.3,96.5]
mix = ["Hamza",44.2,221,True,'Pakistan',False]
#accessing value with index
print(mix[4])
#getting length
print("Length is:",len(mix))
#adding into list
print(listInt)
listInt.append(11)
print(listInt)
#insert function takes index and value
#listInt.insert(1,33) index 1 and value 33
#extend also appends value but more than 1
listInt.extend([12,13])
print(listInt)
#count returns the occurance of anything in list
print(listInt.count(6))
#index functuin return the index of value
print(mix.index('Pakistan'))
mix2 =mix.copy() #by value copy it will not get the change
mix3 = mix #by reference copy it will get change 
#removing item from list by index keyword del
del listInt[12]
print(listInt)
#again added
listInt.append(13)
#removing by value
listInt.remove(13) 
print(listInt)
#again added
listInt.append(13)
#pop will also remove using index also returns value . without index stack like 
popped=listInt.pop()
print(popped)
#slicing
print(mix[1:4])
#mix[3:]
#step in list last slice 2 tells how many steps 
print(mix[0:5:2])
#to delete del mix[1:4]
#lists have double index positive and negative
print(len(mix))