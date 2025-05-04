import os
import json
import pytest
from pathlib import Path
from app import load_tasks, save_tasks, create_task, delete_task, edit_task

DATA_FILE = Path("tasks.json")

@pytest.fixture(autouse=True)
def clean_tasks_file():
    # Antes de cada test: asegurarse de que el archivo esté limpio
    if DATA_FILE.exists():
        DATA_FILE.unlink()
    yield
    # Después del test: eliminar el archivo si existe
    if DATA_FILE.exists():
        DATA_FILE.unlink()

def test_create_task():
    create_task("Aprender Python")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Aprender Python"

def test_delete_task():
    create_task("Tarea 1")
    create_task("Tarea 2")
    delete_task(1)
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2
    assert tasks[0]["title"] == "Tarea 2"

def test_edit_task():
    create_task("Viejo título")
    edit_task(1, "Nuevo título")
    tasks = load_tasks()
    assert tasks[0]["title"] == "Nuevo título"

def test_load_empty_tasks():
    tasks = load_tasks()
    assert tasks == []
