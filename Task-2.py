#1. write a python program to calcuate the total number of vowels and count of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited"
# Input string
input_string = "Guvi Geeks Network Private Limited"

# Convert the string to lowercase to handle case insensitivity
input_string = input_string.lower()

# Initialize a dictionary to count each vowel
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Initialize a variable to count total vowels
total_vowels = 0

# Loop through each character in the string
for char in input_string:
    if char in vowel_count:
        vowel_count[char] += 1
        total_vowels += 1

# Display the total number of vowels
print(f"Total number of vowels: {total_vowels}")

# Display the count of each individual vowel
for vowel, count in vowel_count.items():
    print(f"Count of '{vowel.upper()}': {count}")

#2.crete a pyramid of numers frm 1to 20 using for loop
def number_pyramid(n):
    """
    Prints a number pyramid from 1 to n using nested for loops.
    """
    for i in range(1, n + 1):
        # Print spaces to align the pyramid
        for j in range(n - i):
            print(" ", end="")
        # Print numbers in the current row
        for k in range(1, i + 1):
            print(k, end=" ")
        print()  # Newline after each row

# Example usage
number_pyramid(20) 

#3.write a program that takes a string and returns a new string with all the vowels removed
def remove_vowels(input_string):
    # Define the vowels
    vowels = "aeiouAEIOU"
    
    # Use list comprehension to filter out vowels and join the result into a new string
    result = ''.join([char for char in input_string if char not in vowels])
    
    return result

# Input string "sujatha"
input_string = "sujatha"
output_string = remove_vowels(input_string)
print("String with vowels removed:", output_string)

#4. writea program that takes a string and returns the number of unique characters in it
def count_unique_characters(input_string):
    # Convert the string to a set to remove duplicates
    unique_chars = set(input_string)
    
    # Return the number of unique characters
    return len(unique_chars)

# String "sujatha"
input_string = "sujatha"
unique_count = count_unique_characters(input_string)
print("Number of unique characters:", unique_count)

#5.write a program that takes a string and returns true ifit is a palindrome, false otherwise.
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return input_string == input_string[::-1]

# Example usage with the string "automation testing"
input_string = "automation testing"
if is_palindrome(input_string):
    print("True: The string is a palindrome.")
else:
    print("False: The string is not a palindrome.")

    #6. write a program that takes astring and returns the most frequent character in it
    from collections import Counter

def most_frequent_character(input_string):
    # Remove spaces (if you want to consider only characters)
    input_string = input_string.replace(" ", "")
    
    # Use Counter to count frequency of each character
    freq = Counter(input_string)
    
    # Find the character with the maximum frequency
    most_frequent_char, frequency = freq.most_common(1)[0]
    
    return most_frequent_char, frequency

# Example usage with the string "software developer"
input_string = "software developer"
char, freq = most_frequent_character(input_string)
print(f"The most frequent character is '{char}' with {freq} occurrences.")

#7. def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase to ensure case-insensitive comparison
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
    
    # Sort both strings and compare
return sorted(str1) == sorted(str2)

# Example usage
str1 = "automation"
str2 = input("Enter another string to check if it's an anagram of 'automation': ")

if are_anagrams(str1, str2):
    print("True: The strings are anagrams.")
else:
    print("False: The strings are not anagrams.")

#write a program tha takes a string and returns the numbers of words in it
def count_words(input_string):
    # Split the string by spaces
    words = input_string.split()
    
    # Return the number of words
    return len(words)

# Example usage with the string "automation"
input_string = "automation"
word_count = count_words(input_string)
print("Number of words:", word_count)



