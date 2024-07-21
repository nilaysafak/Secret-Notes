from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt():
    title = entry.get()
    notes = multitext.get("1.0",END)
    masterkey = entry2.get()


    if len(title)==0 or len(notes)==0 or len(masterkey)==0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
    else:
        #encryption
        message_encrypted = encode(masterkey,notes)
        try: 
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            entry.delete(0,END)
            multitext.delete("1.0",END)
            entry2.delete(0,END)


def decrypt_notes():
    message_encrypted = multitext.get("1.0",END).strip()
    masterkey = entry2.get()

    if len(message_encrypted)==0 or len(masterkey)==0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
    else:
        try:
            decrypted_message = decode(masterkey,message_encrypted)
            multitext.delete("1.0",END)
            multitext.insert("1.0",decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")




window =Tk()
window.title("Secret Notes")
window.minsize(550,650)


image_path = r"C:\Users\nilay\Downloads\secret notes (1).png"
original_image = Image.open(image_path)
resize_image = original_image.resize((100,100))
photo = ImageTk.PhotoImage(resize_image)

#canvas kullanılabilir

image_label = Label(window,image=photo)
image_label.pack()


label1 = Label(text="Enter your title",font=(5))
label1.config(padx=15,pady=15)
label1.pack()


entry = Entry(width=35)
entry.focus()
entry.pack()

label2 = Label(text="Enter your secret",font=2)
label2.config(padx=15,pady=15)
label2.pack()

multitext = Text(width=30,height=15)
multitext.pack()

label3 = Label(text="Enter master key",font=1)
label3.config(padx=10,pady=10)
label3.pack()

entry2 = Entry(width=35)
entry2.pack()


button = Button(text="Save&encrypt",command=save_and_encrypt)
button.pack()

decrypt_button = Button(text="Decrypt",command=decrypt_notes)
decrypt_button.pack()

window.mainloop()