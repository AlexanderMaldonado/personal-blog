# Personal Blog
link: https://roadmap.sh/projects/personal-blog
link2: https://roadmap.sh/projects/blogging-platform-api
A personal blog built with Flask and SQLite. Features a public section to read articles and a protected admin panel to manage them.

## Stack

- Python + Flask
- SQLite via Flask-SQLAlchemy
- Jinja2 templates
- python-dotenv for environment variables

## Features

- Home page with list of published articles
- Individual article page
- Admin login with session authentication
- Dashboard to create, edit, and delete articles

## Setup

```bash
git clone https://github.com/tu-usuario/personal-blog.git
cd personal-blog

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the root:

```
SECRET_KEY=your-secret-key
ADMIN_USERNAME=your-username
ADMIN_PASSWORD=your-password
```

Run the server:

```bash
python app.py
```

Open `http://localhost:5000` in your browser.
