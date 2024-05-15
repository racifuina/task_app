from model import TaskModel
from view import TaskView
from controller import TaskController

# main.py

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        print("\n1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Marcar Tarea como Completada")
        print("4. Mostrar Tareas")
        print("5. Salir")
        choice = input("Ingrese su elección: ")

        if choice == '1':
            description = input("Ingrese la descripción de la tarea: ")
            controller.add_task(description)
        elif choice == '2':
            index = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
            controller.remove_task(index)
        elif choice == '3':
            index = int(input("Ingrese el índice de la tarea a marcar como completada: ")) - 1
            controller.mark_task_completed(index)
        elif choice == '4':
            controller.show_tasks()
        elif choice == '5':
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
