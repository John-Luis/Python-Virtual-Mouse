class Task:
    def __init__(self, description, priority):
        self.description = description
        # We normalize priority to lowercase to make filtering easier later
        self.priority = priority.lower()
        self.is_done = False

    def mark_complete(self):
        self.is_done = True

    def __str__(self):
        # Displays a checkmark [X] if done, otherwise [ ]
        status = "X" if self.is_done else " "
        return f"[{status}] {self.description} (Priority: {self.priority.capitalize()})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.tasks.append(new_task)

    def show_all_tasks(self):
        print("\n--- My To-Do List ---")
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)

    def show_by_priority(self, level):
        print(f"\n--- {level.capitalize()} Priority Tasks ---")
        # Filtering logic: only print if the priority matches
        found = False
        for task in self.tasks:
            if task.priority == level.lower():
                print(task)
                found = True
        if not found:
            print(f"No {level} priority tasks.")

    def clear_completed(self):
        # We keep only the tasks that are NOT done
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.is_done]
        print(f"\nCleared {initial_count - len(self.tasks)} completed tasks.")

# --- Using the Task Manager ---
manager = TaskManager()

# Adding tasks based on your current schedule
manager.add_task("Review Physics vectors", "High")
manager.add_task("Fix PyCharm login issue", "Medium")
manager.add_task("Play Assassin's Creed Unity", "Low")

# Mark one as done
manager.tasks[1].mark_complete()

# Filter by high priority
manager.show_by_priority("High")

# Show everything
manager.show_all_tasks()