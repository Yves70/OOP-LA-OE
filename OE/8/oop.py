import tkinter as tk

root = tk.Tk()
root.title("Task Management")
root.geometry("400x300")
root.configure(bg="pink")

counter = 1
def display_text():
    global counter
    print(counter,name.get())
    counter += 1

button = tk.Button(root,text= "Submit", command=display_text)
button.grid(row=0, column=1 , padx=0, pady=20)

name = tk.Entry(root)
name.grid(row=0, column=0, padx=20, pady=0)

root.mainloop()