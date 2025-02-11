from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    print("Decryption functionality will be implemented here.")

def encrypt():
    password = code.get()

    if password == "1234":
        # Open a new window for the decryption output
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        # Get the message from text1, encode, and encrypt it
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(decode_message)
        decrypt = base64_bytes.decode("ascii")
        
        # Label to display "DECRYPT" text
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        
        # Display the encrypted text in a Text widget
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt)  # Insert the encrypted text
        text2.config(state=DISABLED)  # Make the text read-only

    elif password == "":
        messagebox.showerror("encryption", "Input password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid password")

def main_screen():
    global screen, code, text1
    
    screen = Tk()
    screen.geometry("375x398")
    
    # Load image icon
    try:
        image_icon = PhotoImage(file="keys.png")
        screen.iconphoto(False, image_icon)
    except Exception as e:
        print("Error loading image:", e)
    
    screen.title("PctApp")

# Function to reset fields
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    # UI components
    Label(text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    # Buttons for encryption, decryption, and reset
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    
    screen.mainloop()

main_screen()