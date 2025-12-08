
#!/usr/bin/python3
from flask import Flask, jsonify
import random
import logging

12345

# Отключаем логи Flask
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)

@app.route('/numbers123')
def get_numbers():
    numbers = [random.randint(1, 100) for _ in range(10)]
    return jsonify({"numbers123": numbers})

if __name__ == '__main__':
    # Запускаем без debug режима
    app.run(host='0.0.0.0', port=5000, debug=False)


print ...

