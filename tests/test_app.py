import pytest
import os
import json
from pathlib import Path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import load_tasks, save_tasks, create_task, delete_task, edit_task

TEST_FILE = Path("test_tasks.json")

def setup_function():
    # Preparar un archivo temporal de tareas vacío
    save_tasks([], file_path=TEST_FILE)  # Inicializa el archivo con una lista vacía

def teardown_function():
    if TEST_FILE.exists():
        TEST_FILE.unlink()

def test_create_task():
    create_task("Prueba 1", file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    
    # Imprime las tareas cargadas para depuración
    print(f"Tareas cargadas: {tasks}")
    
    assert tasks  # Verifica que la lista no esté vacía
    assert tasks[0]["title"] == "Prueba 1"  # Verifica que la tarea creada sea la correcta

def test_delete_task():
    create_task("Prueba 2", file_path=TEST_FILE)
    delete_task(1, file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert len(tasks) == 0

def test_edit_task():
    create_task("Original", file_path=TEST_FILE)
    edit_task(1, "Modificado", file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert tasks[0]["title"] == "Modificado"
