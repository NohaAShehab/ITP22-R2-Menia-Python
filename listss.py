## list is the most popular datatype in python

# hold different elements from different datatypes

# 1- to define a list
l  = []
myl = list([])

### list ---> can hold different values from different datatypes

l = ['iti', 2023, True, 'Test', 44.5, 'python', 'python']
print(l)

### list ---> you can access its elements using index --> index start from 0
# print(l[0])
# print(l[3])

### list ---> is mutable ?
l[3] = 'python'
print(l)

# l[7]= 'element'

#### get len of the list ?
print(len(l))

##### append element to the list  => at the end of the list
l.append("added element ? ")
print(l)

### insert element at certain position
l.insert(4, 'inserted')
l.insert(100, 'new inserted')
print(l)
# print(type(l))
# print(type(10))

###### pop element form the list ? --
# popped_element= l.pop() # pop -- the last element from the list
# print(popped_element)
# print(l)

######
popped_element= l.pop(4) # pop -- the last element from the list
print(popped_element)
print(l)

##### remove element ?
# l.remove('python')  # remove first occurence of the elements.
# print(l)

######## check if values exists in list
print('pythonn' in l)


############ count element in the list
print(l.count('python'))

# get element index in the list
print(l.index('python')) # return with the index of the first element

############################################################################
### list ---> iterable datatype ---> loop over the list ?
# for item in l:
#     print(f"item = {item}")

## get index of each item ?
for index in range(len(l)):
    print(f"{index}, {l[index]}")


#### enumarate ?
# list_indecies= enumerate(l)
# print(list_indecies)  # enumerate object   # iterable
#
# for index, item in list_indecies:
#     print(f"{index}:{item}")

##################### list concatentation
l1 = [3,4,5,6,'iti']
l2 = ['Ahmed', 'Yossef', 'David', 'Hager', 2023,[4,56], 'iti' ]
l3 = l1 + l2
print(l3)

####### extend a list
l1.extend(l2)
print(l1)

# ###### sorting list ----> list items should be from the same type ---
students = ['David', 'Osama', 'Youssef','Michel', 'Dina', 'Saleh', 'Karim', 'AbdAllah']
# # students.sort() # sort the same object =list=  ascending
# # print(students)
# students.sort(reverse=True) # sort the same object =list=  ascending
# print(students)


######################## reverse the list
myl= [4,5,True, 'iti', ['56', '55'], 'Python']
myl.reverse()
print(myl)

####### empty list ---> ? Falsy values

######### min , max
# print(min(students))
# print(max(students))

####################3 convert string to list ?
name = 'noha'
l = list(name)
print(l)

## convert list to string ?

myl = ['abc', 'test', 'mm', 'll']
newstring ='||'.join(myl)
print(newstring)




