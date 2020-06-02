#This Program is about Parents and Child Generation With Random Selection of Parents There Crossover and Mutation 
dataset=['A','B','C','D','E']



print("Dataset:",dataset)
import random

#p1=[dataset[random.randrange(len(dataset))]
              #for item in range(1)]
#p2=[dataset[random.randrange(len(dataset))]
              #for item in range(1)]

w,h=10,10
Matrix=[[random.sample(dataset,5) for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        print (Matrix[i][j])
        
w,h=10,10
Matrix=[[random.sample(dataset,5) for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix1=(Matrix[i][j])
        

p1=random.sample(Matrix1,5)
p2=random.sample(Matrix1,5)


p1=''.join(str(i) for u in p1 for i in u)

p2=''.join(str(j) for v in p2 for j in v)

#point=input("Enter location:")

#Matrix2=[]

#for i in range(w):
#    for j in range(h):
 #       if(point==Matrix[i][j][4]):
  #          Matrix2.append((Matrix[i][j]))
   #         print(Matrix2)
            
dict={'AB':1,'AC':2,'AD':3,'AE':3,'AF':24,'BA':4,'BC':5,'BD':3,'BE':1,'BF':42,'CA':5,'CB':3,'CD':5,'CE':6,'CF':22,'DA':7,'DB':4,'DC':3,'DE':8,'DF':13,'EA':2,'EB':7,'EC':5,'ED':9,'EF':42,'FA':1,'FB':2,'FC':3,'FD':4,'FE':5}
#add1=dict[(p1[0:2])]+dict[(p1[2:4])]
#add2=dict[(p2[0:2])]+dict[(p2[2:4])]
#print(add1)
#print(add2)



print("First Parent=",p1)
print("Second Parent=",p2)
print("Crossover point is 3 by default")
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
#Mutation
#child1 FirstCheck

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      a=child1[:-1]
      c1=p1[4]+a

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):      
      a=child1[:-2]
      c1=p1[3:5]+a

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      c1=p1[2:5]+child1[:-3]

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      a=child1[:-4]
      c1=p1[1:5]+a

if(child1[0]==child1[1] or child1[0]==child1[2] or child1[0]==child1[3] or child1[0]==child1[4]):
      a=child1[:-5]
      c1=p1[0:5]+a
#child1 2nd Check

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      a=child1[:-1]
      c1=p1[4]+a

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      a=child1[:-2]
      c1=p1[3:5]+a

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      c21=child1[:-3]
      c1=c21+p1[2:5]

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      c21=child1[:-4]
      c1=c21+p1[1:5]

if(child1[1]==child1[0] or child1[1]==child1[2] or child1[1]==child1[3] or child1[1]==child1[4]):
      c21=child1[:-5]
      c1=c21+p1[0:5]
#child1 3rd check

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      c21=child1[:-1]
      c1=c21+p1[4]

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[1]==child1[3] or child1[1]==child1[4]):
      c21=child1[:-2]
      c1=c21+p1[3:5]

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      c21=child1[:-3]
      c1=c21+p1[2:5]

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      c21=child1[:-4]
      c1=c21+p1[1:5]

if(child1[2]==child1[0] or child1[2]==child1[1] or child1[2]==child1[3] or child1[2]==child1[4]):
      c21=child1[:-5]
      c1=c21+p1[0:5]
#child1 4th check

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      c21=child1[:-1]
      c1=c21+p1[4]

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      c21=child1[:-2]
      c1=c21+p1[3:5]

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      c21=child1[:-3]
      c1=c21+p1[2:5]

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      c21=child1[:-4]
      c1=c21+p1[1:5]

if(child1[3]==child1[0] or child1[3]==child1[1] or child1[3]==child1[2] or child1[3]==child1[4]):
      c21=child1[:-5]
      c1=c21+p1[0:5]
#child1 5th check

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      c21=child1[:-1]
      c1=p1[4]+c21

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      c21=child1[:-2]
      c1=p1[3:5]+c21

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      c21=child1[:-3]
      c1=p1[2:5]+c21

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      c21=child1[:-4]
      c1=p1[1:5]+c21

if(child1[4]==child1[0] or child1[4]==child1[1] or child1[4]==child1[2] or child1[4]==child1[3]):
      c21=child1[:-5]
      c1=p1[0:5]+c21
#CHILD2 1st check

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      c12=child2[:-1]
      c2=p2[4]+c12

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):      
      c12=child2[:-2]
      c2=p2[3:5]+c12

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      c12=child2[:-3]
      c2=p2[2:5]+c12

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      c12=child2[:-4]
      c2=p2[1:5]+c12

if(child2[0]==child2[1] or child2[0]==child2[2] or child2[0]==child2[3] or child2[0]==child2[4]):
      c12=child2[:-5]
      c2=p2[0:5]+c12
#child2 2nd Check

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      c12=child2[:-1]
      c2=p2[4]+c12

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      c12=child2[:-2]
      child2=p2[3:5]+c12

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      c12=child2[:-3]
      c2=p2[2:5]+c12

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      c12=child2[:-4]
      c2=p2[1:5]+c12

if(child2[1]==child2[0] or child2[1]==child2[2] or child2[1]==child2[3] or child2[1]==child2[4]):
      c12=child2[:-5]
      c2=p2[0:5]+c12
#child2 3rd check

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      c12=child2[:-1]
      c2=p2[4]+c12

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[1]==child2[3] or child2[1]==child2[4]):
      c12=child2[:-2]
      c2=p2[3:5]+c12

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      c12=child2[:-3]
      c2=p2[2:5]+c12

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
      c12=child2[:-4]
      c2=p2[1:5]+c12

if(child2[2]==child2[0] or child2[2]==child2[1] or child2[2]==child2[3] or child2[2]==child2[4]):
    c12=child2[:-5]
    c2=p2[0:5]+c12
#child2 4th check

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      c12=child2[:-1]
      c2=p2[4]+c12

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      c12=child2[:-2]
      c2=p2[3:5]+c12

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      c12=child2[:-3]
      c2=p2[2:5]+c12

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      c12=child2[:-4]
      c2=p2[1:5]+c12

if(child2[3]==child2[0] or child2[3]==child2[1] or child2[3]==child2[2] or child2[3]==child2[4]):
      c12=child2[:-5]
      c2=p2[0:5]+c12
#child2 5th check

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      c12=child2[:-1]
      c2=p2[4]+c12

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      c12=child2[:-2]
      c2=p2[3:5]+c12

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      c12=child2[:-3]
      c2=p2[2:5]+c12

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
      c12=child2[:-4]
      c2=p2[1:5]+c12

if(child2[4]==child2[0] or child2[4]==child2[1] or child2[4]==child2[2] or child2[4]==child2[3]):
    c12=child2[:-5]
    c2=p2[0:5]+c12

print("Modifiedchild=",c1[3:5]+c1[0:3])
print("Modifiedchild=",c2[3:5]+c2[0:3])
print("Dear Sir Kindly Feedback At:farjadmohal@gmail.com")

input("Press ENTER to exit")
