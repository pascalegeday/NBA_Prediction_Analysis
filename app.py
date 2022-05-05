from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

from database_uri import get_db_uri
from queries import retrieve_tables


# Create the flask app
app = Flask(__name__)
# Get DB URI by specifying DB user type
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri("root")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SQLAlchemy instance
db = SQLAlchemy(app)

# Assign DataFrames using DB table names
teams_traditional, teams_advanced, teams_misc = retrieve_tables(db)
tables = {
    "traditional": teams_traditional,
    "advanced": teams_advanced,
    "misc": teams_misc,
}


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/game_evolution")
def game_evolution():
    table_html = tables["traditional"].to_html(
        justify="left",
        border=0,
        classes=["table", "table-dark", "table-striped"],
        index=False,
    )
    return render_template("game_evolution.html", table_html=table_html)


@app.route("/defense_offense")
def defense_offense():

    return render_template("defense_offense.html")


@app.route("/comparison")
def comparison():

    return render_template("comparison.html")


@app.route("/prediction")
def prediction():

    return render_template("prediction.html")


@app.route("/people")
def people():

    return render_template("people.html")


if __name__ == "__main__":
    app.run(debug=True)
