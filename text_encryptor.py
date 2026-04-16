import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet   # type: ignore

# --- Core Logic Functions ---

def generate_key():
    # Standard logic to create a key file
    key = Fernet.generate_key()
    with open("secret_key.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Manager", "New Key generated and saved as 'secret_key.key'")

def load_key():
    try:
        return open("secret_key.key", "rb").read()
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found! Please generate a key first.")
        return None

def encrypt_action():
    key = load_key()
    if key:
        f = Fernet(key)
        message = entry_input.get()
        if message:
            encrypted_msg = f.encrypt(message.encode())
            # Displaying the result in the output field
            entry_output.delete(0, tk.END)
            entry_output.insert(0, encrypted_msg.decode())
        else:
            messagebox.showwarning("Input Error", "Please enter text to encrypt.")

def decrypt_action():
    key = load_key()
    if key:
        f = Fernet(key)
        secret = entry_input.get()
        try:
            decrypted_msg = f.decrypt(secret.encode())
            entry_output.delete(0, tk.END)
            entry_output.insert(0, decrypted_msg.decode())
        except Exception:
            messagebox.showerror("Error", "Decryption failed. Ensure you have the right key/text.")

def clear_fields():
    entry_input.delete(0, tk.END)
    entry_output.delete(0, tk.END)

# --- GUI Layout ---

window = tk.Tk()
window.title("CS Student Project: AES Encrypter")
window.geometry("450x350")

# Title Label
tk.Label(window, text="Simple Encryption Tool", font=("Arial", 14, "bold")).pack(pady=10)

# Input Section
tk.Label(window, text="Enter Message or Cipher:").pack()
entry_input = tk.Entry(window, width=50)
entry_input.pack(pady=5)

# Button Section (The Action Buttons)
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate Key", command=generate_key, width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Encrypt", command=encrypt_action, width=15, bg="#d1e7dd").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Decrypt", command=decrypt_action, width=15, bg="#f8d7da").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Clear", command=clear_fields, width=15).grid(row=1, column=1, padx=5, pady=5)

# Output Section
tk.Label(window, text="Result:").pack()
entry_output = tk.Entry(window, width=50, fg="blue")
entry_output.pack(pady=5)

window.mainloop()