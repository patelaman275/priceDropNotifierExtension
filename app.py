import tkinter as tk
from tkinter import messagebox
from storage import load_data, save_data
from scraper import get_price
import threading

def track_price():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please paste a product URL.")
        return

    price = get_price(url)


    if price:
        data = load_data()
        data[url] = price
        save_data(data)
        messagebox.showinfo("Tracking Started", f"Tracking started at ₹{price}")
    else:
        messagebox.showerror("Error", "Could not fetch price. Please check the URL.")

root = tk.Tk()
root.title("Price Drop")
root.geometry("400x150")

tk.Label(root, text="Paste Product URL:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Button(root, text="Track Price", command=track_price).pack(pady=15)

root.mainloop()

