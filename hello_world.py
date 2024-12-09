import tkinter as tk    

window=tk.Tk()
window.title("Python GUI with Tkinter - Layouts")

#create widgets here

text1 = tk.Label(window, text="this application tests simple layout")
button1 = tk.Button(text="Button 1", fg="green")
button2 = tk.Button(text="Button 2", fg="red")
button3 = tk.Button(text="Button 3", fg = "blue")

#pack widgets

text1.pack()
button1.pack()
button2.pack()
button3.pack()

# Start the main event loop
window.mainloop()