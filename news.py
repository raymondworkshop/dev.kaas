import feedparser
from flask import Blueprint, render_template

bp = Blueprint('news', __name__)

RSS_FEEDS = {
    'Paul Graham': 'http://www.aaronsw.com/2002/feeds/pgessays.rss',
    #'acmqueue': 'https://queue.acm.org/rss/feeds/articles.xml'
}

@bp.route('/news')
def news():
    #feeds = [feed for feed in RSS_FEEDS.values()]
    entries = {}
    for title, rss_url in RSS_FEEDS.items():
        feed = feedparser.parse(rss_url)
        entries[title] = feed['items'][0:7]
        #entries.extend(feed['items'])
    #print(entries[0])
    return render_template('info/news.html', entries=entries)