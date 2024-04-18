import tkinter as tk
from tkinter import ttk

class SimpleCurrencyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Simple Currency Converter")

        
        self.conversion_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 110.0,
            'INR':83.13,
            
        }

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = tk.Label(master, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_currency_combobox = ttk.Combobox(master, values=list(self.conversion_rates.keys()))
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency_combobox.set("USD")

        self.to_currency_label = tk.Label(master, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_currency_combobox = ttk.Combobox(master, values=list(self.conversion_rates.keys()))
        self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.to_currency_combobox.set("EUR")

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, state="readonly", textvariable=self.result_var)
        self.result_entry.grid(row=3, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()

            if from_currency == to_currency:
                result = amount
            else:
                conversion_rate = self.conversion_rates[to_currency] / self.conversion_rates[from_currency]
                result = round(amount * conversion_rate, 2)

            self.result_var.set(f"{amount} {from_currency} = {result} {to_currency}")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCurrencyConverter(root)
    root.mainloop()