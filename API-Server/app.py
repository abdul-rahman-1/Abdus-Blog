import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Allow CORS from all origins
CORS(app, resources={r"/api/*": {"origins": "*"}})

# MongoDB connection string from .env
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client['Blogs']          # your DB name
collection = db['Blog']       # your collection name

@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = []
    for doc in collection.find():
        doc['_id'] = str(doc['_id'])  # convert ObjectId to string
        blogs.append(doc)
    return jsonify(blogs)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
