from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.json.get('task')
    due_date = request.json.get('dueDate')
    if task:
        todos.append({"task": task, "dueDate": due_date})
        return jsonify({'message': 'Todo added!'}), 201
    return jsonify({'error': 'Task is required!'}), 400

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if 0 <= todo_id < len(todos):
        updated_task = request.json.get('task')
        updated_due_date = request.json.get('dueDate')
        if updated_task:
            todos[todo_id] = {"task": updated_task, "dueDate": updated_due_date}
            return jsonify({'message': 'Todo updated!'}), 200
        return jsonify({'error': 'Task is required!'}), 400
    return jsonify({'error': 'Invalid ID!'}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
        return jsonify({'message': 'Todo deleted!'}), 200
    return jsonify({'error': 'Invalid ID!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
