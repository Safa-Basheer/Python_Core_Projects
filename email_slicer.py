
import tkinter as tk

def slice_email():
    email = email_entry.get()
    username, domain = email.split('@')
    result_label.config(text=f"Username: {username}\nDomain: {domain}")

root = tk.Tk()
root.title("Email Slicer")
root.geometry("480x440")
root.resizable(width=False,height=False)
email_label = tk.Label(root, text="Enter your email address:")
email_entry = tk.Entry(root)

slice_button = tk.Button(root, text="Slice", command=slice_email)

result_label = tk.Label(root, text="")

email_label.pack()
email_entry.pack()
slice_button.pack()
result_label.pack()

root.mainloop()

      