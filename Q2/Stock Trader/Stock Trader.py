import tkinter as tk
from tkinter import messagebox, simpledialog
from random import uniform
from PIL import Image, ImageTk

class Stock:
    def __init__(self, name, initial_price):
        self.name = name
        self.starting_price = initial_price
        self.current_price = initial_price
        self.quantity = 0

def generate_stock_price(stock):
    # Simulate random stock price movement
    price_change = uniform(-1, 1)  # Adjust the range as needed
    stock.current_price += price_change
    stock.current_price = max(1, stock.current_price)  # Ensure price doesn't go below 1
    # TODO: Add more logic here based on the current price of the stock
    # TODO: Make different patterns that the stock price can follow (e.g. slow rise, slow fall, sudden spike, chaotic, etc.)

def simulate_stock_market(stocks):
    for stock in stocks:
        generate_stock_price(stock)

class StockTradingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Trading Simulator")

        self.balance = 100  # Starting balance
        self.stocks = [
            Stock("Sus-Co.", 50),
            Stock("Conductors-Corp", 30),
            # Add more stocks as needed
        ]

        self.create_widgets()

    def create_widgets(self):
        # Create GUI components

        # Left Box for current stock prices and buying
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, padx=10)

        self.current_prices_label = tk.Label(self.left_frame, text="Current Stock Prices")
        self.current_prices_label.pack()

        # Display stock buttons with images
        for stock in self.stocks:
            stock_button = tk.Button(
                self.left_frame,
                text=f"{stock.name}\n${stock.current_price:.2f}",
                compound=tk.TOP,
                command=lambda s=stock: self.buy_stock(s),
            )
            stock_button.image = self.load_stock_image(stock.name)
            stock_button.config(image=stock_button.image, width=100, height=100)
            stock_button.pack(pady=5)

        # Right Box for owned stocks and selling information
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side=tk.RIGHT, padx=10)

        self.owned_stocks_label = tk.Label(self.right_frame, text="Owned Stocks")
        self.owned_stocks_label.pack()

        self.owned_stocks_text = tk.Text(self.right_frame, height=10, width=30, wrap=tk.NONE)
        self.owned_stocks_text.pack()

        self.sell_button = tk.Button(self.right_frame, text="Sell", command=self.sell_stock)
        self.sell_button.pack(pady=5)

        self.update_button = tk.Button(self.master, text="Update Prices", command=self.update_stock_prices)
        self.update_button.pack(pady=10)

        self.update_stock_prices()

    def update_stock_prices(self):
        simulate_stock_market(self.stocks)
        self.update_stock_buttons()

    def update_owned_stocks_display(self):
        self.owned_stocks_text.delete("1.0", tk.END)
        for stock in self.stocks:
            if stock.quantity > 0:
                total_cost = stock.starting_price * stock.quantity
                potential_profit = (stock.current_price - stock.starting_price) * stock.quantity
                self.owned_stocks_text.insert(
                    tk.END,
                    f"{stock.name}: {stock.quantity} shares, Total Cost: ${total_cost:.2f}, "
                    f"Potential Profit: ${potential_profit:.2f}\n"
                )

    def load_stock_image(self, stock_name):
        try:
            image_path = f"{stock_name.lower()}.png"
            img = Image.open(image_path)
            img = img.resize((100, 100), Image.ANTIALIAS)
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            # If the image file is not found, use a default image
            return ImageTk.PhotoImage(Image.new("RGB", (100, 100), "white"))

    def update_stock_buttons(self):
        for stock in self.stocks:
            for widget in self.left_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text").startswith(stock.name):
                    widget.config(text=f"{stock.name}\n${stock.current_price:.2f}")

    def buy_stock(self, stock):
        try:
            quantity = int(self.ask_for_quantity())
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")
        except ValueError as e:
            messagebox.showinfo("Error", str(e))
            return

        total_cost = stock.current_price * quantity
        if total_cost > self.balance:
            messagebox.showinfo("Error", "Insufficient funds.")
            return

        response = messagebox.askyesno(
            "Confirm Purchase",
            f"Buy {quantity} shares of {stock.name} for ${total_cost:.2f}?",
        )

        if response:
            stock.quantity += quantity
            self.balance -= total_cost
            messagebox.showinfo("Success", "Purchase successful!")
            self.update_owned_stocks_display()

    def sell_stock(self):
        selected_index = self.owned_stocks_text.index(tk.SEL_FIRST)
        if not selected_index:
            messagebox.showinfo("Error", "Please select a stock to sell.")
            return

        stock = self.stocks[int(selected_index[0]) - 1]
        try:
            quantity = int(self.ask_for_quantity())
            if quantity <= 0 or quantity > stock.quantity:
                raise ValueError("Invalid quantity.")
        except ValueError as e:
            messagebox.showinfo("Error", str(e))
            return

        total_profit = stock.current_price * quantity
        response = messagebox.askyesno(
            "Confirm Sale",
            f"Sell {quantity} shares of {stock.name} for ${total_profit:.2f}?",
        )

        if response:
            stock.quantity -= quantity
            self.balance += total_profit
            messagebox.showinfo("Success", "Sale successful!")
            self.update_owned_stocks_display()

    def ask_for_quantity(self):
        return simpledialog.askinteger("Quantity", "Enter quantity:")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockTradingApp(root)
    root.mainloop()
