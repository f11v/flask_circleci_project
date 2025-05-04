import pytest
from pathlib import Path
from app import load_tasks, save_tasks, create_task, delete_task, edit_task

# Ruta del archivo de tareas de prueba
TEST_FILE = Path("/tmp/tasks_test.json")

@pytest.fixture(scope="function")
def setup_file():
    """Inicializa un archivo vacío de tareas antes de cada prueba y lo limpia después."""
    # Preparar un archivo temporal de tareas vacío antes de cada prueba
    save_tasks([], file_path=TEST_FILE)
    yield  # Ejecuta la prueba
    # Limpiar el archivo de prueba después de cada prueba
    if TEST_FILE.exists():
        TEST_FILE.unlink()

def test_create_task(setup_file):
    """Prueba la creación de una tarea."""
    create_task("Prueba 1", file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    
    # Imprime las tareas cargadas para depuración
    print(f"Tareas cargadas: {tasks}")
    
    assert tasks  # Verifica que la lista no esté vacía
    assert tasks[0]["title"] == "Prueba 1"  # Verifica que la tarea creada sea la correcta

def test_delete_task(setup_file):
    """Prueba la eliminación de una tarea."""
    create_task("Prueba 2", file_path=TEST_FILE)
    delete_task(1, file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert len(tasks) == 0  # Verifica que la lista de tareas esté vacía

def test_edit_task(setup_file):
    """Prueba la edición de una tarea."""
    create_task("Original", file_path=TEST_FILE)
    edit_task(1, "Modificado", file_path=TEST_FILE)
    tasks = load_tasks(file_path=TEST_FILE)
    assert tasks[0]["title"] == "Modificado"  # Verifica que la tarea haya sido modificada correctamente
