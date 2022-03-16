import os

from flask import Blueprint, render_template
from markupsafe import escape

# from flask_flatpages import FlatPages

bp = Blueprint("blog", __name__)

from app import pages

# FLATPAGES_AUTO_RELOAD = DEBUG
# FLATPAGES_EXTENSION = [".md", ".markdown"]
# POST_DIR = 'posts'
# FLATPAGES_AUTO_RELOAD = DEBUG
# FLATPAGES_EXTENSION = '.md'

DRAFT = ["draft", "test", "diary", "learning", "course"]


def _list_no_draft():
    tagged = []
    for page in pages:
        tags = []
        tags = page.meta.get("tags", [])
        if not tags:
            tags = page.meta.get("categories", [])

        # print("tags:", tags)
        # print("type(tags):", type(tags))
        if isinstance(tags, str):  # str
            _tags_list = tags.split(",")
            tags_list = [tag.strip() for tag in _tags_list]
            # print("tags_list:", tags_list)
            if not list(set(tags_list) & set(DRAFT)):
                tagged.append(page)
        elif isinstance(tags, list):  # list
            if not list(set(tags) & set(DRAFT)):
                tagged.append(page)
        else:  # str
            pass

    return tagged


def _tag(tag):
    tagged = []
    for page in pages:
        if tag in page.meta.get("categories", []) or tag in page.meta.get("tags", []):
            # print("page.meta:", page.meta)
            tagged.append(page)
    return tagged


@bp.route("/")
def index():
    # page = pages.get('hello')
    # print(type(pages))
    # page = pages.get('hello')
    # print(page.title)
    # don't list posts tagging with DRAFT
    # tagged = _list_no_draft()
    tagged = _tag("home")
    return render_template("blog/index.html", pages=tagged)


@bp.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("blog/page.html", page=page)


@bp.route("/blog")
def blog():
    # pages = [page for page in pages if page.meta.get("title", []) != 'link']
    # print("pages:", )
    # tagged = _list_no_draft()
    tagged = _tag("home")
    return render_template("blog/index.html", pages=tagged)


@bp.route("/<string:tag>/")
def tag(tag):
    # tagged = [page for page in pages if tag in page.meta.get("tags", [])]
    # tagged = [page for page in pages if tag in page.meta.get("tags", [])] +

    # tagged = [page for page in pages if tag in page.meta.get("categories")]
    # tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    # print("tagged:", _tagged)
    tagged = _tag(tag)
    return render_template("blog/tag.html", tagged=tagged, tag=tag)


"""
@bp.route('/art')
def art():
    files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('art/index.html', images=files_list)
"""
