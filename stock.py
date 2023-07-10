import tkinter as tk
from tkinter import ttk
import requests

API_KEY = "VSM7BAEQTYOAW2IK"

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Market App")
        self.root.geometry("250x200")
        self.root.config(bg="#542C6F")

        # Create input field for symbol
        self.symbol_label = tk.Label(root, text="\nEnter Valid Stock Symbol", font=("Times New Roman", 15, "underline"), bg="#542C6F")
        self.symbol_label.pack()

        # Currencies used in the program
        Symbols = ['ALL','AAC','AADI','AACI','ABNB']

        # Entry (Combobox)
        self.symbol_combobox = ttk.Combobox(root, values=Symbols)
        self.symbol_combobox.pack()

        # Create buttons
        # Get real-time data
        self.realtime_button = tk.Button(root, text="Real-Time Price", command=self.get_realtime_price, bg="#542C6F")
        self.realtime_button.pack()

        # Get historical time data
        self.historical_button = tk.Button(root, text="Historical Prices", command=self.get_historical_prices, bg="#542C6F")
        self.historical_button.pack()

        # Create output field
        self.output_label = tk.Label(root, text="output", fg="#C8C5C4", bg="#542C6F")
        self.output_label.pack()

    def get_realtime_price(self):
        symbol = self.symbol_combobox.get()
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if "Global Quote" in data:
            price = data["Global Quote"]["05. price"]
            self.output_label.config(text=f"Real-Time Price: {price}",font=("Times New Roman", 12, "underline"))
        else:
            self.output_label.config(text="Error retrieving data.\nCheck symbol.")

    def get_historical_prices(self):
        symbol = self.symbol_combobox.get()
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if "Time Series (Daily)" in data:
            # Get the latest 5 days' closing prices
            time_series = data["Time Series (Daily)"]
            # Last 5 dates
            dates = list(time_series.keys())[:5]
            prices = [float(time_series[date]["4. close"]) for date in dates]
            self.output_label.config(text=f"Last 5 Days' Closing Prices: {prices}",font=("Times New Roman", 12, "underline"))
        else:
            self.output_label.config(text="Error retrieving data.\nCheck symbol.")

# Create the Tkinter application window
root = tk.Tk()

# Create an instance of the StockApp class
app = StockApp(root)

# Start the Tkinter event loop
root.mainloop()