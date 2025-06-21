import json
class Habit:
    def __init__(self,name:str,description:str):
        self.name = name
        self.description = description
        self.__history = []
    def mark_done(self,date:str) -> None:
        self.__history.append(date)
    def __str__(self) -> str:
        return "Habit(name={}, description={}, history={})".format(self.name,self.description,self.__history)
    def __repr__(self) -> str:
        return "Habit(name={}, description={}, history={})".format(self.name,self.description,self.__history)

class PersistenceError(Exception):
    """Raised when saving/loading habits fails."""
    pass

class HabitTracker:
    date_format="%Y-%m-%d"
    def __init__(self):
        self.habits={}
    def add_habit(self,name:str,desc:str)->None:
        if name not in self.habits:
            self.habits[name]=Habit(name, desc)
        else:
            print("Habit already exists.")
    def remove_habit(self,name:str)->None:
        if name in self.habits:
            del self.habits[name]
        else:
            print("Habit not found.")
    def mark_done(self,name:str,date:str="today")->None:
        if name in self.habits:
            self.habits[name].mark_done(date)
        else:
            print("Habit not found.")
    def list_habits(self)->list:
        return list(self.habits.values())
    def report(self)->dict:
        return {name: habit.streak() for name, habit in self.habits.items()}
    def save(self, filename:str) -> None:
        try:
            with open(filename, 'w') as f:
                json.dump({name: habit.__dict__ for name, habit in self.habits.items()}, f)
        except OSError as e:
            raise PersistenceError("Failed")
    def load(self, filename:str) -> None:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for name, habit_data in data.items():
                    habit = Habit(name, habit_data['description'])
                    habit._Habit__history = habit_data['_Habit__history']
                    self.habits[name] = habit
        except FileNotFoundError:
            self.habits = {}
        except json.JSONDecodeError:
            raise PersistenceError("Failed")
    def __add__(self, other:'HabitTracker')->'HabitTracker':
        new_tracker=HabitTracker()
        for habit in self.habits.values():
            new_tracker.add_habit(habit.name, habit.description)
        for other_habit in other.habits.values():
            new_tracker.add_habit(other_habit.name,other_habit.description)
        return new_tracker

