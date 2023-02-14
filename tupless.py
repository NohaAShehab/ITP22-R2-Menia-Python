#### tuples immutable datatype

## to define tuple

t = ()
myt = tuple()

### tuple ---> can hold different values from different datatypes

t = ('iti', 2023, True, 'Test', 44.5, 'python', 'python')
print(t)


### tuple ---> you can access its elements using index --> index start from 0
print(t[0])
print(t[3])

#### get len of the tuple ?
print(len(t))

######## check if values exists in tuple
print('pythonn' in t)

############ count element in the tuple
print(t.count('python'))

# get element index in the tuple
print(t.index('python')) # return with the index of the first element


### tuple ---> iterable datatype ---> loop over the list ?
for item in t:
    print(f"item = {item}")

## get index of each item ?
for index in range(len(t)):
    print(f"{index}, {t[index]}")

#### enumarate ?
tuple_indecies= enumerate(t)
print(tuple_indecies)  # enumerate object   # iterable

for index, item in tuple_indecies:
    print(f"{index}:{item}")

##################### tuple concatentation
t1 = (3,4,5,6,'iti')
t2 = ('Ahmed', 'Yossef', 'David', 'Hager', 2023,[4,56], 'iti' )
t3 = t1 + t2
print(t3)

####### empty tuple ---> ? Falsy values

######### min , max
students = ('David', 'Osama', 'Youssef','Michel', 'Dina', 'Saleh', 'Karim', 'AbdAllah')

print(min(students))
print(max(students))


####################3 convert string to tuple ?
name = 'noha'
l = tuple(name)
print(l)


#### tuple of one element
myt = tuple(['noha'])

mytt= ('noha')

##### cast list to tuple and vise verca

l = [5,4,'re', True]
print(l, type(l))
l = tuple(l)
print(l, type(l))

###############33 convert tuple to list ?
tt = (4,5,6, 'iti')
tt = list(tt)
print(tt, type(tt))






