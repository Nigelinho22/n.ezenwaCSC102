import tkinter as tk
from tkinter import messagebox

# Lists to hold admitted and not-admitted candidates
admitted = []
not_admitted = []

# Function to check admission
def check_admission():
    name = name_entry.get()
    dept = dept_entry.get().lower()
    try:
        jamb = int(jamb_entry.get())
        credits = int(credits_entry.get())
        interview_passed = interview_var.get()
    except ValueError:
        messagebox.showerror("Input Error", "JAMB and credits must be numbers.")
        return

    if dept == "computer science":
        if jamb >= 250 and credits >= 5 and interview_passed:
            admitted.append(name)
            messagebox.showinfo("Result", f"{name} has been ADMITTED into Computer Science.")
        else:
            not_admitted.append(name)
            messagebox.showinfo("Result", f"{name} has NOT been admitted into Computer Science.")
    elif dept == "mass communication":
        if jamb >= 230 and credits >= 5 and interview_passed:
            admitted.append(name)
            messagebox.showinfo("Result", f"{name} has been ADMITTED into Mass Communication.")
        else:
            not_admitted.append(name)
            messagebox.showinfo("Result", f"{name} has NOT been admitted into Mass Communication.")
    else:
        messagebox.showerror("Input Error", "Invalid department name.")
        return

# GUI setup
root = tk.Tk()
root.title("Admission Checker")
root.geometry("350x350")

tk.Label(root, text="Enter Full Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Department (computer science or mass communication):").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

tk.Label(root, text="JAMB Score:").pack()
jamb_entry = tk.Entry(root)
jamb_entry.pack()

tk.Label(root, text="Number of Credits in 5 Key Subjects:").pack()
credits_entry = tk.Entry(root)
credits_entry.pack()

tk.Label(root, text="Did you pass the interview?").pack()
interview_var = tk.BooleanVar()
tk.Checkbutton(root, text="Yes", variable=interview_var).pack()

tk.Button(root, text="Check Admission", command=check_admission).pack(pady=10)

# Run the application
root.mainloop()
