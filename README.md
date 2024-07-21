This project aims to create a simple note-taking application that allows users to encrypt and decrypt their notes using a master key. The application is built using Python and the Tkinter library for the GUI, with additional functionality from the Pillow library for image handling and the base64 module for encoding and decoding.

### Key Components:
1. **Tkinter**: Used for creating the graphical user interface (GUI).
2. **Pillow (PIL)**: Used for handling and displaying images.
3. **Base64**: Used for encoding and decoding the text to ensure secure storage.

### Functionality:
- **Encryption and Decryption**: The `encode` and `decode` functions encrypt and decrypt the notes using a master key provided by the user.
- **GUI Elements**: 
  - Labels and entry fields for the note title, content, and master key.
  - Buttons to save (encrypt) and decrypt notes.
- **File Handling**: Encrypted notes are saved to a file named `mysecret.txt`.

### How it Works:
1. **Save and Encrypt**:
   - The user enters a title, note content, and a master key.
   - Upon clicking "Save & Encrypt", the note is encrypted and saved to a file.
2. **Decrypt Notes**:
   - The user can decrypt previously saved notes by entering the encrypted text and the master key, then clicking "Decrypt".

### GUI Layout:
- An image at the top for visual enhancement.
- Text fields for the note title and content.
- An entry field for the master key.
- Buttons to trigger the save/encrypt and decrypt functions.
