Project: Symmetric Text Encryption Suite

🎯 Objective

The primary goal of this project was to design and implement a secure, user-friendly desktop application for data confidentiality. It demonstrates the practical application of AES (Advanced Encryption Standard) to protect text-based information from unauthorized access.

🛠️ Technical Stack (Tools Used)

Language: Python 3.x

Cryptography: cryptography.fernet (Symmetric AES-128)

GUI Framework: Tkinter (Python Standard Library)

IDE: VS Code

Version Control: Git & GitHub

📝 Project Components & Implementation

1. Cryptographic Logic

I implemented a symmetric-key system where a single 128-bit key is responsible for both encryption and decryption.

Key Generation: The script creates a persistent secret_key.key file.

Data Scrambling: Plaintext is encoded to bytes and processed through a Fernet cipher to produce an immutable ciphertext.

2. Graphical User Interface (GUI)
   
To move away from the command line, I built a front-end that handles:

Real-time input/output display.

One-click key management.

Visual feedback for successful operations and error handling.

3. Security Features
    
4. Integrity Verification: The system automatically detects if the ciphertext has been tampered with and prevents decryption.

5. Key Isolation: The logic separates the key from the code, allowing the key to be managed independently of the application logic.

📌 Key Takeaways

Understanding the lifecycle of a cryptographic key.

Handling byte-to-string conversions in Python.

Developing event-driven applications using Tkinter.
