from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Article {self.id}>'