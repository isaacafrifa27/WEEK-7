names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)



sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}
print(unique_letters)


sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence if x != " "}
print(unique_letters)



names = {'Abdullah', 'Bradley', 'Bobby', 'David'}
name = input("Enter your name: ")
if name not in names:
    print("You are not listed in the set of known names")
else:
    print("You are listed in the set of known names")



help(set)
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}



staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

staff = staff.union({"Mark", "Ringo"})
print("Union:", staff)

staff_directors = staff.intersection(directors)
print("Intersection:", staff_directors)

external = directors.difference(staff)
print("Difference:", external)

staff_or_external = directors.symmetric_difference(staff)
print("Symmetric Difference:", staff_or_external)



vowels = set({"a", "e", "i"})
missing_vowels = {"o", "u"}
vowels.update(missing_vowels)
print("Updated Set:", vowels)



staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members")

if staff.issuperset(managers):
    print("All managers are staff members")



help(frozenset)



import math
roots = {n: math.sqrt(n) for n in range(1, 26)}
print(roots)



stock = {"pear": 50, "apple": 5}
stock["kiwi"] = 10
print(stock)



help(dict)
stock = {"pear": 50, "apple": 5, "kiwi": 10, "orange": 15}
removed_item = stock.popitem()
print(f"Removed: {removed_item}")
print("Updated Stock:", stock)



import math
roots = {n: math.sqrt(n) for n in range(1, 26)}
for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")
