import sqlalchemy

from band.data.modelbase import SqlAlchemyBase


class Album(SqlAlchemyBase):
    __tablename__ = 'Album'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    year = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    price = sqlalchemy.Column(sqlalchemy.Float, index=True)
    album_image = sqlalchemy.Column(sqlalchemy.String)
