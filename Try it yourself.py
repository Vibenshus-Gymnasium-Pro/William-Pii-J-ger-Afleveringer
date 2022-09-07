#Tasks
#- 7-4, 7-8 


cube = [value**3 for value in range(1, 11)]
cubelen = int(len(cube)/2)

print("Cube: " +str(cube))
print("The first three items in the list are: " + str(cube[0:3]))
print("Three items from the middle of the list are: " + str(cube[cubelen-2:cubelen+1]))
print("The last three items in the list are: " + str(cube[-3:]))


# Task 5-10
print("\n\nTask 5-10")
current_users = ["Kyle", "Stan", "Kenny", "Cartman", "AnoN"]
new_users = ["Bob", "kYle", "AnOn", "Chell", "Sara"]

casesensitive = {i.lower() for i in new_users}
for item in current_users:
    if item.lower() in casesensitive:
        print("The username "+ str(item) + " has already been used")
    else:
        print("The username " + item + " is avalible")


# Rask 5-11
print("\n\nTask 5-11")

numberlist = [value for value in range (1,10)]
for x in numberlist:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")


#Task 6-5
print("\n\nTask 6-5")

rivers = {'Amur River': 'Russia', 'Nile': 'Egypt', 'Mississippi': 'US', 'Green River': 'US'}
for name in rivers:
    print("The " + str(name) + " is located in " + str(rivers[name].title()))

print("\nRivers in dictonary:")
for name in rivers: {print(name)}
print("\nName of each country in dictonary:")
for name in set(rivers.values()): {print(name.title())}


#7-4
print("\n\nTask 7-4")

prompt = "\nPlease enter a pizza topping:"
prompt += "\n(Enter 'quit' when you are finished.) "
pizzatopping_list = []
while True:
    pizzatopping = input(prompt)
    if pizzatopping.lower() == 'quit':
        print("Your pizza toppings: " + str(pizzatopping_list))
        break
    print("I will add " + pizzatopping + " to the list")
    pizzatopping_list.append(pizzatopping)
    print(pizzatopping_list)


#7-8
print("\n\nTask 7-8")
sandwich_orders = ["tuna sandwich", "beef sandwich", "chicken sandwich", "big sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print("I finished your " + str(current_sandwich))
print("Finished sandwiches: " + str(finished_sandwiches))
