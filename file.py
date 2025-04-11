import tkinter as tk
from tkinter import messagebox

def track_price():
    url = url_entry.get()
    messagebox.showinfo("Tracking Started", f"Tracking price for:\n{url}")

root = tk.Tk()
root.title("Price Drop Notifier")

tk.Label(root, text="Paste Product URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Track Price", command=track_price).pack(pady=10)

root.mainloop()
