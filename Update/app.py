from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import base64
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["Blogs"]
collection = db["Blog"]

def encode_image_to_base64(file):
    if file:
        return "data:image/jpeg;base64," + base64.b64encode(file.read()).decode('utf-8')
    return ""

@app.route("/")
def index():
    blogs = list(collection.find())
    return render_template("index.html", blogs=blogs)

@app.route("/add", methods=["GET", "POST"])
def add_blog():
    if request.method == "POST":
        image_data = encode_image_to_base64(request.files["image"])
        blog = {
            "heading": request.form["heading"],
            "title": request.form["title"],
            "short_content": request.form["short_content"],
            "content": request.form["content"],
            "date": request.form["date"],
            "image_base64": image_data
        }
        collection.insert_one(blog)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_blog(id):
    blog = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        updated_data = {
            "heading": request.form["heading"],
            "title": request.form["title"],
            "short_content": request.form["short_content"],
            "content": request.form["content"],
            "date": request.form["date"],
        }

        if request.files["image"]:
            updated_data["image_base64"] = encode_image_to_base64(request.files["image"])
        else:
            updated_data["image_base64"] = blog["image_base64"]

        collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for("index"))

    return render_template("edit.html", blog=blog)

@app.route("/delete/<id>")
def delete_blog(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
