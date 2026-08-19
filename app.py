from flask import Flask, render_template, request
from config import APP_NAME, DEBUG
from services.LMStudioService import LMStudioService

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME
    )


@app.route("/submit", methods=["POST"])
def submit():

    user_input = request.form.get("message")

    result = LMStudioService.Chat(user_input)

    return render_template(
        "index.html",
        result=result,
        user_input=user_input,
        app_name=APP_NAME
    )


if __name__ == "__main__":
    app.run(debug=DEBUG)
