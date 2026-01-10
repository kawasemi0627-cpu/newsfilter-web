from flask import Flask, render_template
import feedparser
from collections import defaultdict
import os

app = Flask(__name__)

rss_feeds = {
    "主要": "https://news.yahoo.co.jp/rss/topics/top-picks.xml",
    "国内": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
    "国際": "https://news.yahoo.co.jp/rss/topics/world.xml",
    "経済": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "IT": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "科学": "https://news.yahoo.co.jp/rss/topics/science.xml",
    "スポーツ": "https://news.yahoo.co.jp/rss/topics/sports.xml",
    "エンタメ": "https://news.yahoo.co.jp/rss/topics/entertainment.xml"
}

@app.route("/")
def index():
    articles_by_category = defaultdict(list)

    for category, url in rss_feeds.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles_by_category[category].append({
                "title": entry.title,
                "link": entry.link
            })

    return render_template("index.html", articles_by_category=articles_by_category)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
