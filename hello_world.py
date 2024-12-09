import tkinter as tk    


# Create the main window

window=tk.Tk()
window.title("Exercise 1")

#create frames here

top_frame = tk.Frame(window)
middle_frame1 = tk.Frame(window)
middle_frame2 = tk.Frame(window)
bottom_frame = tk.Frame(window)

#pack frames here

top_frame.pack()
middle_frame1.pack()
middle_frame2.pack()
bottom_frame.pack()

#create widgets here

text1 = tk.Label(top_frame, text="this application demostrates frame layout")
button1 = tk.Button(middle_frame1, text="Button 1", fg="green")
button2 = tk.Button(middle_frame1, text="Button 2", fg="red")
button3 = tk.Button(middle_frame1, text="Button 3", fg = "blue")
button4 = tk.Button(middle_frame2, text="Button 4", fg = "blue")
button5 = tk.Button(middle_frame2, text="Button 5", fg = "green")
button6 = tk.Button(middle_frame2, text="Button 6", fg = "red")
button7 = tk.Button(bottom_frame, text="Button 7", fg = "blue")
button8 = tk.Button(bottom_frame, text="Button 8", fg = "blue")
button9 = tk.Button(bottom_frame, text="Button 9", fg = "blue")


#pack widgets

text1.pack()
button1.pack(side= tk.LEFT)
button2.pack(side= tk.LEFT)
button3.pack(side= tk.LEFT)
button4.pack(side= tk.LEFT)
button5.pack(side= tk.LEFT)
button6.pack(side= tk.LEFT)
button7.pack(side= tk.LEFT)
button8.pack(side= tk.LEFT)
button9.pack(side= tk.LEFT)


# Start the main event loop
window.mainloop()