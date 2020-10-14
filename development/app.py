from flask import Flask, render_template


app = Flask(__name__)


@app.route('/development/')
def development():
    return render_template(
        "development.html",
        name="development",
    )

if __name__ == "__main__":
    app.run()
