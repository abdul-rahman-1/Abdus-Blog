import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

# load MONGO_URI and PORT from .env
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# connect to your Atlas cluster
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# two separate databases & collections
blogs_db       = client['Blogs']
blogs_coll     = blogs_db['Blog']

news_db        = client['News']
news_coll      = news_db['News_Card']

@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    output = []
    for doc in blogs_coll.find():
        doc['_id'] = str(doc['_id'])
        output.append(doc)
    return jsonify(output), 200

@app.route('/api/news', methods=['GET'])
def get_news():
    output = []
    for doc in news_coll.find():
        doc['_id'] = str(doc['_id'])
        output.append(doc)
    return jsonify(output), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
