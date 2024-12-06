from tkinter import Tk, Canvas
from datetime import date, datetime
from playsound import playsound

# Window init
root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
root.resizable(False, False)
root.title("Christmas Countdown")
root.iconbitmap("window_icon.ico")
c.pack()

#Audio
playsound('audio/bells.wav')

#Text creation
c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold', text='Christmas countdown🎄')

root.mainloop()