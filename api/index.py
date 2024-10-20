from flask import Flask, jsonify, abort

app = Flask(__name__)

# Хранилище данных пользователей с ID
users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]

# Эндпоинт для получения списка пользователей
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Эндпоинт для получения пользователя по ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)  # Возвращаем 404, если пользователь не найден
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)