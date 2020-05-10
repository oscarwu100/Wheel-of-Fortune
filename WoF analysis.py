################################################################################
# Author: BO-YANG WU
# Date: 04/23/2020
# This program counts the number of times each letter in the phrases.txt file is used. 
################################################################################
import re
import matplotlib.pyplot as plt

f= open('phrases.txt')
f1= f.read()
s1 = re.sub(r'[^\w 0-9]|_', '', f1)
f.close()

data= s1.split()
data1= [list(i.upper()) for i in data]
data2= []
for i in data1:
    for j in range(len(i)):
        data2.append(i[j])
data3= sorted(data2)
data3.append('')
y= []
j= 1
t= 0
for i in range(len(data3)- 1):
    if data3[i+ 1]== data3[i]:
        j+= 1
    else:
        t+= j
        y.append(j)
        j= 1
y1= []
for i in y:
    y1.append(i/ t)
fig, ax = plt.subplots()
x= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x= list(x)
ax.bar(x, y1)
ax.grid()
plt.title('Letter Frequency in Puzzle Phrases')
plt.xlabel('Letter', fontsize=10)
plt.ylabel('Letter Appearance Frequency', fontsize=10)

plt.savefig('WoF analysis.pdf', dpi=500, bbox_inches='tight')

plt.show()