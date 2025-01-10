import tkinter as tk
import random

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


colors = [
    "#FF0000",  # Red
    "#FF4000",  # Slightly lighter orange
    "#FF7F00",  # Orange
    "#FFB000",  # Yellow
    "#F4FF00",  # Bright Yellow
    "#8CFF00",  # Lime
    "#1FFF00",  # Bright Green
    "#007D12",  # Green
    "#00FFA0",  # Blue-Green
    "#00DFFF",  # Bright Blue
    "#0042FF",  # Blue
    "#8000FF",  # Violet
    "#FF00E8"   # Deep Pink
]
num_of_conections = 0
letter_to_bind1 = None
letter_to_bind2 = None

# Rotor dictionaries
rotor1 = {
 'A': 'O',
 'B': 'Q',
 'C': 'H',
 'D': 'S',
 'E': 'C',
 'F': 'P',
 'G': 'B',
 'H': 'T',
 'I': 'M',
 'J': 'A',
 'K': 'K',
 'L': 'W',
 'M': 'Z',
 'N': 'G',
 'O': 'D',
 'P': 'R',
 'Q': 'F',
 'R': 'E',
 'S': 'Y',
 'T': 'N',
 'U': 'V',
 'V': 'X',
 'W': 'L',
 'X': 'I',
 'Y': 'U',
 'Z': 'J'
}

rotor2 = {
 'A': 'F',
 'B': 'E',
 'C': 'W',
 'D': 'Z',
 'E': 'O',
 'F': 'M',
 'G': 'U',
 'H': 'V',
 'I': 'X',
 'J': 'A',
 'K': 'L',
 'L': 'K',
 'M': 'Y',
 'N': 'D',
 'O': 'B',
 'P': 'Q',
 'Q': 'T',
 'R': 'J',
 'S': 'C',
 'T': 'R',
 'U': 'P',
 'V': 'S',
 'W': 'I',
 'X': 'G',
 'Y': 'H',
 'Z': 'N'
}

rotor3 = {
 'A': 'E',
 'B': 'F',
 'C': 'G',
 'D': 'P',
 'E': 'S',
 'F': 'M',
 'G': 'C',
 'H': 'N',
 'I': 'J',
 'J': 'I',
 'K': 'A',
 'L': 'Q',
 'M': 'V',
 'N': 'W',
 'O': 'Y',
 'P': 'D',
 'Q': 'L',
 'R': 'O',
 'S': 'X',
 'T': 'U',
 'U': 'Z',
 'V': 'B',
 'W': 'T',
 'X': 'R',
 'Y': 'H',
 'Z': 'K'
}

rev1 = {value: key for key, value in rotor1.items()}
rev2 = {value: key for key, value in rotor2.items()}
rev3 = {value: key for key, value in rotor3.items()}

plugboard = {
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "N",
    "O": "O",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z"
}


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
        update_rotors(rotor, rotor_num)
        if pos1 > 26:
            pos1 = 1
            update_rotors(rotor, rotor_num)
            pos2 += 1
            update_rotors(rotor2, 2)
            if pos2 > 26:
                pos2 = 1
                update_rotors(rotor2, 2)
                pos3 += 1
                update_rotors(rotor3, 3)
                if pos3 > 26:
                    pos3 = 1
                    update_rotors(rotor3, 3)
    elif rotor_num == 2:
        pos2 += 1
        update_rotors(rotor, rotor_num)
        if pos2 > 26:
            pos2 = 1
            update_rotors(rotor2, 2)
            pos3 += 1
            update_rotors(rotor3, 3)
            if pos3 > 26:
                pos3 = 1
                update_rotors(rotor3, 3)
    elif rotor_num == 3:
        pos3 += 1
        update_rotors(rotor3, 3)
        if pos3 > 26:
            pos3 = 1
            update_rotors(rotor3, 3)


def rotate_rotor_reversed(rotor, rotor_num):
    global pos1, pos2, pos3
    if rotor_num == 1:
        pos1 -= 1
        update_rotors_reversed(rotor, rotor_num)
        if pos1 < 1:
            pos1 = 26
            update_rotors_reversed(rotor1, 1)
            pos2 -= 1
            update_rotors_reversed(rotor2, 2)
            if pos2 < 1:
                pos2 = 26
                update_rotors_reversed(rotor2, 2)
                pos3 -= 1
                update_rotors_reversed(rotor3, 3)
                if pos3 < 1:
                    pos3 = 26
                    update_rotors_reversed(rotor3, 3)
    elif rotor_num == 2:
        pos2 -= 1
        update_rotors_reversed(rotor, rotor_num)
        if pos2 < 1:
            pos2 = 26
            update_rotors_reversed(rotor2, 2)
            pos3 -= 1
            update_rotors_reversed(rotor3, 3)
            if pos3 < 1:
                pos3 = 26
                update_rotors_reversed(rotor3, 3)
    elif rotor_num == 3:
        pos3 -= 1
        update_rotors_reversed(rotor3, 3)
        if pos3 < 1:
            pos3 = 26
            update_rotors_reversed(rotor3, 3)

def update_rotors(rotor, rotor_num):
    # Update the rotor mappings based on the positions
    global rotor1, rotor2, rotor3
    keys = list(rotor.keys())
    values = list(rotor.values())

    temp = values[1:] + [values[0]]

    for keys, new_value in zip(keys, temp):
        rotor[keys] = new_value

    rev1 = {value: key for key, value in rotor1.items()}
    rev2 = {value: key for key, value in rotor2.items()}
    rev3 = {value: key for key, value in rotor3.items()}    


    # Update the rotor labels on the GUI
    rotor1label.config(text=str(pos1))
    rotor2label.config(text=str(pos2))
    rotor3label.config(text=str(pos3))

def update_rotors_reversed(rotor, rotor_num):
    # Update the rotor mappings based on the positions
    global rotor1, rotor2, rotor3
    keys = list(rotor.keys())
    values = list(rotor.values())

    temp = [values[-1]] + values[:-1]

    for keys, new_value in zip(keys, temp):
        rotor[keys] = new_value

    rev1 = {value: key for key, value in rotor1.items()}
    rev2 = {value: key for key, value in rotor2.items()}
    rev3 = {value: key for key, value in rotor3.items()}


    # Update the rotor labels on the GUI
    rotor1label.config(text=str(pos1))
    rotor2label.config(text=str(pos2))
    rotor3label.config(text=str(pos3))

# Function to simulate Enigma machine   
def enigma_letter(letter):
    print(letter)
    step1 = plugboard.get(letter)
    step2 = rotor1.get(step1)
    step3 = rotor2.get(step2)
    step4 = rotor3.get(step3)
    reflected = reflector.get(step4)
    rev1 = {value: key for key, value in rotor1.items()}
    rev2 = {value: key for key, value in rotor2.items()}
    rev3 = {value: key for key, value in rotor3.items()} 
    step5 = rev3.get(reflected)
    step6 = rev2.get(step5)
    step7 = rev1.get(step6)
    step8 = plugboard.get(step7)
    return step8

frame_b = tk.Frame(root)
frame_b.grid(row=2, column=0, padx=20, pady=20)

for i, letter in enumerate(alphabet):
    button = tk.Button(frame_b, text=letter, font=font, width=5, height=2,
                       bg=button_color, activebackground=hover_color,
                       command=lambda l=letter: on_button_b_click(l))
    button.grid(row=i // 7, column=i % 7, padx=5, pady=5)

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

plugboard_label = tk.Label(root, text = "Plugboard", font= 30)
plugboard_label.place(relx=0.435, rely= 0.08, anchor="center")

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


plugboard_frame = tk.Frame(root)
plugboard_frame.place(relx=0.4, rely=0.1)

def on_plugboard_button_click(letter, button):
    global letter_to_bind1, letter_to_bind2, num_of_conections
    button_clicked = plugboard_buttons[letter]
    
    if letter_to_bind1 == None:
        letter_to_bind1 = letter
        if plugboard[letter_to_bind1] != letter_to_bind1:
            print("deselect")
            num_of_conections -= 1
            plugboard_buttons[letter_to_bind1].config(bg = "#FFFFFF")
            plugboard_buttons[plugboard.get(letter_to_bind1)].config(bg = "#FFFFFF")
            plugboard[plugboard.get(letter_to_bind1)] = plugboard.get(letter_to_bind1)
            plugboard[letter_to_bind1] = letter_to_bind1
            letter_to_bind1 = None
            return
        print(letter_to_bind1)
        button_clicked.config(bg = "#808080")
    else:
        letter_to_bind2 = letter
        print(letter_to_bind2)
        if letter_to_bind1 == letter_to_bind2:
            print("same twice")
            button_clicked.config(bg = "#FFFFFF")
            letter_to_bind1 = None
            letter_to_bind2 = None
        elif plugboard[letter_to_bind1] != letter_to_bind1 or plugboard[letter_to_bind2] != letter_to_bind2:
            print("attempted to pair an already paired")
            if plugboard[letter_to_bind1] != letter_to_bind1:
                print("hi mom")
                plugboard_buttons[letter_to_bind1].config(bg = colors[num_of_conections])
                letter_to_bind1 = None
                letter_to_bind2 = None
            else:
                print("hi dad")
                plugboard_buttons[letter_to_bind2].config(bg = colors[num_of_conections])
                plugboard_buttons[letter_to_bind1].config(bg = "#FFFFFF")
                letter_to_bind1 = None
                letter_to_bind2 = None
        elif plugboard[letter_to_bind1] == letter_to_bind1:
            print("paired")
            plugboard[letter_to_bind1] = letter_to_bind2
            plugboard[letter_to_bind2] = letter_to_bind1
            plugboard_buttons[letter_to_bind1].config(bg = colors[num_of_conections])
            plugboard_buttons[letter_to_bind2].config(bg = colors[num_of_conections])
            num_of_conections += 1
            print(num_of_conections)
            letter_to_bind1 = None
            letter_to_bind2 = None
            
# Generate buttons for Set B (A-Z)

plugboard_buttons = {}
for i, letter in enumerate(alphabet):
    button = tk.Button(plugboard_frame, text=letter, font=("Arial", 14), width=4, height=2,
                    command=lambda l=letter: on_plugboard_button_click(l, button))
    button.grid(row=i // 13, column=i % 13, padx=5, pady=5)
    plugboard_buttons[letter] = button
    

# Run the Tkinter main loop
root.mainloop()