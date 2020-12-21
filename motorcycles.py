# Modofying elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'triumph'
print(motorcycles)

# Adding elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('triumph')
print(motorcycles)

# Adding elements into an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('kawasaki')
motorcycles.append('triumph')

print(motorcycles)

# Deleting items - first element
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Deleting items - any other element
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# Popping an item
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'triumph', 'suzuki']
motorcycles.remove('triumph')
print(motorcycles)

