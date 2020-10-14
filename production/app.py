from flask import Flask, render_template


app = Flask(__name__)


@app.route('/production/')
def index():
    return render_template(
        "production.html",
        name="production",
    )


if __name__ == "__main__":
    app.run()
