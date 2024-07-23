import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

root = ctk.CTk()
root.title('Login Page')
root.resizable(False, False)
root.config(bg='white')

# Load the background image using PIL.Image and convert to PhotoImage
bg_image = Image.open("bg2.jpg").resize((500, 500))
bg_img = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = ctk.CTkLabel(root, image=bg_img, text="")
bg_label.grid(row=0, column=0)

frame = ctk.CTkFrame(root, bg_color="#D9D9D9", fg_color="white", height=350, width=300, corner_radius=20)
frame.grid(row=0, column=1, padx=40)

def login():
    email = email_entry.get()
    password = passwd_entry.get()
    if email == 'admin@mail.com' and password == 'admin':
        tk.messagebox.showinfo(title='Login-Page', message='Login Successfully')
    elif email == 'admin@mail.com':
        tk.messagebox.showwarning(title='Warning', message='Please enter your password')
    elif password == 'admin':
        tk.messagebox.showwarning(title='Warning', message='Please Enter your Email')
    else:
        tk.messagebox.showerror(title='Login Page', message='Wrong mail or password')
    email_entry.delete(0, tk.END)
    passwd_entry.delete(0, tk.END)

welcome_label = ctk.CTkLabel(frame, text="Welcome Back! \nLogin to Account", text_color="black", font=("", 35, "bold"))
welcome_label.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

email_entry = ctk.CTkEntry(frame, text_color="white", placeholder_text="Username", fg_color="black",
                           placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15, height=45)
email_entry.grid(row=1, column=0, sticky="nwe", padx=30)

passwd_entry = ctk.CTkEntry(frame, text_color="white", placeholder_text="Password", fg_color="black",
                            placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15,
                            height=45, show="*")
passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)

login_button = ctk.CTkButton(frame, text="Login", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF",
                             cursor="hand2", corner_radius=15, command=login)
login_button.grid(row=3, column=0, sticky="ne", pady=20, padx=35)

root.mainloop()
