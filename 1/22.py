
#!/usr/bin/python3
from flask import Flask, jsonify
import random
import logging

11111111111111111111111111111111111111
22222222222222222222222222222222222222
33333333333333333333333333333333333333
44444444444444444444444444444444444444

# Отключаем логи Flask
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)

@app.route('/numbers123456')
def get_numbers():
    numbers = [random.randint(1, 100) for _ in range(10)]
    return jsonify({"numbers123456": numbers})

if __name__ == '__main__':
    # Запускаем без debug режима
    app.run(host='0.0.0.0', port=5000, debug=False)


print ...

