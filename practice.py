import tkinter as tk
from tkinter import ttk
from tqdm import tqdm
import time

def run_task():
    for i in tqdm(range(100), desc="Processing"):
        time.sleep(0.05)

app = tk.Tk()
app.title("Tkinter with tqdm")

progress_button = ttk.Button(app, text="Start Task", command=run_task)
progress_button.pack()

app.mainloop()
