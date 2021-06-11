thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  #----------------------------short expression via list------------------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


def change(x):
	return x.upper()
    

newlist = [change(x) for x in fruits]

print(newlist)

#-------------------------------------------------------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#--------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#-------------------------short expressin via list-------------------------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 

#----------------------sort list------------------------------------------------------------------------------------------

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#--------------------copy list-1-way-----------------------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#--------------------copy list 2-way---------------------------------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#------------------join two list 1-way-------------------------------------------------------------------------------------------------------------------------

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

#------------------------join two list 2-way---------------------------------------------------------------------------------------------------

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

#----------------join two list 3 way----------------------------------------------------------------------------------------------------------------------

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 

#-------------------count list specific element-----------------------------------------------------------------------------------------------------------

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

#----------------------------return indexs of list -----------------------------------------------------------------------------------------------------

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry") 

#-----------------insert value at the specific position---------------------------------------------------------------------------------------------------
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

#--------------------remove value by index ----------------------------------------------------------------------------------------------------------------
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1) 
#--------------------remove value by value--------------------------------------------------------------------------------------------------------------------------------------
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana") 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


