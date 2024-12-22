import tkinter as tk

your_name = "CEDRICK_PATARAY"
your_section = "BSIT-2A"

root = tk.Tk()
root.title(f"OOP LA29 {your_name}")
root.geometry("400x300")
root.configure(bg="pink")

label = tk.Label(text=f"OOP LA28 {your_name}{your_section}")
label.grid(row=0, column=0, padx=100, pady=130)

root.mainloop()