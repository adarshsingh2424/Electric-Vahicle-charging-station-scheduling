import csv
from datetime import time
def check():
    l=[]
    l1=[]
    f=open('charging.csv','r+',newline='')
    read1=csv.reader(f)
    for row in read1:
        l.append(row)
    for i in range(1,len(l)):
        h,m=l[i][1].split(':')
        l[i][1]=[int(h),int(m)]
        charge=int(l[i][2])
        left_charge=100-charge
        if left_charge<60:
            left_charge=[0,left_charge]
        else:
            left_charge=[1,left_charge-60]
        l[i][2]=left_charge
    for i in range(1,len(l)):l[i][3]=[0,0]
    x=[l[1][1][0]+l[1][2][0],l[1][1][1]+l[1][2][1]]
    if x[1]>=60:
        x=[x[0]+1,x[1]-60]
    l[1][3]=x
    l1.append(l[0])
    l1.append(l[1])
    for i in range(2,len(l)):
        if l[i][1][0]>=l1[-1][3][0]:
            if l[i][1][1]>=l1[-1][3][1]:
                
                x=[l[i][1][0]+l[1][2][0],l[i][1][1]+l[i][2][1]]
                if x[1]>=60:x=[x[0]+1,x[1]-60]
                l[i][3]=x
                l1.append(l[i])
    profit=0   
    for i in range(1,len(l1)):
        l1[i][1]=str(l1[i][1][0])+":"+str(l1[i][1][1])
        x=(l1[i][2][0])*60+(l1[i][2][1])
        profit+=10*x
        l1[i].append(x*10)
        l1[i][2]=100-x
        
        l1[i][3]=str(l1[i][3][0])+":"+str(l1[i][3][1])
    print("-------------------------fcfs---------------------------------")
    print("Total Profit=",profit)
    print("Total cars charged=",len(l1))
    print(l1[0][0],l1[0][1],l1[0][2],l1[0][3],'Profit','slot')
    for i in range(1,len(l1)):
        print(l1[i][0],"\t",l1[i][1],"\t",l1[i][2],"\t",l1[i][3],"\t",l1[i][4],'\t','1')    
    return([profit,len(l1)])
