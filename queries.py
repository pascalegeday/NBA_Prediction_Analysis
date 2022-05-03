import pandas as pd
from sqlalchemy.ext.automap import automap_base


def retrieve_tables(db):
    # Reflect the tables in the database
    Base = automap_base()
    Base.prepare(engine=db.engine, autoload_with=db.engine)

    # Map the tables to python classes
    TeamsTraditional = Base.classes.teams_traditional
    TeamsAdvanced = Base.classes.teams_advanced
    TeamsMisc = Base.classes.teams_misc

    tables = [TeamsTraditional, TeamsAdvanced, TeamsMisc]
    dataframes = []

    for table in tables:
        # Create the query
        query = db.session.query(table)
        # Create a DataFrame from the query statement
        df = pd.read_sql(sql=query.statement, con=db.engine)
        # Chang the SEASON column to the year as an integer
        df["SEASON"] = df["SEASON"].dt.year
        dataframes.append(df)

    return tuple(dataframes)
