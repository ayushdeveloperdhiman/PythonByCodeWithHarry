# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities1.union(cities2)
# print(cities3)

# cities3 = cities1.intersection(cities2)
# print(cities3)

# cities1.intersection_update(cities2)
# print(cities1)

# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

# cities1.symmetric_difference_update(cities2)
# print(cities1)

# cities3 = cities1.difference(cities2)
# print(cities3)

# cities1.difference_update(cities2)
# print(cities1)

# print(cities1.isdisjoint(cities2))

# print(cities1.issuperset(cities2))
cities3 = {"Tokyo", "Berlin", "Delhi"}
# print(cities1.issuperset(cities3))

print(cities3.issubset(cities1))

cities1.add("Helsinki")
print(cities1)

cities1.remove("Helsinki")
print(cities1)

cities1.discard('Delhi')
print(cities1)

item_popped = cities1.pop()
print(item_popped)

# del cities1
# print(cities1)

cities2.clear()
print(cities2)

info = {'Carla', 19, False, 5.9, 19}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is not present")