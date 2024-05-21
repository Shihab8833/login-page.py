import tkinter as tk
import webbrowser

def login():
    # Get the email and password entered by the user
    email = email_entry.get()
    password = password_entry.get()

    # Display the email and password in the terminal
    print("Email:", email)
    print("Password:", password)

    # Change the text color of email and password labels to red
    email_label.config(foreground="red")
    password_label.config(foreground="red")

    # Open a web browser to the specified link
    webbrowser.open("https://www.google.co.uk")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")  # Set window size

# Create email label and entry
email_label = tk.Label(root, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a hyperlink for password recovery
password_recovery_link = "https://www.google.co.uk/"
hyperlink = tk.Label(root, text="Forgot password?", fg="blue", cursor="hand2")
hyperlink.grid(row=3, column=0, columnspan=2)
hyperlink.bind("<Button-1>", lambda event: webbrowser.open_new(password_recovery_link))

# Run the Tkinter event loop
root.mainloop()
