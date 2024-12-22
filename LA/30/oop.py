import tkinter as tk

your_name = "CEDRICK_PATARAY"
your_section = "BSIT-2A"
anime_title = "One Piece"

root = tk.Tk()
root.title(f"OOP LA29 {your_name}")
root.geometry("400x300")
root.configure(bg="pink")

counter = 0
def display_text():
    global counter
    print(f"{counter} My favorite anime is {anime_title}")
    counter += 1

button = tk.Button(root,text= "Run", command=display_text)
button.grid(row=0, column=0 , padx=185, pady=50)

root.mainloop()