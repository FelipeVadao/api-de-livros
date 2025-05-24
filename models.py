from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer)
