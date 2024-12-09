import tkinter as tk    

window=tk.Tk()
window.title("Python GUI with Tkinter - Frames")
top_frame = tk.Frame(window)
bottom_frame = tk.Frame(window)

top_frame.pack()
bottom_frame.pack()

#create widgets here

text1 = tk.Label(top_frame, text="this application tests frame layout")
button1 = tk.Button(bottom_frame, text="Button 1", fg="green")
button2 = tk.Button(bottom_frame, text="Button 2", fg="red")
button3 = tk.Button(bottom_frame, text="Button 3", fg = "blue")

#pack widgets

text1.pack()
button1.pack(side= tk.LEFT)
button2.pack(side= tk.LEFT)
button3.pack(side= tk.LEFT)

# Start the main event loop
window.mainloop()