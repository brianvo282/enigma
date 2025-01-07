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
    "A": "Y", "B": "X", "C": "W", "D": "V", "E": "U", "F": "T", "G": "S", "H": "R",
    "I": "Q", "J": "P", "K": "O", "L": "N", "M": "M", "N": "L", "O": "K", "P": "J",
    "Q": "I", "R": "H", "S": "G", "T": "F", "U": "E", "V": "D", "W": "C", "X": "B",
    "Y": "A"
}

# Function to rotate the rotor
def rotate_rotor(rotor):
    global pos1, pos2, pos3
    if rotor == rotor1:
        pos1 += 1
        if pos1 > 26:
            pos1 = 1
            pos2 += 1
            if pos2 > 26:
                pos2 = 1
                pos3 += 1
                if pos3 > 26:
                    pos3 = 1
    elif rotor == rotor2:
        pos2 += 1
        if pos2 > 26:
            pos2 = 1
            pos3 += 1
            if pos3 > 26:
                pos3 = 1
    elif rotor == rotor3:
        pos3 += 1
        if pos3 > 26:
            pos3 = 1

    rotor1label.config(text=str(pos1))  # Update rotor1 label text
    rotor2label.config(text=str(pos2))
    rotor3label.config(text=str(pos3))

    rotor_values = list(rotor.values())
    rotated_values = rotor_values[1:] + rotor_values[:1]
    for i, key in enumerate(rotor.keys()):
        rotor[key] = rotated_values[i]

# Function to simulate Enigma machine
def enigma_letter(letter):
    step1 = rotor1.get(letter)
    step2 = rotor2.get(step1)
    step3 = rotor3.get(step2)
    reflected = reflector.get(step3)
    step4 = rev3.get(reflected)
    step5 = rev2.get(step4)
    step6 = rev1.get(step5)
    return step6

# Label to display the rotor1 position
rotor1label = tk.Label(root, text=str(pos1), bg="#c8c8ff", width=5, height=5, font=30)
rotor1label.place(relx=0.6, rely=0.5, anchor="center")

rotor2label = tk.Label(root, text=str(pos2), bg="#c8c8ff", width=5, height=5, font=30)
rotor2label.place(relx=0.55, rely=0.5, anchor="center")

rotor3label = tk.Label(root, text=str(pos3), bg="#c8c8ff", width=5, height=5, font=30)
rotor3label.place(relx=0.5, rely=0.5, anchor="center")


# Function to handle button click in Set B
def on_button_b_click(letter):
    highlighted_letter_b.set(letter)
    highlighted_letter_a.set(enigma_letter(letter))  # Show corresponding letter in Set A
    rotate_rotor(rotor1)
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