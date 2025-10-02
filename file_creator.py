name = input("What's your name? \n")
color = input("What's your favorite color? \n")
season = input("What's your season? \n")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file")
    file.write(f"{color} created this file")
    file.write(f"{season} created this file")