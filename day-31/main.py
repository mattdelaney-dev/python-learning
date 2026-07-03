from tkinter import *
import os
import pandas
import random
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BACKGROUND_COLOR = "#B1DDC6"

# Loads words if it doesn't exist it gets it from french_words.
try:
    file_path = os.path.join(BASE_DIR, "data", "words_to_learn.csv")
    french_words = pandas.read_csv(file_path)
except FileNotFoundError:
    file_path = os.path.join(BASE_DIR, "data", "french_words.csv")
    french_words = pandas.read_csv(file_path)

french_words = french_words.to_dict(orient="records")

current_card = {}
flip_timer = None


def random_word():
    global current_card, flip_timer

    window.after_cancel(flip_timer) if flip_timer else None
    current_card = random.choice(french_words)
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

# Flip card function
def flip_card():
    global current_card

    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")

# Is known function
def is_known():
    
    french_words.remove(current_card)

    file_path = os.path.join(BASE_DIR, "data", "words_to_learn.csv")
    new_data = pandas.DataFrame(french_words)
    new_data.to_csv(file_path, index=False)




    random_word()


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
right_image = PhotoImage(file=os.path.join(BASE_DIR, "images", "right.png"))
wrong_image = PhotoImage(file=os.path.join(BASE_DIR, "images", "wrong.png"))
card_front = PhotoImage(file=os.path.join(BASE_DIR, "images", "card_front.png"))
card_back = PhotoImage(file=os.path.join(BASE_DIR, "images", "card_back.png"))

# Canvas Placements
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_back)
canvas.itemconfig(card_image, image=card_front)
language_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
random_word()

# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)



window.mainloop()