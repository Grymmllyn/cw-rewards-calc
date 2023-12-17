import tkinter as tk

def calculate_earnings(time, time_unit):
    credits_rate = 50
    aether_rate = 15
    xp_rate = 100

    if time_unit == "Minutes":
        time_minutes = time
    elif time_unit == "Hours":
        time_minutes = time * 60
    elif time_unit == "Weeks":
        time_minutes = time * 60 * 24 * 7
    else:
        raise ValueError("Invalid time unit")

    total_credits = (credits_rate / 10) * time_minutes
    total_aether = (aether_rate / 10) * time_minutes
    total_xp = (xp_rate / 10) * time_minutes

    return total_credits, total_aether, total_xp

def calculate_and_display():
    try:
        time = float(entry_time.get())
        time_unit = unit_var.get()
        total_credits, total_aether, total_xp = calculate_earnings(time, time_unit)

        result_text = (
            f"Total Credits: {total_credits} credits\n"
            f"Total Aether: {total_aether} Aether\n"
            f"Total XP: {total_xp} XP"
        )
        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# GUI setup
window = tk.Tk()
window.title("Earnings Calculator")

# Input fields
label_time = tk.Label(window, text="Enter the time:")
label_time.pack()

entry_time = tk.Entry(window)
entry_time.pack()

# Time unit dropdown menu
unit_var = tk.StringVar()
unit_var.set("Minutes")
unit_options = ["Minutes", "Hours", "Weeks"]
unit_menu = tk.OptionMenu(window, unit_var, *unit_options)
unit_menu.pack()

# Button to calculate and display earnings
calculate_button = tk.Button(window, text="Calculate Earnings", command=calculate_and_display)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
