square = [i**2 for i in range(1, 11)]

print(square) 

even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(even_numbers)

words =  ["hello", "WORLD", "PyThOn"]

words_lower = [word.lower() for word in words]
print(words_lower)