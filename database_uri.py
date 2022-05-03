import configparser
from pathlib import Path


def get_db_uri(user_type):
    config = configparser.ConfigParser()
    config.read(Path("config.ini"))

    # database and root user credentials
    host = config["DATABASE"]["HOST"]
    port = config["DATABASE"]["PORT"]
    db = config["DATABASE"]["DB"]

    if user_type == "root":
        # root user credentials
        root_user = config["ROOT"]["USERNAME"]
        root_pwd = config["ROOT"]["USERNAME"]

        # root user db uri
        db_uri = f"postgresql://{root_user}:{root_pwd}@{host}:{port}/{db}"

    elif user_type == "user":
        # user credentials
        user = config["USER"]["USERNAME"]
        pwd = config["USER"]["PASSWORD"]

        # user db uri
        db_uri = f"postgresql://{user}:{pwd}@{host}:{port}/{db}"

    return db_uri
