from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_id = len(tasks) + 1
    tasks[task_id] = {'id': task_id, 'title': data.get('title'), 'description': data.get('description')}
    return jsonify(tasks[task_id]), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values())), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if task_id in tasks:
        tasks[task_id].update({'title': data.get('title'), 'description': data.get('description')})
        return jsonify(tasks[task_id]), 200
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        return jsonify(deleted_task), 200
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
