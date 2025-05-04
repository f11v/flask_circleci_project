import json
import os
from app import load_tasks, save_tasks, create_task, delete_task, edit_task, list_tasks

# Helper function to reset tasks file for testing
def reset_tasks_file():
    if os.path.exists('tasks.json'):
        os.remove('tasks.json')

# Test case to create a task
def test_create_task():
    reset_tasks_file()
    create_task("Tarea de prueba")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Tarea de prueba"
    assert tasks[0]["id"] == 1

# Test case to edit a task
def test_edit_task():
    reset_tasks_file()
    create_task("Tarea inicial")
    edit_task(1, "Tarea editada")
    tasks = load_tasks()
    assert tasks[0]["title"] == "Tarea editada"

# Test case to delete a task
def test_delete_task():
    reset_tasks_file()
    create_task("Tarea para eliminar")
    delete_task(1)
    tasks = load_tasks()
    assert len(tasks) == 0

# Test case to list tasks (this just checks that the function doesn't raise errors)
def test_list_tasks():
    reset_tasks_file()
    create_task("Tarea de listado")
    try:
        list_tasks()  # Should print the task to the console
    except Exception as e:
        assert False, f"Error al listar tareas: {e}"

# Test case to check the file saving functionality
def test_save_tasks():
    reset_tasks_file()
    tasks = [{"id": 1, "title": "Tarea guardada"}]
    save_tasks(tasks)
    loaded_tasks = load_tasks()
    assert loaded_tasks == tasks

