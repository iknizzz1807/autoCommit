import requests
import os
import random
import string


# Updata the file
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def write_to_file(file_path, text):
    try:
        # Open file in append mode ('a' mode), create if doesn't exist
        with open(file_path, "a") as file:
            # Write the text to the file
            file.write(text + "\n")  # Adding a newline after each write
        print(f"Successfully wrote '{text}' to '{file_path}'")
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")


# Example usage
file_path = r"D:\Coding\autoCommit\file.txt"
text_to_write = generate_random_string(40)

write_to_file(file_path, text_to_write)
