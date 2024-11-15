from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Путь к базе данных
DATABASE = 'mydatabase.db'

# Создание таблицы (выполняется один раз)
def create_table():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      description TEXT
    )
  ''')
  conn.commit()
  conn.close()

create_table()


# Маршрут для получения данных
@app.route('/api/items')
def get_items():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM items")
  items = cursor.fetchall()
  conn.close()

  # Преобразование результатов в JSON
  item_list = []
  for item in items:
    item_list.append({'id': item[0], 'name': item[1], 'description': item[2]})

  return jsonify(items=item_list)

if __name__ == '__main__':
  app.run(debug=True) # debug=True только для разработки! Удалите это в продакшне.
