text = input("Enter your text:")

def character_frequency(text):
    result = {}
    for char in text:
        result[char] = result.get(char,0)+1
    return result

print(character_frequency(text))
