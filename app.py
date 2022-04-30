from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from database_uri import get_db_uri
import pandas as pd

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri("root")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# teams_traditional = db.Table(
#     "teams_traditional", db.metadata, autoload=True, autoload_with=db.engine
# )

Base = automap_base()
Base.prepare(engine=db.engine, autoload_with=db.engine)
TeamsTraditional = Base.classes.teams_traditional


@app.route("/")
def index():
    query = db.session.query(TeamsTraditional)
    df = pd.read_sql(sql=query.statement, con=db.engine)
    df["SEASON"] = df["SEASON"].dt.year
    table_html = df.to_html(
        justify="left",
        border=0,
        classes=["table", "table-dark", "table-striped"],
        index=False,
    )
    return render_template("index.html", table=table_html)


@app.route("/embed")
def index_embed():
    query = db.session.query(TeamsTraditional)
    df = pd.read_sql(sql=query.statement, con=db.engine)
    df["SEASON"] = df["SEASON"].dt.year
    table_html = df.to_html(
        justify="left",
        border=0,
        classes=["table", "table-dark", "table-striped"],
        index=False,
    )
    return render_template("index_embed.html", table=table_html)


@app.route("/embed_api")
def index_embed_api():
    query = db.session.query(TeamsTraditional)
    df = pd.read_sql(sql=query.statement, con=db.engine)
    df["SEASON"] = df["SEASON"].dt.year
    table_html = df.to_html(
        justify="left",
        border=0,
        classes=["table", "table-dark", "table-striped"],
        index=False,
    )
    return render_template("index_embed_api.html", table=table_html)


@app.route("/web_comp")
def index_web_comp():
    query = db.session.query(TeamsTraditional)
    df = pd.read_sql(sql=query.statement, con=db.engine)
    df["SEASON"] = df["SEASON"].dt.year
    table_html = df.to_html(
        justify="left",
        border=0,
        classes=["table", "table-dark", "table-striped"],
        index=False,
    )
    return render_template("index_web_comp.html", table=table_html)


if __name__ == "__main__":
    app.run(debug=True)
