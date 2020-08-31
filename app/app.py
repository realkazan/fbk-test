from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

db = psycopg2.connect(
    database="postgres",
    user="postgres",
    host="postgres",
    port="5432"
)


@app.route('/', methods=['GET'])
def base():
    return jsonify({'route': 'empty'}), 200


@app.route('/item', methods=['POST'])
def post_items():
    data = request.get_json()
    if 'name' in data:
        cursor = db.cursor()
        cursor.execute("INSERT INTO items (name) VALUES (%s) RETURNING id;", (data['name'], ))
        insert_id = cursor.fetchone()[0]
        db.commit()
        cursor.close()
        return jsonify({"id": insert_id}), 201
    return jsonify({'error': '`name` parameter not set'}), 400


@app.route('/item/<item_id>', methods=['GET'])
def get_items(item_id):
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM items WHERE id = %s;", (item_id, ))
    result = cursor.fetchone()
    cursor.close()
    if result and len(result) > 0:
        item = {
            'id': result[0],
            'name': result[1]
        }
        return jsonify(item), 200
    return jsonify({'error': 'item not found'}), 404


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        debug=False
    )
