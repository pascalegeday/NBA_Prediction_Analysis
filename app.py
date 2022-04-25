from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import db_username, db_password, db_endpoint, port

app = Flask(__name__)

database = "test"
db_uri = f"postgresql://{db_username}:{db_password}@{db_endpoint}:{port}/{database}"

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
# db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
