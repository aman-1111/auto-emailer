import smtplib
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass  # only for secure terminal version

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_emails():
    sender_email = email_entry.get()
    password = password_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    if not all([sender_email, password, subject, message, contacts_path.get()]):
        messagebox.showerror("Error", "Please fill in all fields and select a contacts file.")
        return

    try:
        with open(contacts_path.get(), newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipient_name = row['name']
                recipient_email = row['email']

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject

                personalized = message.replace("{{name}}", recipient_name)
                msg.attach(MIMEText(personalized, 'plain'))

                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.send_message(msg)
                    print(f"✅ Email sent to {recipient_name}")
        messagebox.showinfo("Success", "All emails sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def select_contacts_file():
    path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    contacts_path.set(path)

# --- GUI Setup ---
root = tk.Tk()
root.title("Auto Email Sender")
root.geometry("500x500")

tk.Label(root, text="Your Gmail:").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="App Password:").pack()
password_entry = tk.Entry(root, show="*", width=50)
password_entry.pack()

tk.Label(root, text="Subject:").pack()
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Message (use {{name}} for personalization):").pack()
message_text = tk.Text(root, height=10, width=60)
message_text.pack()

contacts_path = tk.StringVar()
tk.Button(root, text="📂 Select Contacts CSV", command=select_contacts_file).pack()
tk.Label(root, textvariable=contacts_path).pack()

tk.Button(root, text="📤 Send Emails", command=send_emails, bg="green", fg="white").pack(pady=10)

root.mainloop()
