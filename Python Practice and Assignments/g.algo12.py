dataset=['A','B','C','D','E']


AB=1
AC=2
AD=3
AE=3
BA=4
BC=5
BD=3
BE=1
CA=5
CB=3
CD=5
CE=6
DA=7
DB=4
DC=3
DE=8
EA=2
EB=7
EC=5
ED=9

print("Dataset:",dataset)
import random

#p1=[dataset[random.randrange(len(dataset))]
              #for item in range(1)]
#p2=[dataset[random.randrange(len(dataset))]
              #for item in range(1)]

w,h=2,2
Matrix=[[random.sample(dataset,5) for x in range(w)] for y in range(h)]
print (Matrix)

for row in Matrix:
    p1=random.sample(row,1)

for row in Matrix:
    p2=random.sample(row,1)


p1=''.join(str(i) for u in p1 for i in u)

p2=''.join(str(j) for v in p2 for j in v)

print("First Parent=",p1)
print("Second Parent=",p2)
#1stcross over

ch1=[]
i=0
while(i<3):
    ch1.append(p1[i])
    i=i+1



ch2=[]
j=3
while (j<=4):
    ch2.append(p2[j])
    j=j+1
    
    

child1=ch1+ch2
child1=''.join([str(i) for i in child1])
print("First Child=",child1)
#2nd cross over

ch1=[]
i=3
while i<=4:
     
     ch1.append(p1[i])
     i+=1


ch2=[]
i=0
while i<3:
      
      ch2.append(p2[i])
      i+=1


child2=ch2+ch1
child2=''.join([str(i) for i in child2])
print("Second Child=",child2)

#child1 FirstCheck

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      achild1=p1[4:5]
      achild2=child1[:-1]
      achild=achild2+achild1

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):      
      achild1=p1[3:5]
      achild2=child1[:-2]
      achild=achild2+achild1

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      achild1=p1[2:5]
      achild2=child1[:-3]
      achild=achild2+achild1

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      achild1=p1[1:5]
      achild2=child1[:-4]
      achild=achild2+achild1

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      achild1=p1[0:5]
      achild2=child1[:-5]
      achild=achild2+achild1
#child1 2nd Check

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      achild1=p1[4:5]
      achild2=child1[:-1]
      achild=achild2+achild1

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      achild1=p1[3:5]
      achild2=child1[:-2]
      achild=achild2+achild1

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      achild1=p1[2:5]
      achild2=child1[:-3]
      achild=achild2+achild1

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      achild1=p1[1:5]
      achild2=child1[:-4]
      achild=achild2+achild1

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      achild1=p1[0:5]
      achild2=child1[:-5]
      achild=achild2+achild1
#child1 3rd check

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      achild1=p1[4:5]
      achild2=child1[:-1]
      achild=achild2+achild1

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[1]==child1[3] or child1[1]==child1[4]):
      achild1=p1[3:5]
      achild2=child1[:-2]
      achild=achild2+achild1

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      achild1=p1[2:5]
      achild2=child1[:-3]
      achild=achild2+achild1

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      achild1=p1[1:5]
      achild2=child1[:-4]
      achild=achild2+achild1

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      achild1=p1[0:5]
      achild2=child1[:-5]
      achild=achild2+achild1
#child1 4th check

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      achild1=p1[4:5]
      achild2=child1[:-1]
      achild=achild2+achild1

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      achild1=p1[3:5]
      achild2=child1[:-2]
      achild=achild2+achild1

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      achild1=p1[2:5]
      achild2=child1[:-3]
      achild=achild2+achild1

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      achild1=p1[1:5]
      achild2=child1[:-4]
      achild=achild2+achild1
#child1 5th check

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      achild1=p1[4:5]
      achild2=child1[:-1]
      achild=achild2+achild1

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      achild1=p1[3:5]
      achild2=child1[:-2]
      achild=achild2+achild1

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      achild1=p1[2:5]
      achild2=child1[:-3]
      achild=achild2+achild1

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      achild1=p1[1:5]
      achild2=child1[:-4]
      achild=achild2+achild1

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      achild1=p1[0:5]
      achild2=child1[:-5]
      achild=achild2+achild1
#CHILD2 1st check

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      bchild1=p2[4:5]
      bchild2=child2[:-1]
      bchild=bchild2+bchild1

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      bchild1=p2[3:5]
      bchild2=child2[:-2]
      bchild=bchild2+bchild1

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      bchild1=p2[2:5]
      bchild2=child2[:-3]
      bchild=bchild2+bchild1

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      bchild2=child2[:-4]
      bchild1=p2[1:5]
      bchild=bchild2+bchild1

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      bchild1=p2[0:5]
      bchild2=child2[:-5]
      bchild=bchild2+bchild1
#child2 2nd Check

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      bchild1=p2[4:5]
      bchild2=child2[:-1]
      bchild=bchild2+bchild1

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      bchild1=p2[3:5]
      bchild2=child2[:-2]
      bchild=bchild2+bchild1

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      bchild1=p2[2:5]
      bchild2=child2[:-3]
      bchild=bchild2+bchild1

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      bchild1=p2[1:5]
      bchild2=child2[:-4]
      bchild=bchild2+bchild1

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      bchild1=p2[0:5]
      bchild2=child2[:-5]
      bchild=bchild2+bchild1
#child2 3rd check

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      bchild1=p2[4:5]
      bchild2=child2[:-1]
      bchild=bchild2+bchild1

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[1]==child2[3] or child2[1]==child2[4]):
      bchild1=p2[3:5]
      bchild2=child2[:-2]
      bchild=bchild2+bchild1

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      bchild1=p2[2:5]
      bchild2=child2[:-3]
      bchild=bchild2+bchild1

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      bchild1=p2[1:5]
      bchild2=child2[:-4]
      bchild=bchild2+bchild1

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      bchild1=p2[0:5]
      bchild2=child2[:-5]
      bchild=bchild2+bchild1
#child2 4th check

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      bchild1=p2[4:5]
      bchild2=child2[:-1]
      bchild=bchild2+bchild1

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      bchild1=p2[3:5]
      bchild2=child2[:-2]
      bchild=bchild2+bchild1

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      bchild1=p2[2:5]
      bchild2=child2[:-3]
      bchild=bchild2+bchild1

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      bchild1=p2[1:5]
      bchild2=child2[:-4]
      bchild=bchild2+bchild1

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      bchild1=p2[0:5]
      bchild2=child2[:-5]
      bchild=bchild2+bchild1
#child2 5th check

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      bchild1=p2[4:5]
      bchild2=child2[:-1]
      bchild=bchild2+bchild1

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      bchild1=p2[3:5]
      bchild2=child2[:-2]
      bchild=bchild2+bchild1

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      bchild1=p2[2:5]
      bchild2=child2[:-3]
      bchild=bchild2+bchild1

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      bchild1=p2[1:5]
      bchild2=child2[:-4]
      bchild=bchild2+bchild1

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      bchild1=p2[0:5]
      bchild2=child2[:-5]
      bchild=bchild2+bchild1

print("Modifiedchild=",achild)
print("Modifiedchild=",bchild)
AB+AC
AD+AE
BA+BC
BD+BE
CA+CB
CD+CE
DA+DB
DC+DE
EA+EB
EC+ED
input("Press ENTER to exit")
