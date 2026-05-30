from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Tarefas"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index >= len(tasks):
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tasks.pop(index)
    return jsonify({"mensagem": "Tarefa removida"})

if __name__ == "__main__":
    app.run(debug=True)