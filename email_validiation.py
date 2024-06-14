import re
import tkinter as tk
from tkinter import messagebox

def is_valid_email(email):
    """
    Validate an email address based on Google's guidelines.
    Args:
    email (str): The email address to validate.
    Returns:
    tuple: (bool, str) True if the email address is valid, False and error message otherwise.
    """
    local_part_regex = (
        r'^[a-zA-Z0-9._%+-]+'
    )
    domain_part_regex = (
        r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    try:
        local_part, domain_part = email.rsplit('@', 1)
    except ValueError:
        return False, "Email must contain exactly one '@' symbol."
    
    if not re.match(local_part_regex, local_part):
        return False, "Invalid characters in the local part."
    
    if not re.match(domain_part_regex, domain_part):
        return False, "Invalid characters or structure in the domain part."
    
    if len(local_part) > 64:
        return False, "The local part is too long (maximum 64 characters)."
    
    if len(domain_part) > 255:
        return False, "The domain part is too long (maximum 255 characters)."
    
    if '..' in local_part:
        return False, "The local part cannot have consecutive dots."
    
    if local_part[0] == '.' or local_part[-1] == '.':
        return False, "The local part cannot start or end with a dot."
    
    return True, "Valid email address."

def validate_email():
    email = email_entry.get()
    is_valid, message = is_valid_email(email)
    if is_valid:
        messagebox.showinfo("Result", message)
    else:
        messagebox.showerror("Result", message)

# Create the main window
root = tk.Tk()
root.title("Email Validation Checker")

# Create a label
email_label = tk.Label(root, text="Enter an email address:")
email_label.pack(pady=5)

# Create an entry widget
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

# Create a validate button
validate_button = tk.Button(root, text="Validate", command=validate_email)
validate_button.pack(pady=20)

# Run the application
root.mainloop()
