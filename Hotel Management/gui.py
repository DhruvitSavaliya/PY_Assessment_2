import tkinter as tk
from tkinter import messagebox
from hotel import Hotel

hotel = Hotel()

def check_in_guest():
    name = entry_name.get()
    room = entry_room.get()
    balance = entry_balance.get()

    if not name or not room or not balance:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        hotel.check_in(name, int(room), float(balance))
        messagebox.showinfo("Success", f"{name} checked in successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def check_out_guest():
    room = entry_room.get()
    if not room:
        messagebox.showerror("Error", "Enter room number!")
        return

    hotel.check_out(int(room))
    messagebox.showinfo("Success", f"Checked out room {room}")

root = tk.Tk()
root.title("Hotel Management System")

tk.Label(root, text="Guest Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Room Number").pack()
entry_room = tk.Entry(root)
entry_room.pack()

tk.Label(root, text="Balance").pack()
entry_balance = tk.Entry(root)
entry_balance.pack()

tk.Button(root, text="Check In", command=check_in_guest).pack()
tk.Button(root, text="Check Out", command=check_out_guest).pack()

root.mainloop()
