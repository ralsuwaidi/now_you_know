from pydantic import BaseModel


class MovieModelDTO(BaseModel):
    """
    DTO for dummy models.

    It returned when accessing dummy models from the API.
    """

    id: int
    title: str
    year: int
    rating: str

    class Config:
        orm_mode = True


class MovieModelInputDTO(BaseModel):
    """DTO for creating new dummy model."""

    title: str
    year: int
    rating: str
