from flask import Flask, render_template

app = Flask("__main__")

posts = [
    {
        "author": "Omi Gusty Rifani",
        "title": "Blog post 1",
        "content": "First content",
        "date_posted": "28 Dec 2022"
    },
    {
        "author": "Rio",
        "title": "Blog post 2",
        "content": "Second content",
        "date_posted": "26 Dec 2022"
    }
]


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("index.html", posts=posts, title="Home")


@app.route("/about")
def contactPage():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
