from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from now_you_know.db.base import Base


class MovieModel(Base):
    """Model for demo purpose."""

    __tablename__ = "movie_model"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(length=200))  # noqa: WPS432
    year = Column(Integer())
    rating = Column(String(length=10))  # noqa: WPS432
