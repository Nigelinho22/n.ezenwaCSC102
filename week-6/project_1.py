import tkinter as tk
from tkinter import messagebox

# Function to calculate delivery cost
def calculate_cost():
    location = location_entry.get().strip().lower()
    try:
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for weight.")
        return

    # Check location and weight to decide the cost
    if location == "ibeju-lekki":
        if weight >= 10:
            cost = 5000
        else:
            cost = 3500
    elif location == "epe":
        if weight >= 10:
            cost = 10000
        else:
            cost = 5000
    else:
        messagebox.showerror("Invalid Location", "We only deliver to Ibeju-Lekki and Epe.")
        return

    # Show the result
    messagebox.showinfo("Delivery Cost", f"The delivery cost is ₦{cost:,}")

# Set up the GUI
root = tk.Tk()
root.title("Simi Services Delivery Cost")
root.geometry("350x200")

tk.Label(root, text="Enter Delivery Location (Ibeju-Lekki or Epe):").pack(pady=30)
location_entry = tk.Entry(root, width=30)
location_entry.pack()

tk.Label(root, text="Enter Package Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root, width=30)
weight_entry.pack()

tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=15)

root.mainloop()
