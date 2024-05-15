from model import Task, TaskModel
from view import TaskView

# controller.py

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, description):
        task = Task(description)
        self.model.add_task(task)

    def remove_task(self, index):
        try:
            task = self.model.get_tasks()[index]
            self.model.remove_task(task)
        except IndexError:
            print("Índice de tarea inválido.")

    def mark_task_completed(self, index):
        try:
            task = self.model.get_tasks()[index]
            task.mark_completed()
        except IndexError:
            print("Índice de tarea inválido.")

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)
