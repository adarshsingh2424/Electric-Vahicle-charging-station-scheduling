import carcharge_ljf_1
import carcharge_sjf_1
import carchargefcfs_1
import carcharge_ljf_2
import carcharge_sjf_2
import carchargefcfs_2
import carcharge_ljf_4
import carcharge_sjf_4
import carchargefcfs_4
import matplotlib.pyplot as plt
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],f'Rs{y[i]}',ha="center")
ljf_1=carcharge_ljf_1.check()
sjf_1=carcharge_sjf_1.check()
fcfs_1=carchargefcfs_1.check()
ljf_2=carcharge_ljf_2.check()
sjf_2=carcharge_sjf_2.check()
fcfs_2=carchargefcfs_2.check()
ljf_4=carcharge_ljf_4.check()
sjf_4=carcharge_sjf_4.check()
fcfs_4=carchargefcfs_4.check()
data = {f'ljf_1_{ljf_1[1]}':ljf_1[0], f'sjf_1_{sjf_1[1]}':sjf_1[0], f'fcfs_1_{fcfs_1[1]}':fcfs_1[0],
        f'ljf_2_{ljf_2[1]}':ljf_2[0],f'sjf_2_{sjf_2[1]}':sjf_2[0], f'fcfs_2_{fcfs_2[1]}':fcfs_2[0],
        f'ljf_4_{ljf_4[1]}':ljf_4[0], f'sjf_4_{sjf_4[1]}':sjf_4[0], f'fcfs_4_{fcfs_4[1]}':fcfs_4[0]}
slots = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))
plt.bar(slots, values, color ='maroon',width = 0.4)
addlabels(slots,values)
plt.xlabel("method of charging")
plt.ylabel("profit gained")
plt.title("Charging of electric veichels and profit gained")
plt.show()