# Vergel, Chean Bernard Villanueva
# Assignment No. 4
# Question No. 1

# Create Header
import pyfiglet

print("")
print("=" * 80)
print("")
welcome = pyfiglet.figlet_format("Welcome to my space".center(57, " "), font="digital")
print(welcome)
print("")
print("=" * 80)
print("\033[33mHi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.\033[0m")
print("")
# Open the numbers.txt and read the file
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
# Create two empty text files; even.txt and odd.txt
even_file = open("even_file.txt", "w")
odd_file = open("odd_file.txt", "w")
# FOR each number in numbers.txt
# Close both text files
# Print "Completed!"
# Create Footer
