import email
import imaplib
from tkinter import *
from MailOperations import MailOperations
import smtplib
import time
import imaplib
import email
import traceback
import sys
sys.path.append("/path/to/script/file/directory/")


def send_message():
    address_info = str(address.get())
    subject_info = str(subject.get())
    email_body_info = str(email_body.get())

    print(address_info, subject_info, email_body_info)

    sender_email = "sorinsagara@gmail.com"

    sender_password = "Hanna1234"

    # server = smtplib.SMTP('smtp.gmail.com', 587)

    MailOperations(sender_password, sender_email).send_email(subject_info,
                                                             email_body_info,
                                                             address_info)

    address_entry.delete(0, END)
    subject_entry.delete(0, END)
    email_body_entry.delete(0, END)


# fereastra

app = Tk()

app.geometry("800x500")

app.title("Mini aplicația mea în Python!")

heading = Label(text="Mini aplicația mea în Python", bg="#454a52", fg="#c2c6cf", font="10", width="500", height="3")

heading.pack()

address_field = Label(text="Recipient Address :")
subject_field = Label(text="Subject :")
email_body_field = Label(text="Message :")

address_field.place(x=300, y=70)
subject_field.place(x=300, y=140)
email_body_field.place(x=300, y=210)

address = StringVar()
subject = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address, width="30")
subject_entry = Entry(textvariable=subject, width="30")
email_body_entry = Entry(textvariable=email_body, width="30")

address_entry.place(x=300, y=100)
subject_entry.place(x=300, y=180)
email_body_entry.place(x=300, y=260)

button = Button(app, text="Send Message", command=send_message, width="30", height="2", bg="red")

button.place(x=150, y=310)


def openNewWindow():
    import readInbox

btn = Button(app,
             text="Inbox",
             command=openNewWindow, width="30", height="2", bg="gray")
btn.place(x=400, y=310)


mainloop()


