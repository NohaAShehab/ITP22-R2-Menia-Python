
r = range(1, 10)  # range object ?
# for i in r:
#     print(i)

# r = list(r)
# print(r)

# for i in r:
#     print(f"i ={i}")
#
# print("=== loop reached its end === ")
# for i in r:
#     if i==4:
#         break
#     print(f"i ={i}")
#
# print("=== loop reached its end === ")

# for i in r:
#     if i==4:
#         continue
#     print(f"i ={i}")
#
# print("=== loop reached its end === ")


###########################

for i in r:
    if i==4:
        break
    print(f"i ={i}")
else:
    print("---- this block will be executed only if the loop reached its end ---")
    print("=== loop reached its end === ")
    print(i, r)

print(i)

### if (i < 4) {}

# if i==4:
#     pass
#
#
# print("-------------------")

