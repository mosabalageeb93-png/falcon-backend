from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# رابط قاعدة بياناتك الذي استخرجناه سوياً
MONGO_URI = "mongodb+srv://mosabalageeb93_db_user:GfaNn80clHnOCKnX@cluster0.m7ov7k5.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['falcon_system']
students_collection = db['students']

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # البحث عن الطالب في MongoDB
    student = students_collection.find_one({"student_id": username, "password": password})

    if student:
        return jsonify({
            "status": "success",
            "name": student['name'],
            "student_id": student['student_id'],
            "batch": student.get('batch', '24')
        })
    else:
        return jsonify({"status": "error", "message": "رقم الجلوس أو كلمة المرور خطأ"}), 401

@app.route('/')
def home():
    return "Falcon Backend is Running with MongoDB!"

if __name__ == '__main__':
    app.run(debug=True)
