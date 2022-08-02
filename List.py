#create a list of groceries
grocery = ["perfume", "chocolate", "deodorant", "jam", "chinchin", "butter", "soap", "milk"]

#show that indexing of list begins at 0
list_index = grocery[4]

len_list = len(grocery)

grocery[1] = "bread"

print(grocery)

print(len_list)

print(list_index)

grocery = ["perfume", "chocolate", "deodorant", "jam", "jam", "chinchin", "butter", "soap", "milk"]
food_stuff = ["yam", "beans", "rice", "fufu"]

type(grocery)
print(type(grocery))

#show append method
grocery .append("toothpaste")
print(grocery)

food_stuff .extend(grocery)

print(food_stuff)

grocery .insert (0, "tissue")

print(grocery)

#practice remove
grocery .remove("jam")

print(grocery)

#practice pop
grocery .pop(4)
print(grocery)

# practice clear
grocery .clear()
print(grocery)

#practice index
index = grocery .index("jam")

print(index)

#practice sort
grocery .sort()

print(grocery)

#practice reverse
grocery .reverse()

print(grocery)
