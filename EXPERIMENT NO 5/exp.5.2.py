my_list = [10, 20, 30]
print("List elements:")
for item in my_list:
    print(item)

my_tuple = (1, 2, 3)
print("\nTuple elements:")
for item in my_tuple:
    print(item)

my_set = {4, 5, 6}
print("\nSet elements:")
for item in my_set:
    print(item)

my_dict = {"name": "Alice", "age": 22, "city": "Paris"}
print("\nDictionary elements:")

print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Key-Value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)
