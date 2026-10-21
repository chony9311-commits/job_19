# save this as app.py
# app.py

from flask import Flask, render_template, request
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword", default="")

    jobs = search_incruit(keyword)

    return render_template(
        "search.html",
        jobs=jobs,
        keyword=keyword
    )


if __name__ == "__main__":
    app.run(debug=True)