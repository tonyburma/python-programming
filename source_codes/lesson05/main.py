evens = [n for n in range(10) if n % 2 == 0]
print(evens)

names = ['alice', 'bob', 'charlie']
capitalized_names = [name.upper() for name in names]
print(capitalized_names)

students = ["Alice", "Andrew", "Bob", "Beatrice", "Charlie"]
initials = {x[-1] for x in students}
print(initials)

for i in range(5):
  print(i)