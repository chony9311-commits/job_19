# save this as app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")
    keyword = request.args.get("keyword", keyword = keyword)

if __name__ == "__main__":
    app.run(debug=True)