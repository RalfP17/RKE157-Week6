import random

#len()
""" print(f"We have {len(shopping_list)} items on the list.") """

#append()
""" shopping_list.append(["baking powder", "flour", "sugar"]) """

#extend()
""" shopping_list.extend(["baking powder", "flour", "sugar"]) """

#remove()
""" shopping_list.remove("cheese") """

""" for item in shopping_list.copy():
    if item == "cheese":
        shopping_list.remove(item) """

#count()
""" n = shopping_list.count("cheese")

print(f"There are {n} cheese items on the list.") """

#index()
""" apple_index = shopping_list.index("apples")
shopping_list[apple_index] = "bananas" """

""" found = "milk" in shopping_list """

""" for item in shopping_list:
    if item == "milk":
        found = True
        break """

""" if found:
    print("Milk is already on the list.")
else:
    print("There is no milk on the list") """

#sort()

""" print(shopping_list)

shopping_list.sort(reverse=True)

print(shopping_list) """

#reverse()


""" print(shopping_list)

shopping_list.reverse()

print(shopping_list)
 """

#random
shopping_list = ["cheese", "apples", "bread", "milk", "cheese", "eggs", "cheese"]

random_item = random.choice(shopping_list)

print(random_item)

""" for item in shopping_list:
    print(item) """