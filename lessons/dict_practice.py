"""Practice with Dictionaries."""

# can use single quotes in dictionaries 
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

# adding elements
    # we use subscription notation 
# <dict name[<key>] = <value>
# ice_cream["chocolate"] = 12
# ice_cream["mint"] = 3 

ice_cream["mint"] = 3
print("After adding mint: ")
print(ice_cream)

# removing elements 
    # similar to lists, we use pop()
# <dict name.pop(<key>)
# ice_cream.pop("mint")

ice_cream.pop("mint")
print("After removing mint: ")
print(ice_cream)

# access and modify 
# <dict name>["key"]
# ice_cream["vanilla"]
# print(ice_cream["vanilla"])

# f-string - use single quotes with keys 
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# to access a value, use subscription notation: 
    # <dict name>[<key>]
    # ice_cream["vanilla"]
# to modify, also use subscription notation: 
    # <dict name>[<key>] = new_value
    # ice_cream["vanilla"] = 9 or ice_cream["vanilla"] += 1 

ice_cream["vanilla"] += 1 
print("After adding 1 vanilla")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# length of dictionary 
    # len(<dict name>)
    # len(ice_cream)

# check if a key is in dictionary 
    # <key> in <dict name> 
    # "mint" in ice_cream 
    # chocolate in ice_cream

print("mint" in ice_cream)
print("chocolate" in ice_cream)

# cannot have multiple of the same key: causes memory issues
# but you can have duplicates of the same value: ie 5 vanilla, and 5 mint 
