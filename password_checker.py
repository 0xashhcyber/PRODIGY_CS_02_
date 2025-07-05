import tkinter as tk
import re

# Function to evaluate password strength
def check_password_strength():
    password = entry.get()
    strength = 0
    feedback = ""

    # Strength conditions
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[\W_]", password):  # Special characters
        strength += 1

    # Feedback logic
    if strength <= 2:
        feedback = "Weak"
        result_label.config(fg="red")
    elif strength == 3 or strength == 4:
        feedback = "Medium"
        result_label.config(fg="orange")
    else:
        feedback = "Strong"
        result_label.config(fg="green")

    result_label.config(text=f"Password Strength: {feedback}")

# GUI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
title = tk.Label(root, text="Enter your password", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run the app
root.mainloop()
