import numpy as np  
import matplotlib.pyplot as plt

con_arr = []
dev_arr = []

line0 = input()
n = int(line0)
name = ''
for i in  range(50):
	line1 = input()
	name = line1[0:line1.find(" ")]
	line2 = input()
	line3 = input()
	con = int(line2[line2.find(":")+1:])
	dev = float(line3)
	if con > 100:
		continue
	con_arr.append(con)
	dev_arr.append(dev)

for i in range(len(con_arr)):
	tmp = i
	for j in range(i + 1, len(con_arr)):
		if con_arr[tmp] > con_arr[j]:
			tmp = j
	if not tmp == i:
		temp1 = con_arr[tmp]
		temp2 = dev_arr[tmp]
		con_arr[tmp] = con_arr[i]
		dev_arr[tmp] = dev_arr[i]
		con_arr[i] = temp1
		dev_arr[i] = temp2

plt.figure()
plt.xlabel('iterator time')
plt.ylabel('deviation')
plt.plot(con_arr, dev_arr)  
plt.savefig("./"+name+str(n)+".png")  