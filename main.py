from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/profile/')
def profile():
    return render_template("profile.html")


@app.route('/profile/ben')
def ben():
    return render_template("ben.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
