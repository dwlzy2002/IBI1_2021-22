import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/DUWL/desktop")
covid_data=pd.read_csv("full_data.csv")
#print the the first and third columns from rows 10-20. 
print(covid_data.iloc[10:21,1:4:2])
#print the “total cases” for all rows corresponding to Afghanistan(my own way)
i=0
while covid_data.loc[i,"location"]=="Afghanistan":
    i+=1
    if covid_data.loc[i+1,"location"]!="Afghanistan":
        break
print(covid_data.loc[0:i,"total_cases"])
#print the “total cases” for all rows corresponding to Afghanistan(use boolean)
covid_data1=pd.read_csv("full_data.csv")
for m in range(0,7996):
    if covid_data1.loc[m,"location"]=="Afghanistan":
        n = True
        covid_data1.loc[m,"location"] =n
    else:
        n = False
        covid_data1.loc[m,"location"] =n
    my_rows=list(covid_data1.loc[:,"location"])
print(covid_data.loc[my_rows,"total_cases"])
#china datas
covid_data2=pd.read_csv("full_data.csv")
for o in range(0,7996):
    if covid_data2.loc[o,"location"]=="China":
        p = True
        covid_data2.loc[o,"location"] =p
    else:
        p = False
        covid_data2.loc[o,"location"] =p
    my_rows1=list(covid_data2.loc[:,"location"])

china_new_data = covid_data.loc[my_rows1,["date","new_cases","new_deaths"]]
print(china_new_data)

mean=np.mean(covid_data.loc[my_rows1,["new_cases","new_deaths"]])
print(mean)
#box plot
#new_list=list(covid_data.loc[0:i,"new_cases"])
#death_list=list(covid_data.loc[0:i,"new_deaths"])
#new_list.sort()
#death_list.sort()
x = covid_data.loc[my_rows1,["new_cases","new_deaths"]]
plt.boxplot(x,vert=True,whis=1.5,labels=["new_cases","new_deaths"],showbox=True,showfliers=False)
#plot the data over time
china_dates=covid_data.loc[my_rows1,"date"]
china_new_cases=covid_data.loc[my_rows1,"new_cases"]
china_new_deaths=covid_data.loc[my_rows1,"new_deaths"]
plt.plot(china_dates, china_new_cases,'b+')
plt.plot(china_dates, china_new_deaths,'r+')
