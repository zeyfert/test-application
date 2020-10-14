from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        "main.html",
        name="main",
    )


if __name__ == "__main__":
    app.run()
