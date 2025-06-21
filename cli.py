# 3. Command-Line Interface (CLI)
# 1. Display menu:
# 1. Add new habit
# 2. Remove habit
# 3. Mark habit done
# 4. List all habits
# 5. Show streak report
# 6. Save & Exit
import habits as mp
def display_menu():
    print("Habit Tracker")
    print("1. Add new habit")
    print("2. Remove habit")
    print("3. Mark habit done")
    print("4. List all habits")
    print("5. Show streak report")
    print("6. Save & Exit")
tracker=mp.HabitTracker()
while True:
    display_menu()
    choice=input("Choose an option: ")
    if choice == "1":
        name=input("Habit name: ")
        desc=input("Habit description: ")
        tracker.add_habit(name, desc)
    elif choice =="2":   
        name=input("Habit name to remove: ")
        tracker.remove_habit(name)
    elif choice=="3":
        name=input("Habit name to mark done: ")
        date=input("Date: ")
        tracker.mark_done(name, date)
    elif choice=="4":
        habits=tracker.list_habits()
        for habit in habits:
            print(habit)
    elif choice=="5":
        report=tracker.report()
        for name, streak in report.items():
            print(name,"Streak:",streak)
    elif choice=="6":
        try:
            tracker.save("habits.json")
        except mp.PersistenceError:
            print("Failed to save habits.")
        break
    else:
        print("Invalid choice.")