import tkinter as tk

# Initialize Tkinter root window
root = tk.Tk()
root.title("Enigma Machine")
root.geometry("1600x900")

# Set up font and colors
font = ('Arial', 14)
button_color = '#c8c8ff'  # Light blue button color
highlight_color = '#ffff66'  # Light yellow for highlighting
hover_color = '#9999ff'  # Hover effect color

# Alphabet for button labels
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos1 = 1
pos2 = 1
pos3 = 1

# Rotor dictionaries
rotor1 = {alphabet[i]: alphabet[(i + pos1) % 26] for i in range(26)}  # Simple shift by 1
rotor2 = {alphabet[i]: alphabet[(i + pos2) % 26] for i in range(26)}  # Shift by 3
rotor3 = {alphabet[i]: alphabet[(i + pos3) % 26] for i in range(26)}  # Shift by 5
rev1 = {value: key for key, value in rotor1.items()}
rev2 = {value: key for key, value in rotor2.items()}
rev3 = {value: key for key, value in rotor3.items()}

reflector = {
    "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S",
    "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K",
    "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C",
    "Y": "B", "Z": "A"
}


# Function to rotate the rotor
def rotate_rotor(rotor, rotor_num):
    global pos1, pos2, pos3
    if rotor_num == 1:
        pos1 += 1
        if pos1 > 26:
            pos1 = 1
            pos2 += 1
            if pos2 > 26:
                pos2 = 1
                pos3 += 1
                if pos3 > 26:
                    pos3 = 1
    elif rotor_num == 2:
        pos2 += 1
        if pos2 > 26:
            pos2 = 1
            pos3 += 1
            if pos3 > 26:
                pos3 = 1
    elif rotor_num == 3:
        pos3 += 1
        if pos3 > 26:
            pos3 = 1

    update_rotors()

def rotate_rotor_reversed(rotor, rotor_num):
    global pos1, pos2, pos3
    if rotor_num == 1:
        pos1 -= 1
        if pos1 < 1:
            pos1 = 26
            pos2 -= 1
            if pos2 < 1:
                pos2 = 26
                pos3 -= 1
                if pos3 < 1:
                    pos3 = 26
    elif rotor_num == 2:
        pos2 -= 1
        if pos2 < 1:
            pos2 = 26
            pos3 -= 1
            if pos3 < 1:
                pos3 = 26
    elif rotor_num == 3:
        pos3 -= 1
        if pos3 < 1:
            pos3 = 26

    update_rotors()

def update_rotors():
    # Update the rotor mappings based on the positions
    global rotor1, rotor2, rotor3
    rotor1 = {alphabet[i]: alphabet[(i + pos1 - 1) % 26] for i in range(26)}
    rotor2 = {alphabet[i]: alphabet[(i + pos2 - 1) % 26] for i in range(26)}
    rotor3 = {alphabet[i]: alphabet[(i + pos3 - 1) % 26] for i in range(26)}

    # Update the rotor labels on the GUI
    rotor1label.config(text=str(pos1))
    rotor2label.config(text=str(pos2))
    rotor3label.config(text=str(pos3))

# Function to simulate Enigma machine
def enigma_letter(letter):
    print("start")
    step1 = rotor1.get(letter)
    print(step1)
    step2 = rotor2.get(step1)
    print(step2)
    print(rotor3)
    step3 = rotor3.get(step2)
    print(step3)
    reflected = reflector.get(step3)
    print(reflected)
    print("reflected")
    step4 = rev3.get(reflected)
    print(step4)
    step5 = rev2.get(step4)
    print(step5)
    step6 = rev1.get(step5)
    print(step6)
    return step6

# Label to display the rotor1 position
rotor1label = tk.Label(root, text=str(pos1), bg="#c8c8ff", width=5, height=5, font=30)
rotor1label.place(relx=0.5, rely=0.5, anchor="center")

rotor2label = tk.Label(root, text=str(pos2), bg="#c8c8ff", width=5, height=5, font=30)
rotor2label.place(relx=0.45, rely=0.5, anchor="center")

rotor3label = tk.Label(root, text=str(pos3), bg="#c8c8ff", width=5, height=5, font=30)
rotor3label.place(relx=0.4, rely=0.5, anchor="center")

# Buttons for rotor1 rotation (up and down)
rotor1upbutton = tk.Button(root, bg="#c8c8ff", width=2, height=2, command=lambda: rotate_rotor(rotor1, 1))
rotor1upbutton.place(relx=0.5, rely=0.4, anchor="center")

rotor1downbutton = tk.Button(root, bg="#c8c8ff", width=2, height=2, command=lambda: rotate_rotor_reversed(rotor1, 1))
rotor1downbutton.place(relx=0.5, rely=0.6, anchor="center")

# Buttons for rotor2 rotation (up and down)
rotor2upbutton = tk.Button(root, bg="#c8c8ff", width=2, height=2, command=lambda: rotate_rotor(rotor2, 2))
rotor2upbutton.place(relx=0.45, rely=0.4, anchor="center")

rotor2downbutton = tk.Button(root, bg="#c8c8ff", width=2, height=2, command=lambda: rotate_rotor_reversed(rotor2, 2))
rotor2downbutton.place(relx=0.45, rely=0.6, anchor="center")

# Buttons for rotor3 rotation (up and down)
rotor3upbutton = tk.Button(root, bg="#c8c8ff", width=2, height=2, command=lambda: rotate_rotor(rotor3, 3))
rotor3upbutton.place(relx=0.4, rely=0.4, anchor="center")

rotor3downbutton = tk.Button(root, bg="#c8c8ff", width=2, height=2, command=lambda: rotate_rotor_reversed(rotor3, 3))
rotor3downbutton.place(relx=0.4, rely=0.6, anchor="center")

# Function to handle button click in Set B
def on_button_b_click(letter):
    highlighted_letter_b.set(letter)
    highlighted_letter_a.set(enigma_letter(letter))  # Show corresponding letter in Set A
    rotate_rotor(rotor1, 1)
    light_up_set_a_button(enigma_letter(letter))  # Light up corresponding button in Set A

# Function to light up the corresponding button in Set A
def light_up_set_a_button(transformed_letter):
    for letter, button in buttons_set_a.items():
        if letter == transformed_letter:
            button.config(bg=highlight_color)  # Light up the corresponding button
        else:
            button.config(bg=button_color)  # Reset other buttons to normal color

# Create StringVars to store the highlighted letters
highlighted_letter_a = tk.StringVar()
highlighted_letter_b = tk.StringVar()

# Frame for Set A (A-Z)
frame_a = tk.Frame(root)
frame_a.grid(row=0, column=0, padx=20, pady=20)

# Generate buttons for Set A (A-Z)
buttons_set_a = {}
for i, letter in enumerate(alphabet):
    button = tk.Button(frame_a, text=letter, font=font, width=5, height=2, state="disabled",
                       bg=button_color)
    button.grid(row=i // 7, column=i % 7, padx=5, pady=5)
    buttons_set_a[letter] = button

# Frame for Set B (A-Z)
frame_b = tk.Frame(root)
frame_b.grid(row=2, column=0, padx=20, pady=20)

# Generate buttons for Set B (A-Z)
for i, letter in enumerate(alphabet):
    button = tk.Button(frame_b, text=letter, font=font, width=5, height=2,
                       bg=button_color, activebackground=hover_color,
                       command=lambda l=letter: on_button_b_click(l))
    button.grid(row=i // 7, column=i % 7, padx=5, pady=5)

# Run the Tkinter main loop
root.mainloop()