from os import name


evens = [n for n in range(100) if n % 2 == 0]
print(evens)

names = ['alice', 'bob', 'charlie']
capitalized_names = [item.upper() for item in names]
print(capitalized_names)

students = ["Alice", "Andrew", "Bob", "Beatrice", "Charlie"]
initials = {name[-1] for name in students}
print(initials)

