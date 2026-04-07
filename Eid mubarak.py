import tkinter as tk

# Create window
root = tk.Tk()
root.title("Greeting")
root.geometry("400x250")
root.config(bg="lightyellow")

# Function
def show_message():
    label.config(text="🌙 Eid Mubarak! 🌙")

# Heading
title_label = tk.Label(
    root,
    text="Greeting App",
    font=("Arial", 18, "bold"),
    bg="lightyellow",
    fg="darkgreen"
)
title_label.pack(pady=20)

# Button
btn = tk.Button(
    root,
    text="Click Here",
    font=("Arial", 14),
    bg="green",
    fg="white",
    command=show_message
)
btn.pack(pady=10)

# Message label
label = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold"),
    bg="lightyellow",
    fg="purple"

)
label.pack(pady=20)

# Run window
root.mainloop()
