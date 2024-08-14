def count_vowels_and_consonants(s):
    # Convert the string to lowercase to handle both upper and lower case letters
    s = s.lower()

    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Define a set of vowels for efficient checking
    vowels = set("aeiou")

    # Iterate through each character in the string using a for loop
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
        # Check if the character is a consonant (assuming alphabetic characters)






























































        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count

# Example usage
input_string = "bharat is my country"
vowels, consonants = count_vowels_and_consonants(input_string)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
