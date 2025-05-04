import pytest
import os
import json
from pathlib import Path
import sys

# Asegúrate de que app.py está en el directorio raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa las funciones del archivo app.py
from app import load_tasks, save_tasks, create_task, delete_task, edit_task

# Definimos el archivo de prueba
TEST_FILE = Path("test_tasks.json")

# Preparar un archivo temporal de tareas vacío antes de cada prueba
def setup_function():
    save_tasks([], file_path=TEST_FILE)

# Limpiar el archivo temporal después de cada prueba
def teardown_function():
    if TEST_FILE.exists():
        TEST_FILE.unlink()

# Test para crear una tarea
def test_create_task():
    create_task("Prueba 1", file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert tasks[0]["title"] == "Prueba 1"

# Test para eliminar una tarea
def test_delete_task():
    create_task("Prueba 2", file_path=TEST_FILE)
    delete_task(1, file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert len(tasks) == 0  # Verifica que no queden tareas

# Test para editar una tarea
def test_edit_task():
    create_task("Original", file_path=TEST_FILE)
    edit_task(1, "Modificado", file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert tasks[0]["title"] == "Modificado"  # Verifica que el título haya sido modificado

