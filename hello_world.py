import tkinter as tk    


# Create the main window

window=tk.Tk()
window.title("Exercise 1")

#create frames here

top_frame = tk.Frame(window)
big_frame = tk.Frame(window)
small_frame1 = tk.Frame(big_frame)
#small_frame2 = tk.Frame(big_frame)

#pack frames here

top_frame.pack()
big_frame.pack()
small_frame1.pack(side= tk.LEFT)
#small_frame2.pack(side= tk.BOTTOM)    

#create widgets here

text1 = tk.Label(top_frame, text="this application demostrates frame layout")
button1 = tk.Button(small_frame1, text="Button 1", fg="green")
button2 = tk.Button(small_frame1, text="Button 2", fg="red")
button3 = tk.Button(small_frame1, text="Button 3", fg = "blue")
button4 = tk.Button(small_frame1, text="Button 4", fg = "blue")
text2 = tk.Label(big_frame, text="this is a big frame")
#button5 = tk.Button(middle_frame2, text="Button 5", fg = "green")
#button6 = tk.Button(middle_frame2, text="Button 6", fg = "red")
#button7 = tk.Button(bottom_frame, text="Button 7", fg = "blue")
#button8 = tk.Button(bottom_frame, text="Button 8", fg = "blue")
#button9 = tk.Button(bottom_frame, text="Button 9", fg = "blue")


#pack widgets

text1.pack()
button1.pack(side= tk.TOP)
button2.pack(side= tk.LEFT)
button3.pack(side= tk.LEFT)
button4.pack(side= tk.LEFT)
text2.pack()
#button5.pack(side= tk.LEFT)
#button6.pack(side= tk.LEFT)
#button7.pack(side= tk.LEFT)
#button8.pack(side= tk.LEFT)
#button9.pack(side= tk.LEFT)


# Start the main event loop
window.mainloop()