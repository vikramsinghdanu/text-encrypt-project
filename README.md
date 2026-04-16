AES-128 Text Encryption Suite

🎯 Project Objective

The goal of this project was to develop a secure desktop application that simplifies Symmetric Encryption. It demonstrates how to maintain data confidentiality by using industry-standard AES logic while providing a user-friendly graphical interface.

🔑 Core Workflow

The application implements a Symmetric Cryptography lifecycle:

Key Generation: Creates a unique 128-bit key (secret_key.key). This is the single source of truth for both locking and unlocking data.

Encryption: Uses the AES-128 algorithm (Fernet) to transform plaintext into an immutable, base64-encoded ciphertext.

Decryption: Validates the ciphertext against the local key file to reverse the mathematical scramble and restore the original message.

🛠️ Technical Stack

Language: Python 3.x

Encryption Standard: AES-128 (Fernet)

Library: cryptography

Interface: Tkinter (GUI)

💡 Key Takeaways

Data Confidentiality: Demonstrated how AES prevents unauthorized access to sensitive text.

Integrity Verification: Learned how modern encryption libraries detect if data has been tampered with.

Secure Key Handling: Practiced isolating encryption keys from the application source code.

User Experience (UX): Simplified complex cryptographic operations into a clean, three-button interface.
