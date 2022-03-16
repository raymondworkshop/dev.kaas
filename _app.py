import os
import logging 

from flask import Flask, Blueprint, redirect, render_template, url_for, request
from flask_flatpages import FlatPages

from flaskext.markdown import Markdown

#from jinja2 import Environment

#FLATPAGES_AUTO_RELOAD = 'DEBUG'
#FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_pyfile('config.py')
Markdown(app, extensions=['fenced_code'])
pages = FlatPages(app)


@app.route('/hello')
def hello():
#    page = pages.get('hello')
    #logging.debug(f'page.meta:{page.meta}')
#    title = page.meta['title']

#    posts = (p for p in pages if 'date' in p.meta)
#    print(posts)
#    sorted(posts,key=lambda p: p.meta['date'], reverse=True)
#    return render_template('page.html', titles=title)
    return "Hello World"

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html',page=page) 

@app.route('/')
def index():
    return render_template('index.html', pages=pages)
  
@app.route('/about')
def about():
    #return "About"
    return render_template('about.html', pages=pages)

@app.route('/blog')
def blog():
    return render_template('index.html', pages=pages)

@app.route('/proj')
def research():
    #return 'research'
    return render_template('proj.html', pages=pages)

@app.route('/book')
def book():
    #return "book"
    return render_template('book.html', pages=pages)

@app.route('/link')
def link():
    return render_template('link.html', pages=pages)

if __name__ == "__main__":
    app.run()
    