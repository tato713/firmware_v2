print(list(enumerate([])))
print(list(enumerate([1, 2, 3])))
print(list(enumerate([1, 2, 3], 5)))
print(list(enumerate([1, 2, 3], -5)))
print(list(enumerate(range(1000))))

# specifying args with keywords
print(list(enumerate([1, 2, 3], start=1)))
print(list(enumerate(iterable=[1, 2, 3])))
print(list(enumerate(iterable=[1, 2, 3], start=1)))
