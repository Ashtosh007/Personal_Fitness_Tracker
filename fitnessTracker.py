import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        login_frame.pack_forget()
        main_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        users[username] = password
        messagebox.showinfo("Registration Successful", "You can now log in")
    else:
        messagebox.showerror("Error", "Please enter a valid username and password")

def get_time(activity, entry):
    try:
        time = float(entry.get())
        return time
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")
        return 0

def calculate_workout():
    yoga_time = get_time("yoga", yoga_entry)
    cardio_time = get_time("cardio", cardio_entry)
    meditation_time = get_time("meditation", meditation_entry)
    
    total_time = yoga_time + cardio_time + meditation_time
    score = min(5, max(1, int((total_time / 60) * 5)))
    result_label.config(text=f"Your fitness score: {score}/5")

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # Convert cm to meters
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obesity"
        bmi_result.config(text=f"BMI: {bmi:.2f} - {status}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid height and weight")

def calculate_water_intake():
    try:
        weight = float(weight_entry.get()) * 2.20462  # Convert kg to pounds
        age = int(age_entry.get())
        if age < 30:
            water = weight * 40
        elif age < 55:
            water = weight * 35
        else:
            water = weight * 30
        water = (water / 28.3) * 0.0295735  # Convert to liters
        water_result.config(text=f"Daily Water Intake: {water:.2f} L")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight and age")

# GUI Setup
root = tk.Tk()
root.title("Fitness Tracker")
root.geometry("400x500")
root.configure(bg="#2C3E50")

users = {}

# Login Frame
login_frame = tk.Frame(root, bg="#2C3E50")
tk.Label(login_frame, text="Username", bg="#2C3E50", fg="white").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()
tk.Label(login_frame, text="Password", bg="#2C3E50", fg="white").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()
tk.Button(login_frame, text="Login", command=validate_login).pack()
tk.Button(login_frame, text="Register", command=register_user).pack()
login_frame.pack()

# Main Frame
main_frame = tk.Frame(root, bg="#2C3E50")

# Workout Section
tk.Label(main_frame, text="Workout Time (mins)", bg="#2C3E50", fg="white", font=("Arial", 12, "bold")).pack()
yoga_entry = tk.Entry(main_frame)
cardio_entry = tk.Entry(main_frame)
meditation_entry = tk.Entry(main_frame)
for widget in [yoga_entry, cardio_entry, meditation_entry]:
    widget.pack()
tk.Button(main_frame, text="Calculate Workout Score", command=calculate_workout).pack()
result_label = tk.Label(main_frame, text="", bg="#2C3E50", fg="white", font=("Arial", 12))
result_label.pack()

# BMI Section
tk.Label(main_frame, text="Height (cm)", bg="#2C3E50", fg="white").pack()
height_entry = tk.Entry(main_frame)
height_entry.pack()
tk.Label(main_frame, text="Weight (kg)", bg="#2C3E50", fg="white").pack()
weight_entry = tk.Entry(main_frame)
weight_entry.pack()
tk.Button(main_frame, text="Calculate BMI", command=calculate_bmi).pack()
bmi_result = tk.Label(main_frame, text="", bg="#2C3E50", fg="white")
bmi_result.pack()

# Water Intake Section
tk.Label(main_frame, text="Age", bg="#2C3E50", fg="white").pack()
age_entry = tk.Entry(main_frame)
age_entry.pack()
tk.Button(main_frame, text="Calculate Water Intake", command=calculate_water_intake).pack()
water_result = tk.Label(main_frame, text="", bg="#2C3E50", fg="white")
water_result.pack()

root.mainloop()