# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Define the vowels upper and lower case
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
vowel_count = 0

# Loop through each character in the input string
for char in user_input:
    # Check if the character is a vowel
    if char in vowels:
        vowel_count += 1  # Increment the counter if it is a vowel

# Print the result
print("The number of vowels in the string is:", vowel_count)
