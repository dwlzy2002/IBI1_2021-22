#input the marks list.
marks=[45,36,86,57,53,92,65,45]
#Use sorted to sort the list and then give it a new name called new_m.
sorted(marks)
new_m= sorted(marks)
print(new_m)
#import module to draw boxplot.
import matplotlib.pyplot as plt
#Set scores in new_m list as x.
score = new_m
#Plot the boxplot.
plt.boxplot(score, vert=True, whis=1.5, patch_artist=True)
plt.show()
#Use for loop to sum the elements in the list.
total = 0
for scores in marks:
    total= total+ scores
#Use total/length to caculate the average.
mean = total/len(marks)
#Check whether Rob passed the exam. mean<60 failed, mean>=60 pass
if mean >= 60:
    print("Rob's final score is",mean,"Passed.")
else:
    print("Rob's final score is"+" "+str(mean)+"."+"Failed.")
# Rob failed actually.

