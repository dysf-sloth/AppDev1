import tkinter as tk   

# Define button actions

def button1_action():
    text = name_entry.get() + surname_entry.get()
    display_text = "Welcome " + text + "!! You have registered."
    text1.config(text=display_text) 



# Create the main window

window = tk.Tk()
window.title("Clicking application")
window.geometry("300x150")

#create frames here

top_frame = tk.Frame(window)
middle_frame = tk.Frame(window)

#pack frames here

top_frame.pack(fill="both")
middle_frame.pack(fill="both")

#create widgets here

name_label = tk.Label(top_frame, text="Name")
name_entry = tk.Entry(top_frame)
surname_label = tk.Label(middle_frame, text="Surname")
surname_entry = tk.Entry(middle_frame)
button1 = tk.Button(window, text="Register", command=button1_action)
text1 = tk.Label(window, text="") 

#pack widgets

button1.pack()
text1.pack()
name_entry.pack(side="right", fill="both", expand=True)
name_label.pack(side="left")
surname_entry.pack(side="right", fill="both", expand=True)
surname_label.pack(side="left")

# Start the main event loop

window.mainloop()