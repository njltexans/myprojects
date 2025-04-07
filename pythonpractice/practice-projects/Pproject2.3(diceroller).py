# Dice rolling practice project
# Will be utilizing ascii art for the dice
# Will be using random module to simulate dice rolls

import random

# print("\u25CF  \u250C \u2500 \u2510 \u2502 \u2514  \u2518") #python unicode for dice face
# ●  ┌ ─ ┐ │ └  ┘

dice_faces = {
    1: (
        " ┌─────────┐ ",
        " │         │ ",
        " │    ●    │ ",
        " │         │ ",
        " └─────────┘ "
    ),
    2: (
        " ┌─────────┐ ",
        " │ ●       │ ",
        " │         │ ",
        " │       ● │ ",
        " └─────────┘ "
    ),
    3: (
        " ┌─────────┐ ",
        " │ ●       │ ",
        " │    ●    │ ",
        " │       ● │ ",
        " └─────────┘ "
    ),
    4: (
        " ┌─────────┐ ",
        " │ ●     ● │ ",
        " │         │ ",
        " │ ●     ● │ ",
        " └─────────┘ "
    ),
    5: (
        " ┌─────────┐ ",
        " │ ●     ● │ ",
        " │    ●    │ ",
        " │ ●     ● │ ",
        " └─────────┘ "
    ),
    6: (
        " ┌─────────┐ ",
        " │ ●     ● │ ",
        " │ ●     ● │ ",
        " │ ●     ● │ ",
        " └─────────┘ "
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice would you like to roll? "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Prepare the dice faces to be displayed horizontally
dice_rows = [""] * 5  # Each dice face has 5 rows

for die in dice:
    face = dice_faces.get(die)
    for i, line in enumerate(face):
        dice_rows[i] += line + "  "  # Add spacing between dice

# Print the dice faces row by row
for row in dice_rows:
    print(row)

for die in dice:
    total += die
print(f"Total: {total}")