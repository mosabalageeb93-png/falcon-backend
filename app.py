from flask import Flask, request, jsonify
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)

# الرابط المعدل مع كلمة السر الجديدة Mosab@2026
MONGO_URI = "mongodb+srv://mosabalageeb93_db_user:Mosab%402026@cluster0.m7ov7k5.mongodb.net/?appName=Cluster0"

client = pymongo.MongoClient(MONGO_URI)
db = client['falcon_system']
collection = db['students']

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # البحث عن الطالب في قاعدة البيانات
    student = collection.find_one({"student_id": username, "password": password})

    if student:
        return jsonify({
            "status": "success",
            "name": student['name'],
            "student_id": student['student_id'],
            "batch": student.get('batch', '6')
        }), 200
    else:
        return jsonify({"status": "error", "message": "رقم الجلوس أو كلمة المرور خطأ"}), 401

@app.route('/')
def home():
    return "Falcon Backend is Running with MongoDB!"

if __name__ == '__main__':
    app.run(debug=True)
