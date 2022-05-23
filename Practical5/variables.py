a = 19245301
b = 4218520
c = 271
d = b-c
e = a-b
print("d =",d,"e =",e)
if d<e:
  print('The rate of 2021 is greater.')
elif d>e:
  print('The rate of 2020 is greater.')
else:
  print('The rate of 2020 and 2021 are equal.')
# d<e , the rate of 2021 is greater.

X = True
Y = False
W = X and Y
print(W)
X = False
Y = False
W = X and Y
print(W)
X = True
Y = True
W = X and Y
print(W)
X = False
Y = True
W = X and Y
print(W)
