# Get the index of a Key in a Dictionary and access the key

my_dict = {
    'id': 1,
    'name': 'Bobbyhadz',
    'age': 30,
}

index = None

if 'name' in my_dict:
    index = list(my_dict).index('name')

print(index)  # 👉️ 1

key = list(my_dict)[1]
print(key)  # 👉️ name

value = list(my_dict.values())[1]
print(value)  # 👉️ Bobbyhadz