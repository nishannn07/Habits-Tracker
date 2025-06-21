# 🧠 Habits Tracker (CLI)

A simple command-line Habit Tracker built with Python to help track daily habits, maintain streaks, and persist data between runs.

## 🔧 Features

- Add, remove, and list habits
- Mark habits as done (with optional date)
- View current streaks
- Save and load data via JSON file
- Merge two trackers with `+` operator

## 🧩 Structure

- `habits.py` – Core logic: `Habit`, `HabitTracker`, and `PersistenceError`
- `cli.py` – Interactive menu for tracking
- `habits.json` – Example file with pre-filled data

## 🗃️ Concepts Used

- OOP (Classes, Encapsulation, Operator Overloading)
- File I/O with JSON
- Exception Handling (`try/except`, custom exceptions)
- CLI Menus with input validation

## 💻 How to Run

```bash
python cli.py
