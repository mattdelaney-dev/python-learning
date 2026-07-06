from tkinter import *
import requests
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

file_path = os.path.join(BASE_DIR, "background.png")
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=file_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

file_path1 = os.path.join(BASE_DIR, "kanye.png")
kanye_img = PhotoImage(file=file_path1)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()