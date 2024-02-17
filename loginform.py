import tkinter as tk
import ttkbootstrap as ttk #to make a style
import re
import socket

def send():
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            _, domain = email.split('@')
            try:
                socket.getaddrinfo(domain, 25)
                return True
            except socket.gaierror:
                return False
        else:
            return False
    
    def is_valid_password(password):
        if len(password) < 8:
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[^a-zA-Z0-9]', password):
            return False
        common_patterns = [
            'password',
            '123456',
            'qwerty',
            'abcdef',
        ]
        for pattern in common_patterns:
            if pattern in password.lower():
                return False
        return True

    email = username.get()
    if is_valid_email(email):
        mail_validity = True
    else:
        mail_validity = False

    PW = password.get()
    if is_valid_password(PW):
        password_validity = True
    else:
        password_validity= False

    if mail_validity and password_validity:
        username_text = username.get()
        password_text = password.get()
        output_string.set('Welcome Back')
        print("Username:", username_text)
        print("Password:", password_text)
    else:
        output_message = ""
        if not mail_validity:
            output_message += "Invalid email.\n"
        if not password_validity:
            output_message += "Invalid password.\n"
        output_string.set(output_message)
  

# Make a window
window = ttk.Window(themename='solar')
window.title('Window-6X')
window.geometry('600x600')

# title
title_label = ttk.Label(master = window, text = 'Fire Code', font = 'SourceCodePro 24 bold')
title_label.pack() # make txt apear on window

# input
input_frame = ttk.Frame()
username = ttk.Entry(master=input_frame)
username.config(width=30)
password = ttk.Entry(master=input_frame, show='*')
password.config(width=30)
button = ttk.Button(master = input_frame, text = 'Submit', command= send)
username.pack(pady= 10) # insert username on input_frame
password.pack(pady= 10) # insert password on input_frame
button.pack(pady= 10) # insert button on input_frame
input_frame.pack(pady= 50) # insert input_frame on main window


# output
output_string = tk.StringVar() # to make string change on output
output_label = ttk.Label(master=window,font='SourceCodePro 10 ', textvariable=output_string)
output_label.pack()



# run
window.mainloop()

