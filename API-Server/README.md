# API Server for Blog Manager

This Flask-based API provides CRUD endpoints for managing finance & investment blogs stored in MongoDB.

## Features
- List all blogs: `GET /api/blogs`
- Get single blog: `GET /api/blogs/<id>`
- Create blog: `POST /api/blogs` (multipart/form-data: heading, title, short_content, content, date, image)
- Update blog: `PUT /api/blogs/<id>` (multipart/form-data)
- Delete blog: `DELETE /api/blogs/<id>`

## Setup
1. Clone the repo.
2. Copy `.env.example` to `.env` and fill your `MONGO_URI`.
3. Install:
   ```bash
   pip install -r requirements.txt