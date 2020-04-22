a,b=[int(s) for s in input("Enter 2 numbers comma seprated i.e 1,2 : ").split(",")]
def add(num1,num2):
    print('Sum is :',a+b)
def sub(num1,num2):
    print('Subtraction is :',num1-num2)
def mul(num1,num2):
        print('Multiplication is:',a*b)
def div(num1,num2):
    if num2==0:print('Division by zero not possible')
    else:print('Division s:',a/b)

#Sum
add(a,b)
#multiply
mul(a,b)
#divide
div(a,b)
#subtract
sub(a,b)



