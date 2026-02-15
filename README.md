# Incomes_expences
This is incomes and expenses python project
# Income & Expense Tracker (Python CLI Application)

## Description
This is a Python command-line application that allows users to track income and expenses, generate monthly summaries, and export formatted financial reports. The program stores financial records in JSON files, validates user input, and produces detailed monthly reports automatically.

This project demonstrates practical Python programming skills including file handling, data processing, user input validation, and report automation.

---

## Features
- Add income records (source, amount, date, description)
- Add expense records (category, amount, date, description)
- View monthly financial summary
- View expense breakdown by category
- Export monthly financial report as a formatted text file
- Input validation and error handling
- Persistent data storage using JSON files

---

## Technologies Used
- Python 3
- JSON file handling
- datetime module
- Command Line Interface (CLI)

---

## How It Works

### Menu Options

### Add Income
- The user enters income source, amount, date (YYYY-MM), and description.
- Data is stored in `incomes.json`.

### Add Expense
- The user enters category, amount, date (YYYY-MM), and description.
- Data is stored in `expenses1.json`.

### Monthly Summary
- Displays total income, total expenses, and savings.

### Category Report
- Displays expense totals by category for a selected month.

### Export Report
- Generates a formatted monthly report file.
- Example filename: `report_2026_02.txt`

---

## Example Output (Exported Report)
=============================
#MONTHLY FINANCIAL REPORT
 #       2026-02
-Total Income : $ 3500.0
-Total Expenses : $ 2100.0

-Savings : $ 1400.0

-=======Expense Breakdown=======
-Food : $ 600.0
-Rent : $1200.0
-Transport : $ 300.0

-=========Income Sources========
-Salary : $3000.0
-Freelance : $ 500.0

-=============================
-Generated on : 2026-02-15 18:44:10

---

## Project Structure
income_expense_tracker.py
incomes.json
expenses1.json
report_YYYY_MM.txt

---

## How to Run
1. Make sure Python 3 is installed.
2. Open terminal or command prompt.
3. Run:
```bash
python Income_Expense_Tracker.py
```
---

## Author
Alaa Abdulrahman – Python Developer
GitHub: https://github.com/alaaabdul11

