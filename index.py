import base64
import os
import tkinter as tk
from tkinter import messagebox

def decrypt():
    password = code.get()
    if password == "1234":
        message = text1.get("1.0", tk.END)
        # You don't need to decode the message, it's already a string
        decrypted_message = base64.b64decode(message).decode("utf-8")

        screen2 = tk.Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        tk.Label(screen2, text="DECRYPTED MESSAGE", font="arial", fg="white", bg="#00bd56").place(x=10, y=10)
        text2 = tk.Text(screen2, font="Roboto 10", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(tk.END, decrypted_message)

    elif password == "":
        messagebox.showerror("Decryption", "Input password.")
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid password.")

def encrypt():
    password = code.get()
    if password == "1234":
        message = text1.get("1.0", tk.END)  # Use "1.0" instead of 1.0 for Text widget
        encoded_message = message.encode("utf-8")
        encrypted_message = base64.b64encode(encoded_message).decode("utf-8")

        # Create a new window for displaying the encrypted message
        screen1 = tk.Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        tk.Label(screen1, text="ENCRYPTED MESSAGE", font="arial", fg="white", bg="#ed3833").place(x=10, y=10)
        text2 = tk.Text(screen1, font="Roboto 10", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(tk.END, encrypted_message)

    elif password == "":
        messagebox.showerror("encryption", "input password")
    elif password != "1234":
        messagebox.showerror("encryption", "invalid password")       

def main_screen():
    global screen
    global code
    global text1

    screen = tk.Tk()
    screen.geometry("375x398")

    # Icon
    image_icon = tk.PhotoImage(file="C:\\Users\\SOFTRONIICS\\Downloads\\keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete("1.0", tk.END)

    tk.Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)

    text1 = tk.Text(font="Roboto 20", bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    code = tk.StringVar()
    tk.Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    tk.Button(text="ENCRYPT", height="2", width=23, bg="green", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    tk.Button(text="DECRYPT", height="2", width=23, bg="red", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    tk.Button(text="RESET", height="2", width=50, bg="blue", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
