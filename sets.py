### sets are non primitive datatypes

myset = {"Ahmed",4, True, "Ahmed", 'python'}
### sets doesn't allow duplication
### accept different values from different datatypes
### no indecies
print(myset)
### unsorted datatype
#### add element
myset.add('Ali')
print(myset)

### pop element ?
# popped_element = myset.pop()
# print(popped_element)
# print(myset)

### remove element
myset.remove('Ahmed')
print(myset)

print("Ahmed" in myset)

print(len(myset))

# for item in myset:
#     print(f"item = {item}")


for index, item in enumerate(myset):
    print(f" {index}: item = {item}")


#################################
# myset= {4,56,'iti', ('python', 'django')}  # hashing
# print(myset)
# myset= {4,56,'iti', ['python', 'django']}  # unhashable datatype
# print(myset)
############################## update
set1 = {"Ahmed", "Ali", "Noha", "Hager"}
set2 = {"Noha", 'David', 'Osama','Youssef','Karim', 'Mohamed'}
set1.update(set2)
print(set1)