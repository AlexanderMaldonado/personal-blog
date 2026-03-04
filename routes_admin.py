# routes_admin.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Article
from auth import login_required

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@login_required
def dashboard():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("dashboard.html", articles=articles)


@admin_bp.route("/admin/new", methods=["GET", "POST"])
@login_required
def new_article():
    if request.method == "POST":
        title   = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        date    = request.form.get("date", "").strip()

        if not title or not content or not date:
            flash("Todos los campos son obligatorios.", "error")
            return render_template("article_form.html", action="new",
                                   title=title, content=content, date=date)

        article = Article(title=title, content=content, date=date)
        db.session.add(article)
        db.session.commit()
        flash(f'Artículo "{title}" publicado.', "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("article_form.html", action="new",
                           title="", content="", date="")


@admin_bp.route("/admin/edit/<int:article_id>", methods=["GET", "POST"])
@login_required
def edit_article(article_id):
    art = Article.query.get_or_404(article_id)

    if request.method == "POST":
        title   = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        date    = request.form.get("date", "").strip()

        if not title or not content or not date:
            flash("Todos los campos son obligatorios.", "error")
            return render_template("article_form.html", action="edit",
                                   article_id=article_id,
                                   title=title, content=content, date=date)

        art.title   = title
        art.content = content
        art.date    = date
        db.session.commit()
        flash(f'Artículo "{title}" actualizado.', "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("article_form.html", action="edit",
                           article_id=art.id,
                           title=art.title, content=art.content, date=art.date)


@admin_bp.route("/admin/delete/<int:article_id>", methods=["POST"])
@login_required
def delete_article(article_id):
    art = Article.query.get_or_404(article_id)
    db.session.delete(art)
    db.session.commit()
    flash(f'Artículo "{art.title}" eliminado.', "info")
    return redirect(url_for("admin.dashboard"))