from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from now_you_know.db.base import Base


class DummyModel(Base):
    """Model for demo purpose."""

    __tablename__ = "dummy_model"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=200))  # noqa: WPS432
    year = Column(Integer())
