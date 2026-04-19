from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# هذا السطر يسمح لموقعك على GitHub Pages بالاتصال بالسيرفر
CORS(app)

# بيانات تجريبية للدخول (يمكنك تغييرها أو ربطها بقاعدة بياناتك لاحقاً)
USERS = {
    "24001": {"password": "123", "name": "مصعب العجيب", "student_id": "24001", "batch": "24"},
    "24002": {"password": "456", "name": "أحمد محمد", "student_id": "24002", "batch": "24"}
}

@app.route('/')
def home():
    return "Falcon Server is Running!"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in USERS and USERS[username]['password'] == password:
        return jsonify({
            "status": "success",
            "name": USERS[username]['name'],
            "student_id": USERS[username]['student_id'],
            "batch": USERS[username]['batch']
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "رقم الجلوس أو كلمة المرور غير صحيحة"
        }), 401

if __name__ == '__main__':
    app.run(debug=True)
