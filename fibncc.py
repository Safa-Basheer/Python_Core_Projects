import tkinter as tk

def generate_fibonacci_series(n):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series

def display_fibonacci_series():
    try:
        n = int(entry.get())
        fibonacci_series = generate_fibonacci_series(n)
        result_label.config(text=f"Fibonacci Series: {fibonacci_series}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")


root = tk.Tk()
root.title("Fibonacci Series Generator")
root.geometry("600x600")


entry_label = tk.Label(root, text="Enter the number of terms:")
entry_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)


generate_button = tk.Button(root, text="Generate Fibonacci Series", command=display_fibonacci_series)
generate_button.pack(pady=10)


result_label = tk.Label(root, text="Fibonacci Series: -", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
