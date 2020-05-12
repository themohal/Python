for a in range(5):
    print("inner loop begin")
    for char in "China":
        print(a,char)

Tablenumber = int(input("Enter Table Number:"))

for a in range(1,11):
    print(f"{Tablenumber}*{a} = {Tablenumber*a}")


Table = int(input("Enter Table Number:"))
for a in range(1,Table+1):
    for b in range(1,11):
        print(f"{a}*{b} = {a*b}")