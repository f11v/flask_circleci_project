import sys
import json
from pathlib import Path

# Definimos el archivo por defecto donde se guardarán las tareas
DEFAULT_DATA_FILE = Path("tasks.json")

# Función para cargar las tareas desde el archivo
def load_tasks(file_path=DEFAULT_DATA_FILE):
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return []  # Si no existe el archivo o está vacío, retornamos una lista vacía

# Función para guardar las tareas en el archivo
def save_tasks(tasks, file_path=DEFAULT_DATA_FILE):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)  # Guardamos las tareas en formato JSON

# Función para crear una tarea
def create_task(title, file_path=DEFAULT_DATA_FILE):
    tasks = load_tasks(file_path)
    task = {"id": len(tasks) + 1, "title": title}  # Asignamos un ID a la nueva tarea
    tasks.append(task)  # Agregamos la tarea a la lista
    save_tasks(tasks, file_path)  # Guardamos la lista actualizada de tareas
    print(f"Tarea creada: {task}")

# Función para eliminar una tarea
def delete_task(task_id, file_path=DEFAULT_DATA_FILE):
    tasks = load_tasks(file_path)
    tasks = [t for t in tasks if t["id"] != task_id]  # Filtramos la tarea a eliminar
    save_tasks(tasks, file_path)  # Guardamos la lista sin la tarea eliminada
    print(f"Tarea con ID {task_id} eliminada.")

# Función para editar una tarea
def edit_task(task_id, new_title, file_path=DEFAULT_DATA_FILE):
    tasks = load_tasks(file_path)
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = new_title  # Actualizamos el título de la tarea
            print(f"Tarea actualizada: {t}")
            break
    else:
        print(f"No se encontró tarea con ID {task_id}")  # Si no se encuentra la tarea
    save_tasks(tasks, file_path)  # Guardamos la lista con la tarea actualizada

# Función para listar todas las tareas
def list_tasks(file_path=DEFAULT_DATA_FILE):
    tasks = load_tasks(file_path)
    for t in tasks:
        print(f"{t['id']}: {t['title']}")  # Mostramos el ID y título de cada tarea

# Función principal para manejar los comandos de línea de comandos
def main():
    if len(sys.argv) < 2:
        print("Comandos: create <titulo> | delete <id> | edit <id> <nuevo titulo> | list")
        return

    command = sys.argv[1]

    if command == "create" and len(sys.argv) == 3:
        create_task(sys.argv[2])  # Crear tarea con el título proporcionado
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))  # Eliminar tarea por ID
    elif command == "edit" and len(sys.argv) == 4:
        edit_task(int(sys.argv[2]), sys.argv[3])  # Editar tarea por ID y nuevo título
    elif command == "list":
        list_tasks()  # Listar todas las tareas
    else:
        print("Comando inválido o argumentos incorrectos.")

# Ejecutamos la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
