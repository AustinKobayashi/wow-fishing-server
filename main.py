import pigpio
from flask import Flask, request

pi = pigpio.pi()

SERVO_PIN = 27
SERVO_SPEED = 0.1


app = Flask(__name__)


@app.route('/click', methods=['POST'])
def click_handler():
    try:
        if 'click' not in request.json:
            return 'Error', 400

        if request.json['click'] < 700 or request.json['click'] > 1500:
            return 'Error', 400
        
        pi.set_servo_pulsewidth(SERVO_PIN, request.json['click'])

        return 'Success', 200
    except Exception as e:
        print(f'Error handling POST request: {e}')
        return 'Error', 500  # Internal Server Error

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
