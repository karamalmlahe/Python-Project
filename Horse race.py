#שם : קארם טורי
#מספר ת''ז : 323984195
import time
import random
horseList=[['Cisco',3,2,115],['Cash',4,2,40],['Fancy',2,1,50],['Blue',10,3,55],
           ['Gypsy',14,5,120],['Jack',8,2,50],['Spirit',10,4,75],['Lilly',3,5,70],
           ['Rebel',2,5,100],['Black Jack',10,4,40],['Harley',7,1,30],['Prince',11,1,10]]
def HorseRace(R1,R2,Distance=500):# פונקציה המקבלת שני סוסים ומרחק לריצה
    Distance_R2=Distance_R1=Distance
    print('Race << {} And {} >>'.format(R1[0],R2[0]))
    print('Distance : {}m'.format(Distance))
    while Distance_R1>0 and Distance_R2>0:
        Distance_R1-=random.randrange(10,Distance//10)
        Distance_R2-=random.randrange(10,Distance//10)
        if Distance_R1>0 and Distance_R2>0:
            if Distance_R1<Distance_R2: print('{:15}[{:3}] : {:15}[{:3}]'.format(R1[0],Distance_R1,R2[0],Distance_R2))
            else: print('{:15}[{:3}] : {:15}[{:3}]'.format(R2[0],Distance_R2,R1[0],Distance_R1))
        time.sleep(0.2)
    if Distance_R1<Distance_R2:
        print('{:5} Finished First!'.format(R1[0]))
        print('{:5} Finished On 2-th Place!'.format(R2[0]))
        print('----------------------------------------')
        return R1
    else:
        print('{:5} Finished First!'.format(R2[0]))
        print('{:5} Finished On 2-th Place!'.format(R1[0]))
        print('----------------------------------------')
        return R2
def ChoiceHorses(HList,n=4):#HList=Horse List   ,   n=Amount
    NewList=random.sample(HList,n)#בחירת מספר סוסים מהטבלה בלי חזרה
    return NewList
def printList(HList,n=0):
    print('Horses List : ')
    if n==0:#אם המספר הוא 0 יש להציג כל טבלת הסוסים
        for i in range (len(HList)):
            print('{:2}. {:20}{:4}{:4}{:4}'.format(i+1,HList[i][0],HList[i][1],HList[i][2],HList[i][3]))
    elif n>0:#אם המספר הוא חיובי יש להדפיס סוסים מתחילת הרשימה עד המספר
        for i in range (n):
            print('{:2}. {:20}{:4}{:4}{:4}'.format(i+1,HList[i][0],HList[i][1],HList[i][2],HList[i][3]))
    else:#אם המספר הוא שלילי יש להדפיס מסוף הרשימה
        for i in range (len(HList)+n,len(HList),1):
            print('{:2}. {:20}{:4}{:4}{:4}'.format(i+1,HList[i][0],HList[i][1],HList[i][2],HList[i][3]))
def HorseRacing(RName,HList,Distance,n=4):
    ChoiceList=ChoiceHorses(HList,n)
    print('----------------------------------------')
    print('Horse Racing : ',RName)
    print('----------------------------------------')
    print('Horses List : ')
    for i in range (len(ChoiceList)):
        print('{}. {:20}{:4}{:4}{:4}'.format(i+1,ChoiceList[i][0],ChoiceList[i][1],ChoiceList[i][2],ChoiceList[i][3]))
    print('----------------------------------------')
    while len(ChoiceList)>1:#עד שיש ברשימה יותר מסוס אחד
        Max=[]
        i=0
        while i<len(ChoiceList):
            Test=HorseRace(ChoiceList[i],ChoiceList[i+1],Distance)#מחזירים מי המנציח כל פעם 
            Max+=[Test,]#מוספים כל פעם לרשימה מי המנציחים כדי אחר כך לעשות עוד פעם תחרות
            if Test==ChoiceList[i]:  #i הוא המנצח
                HList[HList.index(ChoiceList[i])][2]+=1
                HList[HList.index(ChoiceList[i])][3]+=5#מוסיפים נקודות למי שנצח
            else:  #(i+1) הוא המנצח
                HList[HList.index(ChoiceList[i+1])][2]+=1
                HList[HList.index(ChoiceList[i+1])][3]+=5#מוסיפים נקודות למי שנצח
            i+=2
        ChoiceList=Max
    HList[HList.index(Test)][3]+=5#מוסיפים נקודות למי שנצח בסוף
    print('Tournament {} Winner - {}'.format(RName,Test[0]))
def sortHorses(HList,rp='points',order=2):
    rp=rp.lower()#אם המשתמש נתן מילה עם אותיות גדולות הוא מחליף את האותיות לקטנות 
    if rp=='points':
        if order==2: HList.sort(key=lambda HList : HList[3],reverse=True)
        elif order==1: HList.sort(key=lambda HList : HList[3])
    if rp=='age':
        if order==2: HList.sort(key=lambda HList : HList[1],reverse=True)
        elif order==1: HList.sort(key=lambda HList : HList[1])
    if rp=='wins':
        if order==2: HList.sort(key=lambda HList : HList[2],reverse=True)
        elif order==1: HList.sort(key=lambda HList : HList[2])           
def addHorse(HList):
    HorseN=input('Enter Horse Name : ')
    HorseA=int(input('Enter Age : '))
    Wins=int(input('Enter Number Of Wins In Racing : '))
    Points=int(input('Enter Number Of Points : '))
    HList+=[[HorseN,HorseA,Wins,Points],]#מוסיף את הסוס 
    sortHorses(HList)#מיון יורד לנקודות
def removeHorse(HList):
    sortHorses(HList)#מיון יורד לנקודות
    print('Horse {} Removed From Horses List . '.format(HList[-1][0]))
    HList.remove(HList[-1])#מחיקת את הסוס האחרון מהרשימה
def menu(HList):
    num=0
    while num!=6:
        print('Menu(HorseList)')
        print('----------------------------------------')
        print('[1]Print Horses List.')
        print('[2]Sort Horses List.')
        print('[3]Add Horses.')
        print('[4]Remove Horses.')
        print('[5]Horses Racing.')
        print('[6]Exit.')
        print('----------------------------------------')
        num=int(input('Enter Your Choice : ')or 7)
        if num==1:
            n=int(input('0-All,Positive-First,Negative-Last OR Enter To Default(0) : ')or 0)
            printList(HList,n)
        elif num==2:
            print('Sort Horses List')
            str=input('[points/wins/age], Choice OR Enter To Default(points) : ') or 'points'
            ord=int(input('Ascending/Descending Order], Choice[1/2] OR Enter To Default(2) : ') or 2)
            sortHorses(HList,str,ord)
        elif num==3: addHorse(HList)
        elif num==4: removeHorse(HList)
        elif num==5:
            RN=input('Enter Horse Racing Name : ') or 'N/A'
            n=int(input('Enter Number Of Horses(2,4,8) OR Enter To Default(4) : ') or 4)
            d=int(input('Enter Distance OR Enter To Default(500) : ') or 500)
            HorseRacing(RN,HList,d,n)
        elif num==6: print('Good Bye ! ')
        else: print('Bad Choice')
        print('----------------------------------------')
menu(horseList)



    
