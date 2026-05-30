import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.app import app, tasks


def test_home():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_create_task():

    tasks.clear()

    client = app.test_client()

    response = client.post(
        "/tasks",
        json={"titulo": "Estudar Engenharia de Software"}
    )

    assert response.status_code == 201


def test_update_task():

    tasks.clear()

    tasks.append({"titulo": "Tarefa antiga"})

    client = app.test_client()

    response = client.put(
        "/tasks/0",
        json={"titulo": "Tarefa atualizada"}
    )

    assert response.status_code == 200


def test_delete_task():

    tasks.clear()

    tasks.append({"titulo": "Excluir"})

    client = app.test_client()

    response = client.delete("/tasks/0")

    assert response.status_code == 200