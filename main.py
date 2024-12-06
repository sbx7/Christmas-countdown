from tkinter import Tk, Canvas
from datetime import date, datetime
from playsound3 import playsound
import threading

def play_sound():
    # Play sound in a separate thread
    playsound("audio/bells.wav")

# Window init
root = Tk()
c = Canvas(root, width=600, height=400, bg='red')
root.resizable(False, False)
root.title("Christmas Countdown")
root.iconbitmap("window_icon.ico")
c.pack()

# Start the sound playback in a new thread
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

#Text creation
c.create_text(100, 50, anchor='w', fill='white', font='Arial 28 bold', text='Christmas countdown🎄')

root.mainloop()