a=0
while(a<=10):
    print(a)
    a+=1

for num in range(0,11):
    print(f"{num}:this is for loop printing")

a=1
while(a!=10):
    userInput = int(input("Enter favorite food:"))
    if(userInput==0):
        break
    a+=1

flag =True
foodList=[]
while flag:
    userInput= input("Enter Foods:")
    if(userInput=="Q" or userInput=='q'):
        print(foodList)
        flag=False
    else:
        foodList.append(userInput)
