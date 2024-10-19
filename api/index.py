from flask import Flask, jsonify

app = Flask(__name__)

# Хранилище данных пользователей
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Эндпоинт для получения списка пользователей
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)