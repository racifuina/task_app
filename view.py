# view.py
class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("No hay tareas disponibles.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

    @staticmethod
    def display_task(task):
        print(task)
