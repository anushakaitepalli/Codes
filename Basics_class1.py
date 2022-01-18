#!/usr/bin/env python
# coding: utf-8

# # Basic session

# # String

variable=value

#to comment the line :   ctrl+? (jupyter) or ctrl+!(spyder)

# string1="hello world. this is our first session"
# string2='hello world. this is our first session'
string3=''' hello world. this is our first session'''

# string1
# string2
string3

print("This is string1 value",string1," the text is ended",)
# print(string1)
# print(string1)

print(string3)

stt='''hello world.
this is our first session
'''

stt='hello world.
this is our first session
'

stt

print(stt)


# # numeric

x=100

x

print(x)
y=100.0987
y
print(y)

# stt,x,y
print(type(stt),type(x),type(y))
print()
print()

print("hello world, this is first session")
print("hello world, this is second session")

print(x)
print(y)

# # sequences

# ## List
lst=list([])
lst=list(variable)
lst=[1,2,3,4,5]
# lst=["a","b","c","d","e"]
# 0-a,1-b,2-c

lst
print(lst)

lst[0]

lst[4]

lst[0:4]
lst[:3]
lst[2:]
lst
# replace positon 0 with 10 vlaue
lst[0]=10
lst
lst[-3:-1]
lst[-2:]
# ## Tuple
tup=tuple(variable)
tup=(1,2,3,4,5)
tup(0)
tup[0]
tup[-2:]
tup[0:-1]

#we can not reassign values to tuple values
tup[0]=10

# ## set
sett={}
sett=set(variable)
sett={"a","b","c","d"}
sett
sett{0}
sett[0]
sett={"a","a","b","c","c","z","d"}
sett
#conversion

lst1=[1,2,3,4,5,100,2,3,4,5]
lst1
seq_set=set(lst1)
seq_set
type(seq_set)
lst2=list(seq_set)
lst2
type(lst2)

lst2[0:-1]
lst2[-1]
# # #dict
dictt=dict(variable)
dictt={"class_name" : class_value , "class_name1" : class_value1,   ,   }

dictt={"class_name" : {class_value1,class_value2,..,class_valuen} , "class_name1" : [class_value1,class_value2,..,class_valuen]}

dic_test={      }
dictt={ "states" : "KA" ,"corona_cases" : 2000}
print(dictt)

import numpy as np

dictt

dictt1={ "states" : ["KA","AP","OD","UP"] ,"corona_cases" : [2000,3000,4000,np.nan]}
print(dictt1)


dictt1_test={ "states" : ["KA","AP","OD","UP"] ,"corona_cases" : [2000,3000,4000]}

dictt1_test
dictt1

col1,cl2

dictt1

dictt1.keys()

dictt1[0:3]
get_ipython().show_usage()

dictt1["states"][0:3]

dictt1["states"][-3]

dictt1["corona_cases"][-3]

dictt1["corona_cases"][0:-2]

dictt1["corona_cases"][-3:]
month_filter={'jul','jun','jul'}











