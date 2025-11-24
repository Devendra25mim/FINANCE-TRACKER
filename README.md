# Finance Tracker (CLI)

## Project Title
Finance Tracker — Simple Command-line Expense Manager

## Overview
A lightweight command-line application to record, view, summarize, and delete personal expenses. It stores expense records in memory (a list of dictionaries) and offers quick, interactive operations via a text menu.

## Features
- Add an expense (date, category, description, amount).
- View all expenses with index numbers.
- Calculate and display total expenses.
- Filter and view expenses by category.
- Delete an expense by index.
- View category-wise totals.

## Technologies / Tools Used
- Python 3.8+ (standard library only)
- Runs on Windows / macOS / Linux terminal

## Installation & Run
1. Ensure Python 3.8 or newer is installed.
2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate
python -m pip install --upgrade pip
```

3. Run the program from the project folder:

```powershell
python main.py
```

No external packages are required.

## Instructions for Testing
Manual interactive tests work well for this small CLI app:
- Start the app: `python main.py`
- Add several expenses using option `1` (include different categories and amounts).
- Use option `2` to verify all entries appear and are numbered correctly.
- Use option `3` to verify the total amount is correct.
- Use option `4` to search for an existing category and a non-existing category.
- Use option `5` to delete entries (try valid and invalid indices).
- Use option `6` to check category totals.
- Use option `7` to exit.

Suggested automated testing (future): refactor logic into functions and add unit tests for add, sum, filter, and delete operations using `pytest`.

## Sample Console Excerpt
```
Welcome to the Finance Tracker : Have Less Expense.

===Menu===
1.Add Expenses
2.View All Expenses
3.View Total Expenses
4.View Expenses by Category
5.Delete Expense
6.View Category Summary
7.Exit
Please enter your choice : 1
Enter the date (DD-MM-YYYY) : 24-11-2025
Enter the category of expenses : Food
Enter the extra details of expenses: Lunch
Enter the amount of expenses : 250
Done bro. Expense added successfully
```

## Notes
- Data is stored in memory; closing the program clears all data. Consider adding JSON/CSV/SQLite persistence as a future enhancement.