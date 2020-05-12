fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)


for i in range(5):
    print(i,"Farjad")

for number in range(1,10,3): #with 3 step
    print(number)

for number in range(10,1,-2): #with 3 step in reverse
    print(number)

for k in [12,44,65,32,74,23,72]:
    print(k)