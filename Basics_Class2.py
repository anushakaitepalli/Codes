#!/usr/bin/env python
# coding: utf-8

# # Conditions

# ## if condition

# In[ ]:


# syntax:
if condition:
    
    <expression>
    <...   ...>


# In[ ]:


variable
value
assign operators
variable operator value


# In[1]:


import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
# Read Images 
img = mpimg.imread('pic_for_conditions.png') 

img = mpimg.imread('C:\\Paramatma_Pulivarthi\\Data_Science_course\\python_training_2_December2021\\pic_for_conditions.png')   
# Output Images 
plt.imshow(img)

print("")
print(var)
print("",var)

age=50
# age
print("my age is ",age," age already printed")

# scenario : print sales >50 as weekend sales 
# Sales =60

compare_sale=50
sales=60


if sales > compare_sale :
    print("weekend sales")
# print("the weekend sales",sales)

sales=40
if sales < 50 :
    print("weekend sales")


# # #if else

# Syntax:
if condition:
    <statements>
    <....   ....>
else:
    <statements>
    <....   ...>

# scenario : print sale >50 as weekend sales, otherwise as weekday sales 

sale=60

if sale>50:
    print("weekend sale")
else:
    
    print("weekday sales")

sale=40
if sale>50:
    print("weekend sale")
else:
    print("weekday sales")

# ## if elif else

# Syntax:
if condition:
    <statements>
    <....   ....>
elif condition:
    <statements>
    <....   ....>    
elif condition:
    <statements>
    <....   ....>     
else:
    <statements>
    <....   ...>


# scenario : print sale <15 as "not met average sales",
# sale >=15 & <=20 "met average sales",
#15,16.17.18.19.20

#or
#15  16  20

# sale >20 as "profit sales"

sale=80
if sale<15:
    print("not met average sales")
elif sale>=15 or sale<=20:
    print("met average sales")
else:
    print("profit sales")

#10,20,30

sale=80
if sale<15:
    print("not met average sales")
elif sale>=15 and sale<=20:
    print("met average sales")
else:
    print("profit sales")


# # Loops

# ## for loop

# In[ ]:

#3--
#1-
# syntax:
for expression:
    
    <statements>

# ["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"]

/*
increment

req--
increment-4
kkr
csk
kxiip

increment-1
kkr
mi
CSK
rcb
*/
lst=["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"]

iterate=lst[0]
kkr
iterate=lst[1]
mi
iterate=lst[2]
csk

lst=["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"]
for ipl_team_name in lst:
    
    
    print(ipl_team_name)
    
# ********    
#incream-1

ipl_team_name=lst[increm]
ipl_team_name=lst[0]
kkr
ipl_team_name=lst[1]
mi

ipl_team_name=lst[8]
dc

tup=("KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC")
for p in tup:
    print("the ipl team name is",p)

sett={"KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"}
for p in sett:
    print("********* theis is name of ipl team*********",p)

dictt={"IPL_Teams":["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"]}


for p in dictt["IPL_Teams"]:
    print(p)

/*
kkr
mi
.
.
10
20
30
..
*/

dictt={"IPL_Teams":["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"],"first_score": [10,20,40,50,60,70,80]}
dictt.keys()
for p in dictt:
    print(p)

# range
/*
1
2
3
4
5
6
7
8
9
req-2

101
102
103
104
105
req-2
2
4
6
8
10
requ-7

*/
range(start point,end point,increment point)
range(0,10)
range(0,10,5)
range(0,10,1)
range(10)

for p in range(0,10,1):
    print(p)

for p in range(0,10):
    print(p)

for p in range(10):
    print(p)

for p in range(5,10,2):
    print(p)

for p in range(5,10):
    print(p)

for p in range(0,60,6):
    print(p)

