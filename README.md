# CodeAlpha_Stock_PortFolio_Tracker
# 📈 Stock Portfolio Tracker

A simple and interactive Python script that helps users track their stock investments, compute total portfolio value, and export the results to `.txt` and `.csv` files for reporting and analysis.

---

## 🚀 Features

- ✅ Predefined stock prices for popular companies (AAPL, TSLA, GOOGL, AMZN, INFY)
- 🔄 Interactive input loop for adding multiple stock purchases dynamically
- 💼 Real-time investment summary with total portfolio value
- 📝 Export to TXT and CSV formats
- ❌ Input validation for invalid stock names and quantities

---

## 💻 Requirements

- Python 3.6 or above
- No additional libraries required (uses built-in `csv` module)

---

## 🧑‍💻 How to Use

1. Run the script:
   ```bash
   python stock_portfolio_tracker.py
   ```

2. Follow the prompts:
   - Enter valid stock name from the list
   - Provide quantity purchased
   - Type `done` to finish

3. View the investment summary in the terminal

4. Check the output files:
   - `stock_portfolio_summary.txt`
   - `stock_portfolio_summary.csv`

---

## 📁 Output Example

### Console:
```
AAPL: 5 shares × ₹180 = ₹900
TSLA: 2 shares × ₹250 = ₹500
GOOGL: 3 shares × ₹200 = ₹600

💰 Total Investment: ₹2000
```

### CSV:
```
Stock Name, Quantity, Price, Value
AAPL, 5, 180, 900
TSLA, 2, 250, 500
GOOGL, 3, 200, 600

,,Total,2000
```

---

## 📌 Notes

- Stock prices are hardcoded and do not reflect real
