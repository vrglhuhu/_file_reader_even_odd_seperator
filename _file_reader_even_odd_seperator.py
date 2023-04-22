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

# Ask for the name of the user
name_user = input("\033[40mHow about you what is your name? \033[0m")
print("")
print("\033[40m\033[33mI welcome you on this program. \033[0m")
print("\033[0m")
# Open the numbers.txt and read the file
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
# Create two empty text files; even.txt and odd.txt
with open("even_file.txt", "w") as even_file, open("odd_file.txt", "w") as odd_file: 
# FOR each number in numbers.txt
 for number in numbers:
    number = int(number.strip())
   # IF the number is even, WRITE the number to even.txt
    if number % 2 == 0:
        even_file.write(str(number) + "\n")
   # ELSE, WRITE the number to odd.txt
    else:
        odd_file.write(str(number) + "\n")
# State that the output is in the txt files
print("\033[32mPlease have time to visit the even_file.txt, if you want to look on the even numbers.\033[0m")
print("")
print("\033[32mPlease have time to visit the odd_file.txt, if you want to look on the odd numbers.\033[0m")
print("")
# Print "Completed!"
print("\033[35mCompleted!\033[0m")
# Create Footer
print("")
print("\033[40m\033[33mThank you for your time! \033[0m")
print("")
goodbye = pyfiglet.figlet_format("Visit me again", font = "digital" )
print (goodbye)
print("")

