from flask import Flask, request
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # разрешаем запросы с GitHub Pages

@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    phone = data.get("phone")
    if not phone:
        return "Номер телефона не получен", 400

    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} — {phone}\n")

    return "Регистрация прошла успешно!"

if __name__ == "__main__":
    app.run()
