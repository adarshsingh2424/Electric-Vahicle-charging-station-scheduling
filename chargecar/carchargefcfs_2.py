
import csv

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
    l1.append(l[0])
    '''x=[l[1][1][0]+l[1][2][0],l[1][1][1]+l[1][2][1]]
`    if x[1]>=60:
        x=[x[0]+1,x[1]-60]
        
    l[1][3]=x
    l1.append(l[0])
    l1.append(l[1])'''
    l3=[[],[]]
    x = [l[1][1][0]+l[1][2][0], l[1][1][1]+l[1][2][1]]
    if x[1] >= 60:
        x = [x[0]+1, x[1]-60]
    if x[0] >= 24:
        x[0] = x[0]-24
    x[1] = str(x[1])
    l[1][3] = x
    l3[0] = l[1]
    l[1].append(1)
    l1.append(l[1])
    x = [l[2][1][0]+l[2][2][0], l[2][1][1]+l[2][2][1]]
    if x[1] >= 60:
        x = [x[0]+1, x[1]-60]
    if x[0] >= 24:
        x[0] = x[0]-24
    x[1] = str(x[1])
    l[2][3] = x
    l3[1] = l[2]
    l[2].append(2)
    l1.append(l[2])
    for i in range(1,len(l)):
        
        for j in range (2):
            
            if l[i][1][0] >= int(l3[j][3][0]):
                if l[i][1][0]==int(l3[j][3][0]): #if reach of upcoming car is equal to leaving time of gone car comparing only hrs
                    if l[i][1][1]>=int(l3[j][3][1]):
            
                        x=[l[i][1][0]+l[i][2][0],l[i][1][1]+l[i][2][1]]
                        if x[1]>=60:x=[x[0]+1,x[1]-60]
                        if x[0]>=24:x[0]=x[0]-24
                        x[1]=str(x[1])
                        l[i][3]=x
                        l[i].append(j+1)
                        l1.append(l[i])
                        l3[j]=l[i]
                        break
                
                
        
                elif l[i][1][0]>int(l3[j][3][0]):
                    x=[l[i][1][0]+l[i][2][0],l[i][1][1]+l[i][2][1]]
                    if x[1]>=60:x=[x[0]+1,x[1]-60]
                    if x[0]>=24:x[0]=x[0]-24
                    x[1]=str(x[1])
                    l[i][3]=x
                    l[i].append(j+1)
                    l1.append(l[i])
                    l3[j]=l[i]
                    break
                
                elif l[i][1][0]>int(l3[j][3][0]): #if hrs of upcoming car is greater than hrs of gone car
                    x=[l[i][1][0]+l[i][2][0],l[i][1][1]+l[i][2][1]]
        
                    if x[1]>=60:x=[x[0]+1,x[1]-60]
                    if x[0]>=24:x[0]=x[0]-24
                    x[1]=str(x[1])
                    l[i][3]=x
                    l[i].append(j+1)
                    l1.append(l[i])
                    l3[j]=l[i]
                    break

                    
            
            
        
    profit=0   
    for i in range(1,len(l1)):
        l1[i][1]=str(l1[i][1][0])+":"+str(l1[i][1][1])
        x=(l1[i][2][0])*60+(l1[i][2][1])
        profit+=10*x
        l1[i].append(x*10)
        l1[i][2]=100-x
        
        l1[i][3]=str(l1[i][3][0])+":"+str(l1[i][3][1])
    print("-----------------fcfs---------------------")
    print("Profit gained=",profit)
    print("No of cars charged=",len(l1))
    print(l1[0][0],l1[0][1],l1[0][2],l1[0][3]," Slot number","Profit gained")
    f1=open('charged.csv','a+',newline='')
    writer_object = csv.writer(f1)
    writer_object.writerow(["fcfs",str(profit),str(len(l1))])
    f.close()
    f1.close()
    
    for i in range(1,len(l1)):
        print(l1[i][0],"\t",l1[i][1],"\t",l1[i][2],"\t",l1[i][3],"\t","\t",l1[i][4],"\t\t",l1[i][5])   
    return([profit,len(l1)])
