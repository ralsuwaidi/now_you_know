from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from now_you_know.db.dependencies import get_db_session
from now_you_know.db.models.movie_model import MovieModel


class MovieDAO:
    """Class for accessing movie table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_movie_model(self, title: str, year: int, rating: str) -> None:
        """
        Add single movie to session.

        :param title: title of a movie.
        """
        self.session.add(MovieModel(title=title, year=year, rating=rating))

    async def get_all_dummies(self, limit: int, offset: int) -> List[MovieModel]:
        """
        Get all movie models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        raw_dummies = await self.session.execute(
            select(MovieModel).limit(limit).offset(offset),
        )

        return raw_dummies.scalars().fetchall()

    async def filter(
        self,
        title: Optional[str] = None,
    ) -> List[MovieModel]:
        """
        Get specific movie model.

        :param title: title of movie instance.
        :return: movie models.
        """
        query = select(MovieModel)
        if title:
            query = query.where(MovieModel.title == title)
        rows = await self.session.execute(query)
        return rows.scalars().fetchall()
