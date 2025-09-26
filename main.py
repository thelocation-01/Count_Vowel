def count_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in word.lower():  # Convert to lowercase for case-insensitive check
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Get input from the user
user_word = input("Enter a single word: ")

# Count the vowels
num_vowels = count_vowels(user_word)

# Display the output
print(f"{user_word}")
print(f"{num_vowels} vowels found")