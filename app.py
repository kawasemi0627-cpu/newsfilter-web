import os
from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# 任意のRSSフィード（今回はYahoo!ニュース主要）
RSS_URL = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"

@app.route("/")
def index():
    feed = feedparser.parse(RSS_URL)
    entries = [
        {"title": entry.title, "link": entry.link}
        for entry in feed.entries
    ]
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
