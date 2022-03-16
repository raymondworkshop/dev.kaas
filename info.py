import os

from flask import Blueprint, render_template

# from flask_flatpages import FlatPages
bp = Blueprint("info", __name__)

from app import pages
from app import app

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["UPLOADED_PHOTOS_DEST"] = os.path.join(basedir, "img")


@bp.route("/art")
def art():
    page = pages.get_or_404("art")
    return render_template("info/art.html", page=page)


@bp.route("/link")
def link():
    page = pages.get_or_404("link")
    return render_template("info/link.html", page=page)


@bp.route("/business")
def business():
    page = pages.get_or_404("business")
    return render_template("info/business.html", page=page)


@bp.route("/proj")
def proj():
    page = pages.get_or_404("proj")
    return render_template("info/proj.html", page=page)


@bp.route("/book")
def book():
    page = pages.get_or_404("book")
    return render_template("info/book.html", page=page)


@bp.route("/invest")
def invest():
    page = pages.get_or_404("invest")
    return render_template("info/invest.html", page=page)


@bp.route("/docs")
def docs():
    page = pages.get_or_404("docs")
    return render_template("info/docs.html", page=page)


@bp.route("/about")
def about():
    page = pages.get_or_404("about")
    return render_template("info/about.html", page=page)
