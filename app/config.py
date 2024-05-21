import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "k0ruJ0b5"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'database.db')

    SQLALCHEMY_DATABASE_URI = "postgresql://dbkorujobs_user:TexB7RgXNrCEdgrHHG5LoaZSINT1KPuc@dpg-cp3rusg21fec73bdg85g-a.oregon-postgres.render.com/dbkorujobs"