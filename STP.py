import csv

# 🎯 Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 200,
    "AMZN": 220,
    "INFY": 160
}

portfolio = {}
total_investment = 0

print("\n📈 Welcome to Stock Portfolio Tracker\n")
print("Available Stocks:", ', '.join(stock_prices.keys()))

# 🔄 Dynamic input loop
while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Invalid stock name. Choose from listed options.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("⚠ Quantity must be greater than zero.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠ Please enter a valid number.")

# 🧾 Display investment summary
print("\n💼 Your Portfolio Summary:\n")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment: ₹{total_investment}")

# 📝 Save to TXT file
with open("stock_portfolio_summary.txt", "w") as txt_file:
    txt_file.write("Stock Portfolio Summary:\n\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        txt_file.write(f"{stock}: {quantity} shares x ₹{price} = ₹{value}\n")
    txt_file.write(f"\nTotal Investment: ₹{total_investment}")

# 📊 Save to CSV file
with open("stock_portfolio_summary.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Stock Name", "Quantity", "Price", "Value"])
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        writer.writerow([stock, quantity, price, value])
    writer.writerow([])  # spacing
    writer.writerow(["", "", "Total", total_investment])

print("\n📁 Files 'stock_portfolio_summary.txt' and 'stock_portfolio_summary.csv' saved successfully.")
