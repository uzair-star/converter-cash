import requests
import tkinter as tk
from tkinter import ttk

# create the Tkinter window
window = tk.Tk()
window.title("Currency Converter")

# get the currency exchange rates from the internet
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
rates = response.json()['rates']

# create the available currencies list
available_currencies = list(rates.keys())

# create the input widgets
amount_label = ttk.Label(window, text="Enter amount:")
amount_label.pack()
amount_entry = ttk.Entry(window)
amount_entry.pack()

currency_from_label = ttk.Label(window, text="From:")
currency_from_label.pack()
currency_from_menu = ttk.Combobox(window, values=available_currencies, state="readonly")
currency_from_menu.pack()

currency_to_label = ttk.Label(window, text="To:")
currency_to_label.pack()
currency_to_menu = ttk.Combobox(window, values=available_currencies, state="readonly")
currency_to_menu.pack()

result_label = ttk.Label(window, text="")
result_label.pack()

# create the conversion function
def convert_currency():
    try:
        # get the input values
        amount = float(amount_entry.get())
        currency_from = currency_from_menu.get()
        currency_to = currency_to_menu.get()

        # convert the currency
        result = amount * rates[currency_to] / rates[currency_from]

        # update the result label
        result_label.configure(text=f"{amount:.2f} {currency_from} is equal to {result:.2f} {currency_to}")
    except ValueError:
        result_label.configure(text="Invalid input")

# create the conversion button
convert_button = ttk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

# run the Tkinter event loop
window.mainloop()
