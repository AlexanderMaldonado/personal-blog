# auth.py
import os
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint("auth", __name__)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Debes iniciar sesión primero.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated


@auth_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("admin.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == os.environ.get("ADMIN_USERNAME") and \
           password == os.environ.get("ADMIN_PASSWORD"):
            session["logged_in"] = True
            flash("¡Bienvenido!", "success")
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Usuario o contraseña incorrectos.", "error")

    return render_template("login.html")


@auth_bp.route("/admin/logout")
def logout():
    session.clear()
    flash("Sesión cerrada.", "info")
    return redirect(url_for("public.home"))