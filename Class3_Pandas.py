#!/usr/bin/env python
# coding: utf-8

# Function/ user defined function


# In[ ]:

#10
#20

# syntax:
def function_name(parameters1,par2,par3..,par_n):
    
    jkj
        jkhjkh
    
    <statements>
    <logic>
    return var
    return (var,var,var_n)
/*
10
20

10+20

30    

*/
#scenario : create a function to add two number a and b 

def param():
    a=10
    b=20
    c=a+b
    return c

param()

addition()

var="this is test"

type(var)
def type(para):
         <statement>
         return var
def multiplication(a=10,b=20):    
    c=a*b    
    return c

multiplication(10,20)
multiplication(50,60)
multiplication(60)
type(variable)

#scenario- share market :Returns for your investment amount is 20%. if no.of shares are more than 5 provide 5% extra percentage. 
condition products-shares
investment amount

def share_market(invest_amount=100000,share=4):
    
    if share >5 :
        retun=invest_amount*.25
        100000*.25
    else :
        retun=invest_amount*.20
        100000*.20
    return retun

share_market(100000,8)

share_market(100000,4)

#scenario- IPL-zoomato: Make predicted score & get offer. Team made <150 then 10% off on order. 
# score 150-200 then 20% ,
# score >200 then 50%


# # Pandas

# In[ ]:


#Data Read/Import
#read_csv,read_excel,read_table
#sep,header,sheet_name

import pandas as t
import pandas

/*
100
1
2
98

*/

from pandas  import read_csv,read_excel,
import numpy as np

dictt={"IPL_Teams":["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"],"first_score": [10,20,40,50,60,70,80,np.nan]}

dictt


import pandas 

df=pandas.DataFrame(seq,list,tup,set,dict,array,columns=[])


df=pandas.DataFrame(dictt)


df=pandas.DataFrame({"IPL_Teams":["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"],"first_score": [10,20,40,50,60,70,80,np.nan]})

df


IPL_Teams=["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"]


IPL_Teams


import pandas as pd



df_lst=pd.DataFrame(["KKR","MI","CSK","RCB","KXIIP","RR","SRH","DC"],columns=["ipl team",])



df_lst


import pandas as pd
# syntax?
#pd.read_csv(path,sep='',header=None/'infer')
#C:\Userspulivarthi\AV_Hackthons\Janatahack Healthcare Analytics II\train.csv

df=pd.read_csv("C:\\Users\\ppulivarthi\\AV_Hackthons\\Janatahack Healthcare Analytics II\\train.csv")
df

df=pd.read_csv(r"C:\Users\ppulivarthi\AV_Hackthons\Janatahack Healthcare Analytics II\train.csv",header=None)
df

df=pd.read_csv(r"C:\\Users\\ppulivarthi\\AV_Hackthons\\Janatahack Healthcare Analytics II\\train.csv")
df


df=pd.read_csv(r"C:\\Users\\ppulivarthi\\AV_Hackthons\\Janatahack Healthcare Analytics II\\sample_tab.txt")
df

# syntax
pd.read_excel(path,sheet_name='',header=)

#df_new=pd.read_excel(r"]")

#df_new.head()

df=pd.read_excel("C:\\Users\\ppulivarthi\\AV_Hackthons\\Janatahack Healthcare Analytics II\\train_dict_check_mine.xlsx")

df
# to know type of the dataframe
type(df)

# to display top 5 rows 
df.head()

# to display top 10 rows 
df.head(10)
# to display bottom 5 rows
df.tail()
# to display bottom 8 rows
df.tail(8)
# to display no.of rows and columns
dataframe_tup=df.shape


dataframe_tup[0]
dataframe_tup[1]
    
df_new2.shape[1]

df=pd.read_excel(r"C:\Users\ppulivarthi\AV_Hackthons\Janatahack Healthcare Analytics II\train_dict_check_mine - Copy.xlsx",sheet_name="Sheet2")
df

df_tab=pd.read_csv(r"C:\Users\ppulivarthi\AV_Hackthons\Janatahack Healthcare Analytics II\sample_tab.txt")

df_tab

df_tab.head()

#read_table/

df.head()

# to know dataframe columns data types
df.dtypes
# to display columns of dataframe
df.columns
# create list from dataframe columns names
lst=list(df.columns)

lst


#to print column names one by one
for p in lst:
    print(p)


lst1=lst[2:]

lst1
# to know the index of dataframe
df.index
# to display descriptive information about dataframe
df.info()

# Basic checks
# index,shape,head,tail,colums,dtypes,info



/*
comparsion 
(10,20)

age=[10,20,30,40,50]
[20,30]
[10,20]
variable


filter variable
comparision variable/value
comparision 
*/
# filters/Condition
# ==,!=,>,>=,<,<=
# &(and), | (or), isin, ~isin(not in)
#Scenario: Filter only Department is anesthesia
#Scenario: Filter Department except anesthesia
#Scenario: Filter Visitors with Patient are greater than 2
#Scenario: Filter Admission_Deposit is greater than or equal to 5000
#Scenario: Filter City_Code_Hospital are less than 4
#Scenario: Filter Available Extra Rooms in Hospital is less than or equal to 3
#scenario: filter the data for patientid 31397 and Visitors with Patient 2
#scenario: filter the data for Severity of Illness is Extreme or Type of Admission is Emergency
#scenario: filter the data for Department in 'radiotherapy', 'anesthesia' & 'gynecology'
#scenario: filter the data for Ward_Type not in 'S', 'Q' & 'P'


#Scenario: Filter only Department is anesthesia

import pandas as pd

df=pd.read_csv(r"C:\Users\ppulivarthi\AV_Hackthons\Janatahack Healthcare Analytics II\train.csv")
#to display rows and columns
df.shape
#dataframe slice like lst
lst=[1,2,3,]
df
#syntax 
df[star:end]

#display top 2 rows from dataframe
df[0:2]

#display column names
df.columns

#filter the required columns names
#syntax
df_n=df[["column_name","column_name"]]

# filter column names 'case_id' and "Hospital_code"
df_new=df[['case_id',"Hospital_code"]]

df_new


df.columns
# filter column names 'case_id', 'Hospital_code' and 'Hospital_type_code'
df_col_filter=df[['case_id', 'Hospital_code', 'Hospital_type_code']]


df_col_filter

#filter rows of index 10-20 in casi_id column 
df_col_filter['case_id'][10:20]

# check unique columns or distinct columns in department
df.Department.unique()
df['Department'].unique()


# In[ ]:
df['Department'].unique()

#Scenario: Filter only Department is anesthesia
# syntax:df[filter]
# fil_var='anesthesia'
df_dep_fil=df[ df['Department']  ==  'anesthesia' ]

df_dep_fil


# df[ df['col'] ==    ]

df_dep_fil.Department.unique()

#Scenario: Filter Department except anesthesia

df_dep_fil_ex=df[ df['Department']  != 'anesthesia']

df_dep_fil_ex=df[df['Department']~='anesthesia']

df_dep_fil_ex=df[df['Department']^='anesthesia']

df_dep_fil_ex.Department.unique()

#Scenario: Filter Visitors with Patient are greater than 2

dfgr_2=df[df['Visitors with Patient']>2]

dfgr_2['Visitors with Patient'].unique()

#scenario: filter the data for patientid 31397 and Visitors with Patient 2

df_fil_and=df[  (df['patientid']==31397) &    (df['Visitors with Patient']==2)  ]

df_fil_and.shape

df_fil_and['patientid'].unique()


df_fil_and['Visitors with Patient'].unique()

#scenario: filter the data for Severity of Illness is Extreme or Type of Admission is Emergency
df_fil_or=df[(df['Severity of Illness']=='Extreme')| (df['Type of Admission']=='Emergency')]

df_fil_or['Severity of Illness'].unique()

df_fil_or['Type of Admission'].unique()
  
df[['Severity of Illness','Type of Admission']].head()

df.head()

#scenario: filter the data for Department in 'radiotherapy', 'anesthesia' & 'gynecology'

lst=['x', 'anesthesia', 'gynecology']

df_lst=df[df['Department'].isin(['x', 'anesthesia', 'gynecology'])]
df_lst=df[df['Department'].isin(['x', 'anesthesia', 'gynecology'])]
df_lst=df[df['Department'].isin(['x', 'anesthesia', 'gynecology'])]
df_lst=df[df['Department'].isin(['x', 'anesthesia', 'gynecology'])]
df_lst=df[df['Department'].isin(['x', 'anesthesia', 'gynecology'])]

df_lst.Department.unique()
df_lst=df[df['Department'].isin(lst)]

df_lst=df[df['Department'].isin(lst)]


df_lst=df[df['Department'].isin(lst)]

df_lst=df[df['Department'].isin(lst)]

# df_lst=df[df['Department'].isin(['radiotherapy', 'anesthesia', 'x'])]

# df_lst=df[df['Department'].isin(['radiotherapy', 'anesthesia', 'x'])]

# df_lst=df[df['Department'].isin(['radiotherapy', 'anesthesia', 'x'])]

df_lst=df[df['Department'].isin(['radiotherapy', 'anesthesia', 'gynecology'])]

df_lst.Department.unique()

df_lst_nt=df[~df['Department'].isin(['radiotherapy', 'anesthesia', 'gynecology'])]

df_lst_nt.Department.unique()

# unique()
df.Hospital_code
df['case_id']

df.Hospital_code.unique()
df.Department.unique()

df.columns

df_new=df[['Hospital_code', 'Hospital_type_code']]

lst=['aug', 'jul']

df_new=df[lst]

df_new

df_new[['Hospital_type_code']][1:5]

# df_new[['Hospital_type_code']][-5]

df[1:2][1:5]

df_new.head()

df[['City_Code_Hospital']]


df.head()

# concatination/appending
# axis,ignore_index
import pandas as pd
df=pd.read_csv(r"C:\Users\ppulivarthi\AV_Hackthons\Janatahack Healthcare Analytics II\train.csv")

# df.info()
df.head()

df1=df[:10]

df1.shape
df1.head()
df2=df[10:20]

df2.shape

df2.head()


import pandas as pd

concat(argu,aug1,aur3)
df_new=pd.concat([df1,df2],axis=0)
df_new.shape
df_new
df_new_reverse=pd.concat([df2,df1],axis=0)
df_new_reverse
df_new_reverse_ign=pd.concat([df2,df1],axis=0,ignore_index=True)
df_new_reverse_ign
DataFrame(dict)
dictt1={"IPL Team" : ['RCB','RCB','RCB'],"Match" :['Match-1','Match-2','Match-3'],"Score":[163,109,201]}

dictt2={"IPL Team" : ['RCB',' ',' '],"Match" :['Match-1','Match-2','Match-3'],"Score":[163,109,201]}

df_dict=pd.DataFrame(dictt1)
df_dict_new=pd.DataFrame(dictt2)
df_dict_new
df_dict
#Append dataframes one by one
df_dict_app=pd.concat([df_dict,df_dict_new],axis=0)
df_dict_app
df_dict_app['IPL Team'][1]

#using index options
df_dict_app=pd.concat([df_dict,df_dict_new],axis=0,ignore_index=True)

df_dict_app

df_dict_app['IPL Team'][4]

#append dataframes side by side
df_dict_app_ax=pd.concat([df_dict,df_dict_new],axis=1,ignore_index=True)

df_dict_app_ax.shape


df_dict_app_ax

dict1={"IPL Team" : ['RCB','RCB'], "Match" : ['Match-1','Match-2'], 'SCORE' :[120,168]}


dict2={"IPL Team" : ['RCB','RCB'], "Match" : ['Match-1','Match-2'], 'MANOFMATCH' :["KOHLI","AB DE"]}



df_ipl1=pd.DataFrame(dict1)


df_ipl2=pd.DataFrame(dict2)


df_ipl1


df_ipl2


df_ipl3=pd.concat([df_ipl1,df_ipl2],axis=1,)


df_ipl3


df_ipl3=pd.concat([df_ipl1,df_ipl2],axis=0)
append


df_ipl3



#join/merge
# df1.merge(right,how=,on=)


df.head()

df.columns

df_cl_f1=df[['case_id', 'Hospital_code', 'Hospital_type_code', 'City_Code_Hospital']]

df_cl_f2=df[['case_id','Ward_Type', 'Ward_Facility_Code', 'Bed Grade']]

df_cl_f1.shape

df_cl_f1
df_cl_f2.shape
df_cl_f2

#syntax
df_merge1=df_cl_f1.merge(df,how='inner/left/right/outer',on=['case_id',])


#grouping/Summarizing
df_cl_f2=df[['case_id','Ward_Type', 'Ward_Facility_Code', 'Bed Grade']]
df_cl_f3=df[['case_id','Ward_Type', 'Ward_Facility_Code', 'Bed Grade']]

#creating dataframe with 1000 rows 
df_cl_f3=df_cl_f3[:1000]
df_cl_f2

df_cl_f3.shape
df_cl_f3.head()
df_cl_f2.head()
df_cl_f2.shape
df_cl_f2.columns
df_cl_f3.columns
#inner join-matching rows from two dataframes
df_inner_merge=df_cl_f2.merge(df_cl_f3,how='inner',on='case_id')

df_inner_merge.shape

df_inner_merge.columns

test=df_inner_merge[['case_id', 'Ward_Type_x', 'Ward_Facility_Code_x', 'Bed Grade_x']]
test

df_inner_merge
#left join - full data from  left side dataframe and matching rows from right dataframe
df_left_merge=df_cl_f2.merge(df_cl_f3,how='left',on='case_id')

df_left_merge.shape

df_left_merge.tail()
df_left_merge.head()
#right join- full data from righ side dataframe and matching rows from left dataframe 
df_right_merge=df_cl_f2.merge(df_cl_f3,how='right',on='case_id')

df_right_merge.shape

df_right_merge.tail()

#Full join- full data from two dataframes
df_right_merge=df_cl_f2.merge(df_cl_f3,how='outer',on='case_id')
df_right_merge.shape
df_right_merge.tail()


