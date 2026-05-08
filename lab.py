# import re

# # Function to validate phone number
# def validate_phone_number(phone_number):
#     # Phone number pattern: 10 digits, optional hyphens or spaces
#     pattern = r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$'
    
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False

# # Function to validate email address
# def validate_email(email):
#     # Email address pattern
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
#     if re.match(pattern, email):
#         return True
#     else:
#         return False

# # Read phone number and email address from user
# phone_number = input("Enter phone number: ")
# email = input("Enter email address: ")

# # Validate phone number
# if validate_phone_number(phone_number):
#     print("Phone number is valid.")
# else:
#     print("Phone number is invalid.")

# # Validate email address
# if validate_email(email):
#     print("Email address is valid.")
# else:
#     print("Email address is invalid.")

# ----------------------------------------------------------

# # Function to merge two files into a third file
# def merge_files(file1, file2, merged_file):
#     try:
#         # Open first file in read mode
#         with open(file1, 'r') as f1:
#             # Read contents of first file
#             file1_contents = f1.read()

#         # Open second file in read mode
#         with open(file2, 'r') as f2:
#             # Read contents of second file
#             file2_contents = f2.read()

#         # Open third file in write mode
#         with open(merged_file, 'w') as mf:
#             # Write merged contents to third file
#             mf.write(file1_contents)
#             mf.write(file2_contents)

#         print(f"Contents of '{file1}' and '{file2}' merged successfully into '{merged_file}'.")

#     except Exception as e:
#         print("An error occurred:", e)


# # File paths for the files to be merged and the merged file
# file1 = "file1.txt"
# file2 = "file2.txt"
# merged_file = "merged_file.txt"

# # Call the merge_files function
# merge_files(file1, file2, merged_file)


#--------------------------------------------------------

# # Function to check for given words in a file and display if found
# def check_for_words(file_path, words):
#     try:
#         # Open file in read mode
#         with open(file_path, 'r') as file:
#             # Read contents of file
#             file_contents = file.read()

#         # Loop through each word in the given list
#         for word in words:
#             # Check if word is present in file contents
#             if word in file_contents:
#                 print(f"Word '{word}' found in '{file_path}'")
#             else:
#                 print(f"Word '{word}' not found in '{file_path}'")

#     except Exception as e:
#         print("An error occurred:", e)


# # File path for the file to be checked
# file_path = "file.txt"

# # List of words to be checked in the file
# words_to_check = ["apple", "banana", "cherry"]

# # Call the check_for_words function
# check_for_words(file_path, words_to_check)

#--------------------------------------------------------

# # Function to find the word with most occurrences in a text file
# def find_most_frequent_word(file_path):
#     try:
#         # Open file in read mode
#         with open(file_path, 'r') as file:
#             # Read contents of file
#             file_contents = file.read()

#         # Split the file contents into words
#         words = file_contents.split()

#         # Create a dictionary to store word frequencies
#         word_freq = {}

#         # Loop through each word and count its occurrences
#         for word in words:
#             if word in word_freq:
#                 word_freq[word] += 1
#             else:
#                 word_freq[word] = 1

#         # Find the word with the most occurrences
#         most_frequent_word = max(word_freq, key=word_freq.get)

#         # Return the most frequent word and its frequency
#         return most_frequent_word, word_freq[most_frequent_word]

#     except Exception as e:
#         print("An error occurred:", e)


# # File path for the text file to be read
# file_path = "file.txt"

# # Call the find_most_frequent_word function
# most_frequent_word, frequency = find_most_frequent_word(file_path)

# # Print the most frequent word and its frequency
# print(f"The most frequent word is '{most_frequent_word}' with a frequency of {frequency} times.")

#------------------------------------------------------------

# # Function to count vowels, blank spaces, lower case letters, and uppercase letters in a text file
# def count_chars(file_path):
#     try:
#         # Open file in read mode
#         with open(file_path, 'r') as file:
#             # Read contents of file
#             file_contents = file.read()

#         # Initialize counters
#         num_vowels = 0
#         num_blank_spaces = 0
#         num_lower_case = 0
#         num_upper_case = 0

#         # Loop through each character in the file contents
#         for char in file_contents:

#             if char.isalpha():

#                 # Check for vowels
#                 if char.lower() in ['a', 'e', 'i', 'o', 'u']:
#                     num_vowels += 1

#                 # Check for lowercase letters
#                 if char.islower():
#                     num_lower_case += 1

#                 # Check for uppercase letters
#                 if char.isupper():
#                     num_upper_case += 1

#             elif char.isspace():
#                 # Count blank spaces
#                 num_blank_spaces += 1

#         # Return the counts
#         return num_vowels, num_blank_spaces, num_lower_case, num_upper_case

#     except Exception as e:
#         print("An error occurred:", e)


# # File path for the text file to be read
# file_path = "file.txt"

# # Call the count_chars function
# num_vowels, num_blank_spaces, num_lower_case, num_upper_case = count_chars(file_path)

# # Print the counts
# print(f"Number of vowels: {num_vowels}")
# print(f"Number of blank spaces: {num_blank_spaces}")
# print(f"Number of lower case letters: {num_lower_case}")
# print(f"Number of upper case letters: {num_upper_case}")

#---------------------------------------------------

import tkinter as tk


def submit():
    # Get input from text fields and perform submit operation
    name = name_entry.get()
    age = age_entry.get()

    print(f"Name: {name}, Age: {age}")


def reset():
    # Clear input fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


# Create main window
window = tk.Tk()
window.title("Window Wizard")

# Create text labels
name_label = tk.Label(window, text="Name:")
age_label = tk.Label(window, text="Age:")

# Create text fields
name_entry = tk.Entry(window)
age_entry = tk.Entry(window)

# Create buttons
submit_button = tk.Button(window, text="Submit", command=submit)
reset_button = tk.Button(window, text="Reset", command=reset)

# Place text labels, text fields, and buttons in the window
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button.grid(row=2, column=0, padx=10, pady=10)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# Start main event loop
window.mainloop()