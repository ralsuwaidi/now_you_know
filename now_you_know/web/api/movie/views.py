from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from now_you_know.db.dao.movie_dao import MovieDAO
from now_you_know.db.models.movie_model import MovieModel
from now_you_know.web.api.movie.schema import MovieModelDTO, MovieModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[MovieModelDTO])
async def get_movie_models(
    limit: int = 10,
    offset: int = 0,
    movie_dao: MovieDAO = Depends(),
) -> List[MovieModel]:
    """
    Retrieve all movie objects from the database.

    :param limit: limit of movie objects, defaults to 10.
    :param offset: offset of movie objects, defaults to 0.
    :param movie_dao: DAO for movie models.
    :return: list of movie obbjects from database.
    """
    return await movie_dao.get_all_dummies(limit=limit, offset=offset)


@router.put("/")
async def create_movie_model(
    new_movie_object: MovieModelInputDTO,
    movie_dao: MovieDAO = Depends(),
) -> None:
    """
    Creates movie model in the database.

    :param new_movie_object: new movie model item.
    :param movie_dao: DAO for movie models.
    """
    await movie_dao.create_movie_model(**new_movie_object.dict())


@router.get("/{movie_title}", response_model=List[MovieModelDTO])
async def get_movie_model(
    movie_title,
    movie_dao: MovieDAO = Depends(),
) -> List[MovieModel]:
    """
    Creates movie model in the database.

    :param new_movie_object: new movie model item.
    :param movie_dao: DAO for movie models.
    """
    return await movie_dao.filter(title=movie_title)
