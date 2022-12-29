from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask("__main__")

app.config['SECRET_KEY'] = '1ba8a99cbd9984c74cf378e1cdd9f4c4'

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


@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html", posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "rahasia":
            flash(f'You have been logged in!', 'success')
            return redirect(url_for("home"))
        else:
            flash(f'Login unsuccessful, please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
