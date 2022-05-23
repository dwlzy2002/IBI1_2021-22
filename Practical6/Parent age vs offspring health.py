#Creat a dictionary called "age".Keys are ages.Values are relative risks.
age = {'30':1.03, '35':1.07, '40':1.11, '45':1.17, '50':1.23, '55':1.32, '60':1.42, '65':1.55, '70':1.72, '75':1.94}
#Use "print()"to print the dictionary.
print(age)
#import malplotlib to draw a scatter plot.
import matplotlib.pyplot as plt
#Set ages at x-axis, risks at y-axis. 
x = age.keys()
y = age.values()
#Use the plt.scatter funtion to draw the plot.
plt.scatter(x,y,marker = "o")
plt.xlabel(" father's age")
plt.ylabel("the risk of CHD")
plt.title("The relationship between father's age and the risk of CHD in the offspring ")
#Show the plot.
plt.show()
#Let the user to input the father's age and then print the risk in this age.
print("The relative risk for CHD is",age[str(input("father's age:"))])
