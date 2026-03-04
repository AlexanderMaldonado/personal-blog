# routes_public.py
from flask import Blueprint, render_template, abort
from models import Article

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def home():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("home.html", articles=articles)


@public_bp.route("/article/<int:article_id>")
def article(article_id):
    art = Article.query.get_or_404(article_id)
    return render_template("article.html", article=art)