# 🌟 Abdus Blog Platform

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![GitHub Repo Size](https://img.shields.io/github/repo-size/abdul-rahman-1/Abdus)
![Last Commit](https://img.shields.io/github/last-commit/abdul-rahman-1/Abdus)

> A minimal, responsive blogging platform and personal portfolio by **Abdul Rahman**, featuring a Flask‑powered API, a static frontend, and a self‑contained demo UI.

---

## 📁 Table of Contents

1. [🚀 Features](#-features)
2. [🗂️ File Structure](#️-file-structure)
3. [⚙️ Setup & Installation](#️-setup--installation)

   * [API‑Server](#api-server)
   * [Client (Static Frontend)](#client-static-frontend)
   * [Update Demo (Flask UI)](#update-demo-flask-ui)
4. [🚀 Usage](#-usage)
5. [☁️ Deployment](#️-deployment)
6. [🤝 Contributing](#-contributing)
7. [📄 License](#-license)

---

## 🚀 Features

* **Flask API**

  * CRUD endpoints for blogs (`GET`, `POST`, `PUT`, `DELETE`)
  * Image uploads converted to Base64
  * CORS enabled for public fetches

* **Static Frontend**

  * Portfolio pages: Home, Services, About, Contact, Newsletter, Enquiry
  * **Blog Listing** with cards, “Read More” modal including image
  * Responsive design powered by Bootstrap

* **Update Demo**

  * Self‑contained Flask UI with Jinja2 templates for adding/editing blogs
  * Shared form partial, custom styling, and live environment config

---

## 🗂️ File Structure

```text
Abdus/
🔺 API-Server/               # Flask API backend
├\2500 app.py                # /api/blogs CRUD & image handling
├\2500 requirements.txt      # Python dependencies
├\2500 Procfile              # gunicorn start command for Railway
├\2500 .env.example          # template for MONGO_URI & PORT
├\2500 .gitignore            # ignore .env, __pycache__, *.pyc
└\2500 README.md             # API-specific docs & deploy guide

🔺 Client/                   # Static frontend (portfolio + blog)
├\2500 *.html                # index, services, blog, newsletter, about, enquiry, contact
├\2500 css/
│  ├\2500 style.scss        # SCSS overrides
│  └\2500 style.css         # Compiled CSS
├\2500 js/
│  ├\2500 blog.js           # fetch & render blogs + modal logic
│  └\2500 main.js           # navbar, back‑to‑top, other UI scripts
├\2500 lib/                  # third‑party plugins (owlcarousel, easing, waypoints)
└\2500 img/                  # logos, favicons, preview screenshots

🔺 Update/                   # Self‑contained Flask blog manager demo
├\2500 static/
│  └\2500 style.css         # styles for Jinja2 templates
├\2500 templates/
│  ├\2500 index.html        # list & manage blogs
│  ├\2500 add.html          # add‑blog form
│  ├\2500 edit.html         # edit‑blog form
│  └\2500 form.html         # shared form fields partial
├\2500 app.py                # demo Flask app
├\2500 requirements.txt      # Python dependencies
└\2500 .env                  # live env vars (Mongo URI, PORT)
```

---

## ⚙️ Setup & Installation

### 1. API‑Server

```bash
git clone https://github.com/abdul-rahman-1/Abdus.git
cd Abdus/API-Server
cp .env.example .env  # Edit .env: set MONGO_URI and PORT
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=$PORT
```

Test the API:

```bash
curl http://localhost:5000/api/blogs
```

### 2. Client (Static Frontend)

```bash
cd ../Client
python -m http.server 8000
```

Visit: [http://localhost:8000/blog.html](http://localhost:8000/blog.html)
Make sure to edit `Client/js/blog.js` and point `API_URL` to your local or hosted backend.

### 3. Update Demo (Flask UI)

```bash
cd ../Update
pip install -r requirements.txt
flask run
```

Visit [http://localhost:5000](http://localhost:5000) to manage blogs.

---

## 🚀 Usage

* **List Blogs**: Fetch `GET /api/blogs` from frontend.
* **Create/Edit/Delete**: Use `Update` folder or REST client.
* **Modal Display**: Bootstrap-powered "Read More" modals show full blog and images.

---

## ☁️ Deployment

* **Railway.app**: Connect GitHub, set `MONGO_URI` & `PORT` in ENV.
* **GitHub Pages**: Serve `Client/` as static site.
* **Heroku or Render**: Host `API-Server/` Flask backend with `Procfile`.

---

## 🤝 Contributing

1. Fork the repo & create a new branch
2. Make your changes
3. Commit and push
4. Submit a pull request

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more.

---

> “Code is like humor. When you have to explain it, it’s bad.” — *Cory House*
