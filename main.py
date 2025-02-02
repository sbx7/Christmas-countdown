print("Loading...")
from tkinter import Tk, Canvas
from datetime import date, datetime
from playsound3 import playsound
import threading


def play_sound():
    # Used to play the sound in a separate thread
    playsound("audio/bells.wav")


def get_events():
    list_events=[]
    with open(events) as file: # Extracts events from event file
        for line in file:
            line=line.rstrip('\n') # Gets rid of the newline character
            current_event=line.split('.') # Chops up the name from the date (name.#/#/##)
            event_date = datetime.strptime(current_event[1], '%d/%m/%y'.date)
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events
# idk whats happening lines 19-21 im just reading a book


# Window init
root = Tk()
c = Canvas(root, width=800, height=800, bg='red') # Will change reslution later 
root.resizable(False, False)
root.title("Christmas Countdown")
root.iconbitmap("window_icon.ico")
c.pack()

# Start the sound in a new thread
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

#Text init
c.create_text(100, 50, anchor='w', fill='white', font='Arial 28 bold', text='Christmas countdown🎄')

print("Done loading")
root.mainloop()
sound_thread.join()
playsound("audio/crisler.wav")