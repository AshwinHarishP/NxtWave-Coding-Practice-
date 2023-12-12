fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}
existing_key = input()
new_key = input()

fruits = list(fruits.items())
fruits_copy = fruits.copy()

for elements in range(len(fruits)):
    if fruits_copy[elements][0] == existing_key:
        new_tuple = (new_key,fruits_copy[elements][1])
        fruits_copy[elements] = new_tuple
print(fruits_copy)
