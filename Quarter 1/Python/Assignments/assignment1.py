import pandas
data = pandas.read_csv('G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\Assignments\StudentsPerformance.csv')
gender = data['gender'].values.tolist()
pLevelEdu=data['parental level of education'].values.tolist()
testPrepCourse=data['test preparation course'].values.tolist()
mathScore= data['math score'].values.tolist()
readingScore=data['reading score'].values.tolist()
writingScore =data['writing score'].values.tolist()
fList =[]
mList =[]
PTCTestlist=[]
PTNTestlist=[]
parentAlist=[]
parentBlist=[]
parentClist=[]
parentDlist=[]
parentElist=[]




def betterPerformance():
    
    for (a, b,c,d) in zip(gender, mathScore,readingScore,writingScore):
        if a=='female':
            fList.append(b)
            fList.append(c)
            fList.append(d)
        elif a=='male':
            mList.append(b)
            mList.append(c)
            mList.append(d)
    fCount=0
    mCount=0
    for i,j in zip(fList,mList):
        if i>j:
            fCount+=1
        elif j>i:
            mCount+=1

    if fCount>mCount:
        print("Females are performing well")
    else:
        print("Males are performing well")

def betterPerformanceOnPreparation():
    for (a, b,c,d,e) in zip(gender,testPrepCourse, mathScore,readingScore,writingScore):
        if a=='female' or a=='male' and b=='completed':
            PTCTestlist.append(c)
            PTCTestlist.append(d)
            PTCTestlist.append(e)
        elif a=='female' or a=='male' and b=='none':
            PTNTestlist.append(c)
            PTNTestlist.append(d)
            PTNTestlist.append(e)
    fPCount=0
    mPCount=0
    for i,j in zip(PTCTestlist,PTNTestlist):
        if i>j:
            fPCount+=1
        elif j>i:
            mPCount+=1

    if fPCount>mPCount:
        print("Students who took test preparation course performed well.")
    else:
        print("Students who doesn't took test preparation course performed well.")

def PerformanceOnParentEducation():
    for (a, b,c,d) in zip(pLevelEdu,mathScore,readingScore,writingScore):
        if a=='bachelor\'s degree':
            parentAlist.append(b)
            parentAlist.append(c)
            parentAlist.append(d)
        elif a=='some college':
            parentBlist.append(b)
            parentBlist.append(c)
            parentBlist.append(d)
        elif a=='master\'s degree':
            parentClist.append(b)
            parentClist.append(c)
            parentClist.append(d)
        elif a=='associate\'s degree':
            parentDlist.append(b)
            parentDlist.append(c)
            parentDlist.append(d)
        elif a=='high school':
            parentElist.append(b)
            parentElist.append(c)
            parentElist.append(d)
    countA=0
    countB=0
    countC=0
    countD=0
    countE=0
    for i,j,k,l,m in zip(parentAlist,parentBlist,parentClist,parentDlist,parentElist):
        if i>j and i>k and i>l and i>m:
            countA+=1
        elif j>i and j>k and j>l and j>m:
            countB+=1
        elif k>i and k>j and k>l and k>m:
            countC+=1
        elif l>i and l>j and l>k and l>m:
            countD+=1
        elif m>i and m>j and m>k and m>l:
            countE+=1


    if countA>countB and countA>countC and countA>countD and countA>countE:
        print("Children of those Parents with bachelor\'s degree performed well")
    elif countB>countA and countB>countC and countB>countD and countB>countE:
        print("Children of those Parents with some college degree performed well")
    elif countC>countA and countC>countB and countC>countD and countC>countE:
        print("Children of those Parents with master\'s degree performed well")
    elif countD>countA and countD>countB and countD>countC and countD>countE:
        print("Children of those Parents with associate\'s degree performed well")
    elif countE>countA and countE>countB and countE>countC and countE>countD:
        print("Children of those Parents with high school degree performed well")

    print("Hence Parents Education Has Good Impact On Students Performance")    



betterPerformance()
betterPerformanceOnPreparation()
PerformanceOnParentEducation()

# allFemale= []
# allMale=[]
# # for row in enumerate(data.iterrows()):
# #     for element in row:
# #         if 'female' in (str(element)).lower():
# #             allFemale.append(element)
# #         elif 'male' in (str(element)).lower():
# #             allMale.append(element)

# # print(allMale[0])





    


    
