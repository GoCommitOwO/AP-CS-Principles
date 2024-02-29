import tkinter as tk
from tkinter import ttk


class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 1 / (0.85),
            'GBP': 1 / (0.73),
            'JPY': 1 / (110.0),
        }

        self.create_widgets()

    def convert_currency(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get().upper()
        to_currency = self.to_currency_var.get().upper()

        result = self.convert(amount, from_currency, to_currency)
        if type(result) == str:
            self.result_var.set(result)
        else:
            self.result_var.set(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            return "Invalid currency code"

        rate = self.exchange_rates[from_currency] / self.exchange_rates[to_currency]
        converted_amount = amount * rate
        return converted_amount

    def create_widgets(self):
        # amount entry
        tk.Label(self.master, text="Amount:").grid(row=0, column=0)
        amount_entry = tk.Entry(self.master, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1)

        # "from" currency combobox
        tk.Label(self.master, text="From Currency:").grid(row=1, column=0)
        from_currency_combobox = ttk.Combobox(self.master, textvariable=self.from_currency_var,
                                              values=list(self.exchange_rates.keys()))
        from_currency_combobox.grid(row=1, column=1)
        from_currency_combobox.set("USD")

        #  "to" currency combobox
        tk.Label(self.master, text="To Currency:").grid(row=2, column=0)
        to_currency_combobox = ttk.Combobox(self.master, textvariable=self.to_currency_var,
                                            values=list(self.exchange_rates.keys()))
        to_currency_combobox.grid(row=2, column=1)
        to_currency_combobox.set("USD")

        # Convert Button
        convert_button = tk.Button(self.master, text="Convert", command=self.convert_currency)
        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(self.master, textvariable=self.result_var)
        result_label.grid(row=4, column=0, columnspan=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
