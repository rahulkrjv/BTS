import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

import tkinter as tk
from tkinter import messagebox

def logIn():
    try:        
        con = sql.connect("BTS")
        cursor = con.cursor()

        userId = int(entry_username.get())
        password = entry_password.get()

        qry = f"SELECT * FROM Employee WHERE empCode = '{userId}' AND empPassword = '{password}'"
        cursor.execute(qry)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome!")
            return result
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values.")
    except sql.Error as error:
        messagebox.showerror("Database Error", f"Error occurred - {error}")
    finally:
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

# Create a styled login GUI
root = tk.Tk()
root.title("Bug Tracking System - Login")

# Set window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Configure styles
bg_color = "#f0f0f0"  # Light gray background
fg_color = "#333333"  # Dark text color
font_style = "Helvetica 12 bold"

root.configure(bg=bg_color)

frame = tk.Frame(root, bg=bg_color, padx=20, pady=20)
frame.pack(expand=True)

label_heading = tk.Label(frame, text="Log In", font="Helvetica 16 bold", fg="#009688", bg=bg_color)
label_heading.grid(row=0, columnspan=2, pady=(0, 20))

label_username = tk.Label(frame, text="Username (empCode):", font=font_style, fg=fg_color, bg=bg_color)
label_username.grid(row=1, column=0, sticky=tk.E)

label_password = tk.Label(frame, text="Password:", font=font_style, fg=fg_color, bg=bg_color)
label_password.grid(row=2, column=0, sticky=tk.E)

entry_username = tk.Entry(frame, font=font_style)
entry_username.grid(row=1, column=1)

entry_password = tk.Entry(frame, show="*", font=font_style)
entry_password.grid(row=2, column=1)

btn_login = tk.Button(frame, text="Login", command=logIn, font=font_style, bg="#009688", fg="white")
btn_login.grid(row=3, columnspan=2, pady=10)

root.mainloop()
