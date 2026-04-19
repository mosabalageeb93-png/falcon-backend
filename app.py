from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # للسماح للموقع بالاتصال بالسيرفر من أي مكان

# قاعدة البيانات (يمكنك إضافة طلاب أكثر هنا)
students_db = {
    "12345678": {
        "password": "00000000",
        "name": "مصعب العاقب محمد أحمد",
        "id": "31001418-25",
        "batch": "24",
        "college": "كلية القلم"
    }
}

@app.route('/')
def home():
    return "Falcon Server is Running!"

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if username in students_db and students_db[username]['password'] == password:
            return jsonify({
                "status": "success",
                "name": students_db[username]['name'],
                "student_id": students_db[username]['id'],
                "batch": students_db[username]['batch']
            }), 200
        else:
            return jsonify({"status": "error", "message": "الرقم الجامعي أو كلمة المرور خطأ"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # استخدام المنفذ الذي يحدده Render تلقائياً
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
