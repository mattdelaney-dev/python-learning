import tkinter

window = tkinter.Tk()
window.title("First GUI program!")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24))
my_label.pack(side="left")

window.mainloop()