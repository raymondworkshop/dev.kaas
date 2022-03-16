import os

from flask import Flask, render_template_string
from flask_flatpages import FlatPages, pygments_style_defs
from flask_flatpages.utils import pygmented_markdown
from flaskext.markdown import Markdown

# from flask_mistune import Mistune
# import markdown
# import markdown.extensions.fenced_code
pages = FlatPages()


def my_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)

basedir = os.path.abspath(os.path.dirname(__file__))

# def create_app(test_config=None):
app = Flask(__name__)

# if test_config is None:
app.config.from_pyfile("config.py")
# else:
#    app.config.from_mapping(test_config)
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'img')

@app.route("/hello")
def hello():
    return "Hello, World!"


@app.route("/pygments.css")
def pygments_css():
    return pygments_style_defs("tango"), 200, {"Content-Type": "text/css"}


app.config["FLATPAGES_HTML_RENDERER"] = my_renderer
Markdown(app, extensions=["fenced_code", "codehilite", "tables", "mdx_math"])
pages.init_app(app)

import blog

app.register_blueprint(blog.bp)
# app.add_url_rule('/', endpoint='index')

#import art
#app.register_blueprint(art.bp)

import info
app.register_blueprint(info.bp)

import news
app.register_blueprint(news.bp)

#    return app
