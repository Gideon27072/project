#dictionary with integer keys
gideons_dic = {1: 'apple', 2: 'orange'}

#dictionary with mixed keys
gideons_dic = {1: 'apple', 'orange': 1}

#list as values/values as list
gideons_dic = {1: ['apple','orange'],}

#example 1 : TYPE ERROR, INCORRECT DATATYPE IN KEY
# gideons_dic = {['apple','orange']: 1, 2: 6}
# gideons_dic['goat'] = 1

# print(gideons_dic)

#Example 2:using update() to add multiple key:value pairs to a dictionary
# menu = {"cheesecake": 1, "applepie": 2}

# menu.update({"icecream": 2, "cheese": 1, "yoghurt": 5})

# print(menu['cheesecake'])

#Accessing elements from the dictionary
#Example 3: using square brackets to retreive elements from dictionary
#Creating a dictionary called menu which contains key:value pairs of items and their prices
menu = {"cheesecake" : 2, "applepie" : 3, "icecream" : 4}

print(menu['cheesecake'])

#Example 4:using the get() to retrieve elements from a dictionary
print(menu.get("applepie"))

#Removing elements from the dictionary
#Example 5: removing a particular element and returning the value
print(menu.pop("icecream"))

#Example 6: randomly removes an item and return the key:value pair
print(menu.popitem())

#Example 7: removing all the elements from a dictionary
# menu.clear()
# print(menu)

# #Example 8: deleting the dictionary
# del menu
# print(menu) 

#Dictionary comprehension
#Example 9: combining 2 lists into a dictionary zip()
item = ["cheesecake", "applepie", "icecream"]
price = [2,3,4]
menu = {key:value for key, value in zip(item,price)}
print(menu)

#creating a dictionary with key:value pairs as num:squares
#Example 10: create a dictionary called squares lets consider numbers in range 6
# squares ={}
# for x in range (6):
#     squares[x] = x*x
# print(squares)

#using dictionary comprehension
square = {x: x*x for x in range (6)}
print(square)
