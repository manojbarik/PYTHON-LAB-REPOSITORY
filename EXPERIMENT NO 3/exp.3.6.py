char = input("Enter a character: ").lower()
vowels = ("a", "e", "i", "o", "u")

if char in vowels:
    print("Character is a vowel:", char)
else:
    print("Character is a consonant:", char)