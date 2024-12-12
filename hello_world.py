import tkinter as tk   

# Define button actions

def button1_action():
    text = entry_text.get()
    display_text = "Hello " + text + "! How are you?"
    text1.config(text=display_text) 
    button1.config(fg="purple")
    button1.config(bg="red") 


# Create the main window

window = tk.Tk()
window.title("Clicking application")
window.geometry("300x350")

#create widgets here

text1 = tk.Label(window, text="Enter your name: ")
button1 = tk.Button(window, text="Button 1", fg="green", command=button1_action)
entry_text = tk.Entry(window)   
#pack widgets

button1.pack()
text1.pack()
entry_text.pack()

# Start the main event loop

window.mainloop()