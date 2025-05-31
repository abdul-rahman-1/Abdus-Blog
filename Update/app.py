from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import base64
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))

# Blog DB and Collection
blog_db = client["Blogs"]
blog_collection = blog_db["Blog"]

# News DB and Collection
news_db = client["News"]
news_collection = news_db["News_Card"]

def encode_image_to_base64(file):
    if file:
        return "data:image/jpeg;base64," + base64.b64encode(file.read()).decode('utf-8')
    return ""

# --- Blog routes (unchanged) ---
@app.route("/")
def index():
    blogs = list(blog_collection.find())
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
        blog_collection.insert_one(blog)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_blog(id):
    blog = blog_collection.find_one({"_id": ObjectId(id)})
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
            updated_data["image_base64"] = blog.get("image_base64", "")
        blog_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for("index"))
    return render_template("edit.html", blog=blog)

@app.route("/delete/<id>")
def delete_blog(id):
    blog_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

# --- News Card routes ---

@app.route("/news")
def news_index():
    news_cards = list(news_collection.find().sort("issue", 1))
    return render_template("news_index.html", news_cards=news_cards)

@app.route("/news/add", methods=["GET", "POST"])
def add_news_card():
    if request.method == "POST":
        # Parse sections from form inputs
        sections = []
        section_headings = request.form.getlist("section_heading")
        section_contents = request.form.getlist("section_content")
        for heading, content in zip(section_headings, section_contents):
            if heading.strip() and content.strip():
                sections.append({"heading": heading.strip(), "content": content.strip()})

        news_card = {
            "issue": int(request.form["issue"]),
            "title": request.form["title"],
            "date": request.form["date"],
            "summary": request.form["summary"],
            "sections": sections
        }
        news_collection.insert_one(news_card)
        return redirect(url_for("news_index"))
    return render_template("news_add.html")

@app.route("/news/edit/<id>", methods=["GET", "POST"])
def edit_news_card(id):
    news_card = news_collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        sections = []
        section_headings = request.form.getlist("section_heading")
        section_contents = request.form.getlist("section_content")
        for heading, content in zip(section_headings, section_contents):
            if heading.strip() and content.strip():
                sections.append({"heading": heading.strip(), "content": content.strip()})

        updated_data = {
            "issue": int(request.form["issue"]),
            "title": request.form["title"],
            "date": request.form["date"],
            "summary": request.form["summary"],
            "sections": sections
        }
        news_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for("news_index"))
    return render_template("news_edit.html", news_card=news_card)

@app.route("/news/delete/<id>")
def delete_news_card(id):
    news_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("news_index"))

if __name__ == "__main__":
    app.run(debug=True)
