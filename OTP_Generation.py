import hashlib
from tkinter import *
import time

gen_click_counter = 0

def client():
    window = Tk()

    # add widgets here
    lbl = Label(window, fg='red', font=("Helvetica", 16))
    lbl.place(relx=0.5, anchor=CENTER, rely=0.3)

    hidden_lbl = Label(window)

    btn = Button(window, text="Generate OTP", fg='black',
                 command=lambda: generate_otp_client(label=lbl, hidden_label=hidden_lbl))
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.title('Client')
    window.geometry("300x200+10+20")
    return window


def server():
    window = Toplevel()

    # add widgets here
    entry = Entry(window, fg='red', font=("Helvetica", 16))
    entry.place(relx=0.5, anchor=CENTER, rely=0.3)

    lbl = Label(window, fg='red', font=("Helvetica", 16))
    lbl.place(relx=0.5, anchor=CENTER, rely=0.7)

    btn = Button(window, text="Validate OTP", fg='black',
                 command=lambda: generate_otp_server(label=lbl, text_box=entry))
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.title('Server')
    window.geometry("300x200+10+20")
    return window


def generate_hash(key):
    """
    This method will generate an SHA2 hash on supplied key
    :param key: string to generate hash
    :return: sha2 in string
    """
    return hashlib.new("sha256", key.encode()).hexdigest()


def truncate_hash(hash):
    """
    This method will truncate the hash into a six digit OTP.
    :param hash: sha2
    :return: otp in str
    """
    truncated = str(int(hash, 16))[-6:]
    return truncated


def generate_otp_client(label, hidden_label, key="8EEE70FF00FF080F2"):
    # global variables used
    global gen_click_counter

    if hidden_label["text"] is not None and hidden_label["text"] is not "":
        key = hidden_label["text"]

    gen_click_counter += 1

    # get sha2
    sha2 = generate_hash(key)
    # save sha2 in hidden label for next iteration
    hidden_label["text"] = sha2
    # get otp from seed (i.e. sha2)
    otp = truncate_hash(sha2)
    # update label
    label["text"] = otp


def generate_otp_server(label, text_box, key="8EEE70FF00FF080F2"):
    otp = ""
    for i in range(gen_click_counter):
        # returned sha2 will become the new seed here
        key = generate_hash(key)
        # get otp from seed (i.e. sha2)
        otp = truncate_hash(key)

    if otp == text_box.get():
        label["text"] = "access granted"
    else:
        label["text"] = "access denied"


if __name__ == '__main__':
    w1 = client()
    w2 = server()
    w1.mainloop()
