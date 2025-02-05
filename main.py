print("Loading...")
from tkinter import Tk, Canvas
import datetime
from playsound3 import playsound
import threading


def play_sound():
    # Used to play the sound in a separate thread
    playsound("audio/bells.wav")

# Date Calc
today = datetime.date.today()
future = datetime.date(2025,12,25)
diff = future - today
# print (diff.days) is the magic word

# Window init
root = Tk()
c = Canvas(root, width=600, height=400, bg='red') # Will change reslution later 
root.resizable(False, False)
root.title("Christmas Countdown")
root.iconbitmap("window_icon.ico")
c.pack()

# Start the sound in a new thread
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

#Text init
c.create_text(300, 50, anchor='center', fill='white', font='Arial 28 bold', text='Cristmas Countdown')

print("Done loading")
root.mainloop()
sound_thread.join()
playsound("audio/crisler.wav")