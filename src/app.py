from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ { "id": 69,"label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['PUT'])
def modify_todo(id):
    request_body = request.json
    for elm in todos:
        if elm['id'] == id:
            elm['done'] = request_body['done']
    return jsonify(request_body)

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    pop_value = todos.pop(index)
    return jsonify(f"{todos}, You just deleted {pop_value}")






# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)