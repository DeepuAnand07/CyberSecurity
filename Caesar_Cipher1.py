import tkinter as tk
from tkinter import messagebox, ttk

# Function to encrypt the text
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Keep spaces & special characters unchanged
    return result

# Function to handle encryption
def encrypt_text():
    text = input_text.get()
    try:
        shift = int(shift_value.get())
        output_text.set(caesar_cipher(text, shift, "encrypt"))
    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number!")

# Function to handle decryption
def decrypt_text():
    text = input_text.get()
    try:
        shift = int(shift_value.get())
        output_text.set(caesar_cipher(text, shift, "decrypt"))
    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number!")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Encryption")
root.geometry("400x500")
root.config(bg="#2C3E50")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)

# Title Label
title_label = tk.Label(root, text="Caesar Cipher", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
title_label.pack(pady=10)

# Input Label & Field
tk.Label(root, text="Enter Message:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
input_text = tk.Entry(root, font=("Arial", 14), width=30)
input_text.pack(pady=5)

# Shift Label & Field
tk.Label(root, text="Enter Shift Value:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
shift_value = tk.Entry(root, font=("Arial", 14), width=10)
shift_value.pack(pady=5)

# Output Label
tk.Label(root, text="Result:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
output_text = tk.StringVar()
output_label = tk.Entry(root, font=("Arial", 14), width=30, textvariable=output_text, state="readonly")
output_label.pack(pady=5)

# Encrypt & Decrypt Buttons
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

encrypt_btn = ttk.Button(button_frame, text="Encrypt", command=encrypt_text)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = ttk.Button(button_frame, text="Decrypt", command=decrypt_text)
decrypt_btn.grid(row=0, column=1, padx=5)

# Run the GUI
root.mainloop()
