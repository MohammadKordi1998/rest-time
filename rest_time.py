import time
import tkinter as tk
from tkinter import ttk


def show_displaye_lock():
    window = tk.Tk()
    window.title("Empty Page Example")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    window.overrideredirect(True)

    label_text = "Hi, It's time to rest"
    label = tk.Label(window, text=label_text, background='#6495ED', font=('Arial', 75))
    label.pack(pady=500)
    window.config(bg='#6495ED')
    
    window.after(1000*5, window.destroy)
    window.mainloop()

while True:
    time.sleep(60)
    show_displaye_lock()
    print('hi')


