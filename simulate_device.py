from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/check_password', methods=['GET'])
def check_password():
    default_passwords = ["admin", "password", "1234", "admin123", "default"]
    safe_passwords = ["jdjsksdsj","theworldaroundusisgone","HiHaydar","CTEC445"]
    combined_passwords = default_passwords + safe_passwords
    simulated_password = random.choice(combined_passwords)
    return jsonify({"password": simulated_password})

if __name__ == '__main__':
    app.run(debug=True)
