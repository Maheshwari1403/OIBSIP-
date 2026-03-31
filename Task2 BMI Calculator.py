import tkinter as tk
from tkinter import messagebox
import time


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def animate_widget(widget, animation, duration=0.1, repeat=3):
    for _ in range(repeat):
        for style, value in animation:
            widget.configure(**{style: value})
            root.update()
            time.sleep(duration)


def get_weight_range(height):
    return 18.5 * (height ** 2), 24.9 * (height ** 2)


def get_height_range(weight):
    return (weight / 24.9) ** 0.5, (weight / 18.5) ** 0.5


def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return

    if weight_unit_var.get() == "lbs":
        weight *= 0.453592

    if height_unit_var.get() == "feet":
        height *= 0.3048

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    bmi_label.config(text=f"BMI: {bmi:.2f}")
    category_label.config(text=f"Category: {category}")

    w_low, w_high = get_weight_range(height)
    h_low, h_high = get_height_range(weight)

    weight_range_label.config(text=f"Weight Range: {w_low:.2f} - {w_high:.2f} kg")
    height_range_label.config(text=f"Height Range: {h_low:.2f} - {h_high:.2f} m")

    # Animations
    animate_widget(bmi_label, [("bg", "green"), ("bg", "#f0f0f0")])
    animate_widget(category_label, [("bg", "yellow"), ("bg", "#f0f0f0")])
    animate_widget(weight_range_label, [("bg", "orange"), ("bg", "#f0f0f0")])
    animate_widget(height_range_label, [("bg", "red"), ("bg", "#f0f0f0")])
    animate_widget(calculate_button, [("bg", "#4CAF50"), ("bg", "#2E7D32")])


# GUI
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

# Weight
tk.Label(main_frame, text="Weight:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
weight_entry = tk.Entry(main_frame)
weight_entry.grid(row=0, column=1)

weight_unit_var = tk.StringVar(value="kgs")
tk.OptionMenu(main_frame, weight_unit_var, "kgs", "lbs").grid(row=0, column=2)

# Height
tk.Label(main_frame, text="Height:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w")
height_entry = tk.Entry(main_frame)
height_entry.grid(row=1, column=1)

height_unit_var = tk.StringVar(value="meters")
tk.OptionMenu(main_frame, height_unit_var, "meters", "feet").grid(row=1, column=2)

# Button
calculate_button = tk.Button(
    main_frame,
    text="Calculate",
    command=calculate,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 12, "bold")
)
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

# Results
bmi_label = tk.Label(main_frame, text="BMI:", bg="#f0f0f0", font=("Helvetica", 12))
bmi_label.grid(row=3, column=0, sticky="w")

category_label = tk.Label(main_frame, text="Category:", bg="#f0f0f0", font=("Helvetica", 12))
category_label.grid(row=4, column=0, sticky="w")

weight_range_label = tk.Label(main_frame, text="Weight Range:", bg="#f0f0f0", font=("Helvetica", 12))
weight_range_label.grid(row=5, column=0, sticky="w")

height_range_label = tk.Label(main_frame, text="Height Range:", bg="#f0f0f0", font=("Helvetica", 12))
height_range_label.grid(row=6, column=0, sticky="w")

root.mainloop()