
#### non primitive mutable --- comma seperated key:value pair datatype

d = {}
myd =dict()

#################
myd = {
    "name":'noha',
    "track":"python",
    'name': "Noha Shehab"
}
print(myd)
### doesn't allow key duplicate  from python 3.7 ----> dictionary sorted

### get len of dictionary ?
print(len(myd))

## dictionay is mutable datatype ?
myd['track']= 'Fullstack using python'
print(myd)

myd["intake"] = 43   # if key doesn't exist ---> will add it to the dict
print(myd)
#### pop element from the dict ?
popped_element=myd.pop('intake')
print(popped_element)
print(myd)
##### update dict ?
newd = {"city":"Menia", "Location":"upper Egypt", 'name': "Yossef"}
myd.update(newd)
print(myd)

##### loop over the dict
# for item in myd:  ###### retrurn with the keys ?
#     print(f"item = {item}")

# for item in myd:  ###### retrurn with the keys ?
#     print(f"item = {item}, value = {myd[item]}")
#

#### in operator
# print('Menia' in myd)  # check if the values exists the keys

# #################3 get keys of the dict
#
# myd_keys= myd.keys()
# print(myd_keys)
#
# for k in myd_keys:
#     print(k)

## convert it to list
# myd_keys = list(myd_keys)

#################3 get values of the dict
#
# myd_values= myd.values()
# print(myd_values)

############## dict items ?

myd_items = myd.items()
print(myd_items)

# for m in myd_items:
#     print(m)

# for k , v in myd_items:
#     print(f"{k}: {v}")


# for k,v in myd:
#     print(f"{k}: {v}")



# d = {"name":"Ahmed"}
# d2 = {"city": "Cairo"}
# d3 = d + d2

##### cast dict to list ?
mydl = list(myd)  # keys only
print(mydl)

myd.clear()



