import os
import json
from pathlib import Path

# Cambia la ruta del archivo para usar una ruta absoluta en el entorno de pruebas
TEST_FILE = Path("/tmp/tasks_test.json")  # Ruta absoluta para el archivo de prueba

def load_tasks(file_path=TEST_FILE):
    print(f"Cargando tareas desde: {file_path}")  # Impresión de depuración
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks, file_path=TEST_FILE):
    print(f"Guardando tareas en: {file_path}")  # Impresión de depuración
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)

def create_task(title, file_path=TEST_FILE):
    tasks = load_tasks(file_path)
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    save_tasks(tasks, file_path)
    print(f"Tarea creada: {task}")

def delete_task(task_id, file_path=TEST_FILE):
    tasks = load_tasks(file_path)
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks, file_path)
    print(f"Tarea con ID {task_id} eliminada.")

def edit_task(task_id, new_title, file_path=TEST_FILE):
    tasks = load_tasks(file_path)
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = new_title
            print(f"Tarea actualizada: {t}")
            break
    else:
        print(f"No se encontró tarea con ID {task_id}")
    save_tasks(tasks, file_path)

def list_tasks(file_path=TEST_FILE):
    tasks = load_tasks(file_path)
    for t in tasks:
        print(f"{t['id']}: {t['title']}")

def main():
    import sys

    if len(sys.argv) < 2:
        print("Comandos: create <titulo> | delete <id> | edit <id> <nuevo titulo> | list")
        return

    command = sys.argv[1]

    if command == "create" and len(sys.argv) == 3:
        create_task(sys.argv[2])
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    elif command == "edit" and len(sys.argv) == 4:
        edit_task(int(sys.argv[2]), sys.argv[3])
    elif command == "list":
        list_tasks()
    else:
        print("Comando inválido o argumentos incorrectos.")

if __name__ == "__main__":
    main()
