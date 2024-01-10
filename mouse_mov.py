import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import random
from screeninfo import get_monitors

def get_screen_size():
    monitors = get_monitors()
    if monitors:
        return monitors[0].width, monitors[0].height
    return None

def random_mouse_movement(duration_seconds):
    screen_size = get_screen_size()

    if screen_size is None:
        print("Failed to get screen dimensions.")
        return

    screen_width, screen_height = screen_size

    pyautogui.FAILSAFE = False  

    start_time = time.time()

    try:
        while time.time() - start_time < duration_seconds:
            x_offset = random.randint(0, screen_width)
            y_offset = random.randint(0, screen_height)
            pyautogui.moveTo(x_offset, y_offset, duration=0.1)
            time.sleep(0.1)  

    except KeyboardInterrupt:
        print("\nScript interrupted by user.")

    pyautogui.FAILSAFE = True 

def start_button_clicked():
    try:
        duration_seconds = int(duration_entry.get())
        random_mouse_movement(duration_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number for the duration.")

root = tk.Tk()
root.title("Mouse Movement Script")

ttk.Label(root, text="Duration (seconds):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
duration_entry = ttk.Entry(root)
duration_entry.grid(row=0, column=1, padx=5, pady=5)

start_button = ttk.Button(root, text="Start", command=start_button_clicked)
start_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
