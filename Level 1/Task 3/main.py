"""
Created by: Shingai Dzinotyiweyi

Task 3: Word Counter
Create a Python program that reads a text file and counts the number of words in it.

Objectives:
✅ - Read the content of a file.
✅ - Split the content into words and count them.
✅ - Handle exceptions, such as file not found.
"""

def count_words(lines):
    """
    Counts the total number of words in each line
    """
    word_count = 0

    for line in read_file:
        print(line)
        words = line.split()

        print(words)
        word_count += len(line.split())

    print("Words Found:", word_count)


try:
    with open("words.txt", "r+") as read_file:
        count_words(read_file)

# Create a new file to read if file is not found
except FileNotFoundError:
    print("File does not exist. Creating a new one...")

    with open("words.txt", "a+") as write_file:
        new_string = "File created! Now how many words are there?"
        write_file.write(new_string)
        print(new_string)