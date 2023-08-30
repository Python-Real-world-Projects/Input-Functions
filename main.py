# import random

# import pyautogui as pg

# import time

# animal=('monkey','donkey','dog')

# time.sleep(8)

# for i in range(50):
#     a=random.choice(animal)
#     pg.write("you are a "+a)
#     pg.press('enter')

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Display the result
print(f"The area of the rectangle is {area} square units.")
