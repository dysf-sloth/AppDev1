import tkinter as tk   

# Create the main window

window = tk.Tk()
window.title("python GUI - grid layout")
window.geometry("300x350")


#create widgets here

username_label = tk.Label(window, text="Username")
username_entry = tk.Entry(window)
password_label = tk.Label(window, text="Password")
password_entry = tk.Entry(window)
button1 = tk.Button(window, text="Submit")
button2 = tk.Button(window, text="Clear")
button3 = tk.Button(window, text="Close")


#grid layout for widgets

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)

# using grid_slaves() method

for widget in window.grid_slaves(row=2):
    widget.grid(ipadx=20)

# Start the main event loop

window.mainloop()