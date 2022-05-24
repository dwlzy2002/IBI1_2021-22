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
print(covid_data.loc[0:i-1,"total_cases"])
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
#china datas mean
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
print(mean)#cases mean = 893.923913, deaths mean = 35.967391
#box plot in China
x = covid_data.loc[my_rows1,["new_cases","new_deaths"]]
#Since the outliers are too big, which can affect the comparation between the means of these two types.So I change showfliers to False.
plt.boxplot(x,vert=True,whis=1.5,labels=["new cases","new deaths"],showbox=True, showfliers=False)
plt.ylabel("cases/deaths number")
plt.title("boxplots of new cases and new deaths in China")
plt.show()
#plot the data over time in China
china_dates=covid_data.loc[my_rows1,"date"]
china_new_cases=covid_data.loc[my_rows1,"new_cases"]
china_new_deaths=covid_data.loc[my_rows1,"new_deaths"]
plt.plot(china_dates, china_new_cases,'b+',label="new cases")
plt.plot(china_dates, china_new_deaths,'r+',label="new deaths")
plt.legend()
plt.title("China new cases and deaths")
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.ylabel("cases/deaths number")
plt.legend()
plt.show()
#qestion:how can we see and compare the total cases number in 2020.3.14?
#answer:using a scatter of total cases in 20203.14 to compare the cases number in different countries. The plot can also show the cases number of the whole world.
covid_data3=pd.read_csv("full_data.csv")
for r in range(0,7996):
    if covid_data3.loc[r,"date"]=="2020-03-14":
        s = True
        covid_data3.loc[r,"date"] =s
    else:
        s = False
        covid_data3.loc[r,"date"] =s
    my_rows2=list(covid_data3.loc[:,"date"])
total_in_0314=covid_data.loc[my_rows2,"total_cases"]
countries_name=covid_data.loc[my_rows2,"location"]
plt.figure(figsize=(40,5))
plt.scatter(countries_name,total_in_0314,marker="o")
plt.xticks(rotation=-90)
plt.title("total cases worldwide in 2020.3.14")
plt.ylabel("cases number")
plt.show()
