# ENGR 102 Final Review
# Kyle Blessing
# https://www.w3schools.com/python/default.asp

# Lists

#list1 = [1,2,3,4,5,-5,2.2]  #"string", True, 9.88]
#list2 = [0,1,2,3,4,5,6,7,8,9,10]

#list1.append(6)
#list1.extend([6,7,8])

#list1.remove(list1[5])
#x = list1.pop(0)

#for i in range(len(list1)):
#    print(list1[i])

#print(list1)
#print(x)

#list3 = list1 + list2

#list2 = list1[0:11:2]
#list3 = list1[:-2:2]
#print(list3)

# Dictionaries 
'''
dict1 = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964,
    "colors" : ["red", "white", "blue"]
}

dict1["model"] = "Mustang"
dict1["electric"] = True

print(dict1)
print()
print(dict1.values())
'''


# numpy
import numpy as np
'''
#x = np.array([5,10,15])
#x = np.linspace(0,1,11)

x = np.random.randint(1,7, size=5)

print(x)
'''

# matplotlib
'''
import matplotlib.pyplot as plt

x = np.linspace(0,5,6)
y = np.random.randint(0,10,size=6)

plt.plot(x, y, "b", label="Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Random Graph")
plt.legend(loc="lower right")
plt.show()
'''

from math import *
# funtions
'''
def myFuntion():
    # do stuff in here
    return 
'''

# point one is at (1,1)
# point two is at (5,6)
'''
point1 = [1,1]
point2 = [5,6]

point3 = [8,2]
point4 = [-2,5]

def distEq(p1, p2):
    xVal = abs(p2[0] - p1[0])
    yVal = abs(p2[1] - p1[1])
    distance = sqrt(xVal**2 + yVal**2)
    return distance

length1 = distEq(point3, point1)
length2 = distEq(point1, point4)

print(length1 + length2)


file = open("fileName.txt", "r")
file.close()

with open("fileName.csv", "w") as file:
    # write stuff in the file
    x = [3,2,3,5,6]
    for i in range(len(x)):
        x[i] = str(x[i])
        file.write(x[i] + "\n")
'''

# error handling
'''
try:
    #userInput = float(input("Please enter a number: "))
    x = 8 / 0
except ValueError:
    print("You did not type a number")
except TypeError:
    pass
except ZeroDivisionError:
    print("Cant divide by 0")

   
try:
    file = open("fileName.txt", "r")
finally:
    file.close()
'''



# more depth questions
'''
userInput = input("Please enter a vector separated by commas: ")
print(userInput)
vectorList = userInput.split(",")
for i in range(len(vectorList)):
    vectorList[i] = float(vectorList[i])
print(vectorList)
'''



# misc questions

'''
name = "I enjoy programing in Python"
print(name[4:9])



matrix = [[1, 2, 3, 4],
          [4, 5, 6, 7],
          [8, 9, 10, 11],
          [12, 13, 14, 15]]
#for i in range(0, 3):
    #print(matrix[i][1], end=" ")

listOfLists = [ [1,2,3], [4,5,6], [True, "hello", 7] ]
print(listOfLists[2][1])


def func(x):
    return x - 1

print(func(3) * func(5))

def f1():
    print('Hi')
def f2():
    print('Lo')

f2()
f1()
f1()

'''
fileName = "OddNumbersFile.csv"

with open(fileName, "w") as file:
    for i in range(1,101,2):
        i = str(i)
        file.write(i + "\n")


with open(fileName, "r") as file:
    sum = 0
    for row in file:
        reader = file.readline()
        print(reader)
        reader = float(reader)
        sum += reader

print(sum)