import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        height_cm = float(entry_height.get())
        weight_kg = float(entry_weight.get())
        age = int(entry_age.get())
        gender = gender_var.get()

        # Validate inputs
        if height_cm <= 0 or weight_kg <= 0 or age <= 0:
            messagebox.showerror("Input Error", "Please enter valid positive numbers!")
            return

        # BMI calculation
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 2)

        # Determine weight status
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 25:
            status = "Normal weight"
        elif 25 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        # Display result
        result_label.config(text=f"Your BMI is: {bmi}\nStatus: {status}")

    except ValueError:
        messagebox.showerror("Input Error", "Please fill all fields correctly!")
        # Function to clear all input fields and result
def clear_fields():
    entry_age.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    gender_var.set("Male")
    result_label.config(text="")


# Create main window
root = tk.Tk()
root.title("BMI Calculator V1.0")
root.geometry("700x700")
root.configure(bg="#e0f7fa")  # Light blue background

# Title Label
title = tk.Label(root, text="BMI (Body Mass Index) Calculator", font=("Cairo", 18, "bold"), bg="#e0f7fa", fg="#00796b")
title.pack(pady=20)

# Age Input
tk.Label(root, text="Age:", font=("Cairo", 14), bg="#e0f7fa").pack()
entry_age = tk.Entry(root, font=("Cairo", 14))
entry_age.pack(pady=5)

# Height Input
tk.Label(root, text="Height (cm):", font=("Cairo", 14), bg="#e0f7fa").pack()
entry_height = tk.Entry(root, font=("Cairo", 14))
entry_height.pack(pady=5)

# Weight Input
tk.Label(root, text="Weight (kg):", font=("Cairo", 14), bg="#e0f7fa").pack()
entry_weight = tk.Entry(root, font=("Cairo", 14))
entry_weight.pack(pady=5)

# Gender Selection
tk.Label(root, text="Gender:", font=("Cairo", 14), bg="#e0f7fa").pack()
gender_var = tk.StringVar(value="Male")
frame_gender = tk.Frame(root, bg="#e0f7fa")
frame_gender.pack(pady=5)

tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male", font=("Cairo", 14), bg="#e0f7fa").pack(side="left", padx=10)
tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female", font=("Cairo", 14), bg="#e0f7fa").pack(side="left", padx=10)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_bmi, font=("Cairo", 16), bg="#00796b", fg="white", width=10)
btn_calculate.pack(pady=20)
# Clear Button
btn_clear = tk.Button(root, text="Clear", command=clear_fields, font=("Cairo", 16), bg="#d32f2f", fg="white", width=10)
btn_clear.pack(pady=10)


# Result Display Label
result_label = tk.Label(root, text="", font=("Cairo", 16), bg="#e0f7fa", fg="#004d40")
result_label.pack(pady=20)

# Footer Label
footer = tk.Label(root, text="Made with ❤️ By Ayyoub", font=("Cairo", 10), bg="#e0f7fa", fg="#009688")
footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
