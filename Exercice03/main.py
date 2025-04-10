words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = ["a", "e", "i", "o", "u", "y"]

words_vowels = [(word, sum(1 for char in word if char in vowels)) for word in words]
print(words_vowels)
